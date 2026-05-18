#!/usr/bin/env python3
"""
tif-status-checker.py – checks HTTP status of every feed URL in threat-intelligence-feeds.csv
and writes the result back as a FeedStatus column (Active / Offline).

Run from the scripts/ directory:  python3 tif-status-checker.py
"""

import csv
import os
import sys
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse

CSV_FILE      = os.path.join(os.path.dirname(__file__), '..', 'threat-intelligence-feeds.csv')
DELIMITER     = ';'
URL_COLUMN    = 'Url'
STATUS_COLUMN = 'FeedStatus'
TIMEOUT       = 15
TIMEOUT_ARCHIVE = 30
MAX_WORKERS   = 25

SKIP_CATEGORIES    = {'RESTRICTED'}   # skip HTTP check; set a fixed status
SKIP_STATUS        = {'RESTRICTED': 'Restricted'}
SKIP_URLS = {
    #'http://list.iblocklist.com/?list=nlgdvmvfxvoimdunmuju&fileformat=p2p&archiveformat=gz': 'Active',
    #'https://jamesbrine.com.au/csv': 'Active',
}
ARCHIVE_EXTENSIONS = ('.zip', '.gz', '.tar', '.tar.gz', '.bz2')
DATA_EXTENSIONS = ('.csv', '.json', '.txt', '.netset', '.lst', '.intel')

HEADERS = {
    'User-Agent': (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/120.0.0.0 Safari/537.36'
    )
}


def is_downloadable(url: str) -> bool:
    lower = url.lower()
    path  = urlparse(lower).path
    # Archives
    if any(path.endswith(ext) for ext in ARCHIVE_EXTENSIONS):
        return True
    # Plain data files — use Range to avoid downloading large files
    if any(path.endswith(ext) for ext in DATA_EXTENSIONS):
        return True
    # Query param hints (iBlocklist, MaxMind)
    if any(f'archiveformat={fmt}' in lower for fmt in ('gz', 'zip', 'bz2')):
        return True
    if any(f'suffix={fmt}' in lower for fmt in ('zip', 'gz')):
        return True
    return False


def check_url(url: str) -> str:
    try:
        is_archive = is_downloadable(url)
        if is_archive:
            range_headers = {**HEADERS, 'Range': 'bytes=0-0'}
            resp = requests.get(
                url, timeout=TIMEOUT_ARCHIVE, allow_redirects=True,
                headers=range_headers, stream=True
            )
            if resp.status_code in (200, 206):
                return 'Active'
            resp = requests.head(url, timeout=TIMEOUT_ARCHIVE, allow_redirects=True, headers=HEADERS)
            if resp.status_code in (400, 403, 405):
                resp = requests.get(url, timeout=TIMEOUT_ARCHIVE, allow_redirects=True,
                                    headers=HEADERS, stream=True)
            return 'Active' if resp.status_code < 400 else 'Offline'

        resp = requests.head(url, timeout=TIMEOUT, allow_redirects=True, headers=HEADERS)
        if resp.status_code in (400, 403, 405):
            resp = requests.get(
                url, timeout=TIMEOUT, allow_redirects=True,
                headers=HEADERS, stream=True
            )
        return 'Active' if resp.status_code < 400 else 'Offline'
    except requests.RequestException:
        return 'Offline'


def main() -> None:
    if not os.path.exists(CSV_FILE):
        print(f'[ERROR] CSV file not found: {CSV_FILE}')
        sys.exit(1)

    with open(CSV_FILE, newline='', encoding='utf-8') as f:
        reader    = csv.DictReader(f, delimiter=DELIMITER)
        fieldnames = list(reader.fieldnames or [])
        rows       = list(reader)

    if URL_COLUMN not in fieldnames:
        print(f'[ERROR] Column "{URL_COLUMN}" not found. Columns: {fieldnames}')
        sys.exit(1)

    if STATUS_COLUMN not in fieldnames:
        fieldnames.append(STATUS_COLUMN)

    url_triples = [
        (i, row[URL_COLUMN].strip(), row.get('Category', '').strip())
        for i, row in enumerate(rows)
        if row.get(URL_COLUMN, '').strip()
    ]

    # Pre-fill fixed statuses for categories that should not be checked
    results: dict[int, str] = {}
    for i, url, cat in url_triples:
        if cat in SKIP_CATEGORIES:
            results[i] = SKIP_STATUS[cat]
        elif url in SKIP_URLS:
            results[i] = SKIP_URLS[url]

    to_check = [(i, url) for i, url, cat in url_triples if cat not in SKIP_CATEGORIES]
    total = len(to_check)
    skipped = len(url_triples) - total
    print(f'[INFO] Checking {total} URLs with {MAX_WORKERS} workers … ({skipped} skipped)\n')

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        futures = {pool.submit(check_url, url): (i, url) for i, url in to_check}
        for done_n, future in enumerate(as_completed(futures), start=1):
            idx, url = futures[future]
            status   = future.result()
            results[idx] = status
            icon = '✅' if status == 'Active' else '❌'
            print(f'[{done_n:>4}/{total}] {icon} {status:<8} {url}')

    for i, row in enumerate(rows):
        row[STATUS_COLUMN] = results.get(i, '')

    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=DELIMITER,
                                extrasaction='ignore')
        writer.writeheader()
        writer.writerows(rows)

    active     = sum(1 for s in results.values() if s == 'Active')
    offline    = sum(1 for s in results.values() if s == 'Offline')
    restricted = sum(1 for s in results.values() if s == 'Restricted')
    na         = sum(1 for s in results.values() if s == 'N/A')
    print(f'\n[DONE] Results written to: {os.path.abspath(CSV_FILE)}')
    print(f'       Active    : {active}')
    print(f'       Offline   : {offline}')
    print(f'       Restricted: {restricted}')
    print(f'       N/A (repo): {na}')


if __name__ == '__main__':
    main()