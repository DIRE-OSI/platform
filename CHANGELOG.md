# Changelog

Notable changes to this repository are recorded here, following [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and [Semantic Versioning](https://semver.org/).

## Live platform

Public-safe summaries of each version of the live dashboard at [dire.impact.nltglobal.com](https://dire.impact.nltglobal.com). Full notes for each version are published under [Releases](https://github.com/DIRE-OSI/platform/releases).

### Dashboard v1.1.0 (live 2026-10-22)

- **Forecasts changed:** each forecast horizon (this month, next month, two months ahead) now has its own model; models were retrained and re-evaluated against newer case data; the smoothing for recent months adapts to how far behind case reporting is.
- **Data:** new Peru dengue and Peru malaria data (Peru malaria through August 2026); Brazil malaria counts confirmed cases by probable place of infection; Brazil dengue December 2025 and late-2025 Brazil malaria months restored.
- **Known issue:** Brazil malaria counts are incomplete, because the current source does not include cases reported in the Amazon region. Treat Brazil malaria figures as partial.
- **Interface:** a single Beta notice replaces the two start-up pop-ups; EN/ES/PT language selector; full Spanish and Portuguese interface; Malaria selection fixed in Portuguese; region selection stays consistent across administrative levels; Meet the Team updated.

## [Unreleased]

### Changed
- Documentation aligned with the live dashboard: administrative levels by country, risk-tier and confidence-class descriptions, data downloads and reports, and resource-estimate categories.
- This repository is now the public channel for dashboard feedback, questions and release notes (see SUPPORT.md); new issues notify both maintainers.

### Added
- Dashboard feedback issue form (English, Spanish and Portuguese).
- Live dashboard release notes, published as `dashboard-vX.Y.Z` GitHub Releases.
- Documentation site with methods, research basis, data sources, data dictionary, test-data principles and an indicative roadmap.
- Guidance on using the live dashboard.
- Release guidance for keeping documentation aligned with updates to the live dashboard.
- Community and governance files: licensing (Apache-2.0 for code, CC BY 4.0 for documentation), contribution guidelines, code of conduct, security and support policies, and citation metadata.
