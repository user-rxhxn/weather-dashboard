
import streamlit as st
import requests

API_key = st.secrets["OPENWEATHER_API_KEY"]

st.set_page_config(
    page_title="Weather Dashboard",
    layout="wide"
)

st.title("Weather Dashboard")

city = st.text_input(
    "Enter a city name:",
    placeholder="e.g. Johannesburg"
)


def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_key,
        "units": "metric"
    }

    try:
        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        data = response.json()

        if response.status_code == 200:
            return data, None
        else:
            return None, data.get(
                "message",
                "Unable to retrieve weather data."
            )

    except requests.RequestException:
        return None, "Could not connect to the weather service. Please try again."


if st.button("Search Weather"):
    if city.strip():
        data, error = get_weather(city.strip())

        if error:
            st.error(f"Error: {error}")

        else:
            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric(
                    "Temperature",
                    f"{data['main']['temp']} °C"
                )

            with col2:
                st.metric(
                    "Humidity",
                    f"{data['main']['humidity']}%"
                )

            with col3:
                st.metric(
                    "Wind Speed",
                    f"{data['wind']['speed']} m/s"
                )

            with col4:
                st.metric(
                    "Feels Like",
                    f"{data['main']['feels_like']} °C"
                )

            st.subheader("Weather Details")

            description = data["weather"][0]["description"]
            icon = data["weather"][0]["icon"]

            icon_url = (
                "https://openweathermap.org/img/wn/"
                f"{icon}@2x.png"
            )

            st.image(icon_url, width=100)

            st.write(f"**Condition:** {description.title()}")
            st.write(f"**City:** {data['name']}")
            st.write(f"**Country:** {data['sys']['country']}")

    else:
        st.warning("Please enter a city.")
