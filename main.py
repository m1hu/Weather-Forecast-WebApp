import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the Next Days")

place = st.text_input("Place: ")

days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forcasted days")

option = st.selectbox("Select data to view", ["Temperature", "Sky"])

st.subheader(f"{option} for the next {days} days in {place}")

def get_data(days):
    dates = ["2022-10-01", "2022-10-02", "2022-10-03", "2022-10-04"]
    temps = [10, 9, 12, 19]
    temps = [days*i for i in temps]
    return dates, temps
figure = px.line(x=get_data(days)[0], y=get_data(days)[1], labels={"x": "Date", "y": "Temperature(C)"})
st.plotly_chart(figure)