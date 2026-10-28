# Worked example: Iquitos, Peru — dengue (SYNTHETIC)

A small, self-contained example that shows the structure of DIRE inputs at the lowest administrative level, using two districts of Iquitos (Maynas province, Loreto, Peru). It is intended for learning, testing and reproducibility checks.

> **SYNTHETIC DATA.** District names and UBIGEO codes are public reference identifiers. Every value — cases, population, climate and vegetation — is simulated. The data are not surveillance data, are not DIRE estimates, and must not be used for any public-health decision.

## Data card

| | |
|---|---|
| **Units** | Punchana (UBIGEO 160108), San Juan Bautista (160113), Iquitos (160101) and Belén (160112) district level (administrative level 3)
| **Period** | January 2015 – December 2025, monthly |
| **Disease** | Dengue |
| **Files** | `data/SYNTHETIC_peru_iquitos_dengue_cases.csv`, `data/SYNTHETIC_peru_iquitos_covariates.csv` (created by `generate.py`) |
| **Structure** | Follows the [Data dictionary](https://dire-osi.github.io/platform/DATA_DICTIONARY.html); every row carries `is_synthetic = True` |
| **Generation** | Seeded simulation (`--seed`, default 42): Amazonian wet/dry seasonality, incidence responding to lagged rainfall and temperature, occasional outbreak years, Poisson case counts, and an age 0–19 share |
| **Licence** | CC BY 4.0 (data), Apache-2.0 (code) |

## Run it

Requires Python 3.11+ with `numpy` and `pandas` (available on Google Colab).

```bash
cd examples/peru-iquitos-dengue
python generate.py        # writes the two CSV files to data/
python check_schema.py    # validates them against the data dictionary
```

`check_schema.py` confirms required columns, the synthetic flag, complete monthly series per unit, no duplicate unit-months and consistent units across files.

## Extending the example

- Add covariates listed in the data dictionary (for example land-cover fractions or lagged variables).
- Use the files with the quick-start notebook in `notebooks/` to produce multi-horizon estimates and compare them with a calendar-month baseline.

Contributions follow [CONTRIBUTING.md](../../CONTRIBUTING.md).
