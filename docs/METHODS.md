# Methods & model card

This page summarises how DIRE produces its forecasts, how they are evaluated, and where they should and should not be relied on. It follows the spirit of a *model card*: a short, structured description intended for researchers, public-health users and reviewers. Methods are under active development; this page is updated as the open pipelines are released.

## At a glance

| | |
|---|---|
| **Task** | Short-horizon forecasting of monthly dengue and malaria incidence |
| **Geography** | Peru and Brazil, at administrative levels 1–3 (e.g., department / province / district) |
| **Horizons** | Current month, +1 month, +2 months (one model per horizon) |
| **Target** | Disease Incidence Rate (DIR, cases per 100,000), for the total population and ages 0–19, converted to expected case counts |
| **Approach** | Stacked ensemble of complementary learners, after [Sebastianelli et al. (2024)](RESEARCH_BASIS.md) |
| **Refresh** | Monthly, as new surveillance and climate data become available |
| **Outputs** | Expected cases, five-tier relative risk, low-confidence flag, indicative resource needs |

## Inputs

- **Climate:** temperature, precipitation and humidity from Copernicus ERA5-Land, aggregated to administrative unit × month, including lagged values.
- **Environment:** vegetation indices and land cover (NASA MODIS) and elevation (NASADEM).
- **Population & housing:** census-derived population, age structure, urbanisation and housing characteristics.
- **Recent incidence:** aggregate reported cases by administrative unit and month from national surveillance (Brazil DATASUS/SINAN; Peru MINSA/CDC Perú).

See [Data sources](data-sources/README.md) for access, licensing and caveats.

## Modelling approach

1. **Preparation.** Inputs are cleaned, aligned to a common administrative-unit × month grid, and scaled. Scaling and dimensionality-reduction steps are fitted on training data only and reused unchanged at forecast time, to avoid information leakage.
2. **Base learners.** Gradient-boosted trees (CatBoost), a support-vector regressor and a recurrent neural network (LSTM) each learn the relationship between inputs and incidence; a short-term polynomial trend provides an additional signal.
3. **Ensemble.** A random-forest meta-model combines the base-learner predictions into the final estimate.
4. **Horizons.** Separate models are trained for each forecast horizon, so that each is evaluated and tuned for the lead time it serves.
5. **Recent-data gaps.** Surveillance data typically lag by weeks. Missing recent months are filled with a data-driven approach (model-based for the most recent months, historical monthly patterns beyond that) before forecasting. This approach is under continued evaluation.
6. **Cross-level consistency.** Forecasts at different administrative levels are reconciled so that sub-national estimates are coherent with higher-level totals.

## Evaluation

- **Held-out testing.** Models are trained, tuned on a validation period, and assessed on a later test period not used in training, mimicking real forecasting conditions.
- **Metrics.** Normalised root-mean-square error (NRMSE) and related error measures, reported by horizon, administrative level and disease.
- **Baselines.** Performance is compared against simple reference forecasts, such as the historical average for the same calendar month, to show where the model adds value.
- **Partner review.** Outputs are reviewed with in-country public-health partners before major updates are published.

Evaluation summaries will be published here as they are finalised.

## Outputs and how to read them

- **Expected cases** for each unit, month and horizon.
- **Risk tiers** (Lowest → Highest) that rank units relative to one another; they are not epidemic thresholds.
- **Low-confidence flag** where inputs are sparse or uncertainty is elevated; **No data** where inputs are insufficient.
- **Resource estimates** that translate expected cases into indicative prevention, diagnosis, treatment and program needs (see [Research basis](RESEARCH_BASIS.md#from-forecasts-to-resources)).

## Known limitations

- **Reporting delay and revision.** Recent surveillance data are often provisional and later revised; forecasts are updated as data mature.
- **Uncertainty grows with horizon.** The +2-month forecast is generally less certain than the current-month estimate.
- **Low-count areas.** Units with few cases produce noisier relative errors.
- **Novel conditions.** Unusual climate events, new serotypes, interventions or reporting changes may not be reflected in historical training data.
- **Data dependencies.** Some inputs depend on periodic deliveries from national partners.

## Intended use

DIRE is a **decision-support** tool for planning and situational awareness by public-health agencies, researchers and humanitarian responders. It complements — and does not replace — official surveillance, local knowledge and professional judgement. It is **not** intended for individual clinical decisions or as an official case count. See the [disclaimer](https://github.com/DIRE-OSI/platform/blob/main/DISCLAIMER.md).

## Versioning

Methods, parameters and evaluation results are versioned with each tagged release of this repository (see the [Roadmap](ROADMAP.md)).
