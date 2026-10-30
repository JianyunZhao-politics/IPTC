# Access and limitations

## What is public

Four aggregate CSV tables, a field dictionary and a checking script are public. There is no searchable full-text corpus and no per-record index.

## What is not distributed

The following are not distributed:

- the working research archive (about 100 GB);
- the political texts and source documents;
- source URLs and page snapshots;
- per-record metadata and text hashes;
- quality adjudication records;
- the collection and extraction pipelines.

Where explicitly requested by journal editors or peer reviewers, the authors may arrange confidential access to relevant materials for verification, case by case and subject to technical feasibility, copyright, the source archives' terms of use and any necessary permissions. Such access confers no right to redistribute third-party archival texts. The long-term aim is to make the complete corpus publicly available through staged releases; no timetable is implied.

## Coverage

| Category | Coverage |
|---|---|
| Archived PMO speeches | 2004-06-24 to 2014-05-17 |
| PIB PMO and PIB MHA releases | 2017-01 onward |
| BJP speeches | 42 records dated 2000–2003; 2 undated; years 2003, 2013, 2017 and 2018 are sparse |
| Lok Sabha Hindi daily texts | Last record 2024-06-27 |
| Lok Sabha English daily texts | Last record 2025-04-04 |
| Rajya Sabha debates | 2005-03-10 to 2025-03-20 |

Other points about coverage:

- **No executive source for 2015–2016.** Neither executive category covers these years, because the archived PMO speeches end in 2014 and the PIB releases begin in 2017.
- **2026 is incomplete.** Collection ended between August and October 2026, depending on the source.
- **Use 2004–2026 for annual analyses.** That window contains 75,387 records.
- **Records are not events.** Counts at the source level do not equal counts of institutional events.
- **Same sitting, several editions.** The Lok Sabha English and original-language daily texts overlap on 1,324 sitting days. The Rajya Sabha debates and floor records overlap on 1,197 sitting days. Keeping one version per sitting would remove 4,120 records (227,259,893 words).

## Text quality

Per-category counts are in `data/quality_flags_by_source.csv`.

- **Truncation.** 1,055 Rajya Sabha debate records are truncated at 300,000 characters, and 771 Lok Sabha Hindi daily texts are flagged as possibly truncated.
- **Legacy fonts.** 1,094 Rajya Sabha floor records and 598 Lok Sabha original-language daily texts contain characters in legacy Hindi font encodings. A further 660 Rajya Sabha debate records keep residue from an earlier conversion.
- **Automated review flags.** 17,090 records are flagged for review by automated checks. A flag marks a record for inspection; it does not confirm an error.
- **Human audit.** A stratified human audit of 330 records found that 56.9% were fully correct on a strict composite criterion (weighted; 95% CI 49.9–64.0%). This is not a general measure of transcription accuracy.
- **Language labels.** The Hindi and English labels come from the archives. They are not a validated, aligned language annotation.
- **Exact duplicates.** Matching text hashes do not establish semantic, translation or event equivalence.
