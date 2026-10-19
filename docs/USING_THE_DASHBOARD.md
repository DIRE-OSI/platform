---
title: "Using the dashboard"
nav_order: 2
---
# Using the DIRE Dashboard

This guide explains how to read and use the live DIRE dashboard at **<https://dire.impact.nltglobal.com>**. It doubles as a public FAQ for the platform. The dashboard is in **beta**: user-experience and data-quality reviews are ongoing, and improvements are released regularly.

{: .note }
On first visit the dashboard shows a short notice explaining that outputs are experimental, decision-support estimates provided "as is", with guidance on how to use the forecasts and a list of known issues. Please read it before using the data. See the [disclaimer](https://github.com/DIRE-OSI/platform/blob/main/DISCLAIMER.md).

## Layout at a glance

The dashboard has three areas:

1. **Layers panel (left)** — choose what you're looking at.
2. **Map (center)** — a choropleth of administrative units shaded by risk.
3. **Data panel (right)** — Cases, Resources, and Model Indicators for the selected country/area.

A language selector (**EN / ES / PT** — English, Spanish, Portuguese), an **About** panel, **release notes** with the current version, and a **Generate Report** action are in the top bar. Forecasts are updated at the start of each month.

## The Layers panel (left)

- **Country** — the geography to view (initial coverage: Peru and Brazil; more being onboarded).
- **Disease** — Dengue or Malaria (more being onboarded).
- **Administrative Level** — the granularity (e.g., Department), down to the finest level available: district for Peru (department → province → district) and municipality for Brazil (state → municipality).
- **Prediction Period** — a slider for the forecast horizon: **Current**, **+1 month**, **+2 months** (i.e., the current month plus the next two).
- **Filters / Risk Level legend** — the five risk tiers, plus two special layers:
  - **Lowest → Highest** — five-tier predicted risk.
  - **Low Confidence Prediction** — units in the lowest of three confidence classes (hatched).
  - **No Data** — insufficient inputs for this unit (grey).
- **Health Centers** — toggle facility locations on the map.
- **Basemap** — the background map style (e.g., Grayscale).

## The map (center)

Each administrative unit is shaded by its risk tier for the selected disease, month, and prediction period. Areas flagged **Low Confidence** or **No Data** are styled distinctly so you can see where to treat estimates with extra caution. Select a unit to see its detailed numbers in the data panel.

## The data panel (right) — three views

- **Cases** — predicted case counts for the current month and the next two, alongside a **Historical Reported Cases** chart (a monthly overview of reported surveillance data). You can **download** predictions or resource estimates as CSV, for the whole country and level or for a selected unit. *Note: reported data may lag the current month by several weeks depending on the source.*
- **Resources** — resource-allocation estimates derived from predicted incidence (quantity and cost of commodities and personnel needed for control and treatment), to support health-system planning.
- **Model Indicators** — the covariate layers (remote-sensing, climate, socio-economic) and model-performance/uncertainty indicators that feed the forecast.

## Generate Report

Use **Generate Report** in the top bar to export a customized risk report for a chosen geography and time period — predicted incidence maps and tables, risk-tier breakdowns, historical trends, resource recommendations, and data-provenance/confidence notes. The report can be downloaded as a PDF.

## How to read the forecasts responsibly

- Forecasts are **1-, 2-, and 3-month-ahead estimates** and carry uncertainty that grows with the horizon — always check the **Low Confidence** layer and confidence indicators.
- The platform is a **decision-support** tool; complement it with local knowledge, professional judgment, and official surveillance.

## Known issues

The dashboard lists current known issues in its notice. At the time of writing these include an ongoing **data-quality review** of predictions and resource estimates, and a review of **consistency between administrative levels** for some Brazil units. Known issues are updated as fixes are released.

## Questions or problems?

- **How the platform works, the science, the data:** see [ABOUT.md](ABOUT.md) and [RESEARCH_BASIS.md](RESEARCH_BASIS.md).
- **Report a bug or ask a question:** see [SUPPORT.md](https://github.com/DIRE-OSI/platform/blob/main/SUPPORT.md).
- **Feedback on the live dashboard:** use the feedback form on the site.
