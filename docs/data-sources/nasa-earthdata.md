# Data source: NASA Earthdata (MODIS & NASADEM)

DIRE uses NASA Earthdata products as remote-sensing covariates: **MODIS vegetation indices** and **land cover**, and **NASADEM elevation**. All are free.

## What DIRE uses

| Product | Short name | Cadence | Role in DIRE |
|---|---|---|---|
| MODIS/Terra Vegetation Indices | **MOD13A3** (v6.1) | Monthly, 1 km | NDVI/EVI — vegetation/greenness proxy for vector habitat |
| MODIS/Terra+Aqua Land Cover Type | **MCD12Q1** (v6.1) | Annual, 500 m | Land-cover class covariates |
| NASADEM Merged DEM | **NASADEM** | Static, 30 m | Elevation/topography |

## 1. Create a free Earthdata Login account

Register at **<https://urs.earthdata.nasa.gov/>**. One account covers all NASA DAACs.

## 2. Generate a user token

Earthdata uses **bearer (user) tokens** for programmatic access.

- In the Earthdata Login profile, open **Generate Token**, or follow the guide at
  <https://urs.earthdata.nasa.gov/documentation/for_users/user_token>.
- Tokens are valid for a limited period (typically ~60 days) and can be regenerated.
- Put the token in your `.env` as `EARTHDATA_TOKEN=...` (see [`.env.example`](../../.env.example)).

> **Token expiry is a recurring operational item** — schedule a reminder to regenerate before expiry so automated fetches don't fail.

## 3. Where the data lives

- MODIS products: **LP DAAC** (served via LAADS/`ladsweb.modaps.eosdis.nasa.gov` and USGS). Downloads accept the EDL bearer token.
- NASADEM: **USGS OPeNDAP** / LP DAAC.

For some services you may also need to authorize the application in your Earthdata profile (Applications → Approved Apps) the first time.

## Licensing & citation

NASA Earth-observation data are generally **open and free of restriction**. Cite the specific product and DAAC (e.g., "MOD13A3 v6.1, NASA LP DAAC"). See each product's landing page for the recommended citation.

## Notes for DIRE

- DIRE ingests these as monthly/annual covariates aggregated to administrative units; raw granules are not redistributed in this repository.
- No credentials are required to run the forecasting pipeline against the bundled/synthetic test data — Earthdata is only needed to refresh covariates from source.
