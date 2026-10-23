---
title: "Home"
nav_order: 1
permalink: /
---

<span class="dire-status">Preliminary documentation</span>

# DIRE — Disease Incidence and Resource Estimator
{: .fs-9 }

An open-science initiative for sub-national forecasting of mosquito-borne disease incidence and the estimation of associated public-health resource needs, initially developed for dengue and malaria in Peru and Brazil.
{: .dire-lede }

[Live dashboard](https://dire.impact.nltglobal.com){: .btn .btn-primary .mr-2 }
[Methods](METHODS.md){: .btn .mr-2 }
[Release notes](https://github.com/DIRE-OSI/platform/releases){: .btn .mr-2 }
[Give feedback](https://github.com/DIRE-OSI/platform/issues/new?template=dashboard_feedback.yml){: .btn .mr-2 }
[Source repository](https://github.com/DIRE-OSI/platform){: .btn }

---

## Overview

DIRE combines climate reanalysis, satellite-derived environmental indicators, census-based socio-demographic information and national epidemiological surveillance to produce short-horizon estimates of disease incidence for administrative units. Estimates are translated into indicative requirements for prevention, diagnosis, treatment and programme operations, with the aim of supporting anticipatory public-health planning.

The initiative is in a preliminary phase. Methods, documentation and open workflows are being released progressively and remain subject to review by the collaborating institutions.

## Collaborating institutions

<div class="dire-partners">
  <div class="dire-partner"><strong>University of California San Diego</strong><span>School of Global Policy and Strategy — academic leadership</span></div>
  <div class="dire-partner"><strong>New Light Technologies, Inc.</strong><span>Platform engineering, data science and operations</span></div>
  <div class="dire-partner"><strong>Universidad Peruana Cayetano Heredia</strong><span>Scientific collaboration and regional public-health expertise</span></div>
  <div class="dire-partner"><strong>UNICEF</strong><span>Collaboration on public-health application</span></div>
  <div class="dire-partner"><strong>Wellcome</strong><span>Funding</span></div>
</div>

Roles are indicative and may evolve as the collaboration develops. See [Team &amp; partners](TEAM.md).

## Documentation

| Section | Content |
|---|---|
| [Using the dashboard](USING_THE_DASHBOARD.md) | Reading maps, risk tiers, charts and reports |
| [About DIRE](ABOUT.md) | Diseases, inputs and intended use |
| [Methods](METHODS.md) | Data processing, modelling approach, evaluation design and limitations |
| [Research basis](RESEARCH_BASIS.md) | Scientific rationale and references |
| [Data sources](data-sources/README.md) · [Data dictionary](DATA_DICTIONARY.md) | Inputs, provenance, licensing and data structure |
| [Test data](TEST_DATA.md) · [Processing pipelines](processing/README.md) | Reproducibility without restricted data |
| [Roadmap](ROADMAP.md) | Indicative development pathway |
| [Release notes](https://github.com/DIRE-OSI/platform/releases) | What changed in each update to the live dashboard |

## Feedback and updates

- **Feedback, problems or ideas about the dashboard:** use the [dashboard feedback form](https://github.com/DIRE-OSI/platform/issues/new?template=dashboard_feedback.yml) (English, Spanish or Portuguese). It needs a free GitHub account, and what you post is public.
- **Questions and discussion:** [Discussions](https://github.com/DIRE-OSI/platform/discussions).
- **Release notes:** [Releases](https://github.com/DIRE-OSI/platform/releases). To be notified of new versions, choose **Watch → Custom → Releases** on the repository page.
- **Security or sensitive matters:** report privately through [SECURITY.md](https://github.com/DIRE-OSI/platform/blob/main/SECURITY.md).

## How to cite

<div class="dire-cite">
DIRE: Disease Incidence and Resource Estimator. UC San Diego and New Light Technologies, Inc. (2026). https://github.com/DIRE-OSI/platform. Please also cite Sebastianelli <em>et al.</em> (2024), <em>Scientific Reports</em> 14, 3807. Full citation metadata: <a href="https://github.com/DIRE-OSI/platform/blob/main/CITATION.cff">CITATION.cff</a>.
</div>

{: .important }
DIRE outputs are experimental decision-support estimates provided "as is". They complement, and do not replace, official surveillance and professional judgement. See the [disclaimer](https://github.com/DIRE-OSI/platform/blob/main/DISCLAIMER.md).
