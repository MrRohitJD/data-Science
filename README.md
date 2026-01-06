# CWH — Learning Notebooks and Examples

This repository is a personal collection of tutorials, Jupyter notebooks, and example scripts covering fundamental data-science and web-development topics.

## Overview
- Hands-on notebooks for NumPy, Pandas, Matplotlib/Seaborn, and basic machine learning.
- Web data collection examples using `requests` and `BeautifulSoup`.
- Small ML projects and practical exercises using scikit-learn.

## Top-level structure
- `_01numpys/` — NumPy notebooks and exercises.
- `_02_Pandas/` — Pandas tutorials: cleaning, transforming, aggregation, merging, CSV work.
- `_03_ mathplots/` — Matplotlib and Seaborn plotting notebooks.
- `_04_Data_Collection_Techniques/` — Web scraping notebooks and saved HTML samples.
- `_05_Practical_ML_using_Scikitlearn/` — Scikit-learn examples and datasets.
- `_06_first_ML_project/` — A small housing ML project and related scripts.
- `_07_Web_Development_for_DS/` — Starter Flask notebooks and examples.
- `base/` — Python virtual environment used for these notebooks.

## How to use
1. Install Python 3.8+.
2. Create and activate a virtual environment (recommended):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1   # PowerShell
```

3. Install Jupyter and needed packages (example):

```powershell
pip install jupyter numpy pandas matplotlib seaborn scikit-learn requests beautifulsoup4
jupyter lab   # or `jupyter notebook`
```

4. Open the notebooks with Jupyter or in VS Code (with the Jupyter extension).

## Notes
- The `base/` folder contains a virtual environment — you can create a fresh venv instead of using it.
- Data files used by notebooks are stored alongside the notebooks (e.g., CSV and JSON files).

