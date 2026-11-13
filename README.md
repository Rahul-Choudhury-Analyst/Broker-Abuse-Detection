# Broker Abuse Detection

## Overview
SQL-based fraud detection logic for identifying broker abuse patterns in a trading platform.

## Files
- `fraud_logic.sql`: Core detection query

## Sample Query
```sql
-- Add a sample query from your fraud_logic.sql here
```
# Broker Abuse Detection

![SQL](https://img.shields.io/badge/SQL-Data%20Analysis-blue)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow)
![Python](https://img.shields.io/badge/Python-Data%20Generation-green)

## Business Problem
Retail trading platforms and brokerages face severe financial and regulatory risk when Introducing Brokers (IBs) or clients exploit trading infrastructure. This project engineers a detection engine to automatically identify toxic flow, bonus arbitrage, and suspicious transaction patterns using advanced SQL queries and data visualization.

## Data Architecture
- **Data source:** Synthetic MT5 (MetaTrader 5) transaction logs and client CRM records.
- **Main tables:** `clients_mt5`, `trade_history` (focusing on XAU/USD and BTC/USDT), `funding_transactions` (deposits/withdrawals), and `ip_access_logs`.
- **Data generation:** Engineered a custom Python script utilizing `pandas` and `Faker` to simulate 50,000+ realistic retail trading records, mimicking standard market execution times, latency, and spread deviations to create a robust testing environment.

## Fraud Scenarios Flagged
- **Broker (IB) Abuse (Churning):** Flagged IB networks generating toxic flow by identifying accounts with hyper-active rapid open/close durations (scalping under 2 minutes) designed solely to harvest rebate commissions.
- **Bonus Arbitrage Abuse:** Identified risk-free hedging patterns where clients open opposing positions (buy/sell) across linked IP addresses to systematically convert non-withdrawable credit bonuses into withdrawable equity.
- **Money Laundering (AML/KYC Risk):** Flagged structuring (smurfing) patterns involving rapid, repeated deposits just below standard KYC reporting thresholds, followed by immediate withdrawals with zero or minimal trade volume.

## Visualizations
![Dashboard Overview](screenshots/dashboard.png)
*(Includes automated tracking for Risk Exposure by IB, Daily Toxic Flow Volume, and Flagged Account Clusters.)*

## Business Impact
Automated SQL anomaly flagging reduces manual compliance review time by an estimated 20-25 hours per week, proactively identifying rebate exploitation and preventing credit bonus drain before withdrawal processing.
