# Project 4: Data Storytelling & Insights using Visualizations.

## Project Overview
This project focuses on translating complex transactional retail data into clear, actionable business stories using data visualization. By utilizing Python's charting libraries, the analysis builds a visual narrative around catalog performance, operational inefficiencies, payment preferences, and channel-based customer quality to guide executive decision-making.

---

## Technical Architecture & Core Parameters
The data visualization pipeline is structured using standard Python data science libraries to construct six production-grade visualizations:

* **Tools Used:** Python (`pandas`, `matplotlib`, `seaborn`)
* **Input Dataset:** `Dataset.csv`
* **Dataset Scale:** 1,200 rows × 14 columns
* **Visual Scope:** 6 distinct charts spanning bar, horizontal bar, line, and pie configurations.

---

## Chart Matrix & Operational Findings

### 1. Volume and Revenue Portfolio Analysis
* **Chart 1: Total Orders per Product (Vertical Bar Chart)**
  * **Finding:** Printer is the absolute volume leader with 181 orders, while Phone captures the lowest volume at 156 orders. All 7 products sit within a narrow ~25-order variance band, indicating highly balanced consumer demand across the inventory.
* **Chart 6: Total Revenue by Product (Vertical Bar Chart)**
  * **Finding:** Chair stands as the company's top financial earner, pulling in $195,620. Total revenue across all product catalog categories remains balanced within a tight ~$44,000 threshold.

### 2. Financial Channels & Acquisition Quality
* **Chart 2: Total Revenue per Payment Method (Vertical Bar Chart)**
  * **Finding:** Credit Card serves as the primary revenue gateway ($263,847.63), closely followed by Online payments ($262,442.94), while Debit Cards anchor the bottom ($232,361.18). The narrow ~$31,000 spread confirms stable and even payment gateway adoption across the consumer base.
* **Chart 3: Average Order Value by Referral Source (Horizontal Bar Chart)**
  * **Finding:** Facebook traffic brings in the highest-spending demographics, securing a top-tier Average Order Value (AOV) of $1,098.29. Traditional Referrals yield the lowest AOV ($1,021.69). A minimal ~$77 variation across all acquisition vectors points to consistent customer quality.

### 3. Temporal Trends & System Leakage
* **Chart 4: Monthly Sales Revenue Over Time (Line Chart)**
  * **Finding:** The chronological timeline isolates June 2024 as the absolute historic revenue peak at $68,068. While 2023 established itself as the strongest individual sales year, a visible macro-level decline post-2023 indicates a performance trend that requires deep strategic evaluation.
* **Chart 5: Order Status Breakdown (Pie Chart)**
  * **Finding:** A critical operational vulnerability is brought to light: 41.4% of all logged orders result in either a cancellation or a return. Completed orders account for a minor 19.25% share of total volume, proving a severe transaction attrition rate.

---

## Key Business Insights Summary
* **Balanced Product Contribution:** Inventory distribution is healthy; demand and revenue are evenly spread across the entire product catalog, led by Printers in raw order volume and Chairs in gross revenue.
* **Stable Payment & Traffic Quality:** Checkout and marketing channels demonstrate predictable metrics, though Credit Cards provide the highest absolute financial volume and Facebook ads pull in the highest average cart values.
* **Urgent Operational & Macro Hurdles:** Management must urgently prioritize investigating the 41.4% order cancellation/return rate and address the persistent post-2023 downward trajectory highlighted by the chronological trend analysis.

---


