# Predictors pipeline

**Python pipeline — remote-sensing & climate covariates.**

This pipeline fetches and engineers the environmental predictors used by the DIRE forecasting model, turning raw satellite and climate products into analysis-ready covariate tables keyed by administrative unit and month.

## Inputs

- **NASA Earthdata** — MODIS land cover and vegetation indices; NASADEM elevation. Requires a free `EARTHDATA_TOKEN` (see [../../docs/data-sources/](../../docs/data-sources/)).
- **Copernicus CDS** — ERA5-Land temperature, precipitation, humidity. Requires a free `CDS_API_KEY`.

## Outputs

- Per-admin-unit, per-month covariate tables consumed by the forecasting pipeline.

## Status

🚧 **Phase 0** — this directory documents the pipeline's role and interface. The full source and step-by-step run guide are being prepared for public release; see [../../docs/ROADMAP.md](../../docs/ROADMAP.md) and [../../docs/processing/](../../docs/processing/).

Want to help shape or reproduce this pipeline? See [Get Involved](../../README.md#-get-involved).
