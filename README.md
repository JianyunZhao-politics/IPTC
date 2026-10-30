# Indian Political Text Corpus (IPTC v1.1): aggregate metadata release

This repository is an **aggregate metadata release** for the frozen IPTC v1.1 collection, with a checking script that uses only the Python standard library. It is not the corpus itself and not a full data release. It contains no political texts and no per-record metadata. It also leaves out source PDF or HTML files, page snapshots, source URLs, text hashes and the collection or extraction pipelines.

The frozen IPTC v1.1 archive, which is not included here, contains **75,431** records and **524,473,982** whitespace-delimited words, drawn from 11 source and document-type categories.

## Contents

| File | Content |
|---|---|
| `data/source_summary.csv` | Records and words for each of the 11 source categories |
| `data/source_mapping.csv` | How the 21 upstream source labels map onto the 11 categories |
| `data/source_year_coverage.csv` | Each category's first and last documentary date, undated records, and sparse years |
| `data/quality_flags_by_source.csv` | How many records in each category carry each main quality flag |
| `docs/DATA_DICTIONARY.md` | Definitions of the record-level fields in the internal archive and of the columns in the tables above |
| `docs/ACCESS_AND_LIMITATIONS.md` | Access terms, coverage gaps and known quality issues |
| `scripts/check_public_release.py` | Checks that the tables are consistent with one another and with the frozen totals |

To run the check:

```
python scripts/check_public_release.py
```

## Interpretation

- **Source-defined collection.** IPTC is defined by its sources. It is not a census of Indian political communication.
- **Collection window and uneven coverage.** The principal window is 2004–2026, and coverage differs by source (see `data/source_year_coverage.csv`):
  - The two Press Information Bureau (PIB) categories start in 2017.
  - The archived Prime Minister's Office speeches cover June 2004 to May 2014.
  - No executive source therefore covers 2015–2016.
- **Out-of-window and undated records.** 42 BJP records are dated 2000–2003 and 2 are undated. Analyses by year should use the 75,387 records dated 2004–2026.
- **Incomplete year.** 2026 is incomplete in every source that reaches it.
- **Word counts.** These are whitespace-delimited counts of the retained text, not harmonised multilingual tokens.
- **Party coverage.** The collection includes BJP speeches. It does not include an Indian National Congress archive.
- **Overlapping parliamentary editions.** Several parliamentary editions can describe the same sitting:
  - The Lok Sabha English and original-language daily texts overlap on 1,324 sitting days.
  - The Rajya Sabha debates and floor records overlap on 1,197 sitting days.
  - Keeping one version per sitting would remove 4,120 records and 227,259,893 words.
- **Known quality issues.** These include truncation, legacy-font encoding and extraction noise; see `docs/ACCESS_AND_LIMITATIONS.md`.

## Licence and citation

- **Tables and documentation** (`data/`, `docs/`, this README): [CC BY 4.0](LICENSE-DATA.md). Reuse requires attribution.
- **Code** (`scripts/`): [MIT](LICENSE).
- **Citation:** Zhao, J., Chen, Y., & Ho, M. (2026). *Indian Political Text Corpus (IPTC) v1.1: Public aggregate metadata and verification code* (Version 1.1-metadata-1) [Data set]. GitHub. https://github.com/JianyunZhao-politics/IPTC (see also `CITATION.cff`).

These licences cover only the aggregate metadata and code written by the authors. They grant no rights over the official source documents on which the counts are based.

## Version

The figures describe the frozen IPTC v1.1 release. A later release (v2.0) is planned. Its contents and access terms will be documented when it is released, and nothing in this repository promises them.
