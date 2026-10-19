---
title: "Processing pipelines"
nav_order: 9
permalink: /processing/
---
# Processing pipelines

DIRE's forecasts are produced by two pipelines that run in sequence. This directory documents how to run each end to end.

## 1. Predictors pipeline — `workflows/predictors/`

Fetches and engineers the remote-sensing and climate covariates (MODIS, NASADEM, ERA5-Land) into analysis-ready covariate tables per administrative unit and month.

> `predictors-pipeline.md` — full run instructions (inputs, credentials, steps, outputs) will be added here.

## 2. Forecasting pipeline — `workflows/dengue_forecasting/`

Combines the engineered covariates with surveillance case data, runs the ensemble model (CatBoost + SVM + LSTM synthesized by a Random Forest), and produces predicted cases, risk tiers, and confidence intervals per administrative unit per month.

> `forecasting-pipeline.md` — full run instructions will be added here.

## Running without credentials

The forecasting pipeline can be run against the **bundled aggregate test data** in `workflows/dengue_forecasting/data/` without any external API credentials — useful for reproducing results and validating the method. See the pipeline's own README for details.

## Reproducibility

If you reproduce our results or find a discrepancy, please tell us via an [issue](https://github.com/DIRE-OSI/platform/issues). Reproducibility reports are one of the most valuable contributions to an open-science project.
