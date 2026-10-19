# Using the DIRE Dashboard

This guide explains how to read and use the live DIRE dashboard at **<https://dire.impact.nltglobal.com>**. It doubles as a public FAQ for the platform. The dashboard is in **soft launch** — UX/UI and data-quality reviews are underway, and some known issues are being addressed.

> On first visit you'll see a **Disclaimer** and a **Soft Launch** notice. Please read them; they explain that outputs are experimental, decision-support estimates provided "as is." See [DISCLAIMER.md](https://github.com/DIRE-OSI/platform/blob/main/DISCLAIMER.md).

## Layout at a glance

The dashboard has three areas:

1. **Layers panel (left)** — choose what you're looking at.
2. **Map (center)** — a choropleth of administrative units shaded by risk.
3. **Data panel (right)** — Cases, Resources, and Model Indicators for the selected country/area.

A language toggle (e.g., English / Portuguese) and a **Generate Report** action are in the top bar.

## The Layers panel (left)

- **Country** — the geography to view (initial coverage: Peru and Brazil; more being onboarded).
- **Disease** — Dengue or Malaria (more being onboarded).
- **Administrative Level** — the granularity (e.g., Department), down to GADM Level 3 (department/district).
- **Prediction Period** — a slider for the forecast horizon: **Current**, **+1 month**, **+2 months** (i.e., the current month plus the next two).
- **Filters / Risk Level legend** — the five risk tiers, plus two special layers:
  - **Lowest → Highest** — five-tier predicted risk.
  - **Low Confidence Prediction** — the model is less certain for this unit (hatched).
  - **No Data** — insufficient inputs for this unit (grey).
- **Health Centers** — toggle facility locations on the map.
- **Basemap** — the background map style (e.g., Grayscale).

## The map (center)

Each administrative unit is shaded by its risk tier for the selected disease, month, and prediction period. Areas flagged **Low Confidence** or **No Data** are styled distinctly so you can see where to treat estimates with extra caution. Select a unit to see its detailed numbers in the data panel.

## The data panel (right) — three views

- **Cases** — predicted case counts for the current month and the next two, alongside a **Historical Reported Cases** chart (a monthly overview of reported surveillance data). You can **download** the current predictions by administrative unit. *Note: reported data may lag the current month by several weeks depending on the source.*
- **Resources** — resource-allocation estimates derived from predicted incidence (quantity and cost of commodities and personnel needed for control and treatment), to support health-system planning.
- **Model Indicators** — the covariate layers (remote-sensing, climate, socio-economic) and model-performance/uncertainty indicators that feed the forecast.

## Generate Report

Use **Generate Report** in the top bar to export a customized risk report for a chosen geography and time period — predicted incidence maps and tables, risk-tier breakdowns, historical trends, resource recommendations, and data-provenance/confidence notes.

## How to read the forecasts responsibly

- Forecasts are **1-, 2-, and 3-month-ahead estimates** and carry uncertainty that grows with the horizon — always check the **Low Confidence** layer and confidence indicators.
- The platform is a **decision-support** tool; complement it with local knowledge, professional judgment, and official surveillance.

## Questions or problems?

- **How the platform works, the science, the data:** see [ABOUT.md](ABOUT.md) and [RESEARCH_BASIS.md](RESEARCH_BASIS.md).
- **Report a bug or ask a question:** see [SUPPORT.md](https://github.com/DIRE-OSI/platform/blob/main/SUPPORT.md).
- **Feedback on the live dashboard:** use the feedback form on the site.
