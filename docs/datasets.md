# Datasets

## Source data

The primary datasets we use are listed below.

### Labour Market Statistics time series

https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/employmentandemployeetypes/datasets/labourmarketstatistics

### Consumer price inflation time series

https://www.ons.gov.uk/economy/inflationandpriceindices/datasets/consumerpriceindices

### Young people not in education, employment or training (NEET)

https://www.ons.gov.uk/employmentandlabourmarket/peoplenotinwork/unemployment/datasets/youngpeoplenotineducationemploymentortrainingneettable1

### Claimant count and vacancies time series

https://www.ons.gov.uk/employmentandlabourmarket/peoplenotinwork/unemployment/datasets/claimantcountandvacanciesdataset

### Annual Population Survey / Labour Force Survey

From the [Nomis page](https://www.nomisweb.co.uk/datasets/apsnew).

> A residence based labour market survey encompassing population, economic
> activity (employment and unemployment), economic inactivity and
> qualifications. These are broken down where possible by gender, age,
> ethnicity, industry and occupation. Available at Local Authority level and
> above. Updated quarterly.

We use the
[**Variables (percentages)** analysis (17.5)](https://www.nomisweb.co.uk/api/v01/dataset/NM_17_5/def.htm),
selecting Parliamentary constituency level estimates of unemployment and
economic acticity. Note that this dataset has many surpressed values,
particularly for limited age ranges.

Here are some useful links for the APS/LFS

- [Query builder](https://www.nomisweb.co.uk/query/construct/summary.asp?reset=yes&mode=construct&dataset=17&version=0&anal=5&initsel=)
- [Variable codelist](https://www.nomisweb.co.uk/api/v01/dataset/NM_17_5/variable.def.htm)
- [List of Parliamentary constituencies](https://www.nomisweb.co.uk/api/v01/dataset/NM_17_5/geography/TYPE460.def.htm)

<!--
Links to machine-readble versions of metadata

https://www.nomisweb.co.uk/api/v01/dataset/NM_17_5/def.sdmx.json
https://www.nomisweb.co.uk/api/v01/dataset/NM_17_5/variable.def.sdmx.json
https://www.nomisweb.co.uk/api/v01/dataset/NM_17_5/GEOGRAPHY/TYPE460.def.sdmx.json
-->

### Census 2021

We use ready-made analysis
[RM024 - Economic activity status by sex by age](https://www.nomisweb.co.uk/datasets/c2021rm024)
to extract information about young people's employment status as reported during
the 2021 Census.

> This dataset provides Census 2021 estimates that classify usual residents aged
> 16 years and over in England and Wales by economic activity status, by sex,
> and by age. The estimates are as at Census Day, 21 March 2021.

### Claimant counts

We use the
[counts of UC and JSA claimants](https://www.nomisweb.co.uk/datasets/ucjsa).

> The Claimant Count - the stock of Universal Credit and Job Seekers Allowance
> claimants broken down by sex, age and type of benefit being claimed. Claimant
> count proportions are available but not when the figures are not broken down
> by age.

### Population estimates

We use the
[Population estimates - small area based by single year of age - England and Wales](https://www.nomisweb.co.uk/datasets/pestsyoaoa)
figures as the denominator when calculating percentages.

> The midyear estimates of population are based on results from the latest
> Census of Population with allowance for under-enumeration.

## Raw Data

Unprocessed data is pulled into `data/raw`, generally with a dedicated `dvc`
pipeline stage. In principle, this could also be done with a `dvc import-url`,
although there are issues with Nomis rejecting repeated calls to the same URL,
which it appears `dvc import-url` does.

| Dataset                                        | Description                                                    | DVC Stage                                                                          |
| ---------------------------------------------- | -------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `lms.csv`                                      | Latest release of Labour Market Summary time series            | [pipelines/ons:process@lms](../pipelines/ons/dvc.yaml)                             |
| `mm23.csv`                                     | Latest release of Consumer Prices Index time series            | [pipelines/ons:process@mm23](../pipelines/ons/dvc.yaml)                            |
| `unem.csv`                                     | Latest release of Unemployment and vacancies time series       | [pipelines/ons:process@unem](../pipelines/ons/dvc.yaml)                            |
| `neet-latest.xlsx`                             | Latest analysis of NEET statistics                             | [pipelines/neet:download](../pipelines/neet/dvc.yaml)                              |
| `census-employment.csv`                        | Employment status from 2021 Census                             | [pipelines:nomis-download](../pipelines/dvc.yaml)                                  |
| `claimants-by-pcon-2010-latest.csv`            | Claimant counts                                                | [pipelines:nomis-download](../pipelines/dvc.yaml)                                  |
| `lfs_by_pcon.csv`                              | APS/LFS stats by parliamentary constituency                    | [pipelines/labour-market:download-from-nomis](../pipelines/labour-market/dvc.yaml) |
| `population-estimates-by-pcon-2010-latest.csv` | Mid-year population estimates for parliamentary constituencies | [pipelines:nomis-download](../pipelines/dvc.yaml)                                  |
| `vacancies-by-sector.csv`                      | Result of ONS analysis by sector                               | [pipelines/vacancies:download](../pipelines/vacancies/dvc.yaml)                    |

## Processed Data

These files are published in `data/processed`. These are normalised datasets,
with one variable per line, and as many colums as required to cover the
dimensions.

| Data file                                                                                                          | Description                                                                                                                                          | Pipeline                                                                              |
| ------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| [`lms.csv`](../data/processed/lms.csv)                                                                             | Cleaned monthly LMS stats                                                                                                                            | [pipelines/ons:process@lms](../pipelines/neet/dvc.yaml)                               |
| [`mm23.csv`](../data/processed/mm23.csv)                                                                           | Cleaned monthly CPI stats                                                                                                                            | [pipelines/ons:process@mm23](../pipelines/neet/dvc.yaml)                              |
| [`unem.csv`](../data/processed/unem.csv)                                                                           | Cleaned monthly Unemployment and Vacancies stats                                                                                                     | [pipelines/ons:process@unem](../pipelines/neet/dvc.yaml)                              |
| [`neet.csv`](../data/processed/neet.csv)                                                                           | Cleaned quarterly NEET stats                                                                                                                         | [pipelines/neet:process](../pipelines/neet/dvc.yaml)                                  |
| [`census/employment-status.csv`](../data/processed/census/employment-status.csv)                                   | Processed version of Census 2021 employment status                                                                                                   | [pipelines/census:process-census](../pipelines/census/dvc.yaml)                       |
| [`claimants/claimants-per-population-latest.csv`](../data/processed/claimants/claimants-per-population-latest.csv) | Processed version of Claimant counts - converted to rates, using population estimates as a denominator.                                              | [pipelines/claimants:process-claimants](../pipelines/claimants/dvc.yaml)              |
| [`labour-market/most_recent_by_pcon_2010.csv`](../data/processed/labour-market/most_recent_by_pcon_2010.csv)       | Most recently published APS LFS figures per parliamentary constituency. This creates a backfilled dataset using the [method described below](#patch) | [pipelines/labour-market:process-latest-by-pcon](../pipelines/labour-market/dvc.yaml) |
| [`vacancies/vacancies-growth-by-sector.csv`](../data/processed/vacancies/vacancies-growth-by-sector.csv)           | Processed version of vacancies by sector, including details of key youth employment sector, and sectors that young people want to work in.           | [pipelines/vacancies:process](../pipelines/vacancies/dvc.yaml)                        |

### Backfill patching of data

The LFS data, as a survey, frequently has surpressed values. This is a result of
low levels of statistical significance, or potentially disclosive data (i.e.
small numbers of actual people in data who could be individually identified). As
a result, the 'latest' figures are often missing many parliamentary
constituencies, particularly for filtered age ranges or sex/gender.

To address this, we download the latest 9 periods (reaching back just 2 years
from the latest dates) and then backfill any missing figures from the most
recently available data. Any places with no valid data return the most recent
possible date, and a null value

As an example, raw data of the following format

| geography    |  date   | value |
| :----------- | :-----: | :---: |
| Egchester    | 2023-03 |   -   |
| Egchester    | 2022-12 |  11   |
| Egchester    | 2022-09 |  13   |
| Anotherplace | 2023-03 |  14   |
| Anotherplace | 2022-12 |  12   |
| Anotherplace | 2022-09 |  10   |
| Nulltown     | 2023-03 |   -   |
| Nulltown     | 2022-12 |   -   |
| Nulltown     | 2022-09 |   -   |

Would result in the following output table

| geography    |  date   | value |
| :----------- | :-----: | :---: |
| Egchester    | 2022-12 |  11   |
| Anotherplace | 2023-03 |  14   |
| Nulltown     | 2023-03 |   -   |

This means that the places are not guaranteed to have data from the same date
period, but will be as complete as possible.
