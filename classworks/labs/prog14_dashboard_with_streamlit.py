#Building Your First Interactive Web Dashboard with Streamlit


import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px


st.set_page_config(page_title="Student Performance Dashboard", layout = "wide")

#Generate sample data

@st.cache_data
def load_data():
    np.random.seed(0)
    n = 300
    return pd.DataFrame({
        "Section": np.random.choice(['A', 'B', 'C', 'D'], n),
        "Gender" : np.random.choice(["Male", "Female"], n),
        "StudyHour": np.random.uniform(1, 10, n).round(1),
        "Marks": np.random.uniform(30, 100, n).round(1),
    })


df = load_data()

st.title("Student Performance Dashboard")
st.caption("A basic interactive dashboard built with Streamlit")

st.sidebar.header("Filters")
sections = st.sidebar.multiselect("Select Section(s)",
                                  options=sorted(df["Section"].unique()),
                                  default=sorted(df["Section"].unique()))

gender = st.sidebar.selectbox("Gender", options=["All", "Male", "Female"])
min_marks = st.sidebar.slider("Minimum Marks", 0, 100, 0)

filtered = df[df["Section"].isin(sections) & (df["Marks"] >= min_marks)]
if gender !=  "All":
    filtered = filtered[filtered["Gender"] == gender]


col1, col2, col3 = st.columns(3)
col1.metric("Student (filtered)", len(filtered))
col2.metric("Average Marks", f"{filtered['Marks'].mean():.1f}" if len(filtered) else "N/A")
col3.metric("Average Study Hours", f"{filtered['StudyHour'].mean():.1f}" if len(filtered) else "N/A")


fig  = px.scatter(filtered, x = "StudyHour", y = "Marks", color="Section",
                  hover_data=["Gender"], title="Study Hours vs Marks(filtered)")

st.plotly_chart(fig, width="stretch")

st.subheader("Filtered Data")
st.dataframe(filtered, width="stretch")