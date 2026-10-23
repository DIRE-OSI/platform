# Release process

This document describes how we cut a release of `DIRE-OSI/platform` and the open-source compliance steps that gate it. It satisfies the Wellcome "document the release process" requirement (ongoing compliance).

This repository publishes two kinds of release:

- **Repository releases** (`vX.Y.Z`): versions of the open-science content in this repository (docs, pipelines, test data).
- **Live dashboard releases** (`dashboard-vX.Y.Z`): public release notes for each version of the live dashboard. These are the single public source of the dashboard's release notes.

## Versioning

- Semantic versioning: `vMAJOR.MINOR.PATCH` for repository releases; `dashboard-vMAJOR.MINOR.PATCH` matching the dashboard's own version for live dashboard releases.
- The **latest major repository version** is the artifact archived to Zenodo for a DOI (see step 6).

## Steps (repository releases)

1. **Confirm scope.** Ensure the release contains only cleared, public-safe content (docs, pipelines, non-personal test data). Nothing from internal/production configs, and no secrets.
2. **Run the compliance checklist** (below) and the CI checks (link check, and — once wired — the pipeline reproducibility job).
3. **Update docs & version.** Update `README`, `CHANGELOG` (if present), and any version references.
4. **Open a release PR** into `main`; get maintainer review (CODEOWNERS) and required approval.
5. **Tag & publish a GitHub Release** (`vX.Y.Z`) with release notes.
6. **Zenodo DOI** *(Phase 4)*: with the GitHub↔Zenodo integration enabled for the org, publishing the release **mints a DOI**. Add/refresh the **DOI badge** in the `README`.

## Steps (live dashboard releases)

The last step of every production deployment of the dashboard:

1. Add a short, public-safe summary under **Live platform** in `CHANGELOG.md`, with the date the version went live.
2. Update any docs pages the release changes (see *Alignment with the live dashboard* below).
3. Publish a GitHub Release tagged `dashboard-vX.Y.Z` on `main`, with the same public-safe release notes the dashboard shows. GitHub notifies everyone watching this repository's releases, so no separate email is needed.

## Open-source compliance checklist (per release)

- [ ] No secrets, credentials, tokens, or `.env` values committed (secret scanning is clean).
- [ ] No personal or locational health data; test data is aggregate and non-identifying.
- [ ] `LICENSE` (Apache-2.0) present; docs remain CC-BY-4.0; `NOTICE` attributions current.
- [ ] Dependencies & versions documented (`DEPENDENCIES.md`, pipeline lockfiles committed).
- [ ] Running documentation up to date (`INSTALL.md`, `docs/`).
- [ ] `CITATION.cff` current; DOI badge added/updated after Zenodo mint.
- [ ] Disclaimer and "in active development / in coordination with UCSD & NLT" language intact.
- [ ] Export-control / UCSD authorization for any newly-published code confirmed.

## Alignment with the live dashboard

The documentation here describes the methods, data sources and behaviour of the live dashboard at [dire.impact.nltglobal.com](https://dire.impact.nltglobal.com). To keep the two consistent:

- When a dashboard update changes methods, data sources, forecast horizon or user-facing behaviour, the relevant pages (Methods, Data dictionary, Using the dashboard) are reviewed and updated in the same cycle.
- A short, public-safe summary of each dashboard update is added to `CHANGELOG.md` under a **Live platform** heading, with the date it went live, and published as a `dashboard-vX.Y.Z` GitHub Release.
- Documentation describes what is live. Planned or in-review changes are described only in indicative terms on the [Roadmap](docs/ROADMAP.md).

## Feedback and communication

This repository is the public channel for DIRE: dashboard feedback (issue form), questions (Discussions), release notes (Releases) and confidential reports (private security reports). See [SUPPORT.md](SUPPORT.md).

## Notes

- The internal production source lives in a separate, private repository. Approved content is promoted here one-way through a gated review process; this repository never pushes back to production.
