# Data sources

DIRE integrates open remote-sensing and climate data with national epidemiological surveillance. Each source below is governed by its own terms and licensing. This directory documents how to obtain credentials, what each source covers, and any usage constraints.

| Source | What it provides | Access | Guide |
|---|---|---|---|
| **NASA Earthdata** | MODIS land cover & vegetation indices; NASADEM elevation | Free account + token | [nasa-earthdata.md](nasa-earthdata.md) |
| **Copernicus CDS** | ERA5-Land temperature, precipitation, humidity | Free account + API key | [copernicus-cds.md](copernicus-cds.md) |
| **Brazil DATASUS / SINAN** | Reported dengue/malaria case records (Brazil) | Public surveillance data | [datasus-sinan.md](datasus-sinan.md) |
| **Peru MINSA / CDC Perú** | Reported dengue/malaria case records (Peru) | Public surveillance data | [peru-minsa.md](peru-minsa.md) |

## Provenance at a glance

| Source | Update cadence | Typical latency | Revisions | Terms |
|---|---|---|---|---|
| NASA Earthdata (MODIS, NASADEM) | 8–16 days (MODIS); static (NASADEM) | Days to weeks | Occasional reprocessing | NASA open data policy; cite products |
| Copernicus ERA5-Land | Monthly / daily | About one week | Final after quality control | Copernicus licence; attribution required |
| Brazil DATASUS / SINAN | Continuous; periodic releases | Weeks to months | Provisional → final releases | Public data; cite Ministry of Health / DATASUS |
| Peru MINSA / CDC Perú | Weekly epidemiological reporting | Weeks | Provisional → consolidated | Per open-data portal terms; cite MINSA / CDC Perú |

Field-level definitions for analysis-ready tables are in the [Data dictionary](../DATA_DICTIONARY.md).

## A note on data ethics

DIRE uses only **aggregate** case counts at administrative-unit granularity. No individual patient records or locational personal data are included in this repository or its bundled test data. Contributors must never commit personally identifiable or locational health data — see [CONTRIBUTING.md](https://github.com/DIRE-OSI/platform/blob/main/CONTRIBUTING.md) and [SECURITY.md](https://github.com/DIRE-OSI/platform/blob/main/SECURITY.md).
