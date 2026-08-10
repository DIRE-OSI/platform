# Dependencies

This document lists the languages, tools, and major libraries the DIRE pipelines depend on, to satisfy the open-source "running documentation" requirement (dependencies & versions documented). Exact pinned versions are declared in each pipeline's environment files (`pyproject.toml` / `uv.lock` under `workflows/*`), which are the source of truth.

## Languages & runtimes

| Component | Requirement |
|---|---|
| Python | 3.11+ (3.12 recommended) |
| R | 4.5+ |
| `uv` (Python env manager) | latest |

## Python (indicative major libraries)

Declared and pinned per pipeline in `workflows/predictors/` and `workflows/dengue_forecasting/`:

- **Data/compute:** `numpy`, `pandas`, `xarray`, `pyarrow`
- **Geospatial:** `rasterio`, `rioxarray`, `geopandas`, `shapely` *(as used by the covariate pipeline)*
- **Modelling:** `catboost`, `scikit-learn` (SVM, Random Forest), a deep-learning backend for the **LSTM** (e.g., `tensorflow`/`keras` or `torch`)
- **Data acquisition:** `cdsapi` (Copernicus CDS), Earthdata access utilities

## R (indicative packages)

- **`microdatasus`** — Brazil DATASUS/SINAN download & processing
- Standard tidyverse/data packages as used by the forecasting steps

## External data sources (credentials & licences)

See [`docs/data-sources/`](docs/data-sources/):

| Source | Credential | Licence |
|---|---|---|
| NASA Earthdata (MODIS, NASADEM) | Earthdata user token | Open / free |
| Copernicus CDS (ERA5-Land) | CDS API key | Copernicus licence (attribution) |
| Brazil DATASUS / SINAN | none (public) | Public |
| Peru MINSA / CDC Perú | none (public) | Public |

## How versions are pinned

Each pipeline uses `uv` with a lockfile, so `uv sync` reproduces the exact environment. When adding a dependency, update the pipeline's `pyproject.toml` and commit the refreshed lockfile so reproducibility is preserved.
