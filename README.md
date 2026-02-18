# Cultural-Transmission-Economic-Growth
This study investigates the intergenerational transmission of cultural values and their impact on sustainable economic growth. Utilizing the Overlapping Generations (OLG) Model framework, I analyze how specific traits—Independence, Religious Faith, and Obedience—shift over time and correlate with economic development.
<img width="490" height="188" alt="data cleaning" src="https://github.com/user-attachments/assets/ebfec91e-2601-43eb-b869-34b34376bb8a" />
<img width="1257" height="673" alt="Heatmap" src="https://github.com/user-attachments/assets/d58eea85-03d0-4dcf-bd27-90e5945a67ef" />
<img width="1268" height="689" alt="Independence Map 1981-2022" src="https://github.com/user-attachments/assets/f0d7af45-c7c6-4199-bd85-b25355deb246" />
[Report_Behavioral.pdf](https://github.com/user-attachments/files/25390087/Report_Behavioral.pdf)
[Behavioral_Python.py](https://github.com/user-attachments/files/25390092/Behavioral_Python.py)

  # Case Study: Cultural Transmission & Economic Growth
**A Data-Driven Analysis using OLG Models and Behavioral Economics**

**Author:** Irene Kontiza  
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas)](https://pandas.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-Visualization-3F4F75?style=for-the-badge&logo=plotly)](https://plotly.com/)

---

## 1. Executive Summary & Methodology
This study investigates the intergenerational transmission of cultural values and their impact on sustainable economic growth. Utilizing the **Overlapping Generations (OLG) Model**, I analyze how traits like **Independence**, **Religious Faith**, and **Obedience** shift over time.

### 1.1 Data Pipeline
Data was sourced from the **World Values Survey (WVS)** and cleaned using Python. Below is the logic used to filter negative values and aggregate the data by country.

> **Note:** The full executable code can be found in the [`src/`](src/analysis_code.py) folder.

```python
# --- Data Cleaning Snippet ---
# Filtering out negative values (-1, -2 representing "Don't Know")
wvs_clean = wvs_raw[wvs_raw['Independence'] >= 0]

# Aggregating by Country to create Time-Series averages
final_data = wvs_clean.groupby('COW_ALPHA')[
    ['Obedience', 'Religious_Faith', 'Independence']
].mean().reset_index()

