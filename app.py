import pandas as pd
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Smart School IT Helpdesk Analyzer", layout="wide")

project_root = Path(__file__).resolve().parent
data_path = project_root / "data" / "raw" / "helpdesk_tickets.csv"

st.title("🎓 Smart School IT Helpdesk Analyzer")
st.caption("Interactive dashboard for simulated school ICT support tickets")

df = pd.read_csv(data_path)

# Sidebar filters
st.sidebar.header("Filter Tickets")

departments = st.sidebar.multiselect(
    "Department",
    options=df["Department"].unique(),
    default=df["Department"].unique()
)

devices = st.sidebar.multiselect(
    "Device Type",
    options=df["Device_Type"].unique(),
    default=df["Device_Type"].unique()
)

issues = st.sidebar.multiselect(
    "Issue Type",
    options=df["Issue_Type"].unique(),
    default=df["Issue_Type"].unique()
)

filtered_df = df[
    (df["Department"].isin(departments)) &
    (df["Device_Type"].isin(devices)) &
    (df["Issue_Type"].isin(issues))
]

# Metrics
col1, col2, col3 = st.columns(3)

col1.metric("Total Tickets", len(filtered_df))
col2.metric("Avg Resolution Time (min)", round(filtered_df["Resolution_Time"].mean(), 1))
col3.metric("High Priority %", round((filtered_df["Priority"] == "High").mean() * 100, 1))

st.subheader("Most Common Issues")
st.bar_chart(filtered_df["Issue_Type"].value_counts())

st.subheader("Tickets by Department")
st.bar_chart(filtered_df["Department"].value_counts())

st.subheader("Resolution Time Distribution")
st.line_chart(filtered_df["Resolution_Time"].value_counts().sort_index())

st.subheader("Sample Tickets")
st.dataframe(filtered_df.head(20), use_container_width=True)
