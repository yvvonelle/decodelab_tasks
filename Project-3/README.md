# Project 3: Extracting Business Intelligence

## Project Overview
This project applies structured SQL querying to a retail orders dataset using SQLite. The objective was to move beyond raw transactional data to extract actionable business insights regarding customer acquisition channels, purchasing behavior, payment dynamics, and operational bottlenecks. 

---

## Database Schema & Core Architecture
The analysis is executed against the `retail` schema using a singular, optimized staging table:

* **Table Name:** `cleaned dataset`
* **Dataset Size:** 1,200 rows × 14 columns
* **Key Attributes:** OrderID, Date, CustomerID, Product, Quantity, UnitPrice, ShippingAddress, PaymentMethod, OrderStatus, TrackingNumber, ItemsInCart, CouponCode, ReferralSource, TotalPrice.

---

## Structured Queries & Operational Findings

### 1. Data Integrity & Filtering
* **Table Verification:** Performed structural schema validations via basic selections (`LIMIT 10`) to verify data types and loading consistency across all 14 fields.
* **Fulfillment Metrics:** Isolated successful transactions (`WHERE OrderStatus = 'Completed'`) to baseline business operations.
  * **Finding:** Only 231 out of 1,200 orders reached a completed status, uncovering a low order completion rate of 19.25%.

### 2. Strategic Aggregations & Demand Analysis
* **High-Value Benchmarking:** Isolated the top 10 transactions sorted by gross value (`ORDER BY TotalPrice DESC`).
  * **Finding:** The peak transaction was `ORD200789` (Tablet) at $3,456.40. Premium electronics (Tablets, Monitors, Laptops) completely dominate the high-value spectrum.
* **Catalog Velocity Profiling:** Grouped order volume across inventory categories (`GROUP BY Product`) to assess demand distribution.
  * **Finding:** Printers represent the catalog volume catalyst with 181 total orders. A narrow variance of ~25 orders between top and bottom categories indicates highly balanced demand.

### 3. Revenue Channels & Marketing Metrics
* **Financial Stream Mapping:** Measured transactional revenue streams across checkout options (`SUM(TotalPrice)`).
  * **Finding:** Credit Card leads revenue generation at $263,847.63, tightly followed by Online channels ($262,442.94). A narrow ~$31,000 spread across all five methods shows relatively uniform user adoption.
* **Acquisition Channel Quality:** Quantified marketing referral performance based on average transaction size (`AVG(TotalPrice)`).
  * **Finding:** Facebook traffic yields the premium tier customer value, driving the highest Average Order Value (AOV) of $1,098.29 per transaction. 

### 4. Advanced Threshold Filtering
* **Performance Tiering:** Implemented conditional aggregate filters (`HAVING`) to isolate products surpassing a high-velocity baseline of 170 orders.
  * **Finding:** 4 out of 7 product lines exceeded the threshold: Printer (181), Tablet (179), Chair (178), and Laptop (173). Desks (170), Monitors (163), and Phones (156) fell beneath the volume baseline.

---

## Key Business Insights Summary
* **Critical Funnel Attrition:** Only 19.25% of orders close successfully, revealing a massive 41.4% structural revenue leak due to combined cancellations and returns.
* **Core Volume Anchors:** Printers, Tablets, Chairs, and Laptops form the high-velocity volume core of the company's product catalog.
* **Balanced Financial Ecosystem:** Credit Cards serve as the main total revenue pillar ($263,847.63), while Facebook stands out as the most valuable user acquisition channel with a top-tier AOV of $1,098.29.

---

## SQL Toolkit Demonstrated
* **Data Selection & Constraints:** `SELECT`, `WHERE`, `LIMIT`
* **Sorting & Organization:** `ORDER BY`, `GROUP BY`, `HAVING`
* **Mathematical Aggregations:** `COUNT()`, `SUM()`, `AVG()`

---

