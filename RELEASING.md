# Release process

This document describes how we cut a release of `DIRE-OSI/platform` and the open-source compliance steps that gate it. It satisfies the Wellcome "document the release process" requirement (ongoing compliance).

## Versioning

- Semantic versioning: `vMAJOR.MINOR.PATCH`.
- The **latest major version** is the artifact archived to Zenodo for a DOI (see step 6).

## Steps

1. **Confirm scope.** Ensure the release contains only cleared, public-safe content (docs, pipelines, non-personal test data). Nothing from internal/production configs, and no secrets.
2. **Run the compliance checklist** (below) and the CI checks (link check, and — once wired — the pipeline reproducibility job).
3. **Update docs & version.** Update `README`, `CHANGELOG` (if present), and any version references.
4. **Open a release PR** into `main`; get maintainer review (CODEOWNERS) and required approval.
5. **Tag & publish a GitHub Release** (`vX.Y.Z`) with release notes.
6. **Zenodo DOI** *(Phase 4)*: with the GitHub↔Zenodo integration enabled for the org, publishing the release **mints a DOI**. Add/refresh the **DOI badge** in the `README`.

## Open-source compliance checklist (per release)

- [ ] No secrets, credentials, tokens, or `.env` values committed (secret scanning is clean).
- [ ] No personal or locational health data; test data is aggregate and non-identifying.
- [ ] `LICENSE` (Apache-2.0) present; docs remain CC-BY-4.0; `NOTICE` attributions current.
- [ ] Dependencies & versions documented (`DEPENDENCIES.md`, pipeline lockfiles committed).
- [ ] Running documentation up to date (`INSTALL.md`, `docs/`).
- [ ] `CITATION.cff` current; DOI badge added/updated after Zenodo mint.
- [ ] Disclaimer and "in active development / in coordination with UCSD & NLT" language intact.
- [ ] Export-control / UCSD authorization for any newly-published code confirmed.

## Notes

- The internal production source lives in a separate, private repository. Approved content is promoted here one-way through a gated pipeline (see the project's setup plan); this repository never pushes back to production.
