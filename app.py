import pandas as pd
import streamlit as st
from pathlib import Path
import random
import numpy as np

st.set_page_config(page_title="Smart School IT Helpdesk Analyzer", layout="wide")

project_root = Path(__file__).resolve().parent
data_path = project_root / "data" / "raw" / "helpdesk_tickets.csv"
data_path.parent.mkdir(parents=True, exist_ok=True)


def generate_dataset(n_rows=250, seed=42):
    random.seed(seed)
    np.random.seed(seed)

    departments = ["Computer Lab", "Admin Office", "Library", "Science Lab"]
    device_types = ["Desktop", "Laptop", "Printer", "Smartboard"]
    issue_types = [
        "WiFi",
        "Hardware Failure",
        "Login Issue",
        "Software Error",
        "Printer Jam",
        "Email Access",
        "Projector/Display",
        "Slow Computer",
        "Account Locked",
        "Virus/Malware",
    ]

    base_time_map = {
        "WiFi": 25,
        "Hardware Failure": 90,
        "Login Issue": 15,
        "Software Error": 45,
        "Printer Jam": 20,
        "Email Access": 20,
        "Projector/Display": 50,
        "Slow Computer": 60,
        "Account Locked": 10,
        "Virus/Malware": 120,
    }

    rows = []
    for i in range(1, n_rows + 1):
        issue = random.choice(issue_types)

        resolution_time = max(5, int(base_time_map[issue] + np.random.normal(0, 10)))

        if issue in ["Virus/Malware", "Hardware Failure"]:
            priority = random.choices(["High", "Medium", "Low"], weights=[0.7, 0.25, 0.05])[0]
        elif issue in ["WiFi", "Software Error", "Slow Computer"]:
            priority = random.choices(["High", "Medium", "Low"], weights=[0.3, 0.55, 0.15])[0]
        else:
            priority = random.choices(["High", "Medium", "Low"], weights=[0.1, 0.45, 0.45])[0]

        rows.append(
            {
                "Ticket_ID": f"TKT-{i:04d}",
                "Department": random.choice(departments),
                "Device_Type": random.choice(device_types),
                "Issue_Type": issue,
                "Resolution_Time": resolution_time,
                "Priority": priority,
            }
        )

    return pd.DataFrame(rows)


# Ensure dataset exists for Streamlit Cloud
if not data_path.exists():
    df_gen = generate_dataset(n_rows=250, seed=42)
    df_gen.to_csv(data_path, index=False)

df = pd.read_csv(data_path)

st.title("🎓 Smart School IT Helpdesk Analyzer")
st.caption("Interactive dashboard for simulated school ICT support tickets")

# Sidebar filters
st.sidebar.header("Filter Tickets")

departments = st.sidebar.multiselect(
    "Department",
    options=sorted(df["Department"].unique()),
    default=sorted(df["Department"].unique())
)

devices = st.sidebar.multiselect(
    "Device Type",
    options=sorted(df["Device_Type"].unique()),
    default=sorted(df["Device_Type"].unique())
)

issues = st.sidebar.multiselect(
    "Issue Type",
    options=sorted(df["Issue_Type"].unique()),
    default=sorted(df["Issue_Type"].unique())
)

filtered_df = df[
    (df["Department"].isin(departments)) &
    (df["Device_Type"].isin(devices)) &
    (df["Issue_Type"].isin(issues))
]

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
st.dataframe(filtered_df.head(20), width="stretch")