# Data source: Peru MINSA surveillance

DIRE uses Peru's national health-surveillance data (**MINSA** — Ministerio de Salud) for reported **dengue** and **malaria** cases, published by Peru's national epidemiology center (**CDC Perú** — Centro Nacional de Epidemiología, Prevención y Control de Enfermedades).

## What DIRE uses

- Notified dengue and malaria cases by **district (distrito)** and week/month, from Peru's epidemiological surveillance (*vigilancia epidemiológica*).
- Published through MINSA/CDC Perú channels, including the **Sala de Situación de Salud** and Peru's open-data portal (**datosabiertos.gob.pe**).

## Access

- Peru surveillance data are **public**. Obtain the relevant dengue/malaria series
  from the CDC Perú / MINSA published datasets (open-data portal or the
  epidemiological surveillance releases), then **aggregate to administrative unit × month**.
- No credentials are required.

> Exact dataset URLs on Peru's portals change over time — locate the current
> "dengue" / "malaria" vigilancia epidemiológica dataset on the official MINSA /
> CDC Perú / datosabiertos.gob.pe portal.

## Privacy & aggregation

DIRE uses only **aggregate** case counts by administrative unit and month; no personal or locational patient data are ingested or redistributed. See [`../../SECURITY.md`](../../SECURITY.md).

## Licensing & citation

Cite MINSA / CDC Perú as the source of Peru surveillance data, per the terms of the relevant open-data portal.

## Notes for DIRE

- **Loreto** accounts for the large majority of Peru's malaria burden — expect strong spatial concentration in the Amazon basin.
- Reported data may **lag** and be revised.
- No credentials are needed to run the forecasting pipeline against the bundled/synthetic test data.
