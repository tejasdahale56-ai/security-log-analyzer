import pandas as pd
import streamlit as st

st.set_page_config(page_title="Security Log Analyzer")

st.title("Security Log Analyzer")
st.write("A local educational tool for analyzing fake login activity.")

uploaded_file = st.file_uploader(
    "Upload a sample CSV login log",
    type="csv"
)

if uploaded_file is not None:
    logs = pd.read_csv(uploaded_file)
    st.success("Uploaded log file loaded.")
else:
    logs = pd.read_csv("sample_login_logs.csv")
    st.info("Showing the built-in sample log file.")

total_events = len(logs)
failed_logins = (logs["event_type"] == "FAILED_LOGIN").sum()
successful_logins = (logs["event_type"] == "SUCCESS_LOGIN").sum()

st.subheader("Dashboard")

column_1, column_2, column_3 = st.columns(3)

column_1.metric("Total events", total_events)
column_2.metric("Failed logins", failed_logins)
column_3.metric("Successful logins", successful_logins)
st.subheader("Raw login events")

st.dataframe(logs, use_container_width=True)

st.caption(
    "Use only sample logs that you created or are authorized to analyze."
)