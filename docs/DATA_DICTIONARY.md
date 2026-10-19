# Data dictionary

This page describes the **structure** of DIRE's analysis-ready inputs and outputs. All tables are keyed by administrative unit and month. Field names are indicative and will be confirmed against each pipeline release; units and meanings are stable.

## Keys

| Field | Type | Description |
|---|---|---|
| `country` | text | ISO 3166-1 alpha-3 code (`PER`, `BRA`) |
| `admin_level` | integer | Administrative level: 1 (department / state), 2 (province / micro-region), 3 (district / municipality) |
| `admin_id` | text | Stable unit identifier (national geocode, cross-walked to GADM) |
| `admin_name` | text | Unit name as published by the national statistics office |
| `year`, `month` | integer | Calendar year and month of the observation or forecast |
| `disease` | text | `dengue` or `malaria` |

## Surveillance inputs (aggregate)

| Field | Unit | Description |
|---|---|---|
| `cases_total` | count | Reported cases, all ages, in the unit and month |
| `cases_0_19` | count | Reported cases, ages 0–19 |
| `dir_total` | per 100,000 | Disease Incidence Rate, all ages |
| `dir_0_19` | per 100,000 | Disease Incidence Rate, ages 0–19 |
| `data_status` | text | `final`, `provisional`, or `filled` (recent months estimated because of reporting delay) |

## Covariates

| Group | Example fields | Unit | Source |
|---|---|---|---|
| Temperature | `t2m_mean`, `t2m_min`, `t2m_max` | °C | ERA5-Land |
| Precipitation | `precip_total` | mm / month | ERA5-Land |
| Humidity | `rh_mean` (or dew point) | % | ERA5-Land |
| Vegetation | `ndvi_mean`, `evi_mean` | index (−1 to 1) | MODIS |
| Land cover | `lc_<class>_frac` | fraction of unit area | MODIS |
| Terrain | `elev_mean` | m | NASADEM |
| Population | `pop_total`, `pop_0_19`, `pop_density` | persons, persons/km² | National census |
| Settlement & housing | `urban_frac`, `households` | fraction, count | National census |
| Lags | `<field>_lag1` … `<field>_lagN` | as base field | Derived |

## Forecast outputs

| Field | Unit | Description |
|---|---|---|
| `issue_month` | YYYY-MM | Month the forecast was produced |
| `horizon` | months | 0 (current month), 1, or 2 |
| `target_month` | YYYY-MM | Month being forecast |
| `pred_cases` | count | Expected cases, all ages |
| `pred_dir_total`, `pred_dir_0_19` | per 100,000 | Predicted incidence rates |
| `risk_tier` | 1–5 | Relative risk tier (Lowest → Highest) |
| `low_confidence` | boolean | Elevated uncertainty or sparse inputs |

## Synthetic data

Synthetic test files follow the same schema and add `is_synthetic = true` to every row. See [Test data](TEST_DATA.md).
