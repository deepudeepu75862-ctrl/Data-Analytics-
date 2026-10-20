# EDA on Retail Sales Data — OASIS INFOBYTE Data Analytics

**Task folder name:** `DataAnalytics-L1-EDARetailSales`

## Important dataset note
This ZIP includes a **synthetic sample dataset** (`data/retail_sales_sample.csv`) created for learning and to make the project runnable offline. It is not a real company's sales data and findings from it are demonstration-only. Before internship submission, replace it with a suitable real retail dataset you are permitted to use, then rerun the analysis and update your conclusions.

## Project objectives
- Inspect the dataset shape, data types, missing values, and duplicate rows.
- Calculate descriptive statistics (mean, median, mode, standard deviation).
- Visualize monthly and quarterly sales.
- Analyse customer age groups and gender.
- Identify the top 10 products by units sold and revenue by category.
- Create a numerical correlation heatmap.
- Add an extra weekday average transaction visualization.
- Export cleaned data, summary tables, charts, and actionable recommendations.

## Project structure
```text
DataAnalytics-L1-EDARetailSales/
├── data/
│   └── retail_sales_sample.csv
├── outputs/                  # charts and cleaned results appear here after running
├── eda_retail_sales.py       # complete runnable Python analysis
├── retail_sales_eda.ipynb    # notebook version with markdown explanations
├── requirements.txt
└── README.md
```

## Setup (Windows PowerShell)
1. Install Python 3.10 or later.
2. Open PowerShell in this project folder.
3. Create a virtual environment:
   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
4. Install packages:
   ```powershell
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```
5. Run the script:
   ```powershell
   python eda_retail_sales.py
   ```
6. Or open the notebook:
   ```powershell
   jupyter notebook retail_sales_eda.ipynb
   ```
   Run all cells from top to bottom.

## Main output files
The script saves PNG charts and CSV summaries under `outputs/`:
- `monthly_sales.png`
- `quarterly_sales.png`
- `age_group_distribution.png`
- `gender_breakdown.png`
- `top_10_products.png`
- `revenue_by_category.png`
- `correlation_heatmap.png`
- `weekday_average_transaction.png`
- `cleaned_retail_sales.csv`
- `category_revenue_summary.csv`
- `top_products_summary.csv`

## How to use a real dataset
Keep the same column names or adjust the code to match your dataset. Expected columns are:
`Transaction_ID`, `Date`, `Customer_ID`, `Age`, `Gender`, `Product`, `Category`, `Quantity`, `Unit_Price`, `Total_Amount`.
If your dataset has different column names, rename them before analysis. Ensure dates parse correctly and monetary values are numeric.

## Example business recommendations
These recommendations are generated from the sample data and must be checked again after loading a real dataset:
1. Prioritize inventory and promotions for the category with the highest revenue.
2. Feature best-selling products in bundles and recommendations.
3. Use age-group and weekday patterns to test targeted promotions.

## GitHub submission
The OASIS INFOBYTE task guide specifies a shared `OIBSIP` repository and the folder format:
`OIBSIP/DataAnalytics-L1-EDARetailSales/`
Include the source code, README, and relevant outputs/screenshots. The guide also asks for a demo video and a LinkedIn post as part of its workflow; this ZIP does not create or submit those on your behalf.
