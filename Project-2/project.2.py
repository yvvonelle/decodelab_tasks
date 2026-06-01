# %%
import pandas as pd
import numpy as np

# %%
df = pd.read_csv(r"cleaned_dataset.csv",parse_dates=["date"])

# %%
#Explonatory Data Analysis(EDA)
# finding mean,median and count
df[["unit_price","quantity","total_price"]].agg(["mean","median","count"]).round(2)

# %%
#skewness check
#|skew| >1 means a skewed data
#normal skewness
df[["unit_price", "quantity", "total_price"]].skew()

# %%
#outlier detection
cols = ["unit_price", "quantity", "total_price"]

for col in cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]

    print(f"\n{col}: {len(outliers)} outliers")

# %%
#correlation analysis
cols = ["quantity","unit_price","total_price"]
corr =df[cols].corr()
print(corr.round(4))

# %%
#TRENDS AND PATTERNS
#Sales over time
df["month"]=df["date"].dt.to_period("M")
monthly_sales = df.groupby("month")["total_price"].sum().reset_index()
monthly_sales["month"] = monthly_sales["month"].astype(str)
monthly_sales.sort_values("total_price", ascending=False).reset_index(drop=True)


# %%
#order volume over time
monthly_orders = df.groupby("month")["order_id"].count().reset_index()
monthly_orders.columns = ["month", "order_count"]
monthly_orders["month"] = monthly_orders["month"].astype(str)
monthly_orders.sort_values("order_count", ascending=False).reset_index(drop=True)

# %%
#revenue by product
revenue_by_product = df.groupby("product")["total_price"].sum().reset_index()
revenue_by_product.columns = ["product", "total_revenue"]
revenue_by_product = revenue_by_product.sort_values("total_revenue", ascending=False).reset_index(drop=True)
revenue_by_product

# %%
#order status pattern
status_analysis = df.groupby("order_status").agg(
    Order_Count=("order_id", "count"),
    Avg_TotalPrice=("total_price", "mean"),
    Total_Revenue=("total_price", "sum")
).reset_index()
status_analysis = status_analysis.sort_values("Order_Count", ascending=False).reset_index(drop=True)
status_analysis["Avg_TotalPrice"] = status_analysis["Avg_TotalPrice"].round(2)
status_analysis["Total_Revenue"]  = status_analysis["Total_Revenue"].round(2)
status_analysis

# %%
#referral source performance
referral_analysis = df.groupby("referral_source").agg(
    Order_Count=("order_id", "count"),
    Avg_TotalPrice=("total_price", "mean"),
    Total_Revenue=("total_price", "sum")
).reset_index()
referral_analysis = referral_analysis.sort_values("Total_Revenue", ascending=False).reset_index(drop=True)
referral_analysis["Avg_TotalPrice"] = referral_analysis["Avg_TotalPrice"].round(2)
referral_analysis["Total_Revenue"]  = referral_analysis["Total_Revenue"].round(2)
referral_analysis
 

# %%
#payment method vs order value
payment_analysis = df.groupby("payment_method").agg(
    Order_Count=("order_id", "count"),
    Avg_TotalPrice=("total_price", "mean"),
    Total_Revenue=("total_price", "sum")
).reset_index()

payment_analysis = payment_analysis.sort_values("Total_Revenue", ascending=False).reset_index(drop=True)
payment_analysis["Avg_TotalPrice"] = payment_analysis["Avg_TotalPrice"].round(2)
payment_analysis["Total_Revenue"]  = payment_analysis["Total_Revenue"]
payment_analysis


