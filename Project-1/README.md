# Project 1: Data Cleaning & Preparation  

## Overview
This project involved auditing and cleaning a retail orders dataset to ensure data integrity before performing any analysis or visualization.

The dataset was initially provided in Excel format and was converted to CSV for processing. All cleaning and validation work was performed using Python.

---

## Dataset
- **Original File:** Dataset_for_Data_Analytics.xlsx  
- **Working File:** cleaned_dataset.csv  
- **Records:** 1,200 rows  
- **Columns:** 14  

### Column List:
OrderID, Date, CustomerID, Product, Quantity, UnitPrice, ShippingAddress, PaymentMethod, OrderStatus, TrackingNumber, ItemsInCart, CouponCode, ReferralSource, TotalPrice

---

## Tools Used
- Microsoft Excel (for CSV conversion only)
- Python (Pandas, NumPy)

---

## Process

### 1. Data Import & Conversion
- Converted Excel dataset into CSV format using Microsoft Excel
- Loaded dataset into Python using Pandas for analysis and cleaning

### 2. Duplicate Check
- Checked for duplicate **OrderID** values using Python
- Confirmed all OrderIDs were unique

### 3. Date Validation
- Verified consistency of all date formats using Python datetime parsing

### 4. Price Verification
- Validated calculations using Python:
- Confirmed all computed values matched recorded totals

### 5. Missing Values Analysis
- Used Python to check for null and blank values across all columns

### 6. Categorical Consistency
Reviewed and standardized categorical columns:
- Product
- PaymentMethod
- OrderStatus
- ReferralSource

---

## Key Findings

- ✅ No duplicate OrderIDs detected  
- ✅ All date formats are consistent  
- ✅ No mismatches in TotalPrice calculations  
- ✅ All categorical values are clean and standardized  
- ⚠️ 309 blank values found in **CouponCode** column  
- These were retained as valid since coupons are optional  

---



  
