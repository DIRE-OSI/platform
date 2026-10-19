# Methods

This page summarises, in preliminary form, how DIRE produces its estimates, how they are evaluated, and where they should and should not be relied upon. It follows the structure of a *model card*. Methods are under active development and this description will be refined as the open workflows are released.

## Summary

| | |
|---|---|
| **Task** | Short-horizon estimation of monthly dengue and malaria incidence |
| **Setting** | Peru and Brazil; administrative levels 1–3 (e.g. department / province / district) |
| **Horizons** | Current month and the following two months |
| **Target** | Disease Incidence Rate (DIR, cases per 100,000) for the total population and for ages 0–19, converted to expected case counts |
| **Approach** | Stacked ensemble of complementary learners, building on Sebastianelli *et al.* (2024) |
| **Update cycle** | Monthly estimation; periodic retraining as new surveillance data become available |
| **Outputs** | Expected cases, relative risk tiers, confidence classes and indicative resource requirements |

## Data

| Domain | Product / source | Processing |
|---|---|---|
| Climate | Copernicus ERA5-Land hourly reanalysis (0.1°): 2 m air and dew-point temperature, precipitation, surface pressure, 10 m wind | Aggregated to monthly values (precipitation totals; temperature mean, minimum and maximum; other variables averaged); humidity derived from temperature and dew point; zonal means per administrative unit |
| Vegetation | NASA MODIS MOD13A3 (v6.1), monthly, 1 km | Zonal statistics per administrative unit |
| Land cover | NASA MODIS MCD12Q1 (v6.1), annual, 500 m | Class proportions per administrative unit |
| Terrain | NASADEM (~30 m) | Summary elevation statistics, computed once |
| Population and socio-economic context | National censuses: Brazil 2010 and 2022 (IBGE); Peru 2007 and 2017 (INEI) | Housing, water and sanitation, electricity, literacy and population structure per unit |
| Surveillance | Brazil DATASUS/SINAN; Peru national epidemiological surveillance | Aggregated to monthly counts per administrative unit; total and ages 0–19 |

See [Data sources](data-sources/README.md) for access and licensing, and the [Data dictionary](DATA_DICTIONARY.md) for structure.

## Modelling approach

1. **Preparation.** Inputs are checked for temporal continuity, aligned to a common unit-by-month grid and scaled. Covariates are grouped (climate, geographic, socio-economic) and reduced in dimension. Seasonality is represented with cyclical month encoding. All scaling and reduction steps are fitted on training data only and reused unchanged at estimation time, to avoid information leakage.
2. **Base learners.** Gradient-boosted decision trees (CatBoost), support-vector regression and a recurrent neural network (LSTM) are trained on sequences of recent observations; a short-term polynomial trend provides an additional signal.
3. **Ensemble.** A random-forest meta-learner combines the base-learner outputs into a final estimate.
4. **Horizons.** Estimates are produced for the current month and the following two. Horizon-specific models, which allow each lead time to be trained and evaluated separately, are being evaluated for an upcoming release.
5. **Reporting delay.** Where recent surveillance data are not yet available, missing months are provisionally filled using a data-driven procedure before estimation. This procedure is under continued evaluation.
6. **Cross-level consistency.** Estimates at different administrative levels are reconciled so that sub-national values are coherent with higher-level totals.

## Evaluation design

- **Held-out testing.** Models are trained and tuned on earlier periods and assessed on more recent periods withheld from training.
- **Metrics.** Root-mean-square error (RMSE), normalised RMSE (NRMSE) and the coefficient of determination (R²), reported by horizon, administrative level and disease.
- **Reference forecasts.** Performance is compared with simple baselines, such as the historical average for the same calendar month.
- **Confidence classes.** Unit-level validation error (NRMSE) is used to assign three relative confidence classes (high, medium, low); units in the lowest class are flagged on the dashboard.
- **Partner review.** Outputs are reviewed with in-country public-health partners before major updates are published.

Evaluation summaries will be published as they are finalised.

## Outputs and interpretation

- **Expected cases** by unit, month and horizon.
- **Risk tiers** (lowest to highest) as a relative guide to expected burden. In the current beta, a unit's tier reflects both its expected incidence rate and its expected case count, using provisional cut-points that are being evaluated with partners; tiers are not epidemic thresholds.
- **Confidence classes** (high, medium, low), with low-confidence units flagged; **no data** where inputs are insufficient.
- **Resource estimates** that translate expected cases into indicative requirements for prevention, diagnosis, treatment and programme operations (see [Research basis](RESEARCH_BASIS.md#from-estimates-to-resources)).

## Known limitations

- **Reporting delay and revision.** Recent surveillance data are often provisional and subsequently revised.
- **Uncertainty increases with horizon.** Estimates for later months are generally less certain.
- **Low-count settings.** Units with few cases yield noisier relative errors.
- **Novel conditions.** Unusual climatic events, changes in circulating serotypes, interventions or reporting practices may not be represented in historical data.
- **Static socio-economic inputs.** Census-derived indicators are updated infrequently.
- **Data dependencies.** Some inputs rely on periodic deliveries from national partners.

## Intended use

DIRE is a **decision-support** resource for planning and situational awareness by public-health agencies, researchers and humanitarian organisations. It complements, and does not replace, official surveillance, local knowledge and professional judgement, and is not intended for individual clinical decisions or as an official case count. See the [disclaimer](https://github.com/DIRE-OSI/platform/blob/main/DISCLAIMER.md).
