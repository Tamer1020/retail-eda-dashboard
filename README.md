# Retail Product Analysis Dashboard

An interactive Streamlit dashboard for exploring retail product pricing and category patterns. The application combines lightweight data cleaning, filterable summary statistics, and Plotly visualizations in a simple browser interface.

## What It Does

- standardizes inconsistent fat-content labels
- fills missing product weights with the dataset mean
- fills missing outlet-size values with the most frequent category
- filters records by fat content and outlet type
- reports count, mean, standard deviation, minimum, and maximum MRP
- visualizes average MRP by selected categories
- identifies product types represented by fewer than 100 records

## Technology

- Python
- pandas
- Streamlit
- Plotly

## Repository Contents

- `app_with_sidebar.py` — Streamlit dashboard
- `retail_sales_analysis.ipynb` — companion exploratory analysis notebook
- `Test-Set.csv` — dataset used by the dashboard

## Run Locally

Install the required packages:

```bash
python -m pip install streamlit pandas plotly
```

Start the dashboard from the repository root:

```bash
streamlit run app_with_sidebar.py
```

The application expects `Test-Set.csv` to remain in the repository root.

## Scope

This repository is an exploratory data-analysis and visualization project. It demonstrates data cleaning, grouped statistical summaries, interactive filtering, and dashboard development; it does not claim to provide a production forecasting model.
