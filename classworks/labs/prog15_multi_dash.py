# Multi-Tab Interactive Sales Analytics Dashboard

import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Sales Analytics Dashboard", layout="wide")


@st.cache_data
def load_data():
    np.random.seed(21)
    dates = pd.date_range("2024-01-01", periods=365, freq="D")
    regions = ["North", "South", "East", "West"]
    products = ["Laptop", "Mobile", "Tablet", "Accessories"]
    rows = []

    for d in dates:
        for _ in range(np.random.randint(2, 5)):
            region = np.random.choice(regions)
            product = np.random.choice(products)
            units = np.random.randint(1, 20)
            unit_price = {
                "Laptop": 55000,
                "Mobile": 18000,
                "Tablet": 25000,
                "Accessories": 1500,
            }[product]
            rows.append(
                {
                    "Date": d,
                    "Region": region,
                    "Product": product,
                    "Units": units,
                    "Revenue": units * unit_price * np.random.uniform(0.9, 1.1),
                }
            )

    return pd.DataFrame(rows)


df = load_data()

st.sidebar.header("Dashboard Filters")
date_range = st.sidebar.date_input("Data Range", [df["Date"].min(), df["Date"].max()])
region_sel = st.sidebar.multiselect(
    "Region",
    df["Region"].unique(),
    default=list(df["Region"].unique()),
)
product_sel = st.sidebar.multiselect(
    "Product",
    df["Product"].unique(),
    default=list(df["Product"].unique()),
)

mask = (
    (df["Date"] >= pd.to_datetime(date_range[0]))
    & (df["Date"] <= pd.to_datetime(date_range[1]))
    & (df["Region"].isin(region_sel))
    & (df["Product"].isin(product_sel))
)

fdf = df[mask]

st.sidebar.download_button(
    "Download Filtered Data (CSV)",
    fdf.to_csv(index=False).encode("utf-8"),
    file_name="filtered_sales.csv",
    mime="text/csv",
)

st.title("Sales Analytics Dashboard")
st.caption("Capstone dashboard integrating statistical, time-series and geo visualizations")

k1, k2, k3, k4 = st.columns(4)
k1.metric("Total Revenue", f"Rs. {fdf['Revenue'].sum()/1e5:,.1f} L")
k2.metric("Total Units sold", f"{fdf['Units'].sum():,}")
k3.metric("Avg. Order value", f"Rs. {fdf['Revenue'].sum()/max(len(fdf), 1):,.0f}")
k4.metric("Active Regions", fdf["Region"].nunique())

tab1, tab2, tab3, tab4 = st.tabs(
    ["Overview", "Time Trend", "Product & Region Analysis", "Correlation & Raw Data"]
)

with tab1:
    c1, c2 = st.columns(2)

    with c1:
        rev_by_region = fdf.groupby("Region", as_index=False)["Revenue"].sum()
        fig = px.pie(
            rev_by_region,
            names="Region",
            values="Revenue",
            title="Revenue Share by Region",
            hole=0.4,
        )
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        rev_by_product = fdf.groupby("Product", as_index=False)["Revenue"].sum()
        fig = px.pie(
            rev_by_product,
            names="Product",
            values="Revenue",
            title="Revenue by Product",
            hole=0.4,
        )
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    trend_df = fdf.groupby("Date", as_index=False)["Revenue"].sum()
    fig2 = px.line(trend_df, x="Date", y="Revenue", title="Revenue Trend Over Time")
    st.plotly_chart(fig2, use_container_width=True)

with tab3:
    pivot = fdf.pivot_table(index="Region", columns="Product", values="Revenue", aggfunc="sum")
    st.write("Revenue Pivot Table (Region x Product)")
    st.dataframe(pivot.style.background_gradient(cmap="Blues"), use_container_width=True)

    fig3 = px.box(
        fdf,
        x="Product",
        y="Revenue",
        color="Product",
        title="Revenue Distribution by Product (with outliers)",
    )
    st.plotly_chart(fig3, use_container_width=True)

with tab4:
    numeric_df = fdf[["Units", "Revenue"]].copy()
    numeric_df["DayOfWeek"] = fdf["Date"].dt.dayofweek
    corr_fig, ax = plt.subplots(figsize=(5, 4))
    sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(corr_fig)

    st.write("Filtered Raw Data")
    st.dataframe(fdf, use_container_width=True)

st.sidebar.markdown("---")
st.sidebar.info("Tip: Change filters above and watch every tab, KPI and chart update together.")