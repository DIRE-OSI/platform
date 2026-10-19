# Test data

DIRE's open pipelines are designed to be run and validated **without access to restricted or personal data and without external credentials**. This page describes the test data that supports that goal.

## Principles

- **Aggregate only.** Case data are counts by administrative unit and month. No individual records, identifiers, or patient locations are ever included.
- **Clearly labelled.** Synthetic data are marked `SYNTHETIC` in file names and metadata and must never be interpreted as observed surveillance data or as DIRE forecasts.
- **Schema-faithful.** Test data follow the same column structure as the production inputs (see [Data dictionary](DATA_DICTIONARY.md)), so code paths are exercised realistically.

## What is planned

| Dataset | Coverage | Purpose | Status |
|---|---|---|---|
| Synthetic case series | Peru & Brazil · dengue & malaria · monthly | Run the forecasting pipeline end to end | In preparation |
| Synthetic covariate tables | Same units and months | Exercise the covariate join and feature steps | In preparation |
| Example forecast output | 3-month horizon | Illustrate output format and risk tiers | In preparation |

## Worked example

A small synthetic example for two districts of Iquitos, Peru (dengue, monthly, 2015–2025) is available in [`examples/peru-iquitos-dengue`](https://github.com/DIRE-OSI/platform/tree/main/examples/peru-iquitos-dengue), with a generator, a schema check and a data card.

## Using it

Once released, test data will live under `workflows/dengue_forecasting/data/synthetic/`, with a quick-start notebook under `notebooks/`. Installation steps are in [`INSTALL.md`](https://github.com/DIRE-OSI/platform/blob/main/INSTALL.md).

Questions or ideas about test data? Start a [discussion](https://github.com/DIRE-OSI/platform/discussions).
