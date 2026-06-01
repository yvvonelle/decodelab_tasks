# Retail Orders Analytics Project: End-to-End Business Intelligence

## Project Overview
This project analyzes 1,200 retail transactions recorded between 2023 and 2025, taking raw data from a messy spreadsheet all the way to clear, actionable business insights. Developed as part of the **DecodeLabs Data Analytics Internship (Batch 2026)**, the workflow bridges data cleaning, exploratory analysis, relational database querying, and data storytelling.

---

## How the Work Was Done
The lifecycle of this analytics pipeline was executed across four distinct architectural stages:

### Stage 1: Data Cleaning & Preparation (Python)
Before initiating any analysis, the data was rigorously audited to ensure it was completely trustworthy:
* The file was converted from .xlsx to CSV — a lighter, more portable format that worked seamlessly with Python and the SQLite database downstream.
* **Integrity Checks:** Scanned for duplicate order IDs and standardized date formatting across all entries.
* **Mathematical Validation:** Confirmed calculation accuracy for every row using the ledger rule: `Quantity × Price = Total`.
* **Sparsity Audit:** Flagged 309 empty entries in the coupon column, which were validated as operationally normal since not every customer applies a coupon.

### Stage 2: Exploratory Data Analysis (Python)
This stage focused on uncovering the core statistical properties and shapes of the transactional data:
* **Distribution Profiles:** Discovered a heavily right-skewed distribution; the average order value ($1,053) was noticeably higher than the median value ($823), proving a small number of large orders pull the average up.
* **Outlier & Drivers Mapping:** Isolated eight unusually high transactions and statistically confirmed that item price is the single strongest predictor of the final invoice value.

### Stage 3: Relational Database Querying (SQL / SQLite)
The clean dataset was migrated into a database environment to precisely slice, filter, and aggregate multi-dimensional metrics:
* **Granular Deep-Dives:** Formulated structured queries to evaluate completed order volume, inventory velocity by product category, and revenue generation across various payment gateways and marketing acquisition networks.

### Stage 4: Visual Data Storytelling (Python Charts)
The final stage translated tabular, structural metrics into intuitive, executive-level visual representations using `matplotlib` and `seaborn`:
* **Visual Artifacts:** Produced time-series line graphs to trace sales fluctuations, structural pie charts to break down order outcomes, and categorical bar charts to contrast products and marketing channels side by side.

---

## Key Business Revelations
* **Critical Order Attrition (The Main Leak):** Only about 1 in 5 orders (19%) completes successfully. Cancellations and returns combine to make up over 40% of all platform orders—with cancelled transactions heavily trending among higher-value baskets. This stands as the primary obstacle facing the business.
* **Balanced Catalog Portfolio:** Product demand is highly distributed with no single item dominating the catalog. The top seller (Printers: 181 orders) leads the lowest-performing category (Phones: 156 orders) by a tight margin of only ~25 orders. In absolute revenue generation, Chairs lead the entire catalog at $195,620.
* **Financial & Acquisition Drivers:** Credit cards serve as the top revenue gateway ($263,847), closely followed by online payments ($262,442). On the marketing front, Instagram functions as the volume driver (259 orders yielding $275,285 in revenue), while Facebook traffic represents high-value niches, capturing the highest average spend per order ($1,098).
* **Macro Sales Contraction:** Time-series tracking highlights June 2024 as the historic sales peak ($68,068). While 2023 maintained the highest overall consistency, a persistent downward trajectory has developed post-2023 that requires urgent strategic attention.

---

## Strategic Recommendations

1. **Optimize Checkout & Fulfillment Loops:** Addressing the 40%+ order failure rate is paramount. The business must evaluate user drop-off points and cart changes, specifically creating high-touch verification steps for high-value purchases to mitigate cancellations.
2. **Promote Premium Items Over Bulk Discounts:** Because unit price strongly dictates final invoice values rather than raw quantity, marketing placements should highlight high-tier premium items instead of offering volume-based "buy more, save more" discount models.
3. **Bifurcate Marketing Capital Allocation:** Restructure ad spend to align with channel characteristics—allocating Instagram budgets toward wide-funnel reach and high-volume acquisition, while dedicating Facebook budgets toward high-end, premium product ads to leverage their high spending behavior.
4. **Synchronize Inventory and Spend with Seasonality:** Sales consistently peak in June, meaning inventory volumes, marketing campaigns, and staffing configurations should scale up to meet this window. Conversely, scale back financial exposure and ad spend during the slow historical periods of April and May.

---

## Unified Tech Stack & Dataset Blueprint
* **Core Technologies:** Excel · Python (`pandas`, `matplotlib`, `seaborn`) · SQLite
* **Dataset Scope:** 1,200 rows × 14 columns
* **Monitored Fields:** Order ID, Date, Customer ID, Product, Quantity, Price, Shipping Address, Payment Method, Order Status, Tracking Number, Items in Cart, Coupon Code, Referral Source, and Total Price.

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/yvvonelle/Task-1-Yvvone-Muli.git
cd Task-1-Yvvone-Muli
```

### 2. Install Dependencies

Install all required Python packages using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 3. Run Data Cleaning & Conversion (Project 1)

Run the automated pipeline to convert the source Excel file into a clean CSV and perform structural data quality checks:

```bash
project.1.py
```

### 4. Run Exploratory Analysis & Visualization (Projects 2 & 4)

Execute the analysis and visualization scripts to generate business intelligence insights and charts:

```bash
projet.2.py
project.4.py
```



### 5. Run SQL Queries (Project 3)

1. Open **DB Browser for SQLite** (or your preferred SQLite client).
2. Import the generated `cleaned_dataset.csv` file into a new table named `cleaned_dataset`.
3. Open the `queries.sql` file included in this repository.
4. Copy and execute the queries against your database to perform analytical reporting and business insights generation.
