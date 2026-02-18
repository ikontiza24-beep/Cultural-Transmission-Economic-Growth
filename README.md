# Cultural Transmission & Economic Growth
**A Case Study on Behavioral Macroeconomics using Python**

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas)
![Plotly](https://img.shields.io/badge/Plotly-Visualization-3F4F75?style=for-the-badge&logo=plotly)

This project explores the intergenerational transmission of cultural values and their impact on sustainable economic growth using the **Overlapping Generations (OLG) Model**.

---

## Table of Contents
* [1. Project Overview](#1-project-overview)
* [2. Theoretical Framework](#2-theoretical-framework)
* [3. Data Pipeline & Cleaning](#3-data-pipeline--cleaning)
* [4. Geospatial Analysis](#4-geospatial-analysis)
* [5. Statistical Validation](#5-statistical-validation)
* [6. Files & Resources](#6-files--resources)

---

## 1. Project Overview
The goal of this analysis is to investigate how cultural traits—specifically **Independence** vs. **Obedience**—shift over time and correlate with economic development.

Using data from the **World Values Survey (WVS)** and **Global Preference Survey (GPS)**, I test the hypothesis that economic "take-off" requires a critical mass of "Materialist" agents who value autonomy and future investment over traditional obedience.

---

## 2. Theoretical Framework
The analysis is grounded in the **Bisin & Verdier** cultural transmission model.
* **Non-Materialists ($N$):** Derive utility from tradition and obedience.
* **Materialists ($M$):** Derive utility from wealth/innovation and possess high **Patience**.

### Hofstede's Cultural Dimensions
I cross-referenced WVS data with Hofstede’s dimensions for USA, Norway, and China. A key finding is China's "Paradox": High Independence scores (70%) despite a collectivist history, indicating **Self-Reliance** as a modern survival mechanism.

*(Insert your chart below)*
![Hofstede Analysis](hofstede_chart.png)

---

## 3. Data Pipeline & Cleaning
Raw data from WVS contained negative dummy variables for non-responses. Using `pandas`, I cleaned the dataset and aggregated it by country to create time-series averages.

```python
# --- Python Code Snippet: Data Cleaning ---
import pandas as pd

# 1. Filtering out negative values (-1, -2 representing "Don't Know")
wvs_clean = wvs_raw[wvs_raw['Independence'] >= 0]

# 2. Aggregating by Country to create Time-Series averages
final_data = wvs_clean.groupby('COW_ALPHA')[
    ['Obedience', 'Religious_Faith', 'Independence']
].mean().reset_index()

print("Data Cleaning Complete. Rows:", len(final_data))
