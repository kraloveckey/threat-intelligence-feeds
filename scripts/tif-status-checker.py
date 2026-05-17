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

CSV_FILE      = os.path.join(os.path.dirname(__file__), '..', 'threat-intelligence-feeds.csv')
DELIMITER     = ';'
URL_COLUMN    = 'Url'
STATUS_COLUMN = 'FeedStatus'
TIMEOUT       = 12
MAX_WORKERS   = 25

HEADERS = {
    'User-Agent': (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/120.0.0.0 Safari/537.36'
    )
}


def check_url(url: str) -> str:
    """Return 'Active' if the URL responds without an error status, else 'Offline'."""
    try:
        resp = requests.head(url, timeout=TIMEOUT, allow_redirects=True, headers=HEADERS)
        # Some servers reject HEAD – fall back to a streaming GET
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

    url_pairs = [
        (i, row[URL_COLUMN].strip())
        for i, row in enumerate(rows)
        if row.get(URL_COLUMN, '').strip()
    ]

    total = len(url_pairs)
    print(f'[INFO] Checking {total} URLs with {MAX_WORKERS} workers …\n')

    results: dict[int, str] = {}

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        futures = {pool.submit(check_url, url): (i, url) for i, url in url_pairs}
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

    active  = sum(1 for s in results.values() if s == 'Active')
    offline = sum(1 for s in results.values() if s == 'Offline')
    print(f'\n[DONE] Results written to: {os.path.abspath(CSV_FILE)}')
    print(f'       Active : {active}')
    print(f'       Offline: {offline}')


if __name__ == '__main__':
    main()
