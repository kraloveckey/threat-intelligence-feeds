#!/usr/bin/env python3
"""
tif-update-readme.py – rebuilds README-STATISTICS.md AND injects stats + full feed table
into README.md between sentinel comments:

    <!-- STATS_TABLE_START -->  ...  <!-- STATS_TABLE_END -->
    <!-- FEEDS_TABLE_START -->  ...  <!-- FEEDS_TABLE_END -->

Run from the scripts/ directory:  python3 tif-update-readme.py
"""

import csv
import os
import re
from collections import defaultdict

REPO_ROOT   = os.path.join(os.path.dirname(__file__), '..')
CSV_FILE    = os.path.join(REPO_ROOT, 'threat-intelligence-feeds.csv')
README_FILE = os.path.join(REPO_ROOT, 'README.md')
STATS_FILE  = os.path.join(REPO_ROOT, 'README-STATISTICS.md')

CATEGORY_ORDER = [
    'IP', 'DNS', 'URL', 'MD5', 'SHA1', 'SHA256',
    'SSL', 'JA3', 'CVEID', 'RANSOMWARELEAK', 'MISP',
    'IOC', 'BLOCKLIST', 'REPO', 'RESTRICTED',
]

CATEGORY_DESCRIPTIONS = {
    'IP':            'Malicious / suspicious IPv4 addresses and CIDR ranges',
    'DNS':           'Malicious or suspicious domain names',
    'URL':           'Malicious / phishing / C2 URLs',
    'MD5':           'MD5 hashes of malicious files',
    'SHA1':          'SHA1 hashes of malicious files',
    'SHA256':        'SHA256 hashes of malicious files',
    'SSL':           'Malicious SSL certificate fingerprints',
    'JA3':           'JA3 TLS client fingerprints',
    'CVEID':         'Known exploited CVE identifiers',
    'RANSOMWARELEAK':'Ransomware leak site victim data aggregated from multiple gang leak sites',
    'MISP':          'Structured MISP-format feeds (importable directly into MISP platform)',
    'IOC':           'Mixed-type IOC feeds containing multiple indicator types (IP, domain, URL, hash, etc.)',
    'BLOCKLIST':     'General-purpose IP blocklists — ISPs, ASNs, gaming, ad-trackers (not strictly threat intel)',
    'REPO':          'GitHub repositories with IOC collections — no direct machine-readable feed URL',
    'RESTRICTED':    'Feeds requiring registration or an API key (free or commercial) to access',
}

STATUS_ICON = {'Active': '🟢', 'Offline': '🔴', 'Restricted': '🔒', 'N/A': '➖', '': '⚪'}


def load_rows():
    with open(CSV_FILE, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f, delimiter=';'))


def count_categories(rows):
    counts = {}
    for row in rows:
        cat = row.get('Category','').strip()
        if cat:
            counts[cat] = counts.get(cat, 0) + 1
    return counts


def build_stats_table(counts):
    lines = ['| Category | Description | Count |', '| --- | --- | --- |']
    ordered = [c for c in CATEGORY_ORDER if c in counts]
    extras  = sorted(c for c in counts if c not in CATEGORY_ORDER)
    total   = 0
    for cat in ordered + extras:
        desc = CATEGORY_DESCRIPTIONS.get(cat, '')
        lines.append(f'| `{cat}` | {desc} | {counts[cat]} |')
        total += counts[cat]
    lines.append(f'| **Total** | | **{total}** |')
    return '\n'.join(lines)


def build_feeds_table(rows):
    fieldnames = rows[0].keys() if rows else []
    has_status = 'FeedStatus' in fieldnames

    by_cat = defaultdict(list)
    for row in rows:
        by_cat[row['Category'].strip()].append(row)
    for cat in by_cat:
        by_cat[cat].sort(key=lambda r: r['Vendor'].strip().lower())

    lines = []
    ordered = [c for c in CATEGORY_ORDER if c in by_cat]
    extras  = sorted(c for c in by_cat if c not in CATEGORY_ORDER)

    for cat in ordered + extras:
        cat_rows = by_cat[cat]
        lines.append(f'\n### {cat} ({len(cat_rows)})\n')
        if has_status:
            lines.append('| Vendor | Description | Status | URL |')
            lines.append('| --- | --- | :---: | --- |')
            for r in cat_rows:
                vendor = r['Vendor'].strip()
                desc   = r['Description'].strip()
                url    = r['Url'].strip()
                status = r.get('FeedStatus','').strip()
                icon   = STATUS_ICON.get(status, '⚪')
                label  = status if status else 'Not checked'
                lines.append(f'| {vendor} | {desc} | <abbr title="{label}">{icon}</abbr> | [↗]({url}) |')
        else:
            lines.append('| Vendor | Description | URL |')
            lines.append('| --- | --- | --- |')
            for r in cat_rows:
                vendor = r['Vendor'].strip()
                desc   = r['Description'].strip()
                url    = r['Url'].strip()
                lines.append(f'| {vendor} | {desc} | [↗]({url}) |')

    return '\n'.join(lines)


def inject_block(content, start_marker, end_marker, new_body):
    pattern     = re.escape(start_marker) + r'.*?' + re.escape(end_marker)
    replacement = f'{start_marker}\n{new_body}\n{end_marker}'
    new_content, n = re.subn(pattern, replacement, content, flags=re.DOTALL)
    return new_content, n > 0


def main():
    rows   = load_rows()
    counts = count_categories(rows)

    stats_md = build_stats_table(counts)
    feeds_md = build_feeds_table(rows)

    with open(STATS_FILE, 'w', encoding='utf-8') as f:
        f.write(stats_md + '\n')
    print('✅  README-STATISTICS.md updated.')

    with open(README_FILE, encoding='utf-8') as f:
        content = f.read()

    content, ok1 = inject_block(content, '<!-- STATS_TABLE_START -->', '<!-- STATS_TABLE_END -->', stats_md)
    content, ok2 = inject_block(content, '<!-- FEEDS_TABLE_START -->', '<!-- FEEDS_TABLE_END -->', feeds_md)

    with open(README_FILE, 'w', encoding='utf-8') as f:
        f.write(content)

    print('✅  README.md stats table updated.' if ok1 else '⚠️  STATS markers not found in README.')
    print('✅  README.md feeds table updated.' if ok2 else '⚠️  FEEDS markers not found in README.')
    print(f'\nTotal feeds: {sum(counts.values())}')
    print(stats_md)


if __name__ == '__main__':
    main()