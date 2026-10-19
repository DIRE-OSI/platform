# Research basis

DIRE builds on published work on machine-learning forecasting of mosquito-borne disease from environmental and socio-demographic data, and adapts it for operational, sub-national use.

## Methodological foundation

DIRE adopts as its starting point the reproducible ensemble approach of Sebastianelli *et al.* (2024), which combines Earth-observation, climate and socio-demographic covariates with surveillance data in an ensemble of complementary learners. DIRE extends this approach to monthly estimation at several administrative levels and lead times, and to two diseases. See [Methods](METHODS.md).

## Scientific rationale

- **Climate and environment influence transmission.** Temperature, rainfall, humidity, vegetation and land cover affect vector breeding, survival and viral replication, typically with lags of weeks to months.
- **Recent incidence carries strong signal.** Recent case counts are among the most informative predictors; reporting delays therefore directly affect estimation quality.
- **Population and living conditions matter.** Age structure, urbanisation, housing, water storage and sanitation shape exposure and inform the conversion of rates into expected cases and resource needs.
- **Early warning supports cost-effective response.** Timely, spatially explicit estimates can support integrated vector management, clinical preparedness and the targeting of resources.

## From estimates to resources

DIRE translates expected cases into indicative requirements across four areas: **prevention** (vector control, protective measures, community education and awareness), **diagnosis**, **treatment** (general and intensive care) and **programme operations** (personnel and management), with associated costs. Parameters are programme- and country-specific and will be documented as they are released. Resource estimates are planning aids, not prescriptions.

## Selected references

1. Sebastianelli, A., *et al.* (2024). A reproducible ensemble machine learning approach to forecast dengue outbreaks. *Scientific Reports*, 14, 3807. [doi:10.1038/s41598-024-52796-9](https://doi.org/10.1038/s41598-024-52796-9)
2. Leung, X. Y., *et al.* (2023). A systematic review of dengue outbreak prediction models: current scenario and future directions. *PLOS Neglected Tropical Diseases*, 17(2), e0010631.
3. Hussain-Alkhateeb, L., *et al.* (2021). Early warning systems (EWSs) for chikungunya, dengue, malaria, yellow fever, and Zika outbreaks: what is the evidence? A scoping review. *PLOS Neglected Tropical Diseases*, 15(9), e0009686.
4. Buczak, A. L., *et al.* (2018). Ensemble method for dengue prediction. *PLOS ONE*, 13(1), e0189988.
5. Benedum, C. M., *et al.* (2020). Weekly dengue forecasts in Iquitos, Peru; San Juan, Puerto Rico; and Singapore. *PLOS Neglected Tropical Diseases*, 14(10), e0008710.
6. Paz-Bailey, G., *et al.* (2024). Dengue. *The Lancet*, 403.
7. Prokhorenkova, L., *et al.* (2018). CatBoost: unbiased boosting with categorical features. *Advances in Neural Information Processing Systems*, 31.
8. Hochreiter, S., & Schmidhuber, J. (1997). Long short-term memory. *Neural Computation*, 9(8), 1735–1780.
9. Breiman, L. (2001). Random forests. *Machine Learning*, 45, 5–32.
10. Muñoz-Sabater, J., *et al.* (2021). ERA5-Land: a state-of-the-art global reanalysis dataset for land applications. *Earth System Science Data*, 13, 4349–4383.

## How to cite DIRE

Please cite both the software and the methodological reference above. Citation metadata is maintained in [`CITATION.cff`](https://github.com/DIRE-OSI/platform/blob/main/CITATION.cff); GitHub's **"Cite this repository"** function provides APA and BibTeX formats. A persistent identifier (DOI) is planned for tagged releases (see [Roadmap](ROADMAP.md)).
