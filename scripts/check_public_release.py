#!/usr/bin/env python3
"""Checks the published aggregate tables only; needs no texts and reconstructs none."""
from pathlib import Path
import csv
import re

ROOT = Path(__file__).resolve().parents[1]


def read_csv(name):
    with (ROOT / 'data' / name).open(newline='', encoding='utf-8') as handle:
        return list(csv.DictReader(handle))


source = read_csv('source_summary.csv')
mapping = read_csv('source_mapping.csv')
coverage = read_csv('source_year_coverage.csv')
quality = read_csv('quality_flags_by_source.csv')

assert len(source) == 11, f"Expected 11 source categories, got {len(source)}"
assert len(mapping) == 21, f"Expected 21 upstream source labels, got {len(mapping)}"
assert len({r['category_code'] for r in source}) == 11
assert len({r['raw_source_label'] for r in mapping}) == 21
assert {r['analytical_source_category'] for r in mapping} == {r['source_document_type'] for r in source}

count = sum(int(r['records']) for r in source)
words = sum(int(r['whitespace_delimited_words']) for r in source)
assert count == 75431, f"Unexpected count: {count}"
assert words == 524473982, f"Unexpected word total: {words}"

expected = {(r['category_code'], r['source_document_type'], r['records']) for r in source}
for name, table in (('source_year_coverage.csv', coverage), ('quality_flags_by_source.csv', quality)):
    got = {(r['category_code'], r['source_document_type'], r['records']) for r in table}
    assert got == expected, f"{name} categories or record counts differ from source_summary.csv"
    for r in table:
        for key, value in r.items():
            if key not in ('category_code', 'source_document_type', 'first_date', 'last_date', 'sparse_years'):
                assert 0 <= int(value) <= int(r['records']), f"{name}: {r['category_code']} {key} out of range"

undated = sum(int(r['undated_records']) for r in coverage)
before_2004 = sum(int(r['date_out_of_window']) for r in quality)
assert count - undated - before_2004 == 75387, "Records dated 2004-2026 should total 75,387"

# Nothing in the public files may carry a source locator or a text hash.
for path in ROOT.rglob('*'):
    if path.is_file() and path.suffix in ('.csv', '.md', '.cff'):
        text = path.read_text(encoding='utf-8')
        assert not re.search(r'https?://(?!creativecommons\.org/|github\.com/JianyunZhao-politics/IPTC)', text), f"URL found in {path.name}"
        assert not re.search(r'\b[0-9a-f]{64}\b', text), f"Hash-like string found in {path.name}"

print(f"Verified: {count:,} source records, {words:,} whitespace-delimited words")
print("Verified: 11 source categories, 21 raw-source mappings, coverage and quality tables consistent")
print(f"Verified: {count - undated - before_2004:,} records dated 2004-2026")
print("Verified: no source URLs or text hashes in public files")
