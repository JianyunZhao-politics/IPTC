# Data dictionary

## Public tables

**`source_summary.csv`**

| Column | Meaning |
|---|---|
| `category_code` | Category code, A to K |
| `institutional_domain` | Executive, Party, Lok Sabha or Rajya Sabha |
| `source_document_type` | The 11 analytical categories |
| `archival_language_labels` | Language labels used by the source archive |
| `records` | Number of records in the category |
| `whitespace_delimited_words` | Total whitespace-delimited words in the retained text |

**`source_mapping.csv`**

| Column | Meaning |
|---|---|
| `raw_source_label` | One of the 21 upstream source labels |
| `analytical_source_category` | The category the label is mapped to |

**`source_year_coverage.csv`**

| Column | Meaning |
|---|---|
| `category_code`, `source_document_type` | As in `source_summary.csv` |
| `records` | Number of records in the category |
| `undated_records` | Records without a documentary date |
| `first_date`, `last_date` | Earliest and latest documentary dates |
| `years_with_records` | Number of calendar years that contain at least one record |
| `sparse_years` | Years with fewer than 10 records; the count is in parentheses |

**`quality_flags_by_source.csv`**

Each flag column gives the number of records in the category that carry the flag. A record can carry more than one flag.

| Column | Meaning |
|---|---|
| `missing_date` | No documentary date |
| `date_out_of_window` | Dated before 2004 |
| `review_pending` | Flagged by automated checks for review (not a confirmed error) |
| `ocr_noise_high` | High extraction or OCR noise score |
| `legacy_font_encoding` | Contains characters in a legacy Hindi font encoding |
| `legacy_conversion_residue` | Contains residue from an earlier legacy-font conversion |
| `text_truncated_300k` | Text stored only up to 300,000 characters |
| `text_truncated_hindi_daily` | Lok Sabha Hindi daily text that may be truncated |

## Category names

- **Lok Sabha English Part 2 debate sample** is a sample of records from Lok Sabha Debates Part II (proceedings other than questions and answers). It does not cover the whole Part II series.
- **Lok Sabha Questions** are drawn from the Part I (questions and answers) catalogue.

## Fields in the internal archive

These fields are documented for reference only. None of their values are published in this repository.

| Field | Description |
|---|---|
| `doc_id` | Internal identifier. Some identifiers embed source locators, so they are not suitable for publication. Any future public index would assign new identifiers. |
| `source` | Upstream source label (see `source_mapping.csv`) |
| `layer`, `text_source` | Where the adopted text representation came from |
| `lang` | Language label from the source archive |
| `lang_by_script` | Language assigned from the script of the characters (added in v1.1; `lang` is unchanged) |
| `date_iso` | Documentary date where supported. Missing dates stay missing and are not imputed. |
| `date_source` | Where the date came from (added in v1.1) |
| `date_iso_v1_0` | Date before the v1.1 revision (BJP records only) |
| `title`, `title_source`, `title_v1_0` | Title, where it came from, and the value before v1.1 |
| `url`, `url_original` | Source locator. Not published. |
| `text_sha256` | Hash of the retained text, used to detect exact duplicates. Not published. |
| `flags`, `issues`, `issues_v1_0` | Quality flags and issues in v1.1, plus the issue list before v1.1 |
| `noise_score` | Extraction noise score |

Derived quantities:

- **Year** is taken from a full `date_iso`.
- **Words** is the whitespace-delimited count of the retained text.
