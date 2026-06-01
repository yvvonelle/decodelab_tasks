# %%
import pandas as pd
import numpy as np

# %%
#importing dataset
df = pd.read_csv(r"Dataset.csv")


# %%
#checking for columns
df.columns

# %%
#cleaning up columns to give right format
df.columns = [
    "order_id",
    "date",
    "customer_id",
    "product",
    "quantity",
    "unit_price",
    "shipping_address",
    "payment_method",
    "order_status",
    "tracking_number",
    "items_in_cart",
    "coupon_code",
    "referral_source",
    "total_price",
]

# %%
df.columns

# %%
# PHASE 1:STRATEGIC IMPUTATION
# finding count of missing vales
missing_count = df.isnull().sum()
missing_count

# %%
#filing in the missing coupon code with "no coupon"
df['coupon_code'] = df['coupon_code'].fillna("NO_COUPON")

# %%
df.head()

# %%
# PHASE 2:THE INTEGRITY AUDIT
#drop duplicates
df = df.drop_duplicates()

# %%
#ensure order_id is unique
df = df.drop_duplicates(subset=["order_id"],keep="first")

# %%
final_rows = len(df)
final_rows

# %%
# PHASE 3: STANDARDISE FORMATS
#format date format
df["date"] = pd.to_datetime(df["date"],errors="coerce")

# %%
# removing white spaces,convertin to string
for col in ["product", "shipping_address", "payment_method", "order_status"]:
    df[col] = df[col].astype(str).str.strip()

# %%
#convert to uppercase
df["payment_method"] = df["payment_method"].str.upper()

# %%
df["order_status"] = df["order_status"].str.upper()

# %%
df["product"] = df["product"].str.title()

# %%
#rounding off currency to 2 decimal places
df['unit_price'] = df['unit_price'].round(2)
df['total_price'] = df['total_price'].round(2)

# %%
df.to_csv(r"cleaned_dataset.csv")

