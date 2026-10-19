# Research basis & references

DIRE builds on peer-reviewed work on machine-learning forecasting of mosquito-borne disease from environmental and socio-demographic data, adapted for operational, sub-national use in Peru and Brazil.

## Core methodology

- **Sebastianelli, A., et al. (2024).** *A machine learning approach to dengue and malaria incidence forecasting.* *Scientific Reports.* DOI: [10.1038/s41598-024-52796-9](https://doi.org/10.1038/s41598-024-52796-9)

  The study combines Earth-observation and climate covariates with surveillance data in an ensemble of complementary learners. DIRE adopts this ensemble approach as its starting point and extends it for monthly, multi-horizon, multi-level (administrative 1–3) operational forecasting. See [Methods & model card](METHODS.md) for how DIRE implements and evaluates the approach.

## Scientific rationale

- **Climate and environment shape transmission.** Temperature, rainfall, humidity, vegetation and land cover influence vector breeding, survival and viral replication, with lagged effects of several weeks to months. These relationships make short-horizon forecasting feasible.
- **Recent incidence carries strong signal.** Case counts in recent months are among the most informative predictors; reporting delays therefore directly affect forecast quality (see [Methods & model card](METHODS.md#known-limitations)).
- **Population structure matters.** Census-derived population, age structure, urbanisation and housing inform both incidence rates and the conversion of rates into expected cases and resource needs.

## Data foundations

| Domain | Source | Documentation |
|---|---|---|
| Climate reanalysis | Copernicus ERA5-Land | [Copernicus CDS](data-sources/copernicus-cds.md) |
| Remote sensing & terrain | NASA MODIS, NASADEM | [NASA Earthdata](data-sources/nasa-earthdata.md) |
| Surveillance (Brazil) | DATASUS / SINAN | [Brazil DATASUS / SINAN](data-sources/datasus-sinan.md) |
| Surveillance (Peru) | MINSA / CDC Perú | [Peru MINSA](data-sources/peru-minsa.md) |
| Population & housing | National censuses (Brazil 2010, 2022; Peru 2007, 2017) | — |

## From forecasts to resources

DIRE translates predicted cases into indicative **resource needs**: prevention (vector control, community education, awareness), diagnosis, treatment (general and intensive care), and program operations, with associated costs. Parameters are program- and country-specific and are documented as they are released. Resource estimates are planning aids, not prescriptions.

## How to cite DIRE

Please cite both the software and the methodology paper. Citation metadata is maintained in [`CITATION.cff`](https://github.com/DIRE-OSI/platform/blob/main/CITATION.cff); GitHub's **"Cite this repository"** button generates APA and BibTeX. An archival DOI will be added with the first tagged release (see [Roadmap](ROADMAP.md)).
