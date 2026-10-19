"""Generate a small, fully SYNTHETIC dengue example for two districts of Iquitos, Peru.

All values are simulated. District names and UBIGEO codes are public reference
identifiers; every number (cases, population, climate, vegetation) is synthetic
and must not be used for any public-health decision.

Usage:
    python generate.py            # writes data/*.csv next to this script
    python generate.py --seed 7   # different random draw, same structure
"""
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd

# Public reference identifiers (INEI UBIGEO), Maynas province, Loreto department
DISTRICTS = [
    # admin_id, admin_name, synthetic population (all ages), share aged 0-19, baseline incidence /100k
    ("160108", "Punchana", 95_000, 0.38, 35.0),
    ("160113", "San Juan Bautista", 165_000, 0.40, 45.0),
]
START, END = "2015-01", "2025-12"


def simulate(seed: int = 42) -> tuple[pd.DataFrame, pd.DataFrame]:
    rng = np.random.default_rng(seed)
    months = pd.period_range(START, END, freq="M")
    rows_cases, rows_cov = [], []

    for admin_id, name, pop0, share019, base in DISTRICTS:
        elev = rng.normal(105, 4)
        urban = rng.uniform(0.85, 0.97)
        pop = pop0
        precip_lag1 = precip_lag2 = 200.0
        temp_lag1 = 27.0
        outbreak_years = set(rng.choice(range(2015, 2026), size=3, replace=False))

        for m in months:
            pop = int(pop * (1 + 0.012 / 12))  # gentle growth
            # Amazonian seasonality: wetter Nov-May, drier Jun-Oct
            wet = np.cos(2 * np.pi * (m.month - 2) / 12)
            precip = max(20.0, 230 + 90 * wet + rng.normal(0, 35))
            t2m = 26.8 - 0.4 * wet + rng.normal(0, 0.35)
            t2m_min, t2m_max = t2m - rng.uniform(4.5, 5.5), t2m + rng.uniform(5.0, 6.0)
            rh = float(np.clip(82 + 5 * wet + rng.normal(0, 1.5), 60, 99))
            ndvi = float(np.clip(0.72 + 0.04 * wet + rng.normal(0, 0.02), -1, 1))

            # Incidence responds to lagged rainfall and temperature, peaks Jan-Apr
            season = 1 + 0.9 * np.cos(2 * np.pi * (m.month - 3) / 12)
            drivers = 1 + 0.0025 * (precip_lag2 - 200) + 0.25 * (temp_lag1 - 27)
            surge = 3.0 if (m.year in outbreak_years and m.month in (1, 2, 3, 4)) else 1.0
            dir_total = max(0.0, base * season * drivers * surge * rng.lognormal(0, 0.3))
            cases_total = int(rng.poisson(dir_total * pop / 1e5))
            cases_019 = int(rng.binomial(cases_total, 0.45)) if cases_total else 0
            pop019 = int(pop * share019)

            status = "provisional" if m >= months[-2] else "final"
            rows_cases.append(dict(
                country="PER", admin_level=3, admin_id=admin_id, admin_name=name,
                admin2_name="Maynas", admin1_name="Loreto",
                year=m.year, month=m.month, disease="dengue",
                cases_total=cases_total, cases_0_19=cases_019,
                pop_total=pop, pop_0_19=pop019,
                dir_total=round(cases_total / pop * 1e5, 3),
                dir_0_19=round(cases_019 / pop019 * 1e5, 3) if pop019 else 0.0,
                data_status=status, is_synthetic=True,
            ))
            rows_cov.append(dict(
                country="PER", admin_level=3, admin_id=admin_id, year=m.year, month=m.month,
                t2m_mean=round(t2m, 2), t2m_min=round(t2m_min, 2), t2m_max=round(t2m_max, 2),
                precip_total=round(precip, 1), rh_mean=round(rh, 1), ndvi_mean=round(ndvi, 3),
                elev_mean=round(elev, 1), urban_frac=round(urban, 3), is_synthetic=True,
            ))
            precip_lag2, precip_lag1, temp_lag1 = precip_lag1, precip, t2m

    return pd.DataFrame(rows_cases), pd.DataFrame(rows_cov)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--out", type=Path, default=Path(__file__).parent / "data")
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    cases, cov = simulate(args.seed)
    cases.to_csv(args.out / "SYNTHETIC_peru_iquitos_dengue_cases.csv", index=False)
    cov.to_csv(args.out / "SYNTHETIC_peru_iquitos_covariates.csv", index=False)
    print(f"Wrote {len(cases)} case rows and {len(cov)} covariate rows to {args.out}")


if __name__ == "__main__":
    main()
