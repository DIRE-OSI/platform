# Data source: Brazil DATASUS / SINAN

DIRE uses Brazil's notifiable-disease surveillance (**SINAN**, via **DATASUS**) for reported **dengue** and **malaria** case records.

## What DIRE uses

- **SINAN** — *Sistema de Informação de Agravos de Notificação* (Notifiable Diseases Information System), the national reporting system that includes dengue and malaria notifications.
- Accessed and processed with the open-source R package **`microdatasus`**:
  **<https://github.com/rfsaldanha/microdatasus>** (Saldanha et al.). It downloads and parses DATASUS public microdata (`.dbc` files) and helps aggregate them.

## Access

1. Install the R package:
   ```r
   # install.packages("remotes")
   remotes::install_github("rfsaldanha/microdatasus")
   ```
2. Fetch and process SINAN dengue/malaria data for the states and periods of interest, then **aggregate to administrative unit × month**.

No credentials are required — DATASUS microdata are **public**.

## Privacy & aggregation

DATASUS microdata are individual notification records. **DIRE uses only aggregate counts** (by administrative unit and month) and does **not** ingest or redistribute personal identifiers. Contributors must never commit raw record-level or personally identifiable data to this repository. See [`../../SECURITY.md`](../../SECURITY.md) and [`../../CONTRIBUTING.md`](../../CONTRIBUTING.md).

## Licensing & citation

DATASUS data are public. Cite DATASUS / Brazilian Ministry of Health, and the `microdatasus` package for the processing tooling.

## Notes for DIRE

- Reported surveillance data can **lag** the current month by weeks and are subject to revision.
- No credentials are needed to run the forecasting pipeline against the bundled/synthetic test data.
