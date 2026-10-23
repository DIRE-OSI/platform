# 🦟 DIRE

### Disease Incidence and Resource Estimator

**1-, 2-, and 3-month-ahead disease-incidence risk forecasting at sub-national scale**
*Initial coverage: dengue & malaria in Peru and Brazil — additional countries and diseases are being onboarded.*

![License](https://img.shields.io/badge/license-Apache--2.0-blue)
![Docs](https://img.shields.io/badge/docs-CC--BY--4.0-lightgrey)
![Status](https://img.shields.io/badge/status-active%20development-orange)

[🌐 Live Dashboard](https://dire.impact.nltglobal.com) · [🗺️ Using the Dashboard](docs/USING_THE_DASHBOARD.md) · [ℹ️ About](docs/ABOUT.md) · [🔬 Research Basis](docs/RESEARCH_BASIS.md) · [👥 Team](docs/TEAM.md) · [📜 Roadmap](docs/ROADMAP.md) · [📰 Release notes](https://github.com/DIRE-OSI/platform/releases) · [💬 Feedback](https://github.com/DIRE-OSI/platform/issues/new?template=dashboard_feedback.yml) · [🤝 Get Involved](#-get-involved) · [🆘 Support](SUPPORT.md)

> 🚧 **Status: Under active development.** This repository is an early, evolving release published **in coordination with the DIRE project team at UC San Diego (UCSD) and New Light Technologies (NLT)**. Its structure, documentation, and included code are being staged and reviewed phase by phase; content may change. It is shared now to enable open review and collaboration — please treat it as work in progress and coordinate with the project team before relying on it.

> ⚠️ **Disclaimer:** All forecasts and analytical outputs are provided "as is" for decision-support purposes only. New Light Technologies, UC San Diego, and UNICEF expressly disclaim all liability for decisions made using these outputs. See [DISCLAIMER.md](DISCLAIMER.md) for full terms.

---

**Preliminary release.** This repository is being populated, in coordination with the project team at **UCSD and NLT**, with the data-source documentation and Python/R processing pipelines for DIRE. It is the open, community-facing home of the project, released under the Wellcome Trust open-source grant conditions. The forecasting API and interactive dashboard are live at [dire.impact.nltglobal.com](https://dire.impact.nltglobal.com); their source code will follow in subsequent phases. See [docs/ROADMAP.md](docs/ROADMAP.md) for the full release plan.

---

## What is DIRE?

DIRE (Disease Incidence and Resource Estimator) is a machine-learning forecasting platform that produces **1-, 2-, and 3-month-ahead disease-incidence estimates** (the current month plus the following two) at the sub-national administrative level. It is designed to support public-health decision-makers, epidemiologists, and humanitarian responders in anticipating disease burden and allocating resources *before* outbreaks peak.

**Coverage is expanding.** Peru and Brazil — and the diseases dengue and malaria — are the **first countries and diseases** being trialed during the platform's development and operations-and-maintenance (O&M) phase. The methodology and pipelines are built to generalize, and **additional countries and diseases are being onboarded** over time. References to Peru, Brazil, dengue, and malaria throughout this repository describe the *current* rollout, not the platform's ultimate scope.

The platform integrates:

- **Remote-sensing covariates** — NASA Earthdata (MODIS land cover + vegetation indices, NASADEM elevation)
- **Climate covariates** — Copernicus ERA5-Land (temperature, precipitation, humidity)
- **Epidemiological surveillance** — Brazil DATASUS SINAN and Peru MINSA dengue case records
- **An ensemble ML model** — CatBoost, SVM, and LSTM models synthesized with a Random Forest, as described in Sebastianelli et al. (2024)

Risk estimates are mapped to five tiers (Lowest → Highest) for sub-national administrative units (Peru department, province and district; Brazil state and municipality) and are refreshed monthly.

**Collaborating institutions:** UC San Diego School of Global Policy and Strategy · New Light Technologies (NLT) · Universidad Peruana Cayetano Heredia (UPCH) · UNICEF
**Funder:** Wellcome

---

## 🤝 Get Involved

DIRE is an **open science** project. We built this repository so that researchers, public-health agencies, and the broader open-source community can inspect, reproduce, improve, and build on the work — not just read about it. There are several ways to participate, whatever your background.

### For researchers and epidemiologists
- **Reproduce and validate.** Every processing pipeline in [`workflows/`](workflows/) is documented so you can re-run our covariate engineering and forecasting steps against the bundled aggregate data — no credentials or private data required. See [docs/processing/](docs/processing/).
- **Extend the science.** Propose new covariates, alternative model architectures, additional diseases, or new countries. Open a [discussion](https://github.com/DIRE-OSI/platform/discussions) to sketch an idea before you build it.
- **Cite the work.** If DIRE supports your research, please cite both the software and the underlying methodology paper — see [Citation](#citation).

### For public-health practitioners and responders
- **Use the dashboard.** The live platform at [dire.impact.nltglobal.com](https://dire.impact.nltglobal.com) is free to use for planning and situational awareness.
- **Tell us what you need.** Resource-estimation and reporting features are shaped by real operational needs. Use the [dashboard feedback form](https://github.com/DIRE-OSI/platform/issues/new?template=dashboard_feedback.yml) to describe your use case, the decisions you make, and the outputs that would help.
- **Stay up to date.** Each update to the live dashboard is published under [Releases](https://github.com/DIRE-OSI/platform/releases).

### For contributors and developers
- **Report issues** — bugs, unclear docs, or reproducibility gaps.
- **Improve documentation** — clarity fixes and translations are especially welcome, given the platform's Peru/Brazil focus (Spanish and Portuguese).
- **Submit pull requests** — see [CONTRIBUTING.md](CONTRIBUTING.md) for the workflow and the Developer Certificate of Origin (DCO) sign-off we require.

### For data and institutional partners
- We work with surveillance data from national health authorities under appropriate agreements. If your institution wants to collaborate on data, validation, or a country expansion, reach out through the channels in [docs/TEAM.md](docs/TEAM.md).

**Community standards.** Participation in this project is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). Please read it before engaging.

---

## 🆘 Support & contact

Need help, found a bug, or have a question? See **[SUPPORT.md](SUPPORT.md)** for where each request should go. In short:

- **Live dashboard feedback, bugs or ideas** → use the [dashboard feedback form](https://github.com/DIRE-OSI/platform/issues/new?template=dashboard_feedback.yml) (English, Spanish or Portuguese). The "Submit Feedback / Contact Us" link at the bottom of the dashboard opens the same form.
- **Bugs, errors, reproducibility gaps in this repository** → open an [Issue](https://github.com/DIRE-OSI/platform/issues/new/choose).
- **Questions, ideas, new covariates/diseases/countries** → start a [Discussion](https://github.com/DIRE-OSI/platform/discussions).
- **Security vulnerabilities or sensitive matters** → follow [SECURITY.md](SECURITY.md) (please don't open a public issue).
- **Release notes for the live dashboard** → [Releases](https://github.com/DIRE-OSI/platform/releases). To be notified, click **Watch → Custom → Releases** at the top of this repository.

Issues and Discussions need a free GitHub account, and everything posted there is public. Please don't include personal or patient information.

New issues are automatically acknowledged and routed to the maintainers.

---

## Repository contents

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
├── CHANGELOG.md            # Repository and live dashboard change history
├── CITATION.cff            # Machine-readable citation metadata
├── CONTRIBUTING.md         # PR workflow and DCO sign-off
├── CODE_OF_CONDUCT.md      # Community standards
├── LICENSE                 # Apache-2.0 (source code)
├── NOTICE                  # Attribution
├── SECURITY.md             # Vulnerability disclosure
├── SUPPORT.md              # Where to send feedback, questions and reports
├── DISCLAIMER.md           # Platform disclaimer and liability terms
└── .env.example            # Credential template
```

### What is *not* here yet

| Component | Indicative stage ([Roadmap](docs/ROADMAP.md)) |
|---|---|
| Prediction API / backend service | Under consideration |
| Containerized local runner | Stage III (open workflows) |
| Automated test suite + CI | Stage III (open workflows) |
| Interactive dashboard source code | Under consideration |
| Cloud deployment / infrastructure-as-code | Under consideration |
| Archival release with DOI | Stage IV (archival release) |

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
                                confidence class) by admin unit × month
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

- **Software:** New Light Technologies, Inc. (2026). *DIRE: Disease Incidence and Resource Estimator.* GitHub. See [CITATION.cff](CITATION.cff).
- **Methodology:** Sebastianelli, A., et al. (2024). *A reproducible ensemble machine learning approach to forecast dengue outbreaks.* Scientific Reports, 14, 3807. DOI: [10.1038/s41598-024-52796-9](https://doi.org/10.1038/s41598-024-52796-9)

---

## Funding and acknowledgements

This work was funded by a **Wellcome Trust** grant to the **University of California, San Diego (UCSD)**. The software was developed by **New Light Technologies (NLT), Inc.** Scientific collaborators include **Universidad Peruana Cayetano Heredia (UPCH)**. The live DIRE dashboard is operated by NLT, Inc. and is currently in beta, with user-experience and data-quality reviews ongoing.
