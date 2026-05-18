#!/usr/bin/env python3
"""
tif-generate-table-statistics.py – counts feeds per category and writes README-STATISTICS.md.
Run from the scripts/ directory:  python3 tif-generate-table-statistics.py
"""

import csv
import os

CSV_FILE   = os.path.join(os.path.dirname(__file__), '..', 'threat-intelligence-feeds.csv')
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), '..', 'README-STATISTICS.md')

CATEGORY_ORDER = [
    'IP', 'DNS', 'URL', 'MD5', 'SHA1', 'SHA256',
    'SSL', 'JA3', 'CVEID', 'RANSOMWARELEAK', 'MISP',
    'IOC', 'BLOCKLIST', 'REPO', 'RESTRICTED', 'GEOIP',
    'RSS', 'FRAMEWORK', 'OSINT', 'SANDBOX',
]


def count_categories(csv_file: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=';')
        for row in reader:
            cat = (row.get('Category') or '').strip()
            if cat:
                counts[cat] = counts.get(cat, 0) + 1
    return counts


def build_table(counts: dict[str, int]) -> str:
    lines = ['| Category | Count |', '| --- | --- |']

    # Ordered first, then any extras alphabetically
    ordered_cats = [c for c in CATEGORY_ORDER if c in counts]
    extra_cats   = sorted(c for c in counts if c not in CATEGORY_ORDER)

    total = 0
    for cat in ordered_cats + extra_cats:
        lines.append(f'| {cat} | {counts[cat]} |')
        total += counts[cat]
    lines.append(f'| **Total** | **{total}** |')
    return '\n'.join(lines) + '\n'


def main():
    counts = count_categories(CSV_FILE)
    table  = build_table(counts)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(table)

    print(f"✅  Statistics table saved to: {os.path.abspath(OUTPUT_FILE)}")
    print(table)


if __name__ == '__main__':
    main()
