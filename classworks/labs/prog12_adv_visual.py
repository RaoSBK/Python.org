#Author: Suraj Bhan Kumar
#Date: 14/09/2026
 
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
 
# ---- Part A: Dropdown menu to switch between metrics ----
months = pd.date_range("2025-01-01", periods=12, freq="ME").strftime("%b")
np.random.seed(4)
sales   = np.random.randint(100, 200, 12)
expense = np.random.randint(70, 150, 12)
profit  = sales - expense
 
fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=months, y=sales,   mode="lines+markers", name="Sales"))
fig1.add_trace(go.Scatter(x=months, y=expense, mode="lines+markers", name="Expense", visible=False))
fig1.add_trace(go.Scatter(x=months, y=profit,  mode="lines+markers", name="Profit",  visible=False))
 
fig1.update_layout(
    title="Monthly Metric Explorer (use dropdown to switch)",
    updatemenus=[dict(
        buttons=[
            dict(label="Sales",   method="update", args=[{"visible": [True, False, False]}]),
            dict(label="Expense", method="update", args=[{"visible": [False, True, False]}]),
            dict(label="Profit",  method="update", args=[{"visible": [False, False, True]}]),
        ],
        direction="down", x=1.0, y=1.15, showactive=True
    )]
)
fig1.write_html("program12_dropdown.html")
fig1.show()
 
# ---- Part B: Animated bubble chart across "years" ----
np.random.seed(6)
years = [2019, 2020, 2021, 2022, 2023]
countries = ["Nation A", "Nation B", "Nation C", "Nation D", "Nation E"]
rows = []
for yr_idx, yr in enumerate(years):
    for c in countries:
        rows.append({
            "Year": yr, "Country": c,
            "GDP_per_capita": np.random.uniform(2000, 20000) + yr_idx * 800,
            "LifeExpectancy": np.random.uniform(55, 82) + yr_idx * 0.5,
            "Population": np.random.uniform(1e6, 5e7),
        })
gap_df = pd.DataFrame(rows)
 
fig2 = px.scatter(
    gap_df, x="GDP_per_capita", y="LifeExpectancy", size="Population",
    color="Country", animation_frame="Year", size_max=60,
    range_x=[0, 25000], range_y=[50, 90],
    title="Animated GDP vs Life Expectancy Over Time (drag slider / press Play)"
)
fig2.write_html("program12_animation.html")
fig2.show()
