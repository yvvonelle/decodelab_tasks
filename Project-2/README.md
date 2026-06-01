# Project 2: Exploratory Data Analysis (EDA)

## Project Overview
This project performs a comprehensive Exploratory Data Analysis (EDA) on a retail orders dataset consisting of 1,200 rows and 14 columns. Spanning transactions from 2023 to 2025, the analysis focuses on moving past basic descriptive metrics to evaluate data distribution, identify hidden structural leaks (such as high cancellation rates), and map the specific customer behaviors driving overall revenue.

---

## Technical Architecture & Analytical Structure
The analysis is structured around five core data validation and exploratory pillars to ensure insights are statistically sound and actionable:

### 1. Descriptive Statistics & Distribution Analysis
* **Metric Baselines:** Evaluated average order value ($1,053.97) against the median ($823.62) to identify a $230 gap, confirming a heavily right-skewed distribution.
* **Volume Profiling:** Documented typical purchase sizes to find customers average 3 items per transaction, with unit prices covering a broad spectrum ($11.39 to $699.93).

### 2. Outlier Detection & Correlation Mapping
* **Statistical Boundaries:** Implemented Interquartile Range (IQR) analysis on TotalPrice to flag 8 legitimate high-value outliers exceeding the $3,330.41 upper bound.
* **Feature Interdependence:** Built correlation matrices proving UnitPrice is the primary driver of total value (Strong Positive: 0.72) while Quantity maintains a moderate correlation (0.62). 

### 3. Temporal Tracking (Time-Series)
* **Revenue Volatility:** Grouped transactions by month and year to map economic fluctuations, isolating June as a recurring annual peak (peaking in June 2024 at $68,068.54) and flagging April/May as low-performing windows.
* **Volume vs Value:** Cross-referenced order volumes against total monthly revenue to prove transaction value influences bottom-line revenue far more than raw transaction volume.

### 4. Operations, Channels, & Product Performance
* **Fulfillment Integrity:** Evaluated order statuses to map a critical operational failure—discovering cancelled and returned statuses account for 41.4% of total volume.
* **Marketing & Financial Vectors:** Profiled revenue across social acquisition channels (Instagram vs. Facebook) and payment gateways (Credit vs. Debit cards) to rank their fiscal performance.

---

## Key Findings
* **The Revenue Leak:** Cancelled orders (250) are the most frequent order status, outnumbering completed deliveries (231). Worse, cancelled orders carry the highest average transaction value ($1,105.58), meaning the business loses its highest-value customers most frequently.
* **Product Catalog Homogeneity:** Revenue is distributed evenly across all 7 product types with a tight gap of only ~$44,000 between the top category (Chair: $195,620) and the lowest (Phone: $151,722). 
* **Acquisition Efficiency:** Instagram serves as the volume and revenue engine (259 orders, $275,285 total), while Facebook acts as a high-value niche channel, securing the highest average spend per order ($1,098).
* **Payment Gateways:** Credit Card transactions yield both the highest average order value ($1,127.55) and highest aggregate revenue ($263,847), while Debit Card users represent the lowest-spending segment.

---

## Strategic Recommendations
* **Prioritize Cancellation Workflows:** Address the 41.4% order cancellation and return rate immediately. Investigating systemic issues in checkout friction or post-purchase confirmation is the single most urgent revenue recovery opportunity.
* **Shift to Premium Product Marketing:** Because unit price drives total order value heavily while quantity per order remains constant, marketing strategies should favor higher-tier products over volume-discount packages.
* **Optimize Acquisition Spend:** Scale up ad spend on Instagram to leverage its high volume/revenue capture, and deploy highly targeted, high-ticket campaigns toward Facebook demographics to exploit their premium spending habits.
* **Seasonality Alignment:** Restructure annual inventory, marketing budgets, and promotional calendars around the high-performing June surge while minimizing exposure during the consistently slow April/May periods.

---

