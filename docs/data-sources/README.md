# Data sources

DIRE integrates open remote-sensing and climate data with national epidemiological surveillance. Each source below is governed by its own terms and licensing. This directory documents how to obtain credentials, what each source covers, and any usage constraints.

| Source | What it provides | Access | Guide |
|---|---|---|---|
| **NASA Earthdata** | MODIS land cover & vegetation indices; NASADEM elevation | Free account + token | `nasa-earthdata.md` |
| **Copernicus CDS** | ERA5-Land temperature, precipitation, humidity | Free account + API key | `copernicus-cds.md` |
| **Brazil DATASUS / SINAN** | Reported dengue/malaria case records (Brazil) | Public surveillance data | `datasus-sinan.md` |
| **Peru MINSA** | Reported dengue case records (Peru) | Public surveillance data | `peru-minsa.md` |

> Per-source guides (`nasa-earthdata.md`, `copernicus-cds.md`, `datasus-sinan.md`, `peru-minsa.md`) will be added here. Each will cover signup, credential setup, coverage, temporal resolution, and licensing.

## A note on data ethics

DIRE uses only **aggregate** case counts at administrative-unit granularity. No individual patient records or locational personal data are included in this repository or its bundled test data. Contributors must never commit personally identifiable or locational health data — see [CONTRIBUTING.md](../../CONTRIBUTING.md) and [SECURITY.md](../../SECURITY.md).
