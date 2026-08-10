# 🦟 DIRE IMPACT Platform

### Disease Incidence and Resource Estimator

**1-, 2-, and 3-month-ahead disease-incidence risk forecasting at sub-national scale**
*Initial coverage: dengue & malaria in Peru and Brazil — additional countries and diseases are being onboarded.*

[🌐 Live Dashboard](https://dire.impact.nltglobal.com) · [ℹ️ About](docs/ABOUT.md) · [👥 Team](docs/TEAM.md) · [📜 Roadmap](docs/ROADMAP.md) · [🤝 Get Involved](#-get-involved)

> 🚧 **Status: Under active development.** This repository is an early, evolving release published **in coordination with the DIRE project team at UC San Diego (UCSD) and New Light Technologies (NLT)**. Its structure, documentation, and included code are being staged and reviewed phase by phase; content may change. It is shared now to enable open review and collaboration — please treat it as work in progress and coordinate with the project team before relying on it.

> ⚠️ **Disclaimer:** All forecasts and analytical outputs are provided "as is" for decision-support purposes only. New Light Technologies, UC San Diego, and UNICEF expressly disclaim all liability for decisions made using these outputs. See [DISCLAIMER.md](DISCLAIMER.md) for full terms.

---

**Phase 0 — initial release (work in progress).** This repository is being populated, in coordination with the project team at **UCSD and NLT**, with the data-source documentation and Python/R processing pipelines for the DIRE IMPACT Platform. It is the open, community-facing home of the project, released under the Wellcome Trust open-source grant conditions. The forecasting API and interactive dashboard are live at [dire.impact.nltglobal.com](https://dire.impact.nltglobal.com); their source code will follow in subsequent phases. See [docs/ROADMAP.md](docs/ROADMAP.md) for the full release plan.

---

## What is DIRE?

DIRE (Dengue Integrated Risk Estimation) is a machine-learning forecasting platform that produces **1-, 2-, and 3-month-ahead disease-incidence estimates** (the current month plus the following two) at the sub-national administrative level. It is designed to support public-health decision-makers, epidemiologists, and humanitarian responders in anticipating disease burden and allocating resources *before* outbreaks peak.

**Coverage is expanding.** Peru and Brazil — and the diseases dengue and malaria — are the **first countries and diseases** being trialed during the platform's development and operations-and-maintenance (O&M) phase. The methodology and pipelines are built to generalize, and **additional countries and diseases are being onboarded** over time. References to Peru, Brazil, dengue, and malaria throughout this repository describe the *current* rollout, not the platform's ultimate scope.

The platform integrates:

- **Remote-sensing covariates** — NASA Earthdata (MODIS land cover + vegetation indices, NASADEM elevation)
- **Climate covariates** — Copernicus ERA5-Land (temperature, precipitation, humidity)
- **Epidemiological surveillance** — Brazil DATASUS SINAN and Peru MINSA dengue case records
- **An ensemble ML model** — CatBoost, SVM, and LSTM models synthesized with a Random Forest, as described in Sebastianelli et al. (2024)

Risk estimates are mapped to five tiers (Lowest → Highest) at **GADM Level 3** (department/district) granularity and are refreshed monthly.

**Partners:** New Light Technologies (NLT) · UC San Diego School of Global Policy and Strategy · Universidad Peruana Cayetano Heredia (UPCH)
**Funder:** Wellcome Trust

---

## 🤝 Get Involved

DIRE is an **open science** project. We built this repository so that researchers, public-health agencies, and the broader open-source community can inspect, reproduce, improve, and build on the work — not just read about it. There are several ways to participate, whatever your background.

### For researchers and epidemiologists
- **Reproduce and validate.** Every processing pipeline in [`workflows/`](workflows/) is documented so you can re-run our covariate engineering and forecasting steps against the bundled aggregate data — no credentials or private data required. See [docs/processing/](docs/processing/).
- **Extend the science.** Propose new covariates, alternative model architectures, additional diseases, or new countries. Open a [discussion](https://github.com/DIRE-OSI/platform/discussions) to sketch an idea before you build it.
- **Cite the work.** If DIRE supports your research, please cite both the software and the underlying methodology paper — see [Citation](#citation).

### For public-health practitioners and responders
- **Use the dashboard.** The live platform at [dire.impact.nltglobal.com](https://dire.impact.nltglobal.com) is free to use for planning and situational awareness.
- **Tell us what you need.** Resource-estimation and reporting features are shaped by real operational needs. File an [issue](https://github.com/DIRE-OSI/platform/issues) describing your use case, the decisions you make, and the outputs that would help.

### For contributors and developers
- **Report issues** — bugs, unclear docs, or reproducibility gaps.
- **Improve documentation** — clarity fixes and translations are especially welcome, given the platform's Peru/Brazil focus (Spanish and Portuguese).
- **Submit pull requests** — see [CONTRIBUTING.md](CONTRIBUTING.md) for the workflow and the Developer Certificate of Origin (DCO) sign-off we require.

### For data and institutional partners
- We work with surveillance data from national health authorities under appropriate agreements. If your institution wants to collaborate on data, validation, or a country expansion, reach out through the channels in [docs/TEAM.md](docs/TEAM.md).

**Community standards.** Participation in this project is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). Please read it before engaging.

---

## Repository contents (Phase 0)

```
platform/
├── docs/
│   ├── data-sources/       # Per-source credential, license & coverage guides
│   ├── processing/         # End-to-end pipeline run instructions
│   ├── ABOUT.md            # Platform description, diseases, data, references
│   ├── TEAM.md             # Project team and partner organisations
│   └── ROADMAP.md          # Phased release plan
├── workflows/
│   ├── predictors/         # Python pipeline: remote-sensing & climate covariates
│   └── dengue_forecasting/ # Python + R pipeline: disease incidence forecasts
├── CITATION.cff            # Machine-readable citation metadata
├── CONTRIBUTING.md         # PR workflow and DCO sign-off
├── CODE_OF_CONDUCT.md      # Community standards
├── LICENSE                 # Apache-2.0 (source code)
├── NOTICE                  # Attribution
├── SECURITY.md             # Vulnerability disclosure
├── DISCLAIMER.md           # Platform disclaimer and liability terms
└── .env.example            # Credential template
```

### What is *not* here yet

| Component | Planned phase |
|---|---|
| Prediction API / backend service | Phase 1 |
| Containerized one-command local runner | Phase 1 |
| Automated test suite + CI | Phase 1 |
| Interactive dashboard source code | Phase 2 |
| Cloud deployment / infrastructure-as-code | Phase 3 |
| Zenodo DOI archive | Phase 3 |

---

## Architecture overview

```
External data sources
  NASA Earthdata (MODIS, NASADEM) ─────────┐
  Copernicus CDS (ERA5-Land) ──────────────┤──► workflows/predictors/
  Brazil DATASUS SINAN ────────────────────┤        │  covariate tables
  Peru MINSA surveillance ─────────────────┘        ▼
                                        workflows/dengue_forecasting/
                                        ├── feature engineering
                                        ├── CatBoost + SVM + LSTM ensemble
                                        └── Random Forest synthesizer
                                                   │
                                                   ▼
                                Forecast outputs (predicted cases, risk tier,
                                confidence interval) by GADM L3 admin unit × month
                                                   │
                                                   ▼
                                dire.impact.nltglobal.com (live dashboard)
```

See [docs/ABOUT.md](docs/ABOUT.md) for the full description and references.

---

## Quickstart

### Prerequisites

| Tool | Version |
|---|---|
| Python | 3.11+ (3.12 recommended) |
| R | 4.5+ |
| uv (Python env manager) | latest |

### 1. Clone

```bash
git clone https://github.com/DIRE-OSI/platform.git
cd platform
```

### 2. Install dependencies

```bash
# Predictors (remote-sensing + climate) pipeline
cd workflows/predictors && uv sync && cd ../..

# Dengue forecasting pipeline
cd workflows/dengue_forecasting && uv sync && cd ../..
```

### 3. Configure credentials

```bash
cp .env.example .env
# Edit .env and fill in your free API credentials — see docs/data-sources/
```

### 4. Run a pipeline

Full instructions live in [docs/processing/](docs/processing/). The forecasting pipeline can be run against the bundled aggregate data **without any external credentials**.

---

## License

**Source code:** Apache License 2.0 — see [LICENSE](LICENSE) and [NOTICE](NOTICE).
**Documentation and non-code content:** Creative Commons Attribution 4.0 International (CC-BY-4.0).

---

## Citation

If you use this software or the data pipelines, please cite both the software release and the underlying methodology paper.

- **Software:** New Light Technologies, Inc. (2026). *DIRE IMPACT Platform.* GitHub. See [CITATION.cff](CITATION.cff).
- **Methodology:** Sebastianelli, A., et al. (2024). *A machine learning approach to dengue and malaria incidence forecasting.* Scientific Reports. DOI: [10.1038/s41598-024-52796-9](https://doi.org/10.1038/s41598-024-52796-9)

---

## Funding and acknowledgements

This work was funded by a **Wellcome Trust** grant to the **University of California, San Diego (UCSD)**. The software was developed by **New Light Technologies (NLT), Inc.** Scientific collaborators include **Universidad Peruana Cayetano Heredia (UPCH)**. The live DIRE dashboard is operated by NLT, Inc. and is currently in soft-launch with UX/UI and data-quality reviews underway.
