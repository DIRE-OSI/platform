# Installation

This guide sets up the DIRE processing pipelines locally. The **forecasting pipeline can be run against the bundled/synthetic test data with no external credentials** — credentials are only needed to refresh covariates and surveillance data from source.

## Prerequisites

| Tool | Version | Purpose |
|---|---|---|
| Python | 3.11+ (3.12 recommended) | Pipelines |
| R | 4.5+ | Parts of the forecasting pipeline; DATASUS (`microdatasus`) |
| [`uv`](https://docs.astral.sh/uv/) | latest | Python environment/dependency manager |
| Git | any recent | Clone the repo |
| Docker | optional | Containerised runs |

## 1. Clone

```bash
git clone https://github.com/DIRE-OSI/platform.git
cd platform
```

## 2. Install Python dependencies

Each pipeline manages its own environment with `uv`:

```bash
# Predictors (remote-sensing + climate) pipeline
cd workflows/predictors && uv sync && cd ../..

# Dengue/malaria forecasting pipeline
cd workflows/dengue_forecasting && uv sync && cd ../..
```

## 3. Install R dependencies (if fetching Brazil surveillance data)

```r
# install.packages("remotes")
remotes::install_github("rfsaldanha/microdatasus")
```

See [`docs/data-sources/datasus-sinan.md`](docs/data-sources/datasus-sinan.md).

## 4. Configure credentials (only to refresh data from source)

```bash
cp .env.example .env
# then edit .env:
#   EARTHDATA_TOKEN=...   (free — docs/data-sources/nasa-earthdata.md)
#   CDS_API_KEY=...       (free — docs/data-sources/copernicus-cds.md)
```

See [`DEPENDENCIES.md`](DEPENDENCIES.md) for the full dependency list and pinned versions, and [`docs/processing/`](docs/processing/) to run a pipeline.

## 5. Run against test data (no credentials)

The forecasting pipeline can run end-to-end against the bundled/synthetic aggregate data. See [`docs/processing/`](docs/processing/) and [`docs/TEST_DATA.md`](docs/TEST_DATA.md).

## Troubleshooting

- **Earthdata token expired** → regenerate it (tokens are short-lived); see the NASA guide.
- **CDS request hangs or 401** → confirm `~/.cdsapirc` points at the new `https://cds.climate.copernicus.eu/api` and that you accepted the ERA5-Land licence.
- **`uv` not found** → install from <https://docs.astral.sh/uv/>.
