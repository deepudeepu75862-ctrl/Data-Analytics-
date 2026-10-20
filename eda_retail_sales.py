"""
OIBSIP Data Analytics — Task 1: EDA on Retail Sales Data
Run from this folder with: python eda_retail_sales.py
This project uses a clearly labelled synthetic sample dataset so it runs offline.
Replace data/retail_sales_sample.csv with an approved real dataset before final submission.
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "data" / "retail_sales_sample.csv"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)
sns.set_theme(style="whitegrid")

df = pd.read_csv(DATA_PATH, parse_dates=["Date"])
print("\n=== INITIAL INSPECTION ===")
print("Shape:", df.shape)
print("\nData types:\n", df.dtypes)
print("\nMissing values:\n", df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())

# Clean data: remove duplicate rows; fill missing categorical values and numerical values.
df = df.drop_duplicates().copy()
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df["Unit_Price"] = pd.to_numeric(df["Unit_Price"], errors="coerce")
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Gender"] = df["Gender"].fillna("Not specified")
df["Product"] = df["Product"].fillna("Unknown product")
df["Unit_Price"] = df["Unit_Price"].fillna(df["Unit_Price"].median())
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce").fillna(1)
df["Total_Amount"] = df["Quantity"] * df["Unit_Price"]
df["Month"] = df["Date"].dt.to_period("M").astype(str)
df["Quarter"] = df["Date"].dt.to_period("Q").astype(str)
df["Age_Group"] = pd.cut(
    df["Age"], bins=[17, 24, 34, 44, 54, 64, 100],
    labels=["18–24", "25–34", "35–44", "45–54", "55–64", "65+"]
)

print("\n=== DESCRIPTIVE STATISTICS ===")
print(df[["Age", "Quantity", "Unit_Price", "Total_Amount"]].describe())
print("\nMedian:\n", df[["Age", "Quantity", "Unit_Price", "Total_Amount"]].median(numeric_only=True))
print("\nMode:\n", df[["Age", "Quantity", "Unit_Price", "Total_Amount"]].mode().iloc[0])
print("\nStandard deviation:\n", df[["Age", "Quantity", "Unit_Price", "Total_Amount"]].std(numeric_only=True))

# Monthly and quarterly sales trends
monthly = df.groupby("Month", observed=False)["Total_Amount"].sum()
plt.figure(figsize=(12, 5))
monthly.plot(marker="o")
plt.title("Monthly Retail Sales")
plt.xlabel("Month"); plt.ylabel("Revenue"); plt.xticks(rotation=60); plt.tight_layout()
plt.savefig(OUT / "monthly_sales.png", dpi=160); plt.close()

quarterly = df.groupby("Quarter", observed=False)["Total_Amount"].sum()
plt.figure(figsize=(9, 5))
quarterly.plot(kind="line", marker="o")
plt.title("Quarterly Retail Sales")
plt.xlabel("Quarter"); plt.ylabel("Revenue"); plt.xticks(rotation=30); plt.tight_layout()
plt.savefig(OUT / "quarterly_sales.png", dpi=160); plt.close()

# Customer demographics
plt.figure(figsize=(8, 5))
age_order = ["18–24","25–34","35–44","45–54","55–64","65+"]
df["Age_Group"].value_counts().reindex(age_order, fill_value=0).plot(kind="bar")
plt.title("Customer Age Group Distribution"); plt.xlabel("Age group"); plt.ylabel("Transactions")
plt.tight_layout(); plt.savefig(OUT / "age_group_distribution.png", dpi=160); plt.close()

plt.figure(figsize=(7, 5))
df["Gender"].value_counts().plot(kind="bar")
plt.title("Transactions by Gender"); plt.xlabel("Gender"); plt.ylabel("Transactions")
plt.tight_layout(); plt.savefig(OUT / "gender_breakdown.png", dpi=160); plt.close()

# Products and categories
top_products = df.groupby("Product")["Quantity"].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 6))
top_products.sort_values().plot(kind="barh")
plt.title("Top 10 Best-Selling Products by Quantity"); plt.xlabel("Units sold"); plt.ylabel("Product")
plt.tight_layout(); plt.savefig(OUT / "top_10_products.png", dpi=160); plt.close()

category_revenue = df.groupby("Category")["Total_Amount"].sum().sort_values(ascending=False)
plt.figure(figsize=(9, 5))
category_revenue.plot(kind="bar")
plt.title("Revenue by Product Category"); plt.xlabel("Category"); plt.ylabel("Revenue")
plt.xticks(rotation=25, ha="right"); plt.tight_layout()
plt.savefig(OUT / "revenue_by_category.png", dpi=160); plt.close()

# Correlation heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df[["Age","Quantity","Unit_Price","Total_Amount"]].corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix"); plt.tight_layout()
plt.savefig(OUT / "correlation_heatmap.png", dpi=160); plt.close()

# Extra visualization: average transaction value by weekday
df["Weekday"] = df["Date"].dt.day_name()
weekday_order = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
weekday_avg = df.groupby("Weekday")["Total_Amount"].mean().reindex(weekday_order)
plt.figure(figsize=(9, 5))
weekday_avg.plot(kind="bar")
plt.title("Average Transaction Value by Weekday"); plt.xlabel("Weekday"); plt.ylabel("Average transaction value")
plt.xticks(rotation=25, ha="right"); plt.tight_layout()
plt.savefig(OUT / "weekday_average_transaction.png", dpi=160); plt.close()

# Export cleaned dataset and summary tables
df.to_csv(OUT / "cleaned_retail_sales.csv", index=False)
category_revenue.rename("Revenue").to_csv(OUT / "category_revenue_summary.csv")
top_products.rename("Units_Sold").to_csv(OUT / "top_products_summary.csv")

print("\n=== KEY FINDINGS (DEMO DATA) ===")
print("Total revenue:", round(df["Total_Amount"].sum(), 2))
print("Average transaction value:", round(df["Total_Amount"].mean(), 2))
print("Top revenue category:", category_revenue.index[0], "-", round(category_revenue.iloc[0], 2))
print("Best-selling product by units:", top_products.index[0], "-", int(top_products.iloc[0]), "units")
print("Largest age group by transaction:", df["Age_Group"].value_counts().idxmax())
print("\n=== ACTIONABLE RECOMMENDATIONS ===")
print("1. Prioritize inventory and promotions for the category with the highest revenue.")
print("2. Feature best-selling products in bundles and product recommendations.")
print("3. Use age-group and weekday patterns to test targeted promotions; validate using real data.")
print("\nDone. Charts and cleaned tables are saved in the outputs/ folder.")
