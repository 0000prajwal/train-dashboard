import streamlit as st
import pandas as pd

api_response = {
    "train_name": "Express 101",
    "train_number": "12345",
    "route": [
        {"station": "Mumbai", "arrival": "Start", "departure": "06:00"},
        {"station": "Surat", "arrival": "09:00", "departure": "09:10"},
        {"station": "Vadodara", "arrival": "11:00", "departure": "11:05"},
        {"station": "Ahmedabad", "arrival": "13:00", "departure": "End"}
    ]
}

data = []
for stop in api_response["route"]:
    data.append([stop["station"], stop["arrival"], stop["departure"]])

df = pd.DataFrame(data, columns=["Station", "Arrival", "Departure"])

st.markdown(f"## 🚆 {api_response['train_name']} ({api_response['train_number']})")
st.dataframe(df)

station = st.selectbox("Select Station", df["Station"])
row = df[df["Station"] == station].iloc[0]

st.text(f"Arrival: {row['Arrival']}")
st.text(f"Departure: {row['Departure']}")