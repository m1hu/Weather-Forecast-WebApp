import os
import requests

API_KEY = os.environ.get("WEATHER")


def get_data(place, days, option):
    url = (f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}")
    response = requests.get(url)
    data = response.json()

    dates = []
    temps = []
    sky = []

    for i in range(0, days*8):
        dates.append(data["list"][i]["dt_txt"])
        temps.append(round(data["list"][i]["main"]["temp"] / 10, 2))
        sky.append(data["list"][i]["weather"][0]["main"])

    return temps, sky, dates

if __name__ == "__main__":
    get_data("tarnow", 5, "er")