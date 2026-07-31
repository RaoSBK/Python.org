#Date: 31-07-2026
#Author: Suraj Bhan Kumar

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#create sample time series data

np.random.seed(42)
dates = pd.date_range(start="2024-01-02", end = "2024-12-31", freq="D")

prices = np.random.normal(100, 5, len(dates)).cumsum()/10+100


df = pd.DataFrame({
    "Close": prices
}, index=dates)


#calcculate moving averages


df["MA_7"] = df["Close"].rolling(window=7).mean()

df["MA_30"] = df["Close"].rolling(window=30).mean()


#Monthly Average Closing Price
monthly_avg = df["Close"].resample("ME").mean()

#create figure

fig, axes = plt.subplots(2, 1, figsize=(12,8))

#Top plot

axes[0].plot(
    df.index,
    df["Close"],
    color="lightgray",
    label="Daily Price"
)


axes[0].plot(
    df.index,
    df["MA_7"],
    color="blue",
    linewidth=2,
    label="7-Day Moving Average"
)


axes[0].set_title("Daily closing price with moving averages")
axes[0].set_xlabel("Date")
axes[0].set_ylabel("Price")
axes[0].legend()
axes[0].grid(True)


#Bottom plot

axes[1].bar(
    monthly_avg.index.strftime("%b"),
    monthly_avg.values,
    color='skyblue'
)


axes[1].set_title("Monthly Average Closing Price")
axes[1].set_xlabel("Month")
axes[1].set_ylabel("Average Price")
axes[1].grid(axis="y")

plt.tight_layout()
plt.show()