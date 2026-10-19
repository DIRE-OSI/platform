# Contributing to DIRE

Thank you for your interest in contributing. DIRE is an open-science project, and we welcome contributions from researchers, public-health practitioners, and developers alike. This document explains how to participate and what we expect from contributors.

By participating, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md).

## Ways to contribute

- **Report a problem** — open an [issue](https://github.com/DIRE-OSI/platform/issues) for a bug, a reproducibility gap, or unclear documentation.
- **Start a discussion** — for ideas, questions, new covariates, model architectures, or country/disease expansions, open a [discussion](https://github.com/DIRE-OSI/platform/discussions) before writing code.
- **Improve documentation** — clarity fixes and Spanish/Portuguese translations are especially valuable.
- **Submit code** — via a pull request, following the workflow below.

## Pull request workflow

1. **Fork** the repository and create a topic branch from `main` (e.g. `feature/new-covariate`, `fix/pipeline-path`).
2. **Make your change.** Keep pull requests focused — one logical change per PR.
3. **Document and test** your change where applicable.
4. **Sign off your commits** (see DCO below).
5. **Open a pull request** against `main`, describing what you changed and why. Link any related issue.
6. A maintainer will review. Address feedback by pushing additional commits to your branch.

Pull requests require review from a maintainer (see [CODEOWNERS] governance) and must pass any configured checks before merging.

## Developer Certificate of Origin (DCO)

We use the [Developer Certificate of Origin](https://developercertificate.org/) rather than a CLA. It is a lightweight way for you to certify that you wrote or otherwise have the right to submit the code you contribute.

Add a `Signed-off-by` line to every commit:

```bash
git commit -s -m "Your commit message"
```

This appends:

```
Signed-off-by: Your Name <your.email@example.com>
```

Use your real name and an email you can be reached at. Commits without a valid sign-off cannot be merged.

## Coding and documentation standards

- **Python:** target 3.11+, manage environments with `uv`, and follow standard formatting (Black/Ruff conventions).
- **R:** target 4.5+.
- **Docs:** written in Markdown, licensed CC-BY-4.0. Keep instructions runnable and version-pinned where possible.
- **No secrets or private data.** Never commit credentials, tokens, or any personally identifiable or locational health data. See [SECURITY.md](SECURITY.md).

## Data contributions

DIRE relies on surveillance data governed by agreements with national health authorities. If you represent an institution interested in contributing data or collaborating on validation, please reach out through the channels in [docs/TEAM.md](docs/TEAM.md) rather than opening a PR with data.

## Questions

Open a [discussion](https://github.com/DIRE-OSI/platform/discussions) or an issue. We're glad you're here.
