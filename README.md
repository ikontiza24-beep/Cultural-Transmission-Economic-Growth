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
![Hofstede Analysis](hofstede chart.png)

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


4. Geospatial Analysis

Using Plotly, I visualized the global shift from "Obedience" to "Independence" over 40 years.
The Rise of Independence

As productivity increases, the market rewards innovation. The map below shows the high concentration of "Independence" in developed economies, confirming the OLG prediction.

Figure 1: Global distribution of Independence. Darker regions indicate higher intensity.
5. Statistical Validation

To validate the macro-cultural findings, I integrated micro-behavioral data from Falk et al. (2018).
Methodology

I performed an inner merge between the WVS (Cultural) and GPS (Behavioral) datasets and calculated the Pearson Correlation Matrix.
# --- Python Code Snippet: Merging & Correlation ---

# Inner join ensures we only analyze countries present in both datasets
merged_data = pd.merge(wvs_subset, gps_data, left_on='COW_ALPHA', right_on='ISO3', how='inner')

# Calculating Pearson Correlation
corr_matrix = merged_data[['Independence', 'patienceQJE', 'risktaking']].corr()

Key Findings

The Heatmap below confirms the theory:

    Patience vs. Obedience: Strong negative correlation (-0.498). Traditional societies prioritize immediate utility.

    Risk Taking: Positively correlated with Independence (+0.237).

File	Description
Report.pdf	The full economic analysis and mathematical proofs.
analysis_code.py	The complete Python script used for this project.
