# Security Policy

## Reporting a vulnerability

We take the security of DIRE seriously. If you discover a security vulnerability, please report it responsibly.

**Please do not open a public issue for security vulnerabilities.**

Instead, report it privately using GitHub's [private vulnerability reporting](https://github.com/DIRE-OSI/platform/security/advisories/new) for this repository. If that is unavailable, contact the maintainers through the channels listed in [docs/TEAM.md](docs/TEAM.md).

When reporting, please include:

- A description of the vulnerability and its potential impact
- Steps to reproduce, or a proof of concept
- Any relevant versions, configurations, or affected components

We will acknowledge your report, keep you informed of our progress, and credit you (with your permission) once the issue is resolved.

## Scope

This policy covers the code and documentation in this repository. The live dashboard and forecasting API at `dire.impact.nltglobal.com` are operated separately; vulnerabilities affecting the live service can also be reported through the channels above.

## Handling of credentials and data

This repository must never contain secrets, API tokens, or personally identifiable or locational health data. If you find any such material committed to the repository history, please report it immediately as a security issue so it can be revoked and removed.
