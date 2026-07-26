# Date: 24-07-2026
# Author: Suraj Bhan Kumar


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# ----------------------------
# Sample Data
# ----------------------------
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

sales = np.array([120, 180, 250, 220, 300, 280])
expenses = np.array([90, 130, 170, 160, 200, 190])

profit = sales - expenses

regions = ["North", "South", "East", "West"]
region_sales = [300, 250, 200, 150]

cumulative_sales = np.cumsum(sales)

# ----------------------------
# Create Figure
# ----------------------------
fig = plt.figure(figsize=(14, 8))
gs = GridSpec(2, 3, figure=fig)

# ==================================================
# 1. Sales vs Expense Line Chart
# ==================================================
ax1 = fig.add_subplot(gs[:, 0])

ax1.plot(months, sales, marker='o', linewidth=2, label='Sales')
ax1.plot(months, expenses, marker='s', linewidth=2, label='Expenses')

ax1.set_title("Sales vs Expenses")
ax1.set_xlabel("Months")
ax1.set_ylabel("Amount")
ax1.legend()
ax1.grid(True)

# Annotate highest sales
peak = np.argmax(sales)

ax1.annotate(
    "Peak Sales",
    xy=(months[peak], sales[peak]),
    xytext=(months[peak], sales[peak] + 40),
    arrowprops=dict(arrowstyle="->", color="red"),
    fontsize=10,
    color="red"
)

# ==================================================
# 2. Pie Chart
# ==================================================
ax2 = fig.add_subplot(gs[0, 1])

ax2.pie(
    region_sales,
    labels=regions,
    autopct="%1.1f%%",
    startangle=90
)

ax2.set_title("Region-wise Sales")

# ==================================================
# 3. Profit Bar Chart
# ==================================================
ax3 = fig.add_subplot(gs[0, 2])

colors = []

for p in profit:
    if p >= 70:
        colors.append("green")
    else:
        colors.append("orange")

ax3.bar(months, profit, color=colors)

ax3.set_title("Monthly Profit")
ax3.set_xlabel("Months")
ax3.set_ylabel("Profit")

# ==================================================
# 4. Cumulative Sales Area Chart
# ==================================================
ax4 = fig.add_subplot(gs[1, 1:])

ax4.fill_between(months, cumulative_sales,
                 color="skyblue", alpha=0.6)

ax4.plot(months, cumulative_sales,
         color="blue", linewidth=2)

ax4.set_title("Cumulative Sales")
ax4.set_xlabel("Months")
ax4.set_ylabel("Total Sales")
ax4.grid(True)

# ==================================================
# Dashboard Title
# ==================================================
fig.suptitle(
    "Business Sales Dashboard",
    fontsize=18,
    fontweight="bold"
)

plt.tight_layout(rect=[0, 0, 1, 0.95])

plt.show()