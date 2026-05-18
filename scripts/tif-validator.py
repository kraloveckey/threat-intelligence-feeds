#!/usr/bin/env python3
"""
tif-validator.py – validates threat-intelligence-feeds.csv for correct format and categories.
Run from the scripts/ directory:  python3 tif-validator.py
"""

import csv
import os
import sys

VALID_CATEGORIES = [
    'SSL', 'IP', 'DNS', 'URL', 'MD5', 'SHA1', 'SHA256',
    'CVEID', 'RANSOMWARELEAK', 'JA3', 'MISP',
    'IOC', 'BLOCKLIST', 'REPO', 'RESTRICTED', 'GEOIP',
    'RSS', 'FRAMEWORK', 'OSINT', 'SANDBOX',
]

CSV_FILE = os.path.join(os.path.dirname(__file__), '..', 'threat-intelligence-feeds.csv')

BANNER = """\
╔══════════════════════════════════════════════════╗
║         Threat Intel Feeds – CSV Validator       ║
╚══════════════════════════════════════════════════╝
Validating: {}
""".format(os.path.abspath(CSV_FILE))


def validate_csv(csv_file: str) -> int:
    errors = 0
    seen_urls: set[str] = set()

    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=';')

        if reader.fieldnames is None:
            print("[ERROR] Empty or unreadable file.")
            return 1

        required = {'Vendor', 'Description', 'Category', 'Url'}
        missing_cols = required - set(reader.fieldnames)
        if missing_cols:
            print(f"[ERROR] Missing columns: {missing_cols}")
            return 1

        for idx, row in enumerate(reader, start=2):
            vendor      = row.get('Vendor', '').strip()
            description = row.get('Description', '').strip()
            category    = row.get('Category', '').strip()
            url         = row.get('Url', '').strip()

            line = f"Line {idx}"

            if not vendor:
                print(f"[WARN]  {line}: Vendor is empty")
                errors += 1
            if not description:
                print(f"[WARN]  {line}: Description is empty")
                errors += 1
            if not category:
                print(f"[ERROR] {line}: Category is empty")
                errors += 1
            elif category not in VALID_CATEGORIES:
                print(f"[ERROR] {line}: Invalid category '{category}'. "
                      f"Valid: {VALID_CATEGORIES}")
                errors += 1
            if not url:
                print(f"[ERROR] {line}: URL is empty")
                errors += 1
            elif not url.startswith(('http://', 'https://')):
                print(f"[WARN]  {line}: URL does not start with http(s): {url}")
                errors += 1

            dup_key = f"{category}|{url}"
            if dup_key in seen_urls:
                print(f"[WARN]  {line}: Duplicate entry (category+url): {url}")
                errors += 1
            seen_urls.add(dup_key)

    return errors


def main():
    print(BANNER)
    if not os.path.exists(CSV_FILE):
        print(f"[ERROR] File not found: {CSV_FILE}")
        sys.exit(1)

    errors = validate_csv(CSV_FILE)
    if errors == 0:
        print("✅  CSV is valid — no issues found.")
    else:
        print(f"\n❌  Validation finished with {errors} issue(s).")
        sys.exit(1)


if __name__ == '__main__':
    main()
