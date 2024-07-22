import streamlit as st
import plotly.express as px

import backend
from backend import get_data

st.title("Weather Forecast for the Next Days")

place = st.text_input("Place: ")

days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forcasted days")

option = st.selectbox("Select data to view", ["Temperature", "Sky"])

try:
    if place and option == "Sky":
        t, s, d = get_data(place, days, option)

        num_of_indices = [0, (24 - int(d[0][11:13])) / 3]
        u = int(days * 24 / 3) - num_of_indices[1]

        while u > 8:
            num_of_indices.append(8 % u)
            u = u - (8 % u)
        num_of_indices.append(u)

        st.subheader(f"{option} for the next {days} days in {place}")

        for i in range(0, len(num_of_indices) - 1):
            imgs= []

            a = int(sum(num_of_indices[0:i+1]))
            b = int(sum(num_of_indices[0:i+2]))

            print([a, b])
            print(num_of_indices)
            c = 0

            for j in range(a, b):

                imgs.append(f"imgs/{s[int(j)].lower()}.png")
                c = j

            st.text(d[c][0:10])
            captions = [date[11:] for date in d[a:b]]
            st.image(imgs, width=70, caption=captions)

    elif place and option == "Temperature":

        t, s, d = get_data(place, days, option)
        figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature(C)"})

        st.subheader(f"{option} for the next {days} days in {place}")
        st.plotly_chart(figure)

except TypeError:
    st.subheader(f"City {place} not found")
    pass
except KeyError:
    st.subheader(f"City {place} not found")
    pass
