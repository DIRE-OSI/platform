# Data source: Copernicus Climate Data Store (ERA5-Land)

DIRE uses **ERA5-Land** climate reanalysis from the Copernicus **Climate Data Store (CDS)** as climate covariates: temperature, precipitation, and humidity. Free with an ECMWF/CDS account.

## What DIRE uses

| Product | Variables | Role in DIRE |
|---|---|---|
| **ERA5-Land** (hourly, aggregated to monthly) | 2 m temperature, total precipitation, humidity-related fields | Climate drivers of vector dynamics and transmission |

## 1. Create a free CDS account

Register at **<https://cds.climate.copernicus.eu/>** (ECMWF login).

> The CDS was migrated to a **new system**; the current API setup is documented at
> **<https://cds.climate.copernicus.eu/how-to-api>**. If you have an old `~/.cdsapirc`
> pointing at the legacy `.../api/v2` URL, update it (see below).

## 2. Get your API key

- On the CDS site, open your **profile page** — it shows your personal **API key**.
- Configure the `cdsapi` client by creating `~/.cdsapirc`:

  ```
  url: https://cds.climate.copernicus.eu/api
  key: <YOUR-API-KEY>
  ```
- For this repo, also record the key as `CDS_API_KEY=...` in your `.env` (see [`.env.example`](../../.env.example)).

## 3. Accept the dataset licence

Before the first download, open the **ERA5-Land** dataset page on the CDS and **accept its licence terms** (Copernicus licence) under the "Download" / "Terms of use" tab — required once per account.

## 4. Access

Install and use the Python client:

```bash
pip install cdsapi
```

Requests are queued by the CDS and may take time depending on load. See
<https://cds.climate.copernicus.eu/how-to-api> for current request syntax.

## Licensing & citation

ERA5-Land is distributed under the **Copernicus licence** — free to use and redistribute with attribution. Cite: "Generated using Copernicus Climate Change Service information [year]; ERA5-Land, Copernicus Climate Data Store." Neither the European Commission nor ECMWF is responsible for any use of the data.

## Notes for DIRE

- DIRE aggregates ERA5-Land to monthly values per administrative unit.
- No credentials are required to run the forecasting pipeline against the bundled/synthetic test data — the CDS is only needed to refresh climate covariates from source.
