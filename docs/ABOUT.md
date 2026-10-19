# About DIRE

DIRE (Disease Incidence and Resource Estimator) is a machine-learning forecasting platform that produces 1-, 2-, and 3-month-ahead dengue and malaria incidence estimates — the current month plus the following two — at the sub-national administrative level for Peru and Brazil. It is designed to help public-health decision-makers, epidemiologists, and humanitarian responders anticipate disease burden and allocate resources before outbreaks peak.

## The diseases

**Dengue** is a mosquito-borne viral infection transmitted primarily by *Aedes aegypti*. Its incidence is strongly influenced by temperature, rainfall, humidity, and land cover, which shape mosquito breeding and viral replication. Dengue burden in the Americas has risen sharply in recent years, making early risk signals valuable for vector-control and clinical-capacity planning.

**Malaria**, transmitted by *Anopheles* mosquitoes, remains a significant burden in parts of the Amazon basin. Its transmission is likewise sensitive to environmental and climatic conditions, and to human movement and land use.

## How the forecasts are made

DIRE integrates four families of inputs:

- **Remote-sensing covariates** — NASA Earthdata: MODIS land cover and vegetation indices, and NASADEM elevation.
- **Climate covariates** — Copernicus ERA5-Land reanalysis: temperature, precipitation, and humidity.
- **Epidemiological surveillance** — Brazil's DATASUS SINAN and Peru's MINSA reported case records.
- **An ensemble model** — CatBoost, SVM, and LSTM models whose outputs are synthesized by a Random Forest, following the methodology of Sebastianelli et al. (2024).

Forecasts are produced at **GADM Level 3** (department/district) granularity for a rolling horizon of the current month and the following two months (1-, 2-, and 3-month-ahead), mapped to five risk tiers (Lowest → Highest), and refreshed monthly. A low-confidence indicator flags estimates with elevated uncertainty, and a no-data indicator marks units without sufficient inputs.

The dashboard surfaces three analytical views: **Cases** (predicted and historically reported case counts, with a monthly overview of reported data), **Resources** (resource-allocation estimates derived from predicted incidence, to support health-system planning), and **Model Indicators** (the covariate layers and model-performance metrics that feed the ensemble). Reported surveillance data may lag the current month by several weeks depending on the source.

## Intended use

DIRE is a **decision-support** tool. It is intended to complement — not replace — professional judgment, local knowledge, and official surveillance. Please read the [DISCLAIMER](https://github.com/DIRE-OSI/platform/blob/main/DISCLAIMER.md) for the full terms and model limitations.

## References

- Sebastianelli, A., et al. (2024). *A reproducible ensemble machine learning approach to forecast dengue outbreaks.* Scientific Reports, 14, 3807. DOI: [10.1038/s41598-024-52796-9](https://doi.org/10.1038/s41598-024-52796-9)

For how the models are built and evaluated, see [Methods](METHODS.md). For data-source details and licenses, see [data-sources/](data-sources/). For pipeline run instructions, see [processing/](processing/).
