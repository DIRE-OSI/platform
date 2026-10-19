"""Check the SYNTHETIC Iquitos example files against the DIRE data dictionary.

Usage:
    python check_schema.py        # exits non-zero if any check fails
"""
from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

DATA = Path(__file__).parent / "data"
KEYS = ["country", "admin_level", "admin_id", "year", "month"]
CASE_COLS = KEYS + ["admin_name", "disease", "cases_total", "cases_0_19", "pop_total", "pop_0_19",
                    "dir_total", "dir_0_19", "data_status", "is_synthetic"]
COV_COLS = KEYS + ["t2m_mean", "t2m_min", "t2m_max", "precip_total", "rh_mean", "ndvi_mean",
                   "elev_mean", "urban_frac", "is_synthetic"]


def check(name: str, df: pd.DataFrame, cols: list[str]) -> list[str]:
    errs = []
    missing = [c for c in cols if c not in df.columns]
    if missing:
        errs.append(f"{name}: missing columns {missing}")
    if "is_synthetic" in df and not df["is_synthetic"].all():
        errs.append(f"{name}: every row must have is_synthetic = True")
    if df.duplicated(KEYS).any():
        errs.append(f"{name}: duplicate unit-month rows")
    if not df["month"].between(1, 12).all():
        errs.append(f"{name}: month outside 1-12")
    for unit, g in df.groupby("admin_id"):
        p = pd.PeriodIndex.from_fields(year=g["year"], month=g["month"], freq="M").sort_values()
        if len(p) and (p[-1] - p[0]).n + 1 != len(p):
            errs.append(f"{name}: unit {unit} has gaps in its monthly series")
    num = df.select_dtypes("number")
    if (num < 0).any().any() and name == "cases":
        errs.append(f"{name}: negative values found")
    return errs


def main() -> int:
    cases = pd.read_csv(DATA / "SYNTHETIC_peru_iquitos_dengue_cases.csv", dtype={"admin_id": str})
    cov = pd.read_csv(DATA / "SYNTHETIC_peru_iquitos_covariates.csv", dtype={"admin_id": str})
    errs = check("cases", cases, CASE_COLS) + check("covariates", cov, COV_COLS)
    if (cases["cases_0_19"] > cases["cases_total"]).any():
        errs.append("cases: cases_0_19 exceeds cases_total")
    if set(cases["admin_id"]) != set(cov["admin_id"]):
        errs.append("units differ between cases and covariates")
    if errs:
        print("FAILED:\n- " + "\n- ".join(errs))
        return 1
    print(f"OK: {len(cases)} case rows, {len(cov)} covariate rows, "
          f"{cases['admin_id'].nunique()} units, {cases['year'].min()}-{cases['year'].max()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
