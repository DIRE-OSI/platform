# Data source: Peru MINSA surveillance

DIRE uses Peru's national health-surveillance data (**MINSA** — Ministerio de Salud) for reported **dengue** and **malaria** cases, published by Peru's national epidemiology center (**CDC Perú** — Centro Nacional de Epidemiología, Prevención y Control de Enfermedades).

## What DIRE uses

- Notified dengue and malaria cases by **district (distrito)** and month, from Peru's epidemiological surveillance (*vigilancia epidemiológica*).
- Two inputs are combined:
  - **Base series** from MINSA / CDC Perú surveillance files.
  - **Updates from research collaborators in Peru**, who obtain recent case records from MINSA through Peru's public-information request process and share them with the DIRE team.
- Both inputs are **aggregated to district × month** before they enter the pipeline. Overlapping periods are de-duplicated when the files are combined.

## Access

- MINSA / CDC Perú publish surveillance summaries through the **Sala de Situación de Salud** and Peru's open-data portal (**datosabiertos.gob.pe**). DIRE does not currently download from these portals automatically; files are loaded by the team each update cycle.
- The collaborator deliveries are not redistributed. To reproduce DIRE's Peru inputs independently, request the same records from MINSA or use the published aggregate series.

> Exact dataset URLs on Peru's portals change over time — locate the current
> "dengue" / "malaria" vigilancia epidemiológica dataset on the official MINSA /
> CDC Perú / datosabiertos.gob.pe portal.

## Privacy & aggregation

Some files DIRE receives contain **record-level** case data. These files are kept in restricted storage, are used only to compute aggregate counts by district and month, and are **never published** in this repository, on the dashboard, or in exports. Only aggregate counts are used for modeling and display. See [`SECURITY.md`](https://github.com/DIRE-OSI/platform/blob/main/SECURITY.md).

## Licensing & citation

Cite MINSA / CDC Perú as the source of Peru surveillance data, per the terms of the relevant open-data portal.

## Notes for DIRE

- **Loreto** accounts for the large majority of Peru's malaria burden — expect strong spatial concentration in the Amazon basin.
- Reported data may **lag** and be revised; recent months can change when newer files arrive.
- No credentials are needed to run the forecasting pipeline against the bundled/synthetic test data.
