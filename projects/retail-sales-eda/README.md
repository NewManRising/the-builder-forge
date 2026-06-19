
## What This Project Is
I redid my UT Dallas/Full Stack bootcamp data science notebook. This is just pure EDA on retail sales and no models were trained. Most of the code is the same from my old notebook but I switched out the dataset and used the UCI Online Retail II data.


Download the UCI Online Retail II dataset from their website below and place it in `data/raw/online_retail.xlsx`:
https://archive.ics.uci.edu/dataset/502/online+retail+ii


Tasks Completed:
- Swapped synthetic AAL data for real UCI Online Retail II dataset
- Created revenue column, set datetime index
- Analyzed country revenue and volume, hour of day, time series trends
- Built 5 visualizations
- Anomaly/cancellation analysis
- Saved cleaned data and summary tables
- Written summary report


## Project Structure
```text
retail-sales-eda/
│
├── data/
│   ├── processed/
│   │   ├── sales_analysis_cleaned.csv
│   │   ├── by_country_revenue.csv
│   │   ├── top_products_rev.csv
│   │   ├── top_products_qty.csv
│   │   ├── by_hour.csv
│   │   └── monthlytotals.csv
│   └── raw/
│       └── online_retail.xlsx        # Source data - download from UCI Website
│
├── notebooks/
│   └── sales_analysis.ipynb
│
├── outputs/
│   ├── figures/
│   │   ├── revenue_by_country.png
│   │   ├── monthly_revenue_trend.png
│   │   ├── top_products_revenue.png
│   │   ├── top_products_volume.png
│   │   └── sales_by_hour.png
│   └── reports/
│       └── sales_report.txt
│
├── .gitignore
├── README.md
└── requirements.txt
```