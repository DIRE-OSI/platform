# Dengue forecasting pipeline

**Python + R pipeline — disease incidence forecasts.**

This pipeline combines the engineered environmental covariates (from `workflows/predictors/`) with reported surveillance case data and runs the ensemble model to produce 1-, 2-, and 3-month-ahead incidence forecasts (the current month plus the following two).

## Method

- **Ensemble model:** CatBoost, SVM, and LSTM base learners whose predictions are synthesized by a Random Forest, following Sebastianelli et al. (2024).
- **Outputs:** predicted case counts, five-tier risk classification, and confidence intervals per GADM Level 3 administrative unit per month.

## Reproducing without credentials

The pipeline can be run against the **bundled aggregate test data** (no personal or locational data) that will ship in `data/` — no external API credentials required. This is the recommended way to reproduce and validate the method.

## Status

🚧 **Phase 0** — this directory documents the pipeline's role and interface. The full source, bundled test data, and run guide are being prepared for public release; see [../../docs/ROADMAP.md](../../docs/ROADMAP.md) and [../../docs/processing/](../../docs/processing/).

Reproducibility reports and improvements are especially welcome — see [Get Involved](../../README.md#-get-involved).
