# 🌍 Cultural Transmission & Economic Growth: An OLG Approach

> **Project:** Behavioral Macroeconomics & Data Science
> **Tools:** Python (Pandas, Plotly), LyX/LaTeX, OLG Modeling
> **Data:** World Values Survey (WVS) & Global Preference Survey (Falk et al.)

## 📖 Overview
This project investigates the causal link between **cultural values** and **long-run economic development**. Using a **Bisin-Verdier Overlapping Generations (OLG) Model**, I analyze the transition of societies from "Traditional" equilibria (stagnation) to "Modern" equilibria (growth).

The core hypothesis is that culture is not static; it is an endogenous variable that responds to economic incentives. As technology rises, the trait of **"Independence"** replaces **"Obedience"**, creating the behavioral foundations necessary for capitalism.

---

## The Analysis Pipeline (Code Snapshot)
Below is the core Python logic used to bridge the Macro-Cultural data (WVS) with the Micro-Behavioral data (Falk et al.).

```python
import pandas as pd
import plotly.express as px

# --- Step 1: Exploratory Data Analysis (EDA) ---
# Loading the Global Preference Survey (Stata .dta format)
# Source: Falk et al. (QJE, 2018)
gps_data = pd.read_stata('Data/QJE.dta')

# --- Step 2: Data Aggregation & Preparation ---
# The WVS data is time-series (1981-2022). We aggregate it to get
# the long-run cultural average for each country.
wvs_subset = final_data.groupby('COW_ALPHA')[['Obedience', 'Religious_Faith', 'Independence']].mean().reset_index()

# --- Step 3: Merging Heterogeneous Datasets ---
# Inner Join to align Macro-Culture (WVS) with Micro-Behavior (GPS)
# Matching WVS 'COW_ALPHA' codes with GPS 'ISO3' codes.
merged_data = pd.merge(wvs_subset, gps_data, left_on='COW_ALPHA', right_on='ISO3', how='inner')

# Removing potential duplicates to ensure statistical integrity
merged_data = merged_data.drop_duplicates(subset=['COW_ALPHA'])

# --- Step 4: Statistical Analysis (Correlation Matrix) ---
# Defining the variables of interest for the OLG Model validation
wvs_vars = ['Obedience', 'Religious_Faith', 'Independence']
gps_vars = ['patienceQJE', 'risktaking', 'trustQJE', 'negrecip']

# Calculating Pearson Correlation
corr_matrix = merged_data[wvs_vars + gps_vars].corr()

# --- Step 5: Interactive Visualization ---
fig = px.imshow(
    corr_matrix, 
    text_auto=".2f", 
    color_continuous_scale='RdBu_r', 
    title="Correlation Matrix: Cultural Values vs. Economic Preferences"
)
fig.show()
```

## The OLG Theoretical Framework

The project relies on a Dynastic OLG model where cultural transmission is an economic decision.

### 1. The Agents: Materialists vs. Non-Materialists
The economy consists of two distinct cultural types:
* **Non-Materialists ($N$):** Derive utility from "Direct" sources (e.g., religion, tradition, leisure) and sticking to the status quo. They invest little in human capital ($s \approx 0$).
* **Materialists ($M$):** Derive utility from consumption and wealth. They are forward-looking and invest heavily in education/skills ($s > 0$) to maximize future productivity.

### 2. Paternalistic Altruism & Vertical Transmission
Why do cultures change? Parents choose how to socialize their children based on **Paternalistic Altruism**. They want their children to succeed, but "success" is defined by the economic environment.
* **Condition A (Stagnation):** If Technology ($a_t$) is low, "Obedience" is the safer strategy.
* **Condition B (Growth):** If Technology ($a_t$) rises, the return to innovation increases. "Independence" becomes the optimal trait to transmit.

### 3. The "Critical Mass" Threshold ($\hat{e}$)
Growth is not linear. An economy remains trapped in a Malthusian stagnation until the population of Materialists ($M$) crosses a specific threshold ($\hat{e}$). Once this critical mass is reached, the economy experiences a **"Take-off"**, leading to sustained modern growth.

---

## 📊 Empirical Validation: Interpreting the Correlations

To validate this theory, I merged macro-cultural data (WVS) with micro-behavioral data (Falk et al.). The resulting **Correlation Matrix** confirms the OLG predictions with high precision.

![Correlation Heatmap](./heatmap_preview.png)

### Interpretation of Results

#### 1. Independence ↔ Patience (Positive Correlation)
* **The Result:** A strong positive link between *Independence* (WVS) and *Patience* (GPS).
* **Economic Interpretation:** In the OLG model, the "Materialist" agent invests in the future ($s_{t+1}$). Investment, by definition, requires **delaying gratification**. Societies that emphasize "Independence" are effectively training children to have a **low discount rate**, prioritizing future wealth over immediate pleasure. This "patience" is the fuel of capital accumulation.

#### 2. Obedience ↔ Risk Taking (Negative Correlation)
* **The Result:** *Obedience* is negatively correlated with *Risk Taking*.
* **Economic Interpretation:** Innovation is inherently risky; it requires challenging the status quo. A culture of "Obedience" (high Power Distance) penalizes deviation and failure. Consequently, obedient societies suffer from **high Uncertainty Avoidance**, which suppresses the entrepreneurship required for the economic "Take-off."

#### 3. Independence ↔ Negative Reciprocity (Positive Correlation)
* **The Result:** *Independence* correlates positively with *Negative Reciprocity* (the willingness to punish unfair behavior).
* **Economic Interpretation:** This is a crucial finding for modern market functioning. In traditional (Obedient) clans, trust is based on personal ties. In modern (Independent) economies, dealings are anonymous. To sustain cooperation among strangers, a society needs **"Altruistic Punishment"**—agents must be willing to punish free-riders to enforce contracts. This validates that Independent societies develop the complex social enforcement mechanisms needed for advanced capitalism.

---

## 🗺️ Visualizing the Cultural Transition
The map below tracks the global decline of "Obedience" and the rise of "Independence" over 40 years. Darker regions (Scandinavia, Western Europe) represent societies that have successfully crossed the critical mass threshold ($\hat{e}$).

![Independence Map](./map_preview.png)

---

## 📂 Repository Structure

* ** [Read the Full Report (PDF)](./Report.pdf)**: The complete academic report. Includes mathematical proofs of the OLG propositions and detailed country-level case studies (USA vs. Norway vs. China).
* ** [View the Python Code](./Cultural_Analysis.py)**: The full Python script used for data cleaning, merging, and visualization.
* **`Data/`**: Contains snapshots of the datasets used (Note: Full GPS data available via the Briq Institute).

---

*Author: [Eirini Kontiza]*
*Behavioral Macroeconomics*
