import numpy as np
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 150, 130, 200, 180]
expense = [70, 90, 100, 120, 110]
profit = np.array(sales) - np.array(expense)

fig = plt.figure(figsize=(12, 8))
gs = fig.add_gridspec(2, 2)

ax1 = fig.add_subplot(gs[:, 0])
ax2 = fig.add_subplot(gs[0, 1])
ax3 = fig.add_subplot(gs[1, 1])

ax1.plot(months, sales, marker="o", label="Sales")
ax1.plot(months, expense, marker="o", label="Expense")
peak = np.argmax(sales)
ax1.annotate(
    "Peak Sales",
    xy=(peak, sales[peak]),
    xytext=(peak - 1, sales[peak] + 20),
    arrowprops=dict(arrowstyle="->")
)
ax1.set_title("Sales vs Expense")
ax1.legend()

ax2.pie([40, 35, 25], labels=["North", "South", "East"],
        autopct="%1.1f%%")
ax2.set_title("Regional Sales")

ax3.bar(months, profit,
        color=["green" if p >= 50 else "orange" for p in profit])
ax3.set_title("Monthly Profit")

plt.suptitle("Sales Dashboard")
plt.tight_layout()
plt.show()