# Data source: Brazil SIVEP-Malaria

DIRE uses **SIVEP-Malaria** (*Sistema de Informação de Vigilância Epidemiológica da Malária*) for reported **malaria** cases notified in Brazil's **Legal Amazon**, where most of the country's malaria occurs.

## Why DIRE needs it

Brazil records malaria in two systems:

- **SIVEP-Malaria** covers notifications in the nine Legal Amazon states: Acre, Amapá, Amazonas, Maranhão, Mato Grosso, Pará, Rondônia, Roraima and Tocantins.
- **SINAN** covers notifications in the rest of Brazil (see [datasus-sinan.md](datasus-sinan.md)).

The two systems do not overlap, so DIRE combines them to build a complete national case history. SINAN alone holds only a few hundred malaria cases a year, compared with over 100,000 in SIVEP.

## What DIRE uses

- **Records:** SIVEP notifications with a positive exam, excluding cure-verification slides (LVC), for infections acquired in Brazil.
- **Counted by:** probable place of infection and month of notification, in two age groups (0–19 and 20 and over), the same way as SINAN malaria.
- **Levels:** aggregated to state (admin 1) and municipality (admin 2).

## Access

SIVEP-Malaria has no official API or open-data release. The national notification files are published on Zenodo by Raphael Saldanha (Fiocruz), obtained through Brazil's Access to Information Law (LAI), under **CC BY 4.0**:

- 2004–2024: <https://zenodo.org/records/20628478>
- 2025–2026 (preliminary): <https://zenodo.org/records/20632350>

No credentials are required.

## Privacy & aggregation

The Zenodo files are individual notification records. **DIRE uses only aggregate counts** (by administrative unit and month) and does **not** ingest or redistribute personal identifiers. Contributors must never commit raw record-level data to this repository. See [`SECURITY.md`](https://github.com/DIRE-OSI/platform/blob/main/SECURITY.md) and [`CONTRIBUTING.md`](https://github.com/DIRE-OSI/platform/blob/main/CONTRIBUTING.md).

## Licensing & citation

CC BY 4.0. Cite the Zenodo dataset (Saldanha, R., SIVEP-Malaria notification data) and the Brazilian Ministry of Health as the original data producer.

## Notes for DIRE

- **Validation:** combined SIVEP + SINAN national totals match the Ministry of Health's published counts of malaria acquired in Brazil to within 0.2% for 2014–2025.
- **Freshness:** the Zenodo files are released periodically rather than monthly, so Brazil malaria case data are updated as new releases appear. A regular monthly update from both systems is being developed.
- Reported surveillance data can **lag** the current month and are subject to revision; recent months are preliminary.
