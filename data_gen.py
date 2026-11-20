import pandas as pd
import numpy as np
import sweetviz as sv
import random
from datetime import datetime, timedelta

# 1. Generate Fake MT5 Data
print("Generating synthetic MT5 trade data...")
np.random.seed(42)
num_trades = 2000

# Create 50 fake client IDs
client_ids = [f"CID{str(i).zfill(4)}" for i in range(1, 51)]
symbols = ['XAU/USD', 'EUR/USD', 'GBP/JPY', 'BTC/USD']

data = {
    'Ticket': range(100001, 100001 + num_trades),
    'Login': [random.choice(client_ids) for _ in range(num_trades)],
    'Symbol': [random.choice(symbols) for _ in range(num_trades)],
    'Volume': np.round(np.random.uniform(0.1, 5.0, num_trades), 2),
    'Type': [random.choice(['Buy', 'Sell']) for _ in range(num_trades)],
    'Open_Time': [datetime(2026, 11, 1) + timedelta(minutes=random.randint(1, 20000)) for _ in range(num_trades)],
    'Profit_Loss': np.round(np.random.normal(0, 150, num_trades), 2),
    'Bonus_Utilized': [random.choice(['Yes', 'No']) for _ in range(num_trades)]
}

df = pd.DataFrame(data)

# Calculate Close Time (Adding random duration from 1 min to 5 hours)
df['Close_Time'] = df['Open_Time'] + pd.to_timedelta(np.random.randint(1, 300, num_trades), unit='m')
df['Duration_Minutes'] = np.round((df['Close_Time'] - df['Open_Time']).dt.total_seconds() / 60, 2)

# 🚨 INJECT FRAUD: "IB Churning" Pattern
# Make 15% of the trades close in under 2 minutes with near-zero PnL just to generate commission
fraud_indices = df.sample(frac=0.15).index

# FIXED: Using integer SECONDS instead of float minutes to avoid Pandas time format clashes
fraud_seconds = np.random.randint(30, 120, len(fraud_indices)) 
df.loc[fraud_indices, 'Duration_Minutes'] = np.round(fraud_seconds / 60, 2)
df.loc[fraud_indices, 'Close_Time'] = df.loc[fraud_indices, 'Open_Time'] + pd.to_timedelta(fraud_seconds, unit='s')

df.loc[fraud_indices, 'Profit_Loss'] = np.round(np.random.uniform(-5, 5, len(fraud_indices)), 2) 

# Save to CSV for our SQL Engine later
df.to_csv("mt5_mock_data.csv", index=False)
print("Data saved successfully to mt5_mock_data.csv!")

# 2. Generate Sweetviz Data X-Ray Report
print("Running Sweetviz Data X-Ray...")
report = sv.analyze(df)
report.show_html("Broker_Abuse_Report.html")
print("Report generated! Check your browser.")