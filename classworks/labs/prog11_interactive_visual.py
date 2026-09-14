#Author: Suraj Bhan Kumar
#Date 14/09/2026
 
import numpy as np
import pandas as pd
import plotly.express as px
 
np.random.seed(9)
n = 200
df = pd.DataFrame({
    "StudyHours": np.random.uniform(1, 10, n),
    "Marks": np.random.uniform(30, 100, n),
    "Attendance": np.random.uniform(50, 100, n),
    "Gender": np.random.choice(["Male", "Female"], n),
    "Section": np.random.choice(["A", "B", "C"], n),
})
 
# ---- Interactive scatter plot with tooltips ----
fig1 = px.scatter(
    df, x="StudyHours", y="Marks", color="Gender", size="Attendance",
    hover_data=["Section"],
    title="Study Hours vs Marks (interactive, hover for details)"
)
fig1.write_html("program11_scatter.html")
fig1.show()
 
# ---- Interactive line chart: simulated monthly sales trend ----
months = pd.date_range("2025-01-01", periods=12, freq="ME").strftime("%b")
sales = pd.DataFrame({
    "Month": list(months) * 2,
    "Sales": np.concatenate([np.random.randint(80, 150, 12), np.random.randint(90, 170, 12)]),
    "Region": ["North"] * 12 + ["South"] * 12,
})
fig2 = px.line(sales, x="Month", y="Sales", color="Region", markers=True,
               title="Monthly Sales Trend by Region (interactive)")
fig2.write_html("program11_line.html")
fig2.show()
 
# ---- Faceted bar chart: average marks per section, split by gender ----
fig3 = px.bar(df.groupby(["Section","Gender"], as_index=False)["Marks"].mean(),
              x="Section", y="Marks", color="Gender", facet_col="Gender",
              title="Average Marks by Section, Faceted by Gender")
fig3.write_html("program11_facet_bar.html")
fig3.show()
