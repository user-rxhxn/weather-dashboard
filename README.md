Weather Dashboard

A weather dashboard built with Python and Streamlit that retrieves current weather information using the OpenWeatherMap API.

Features

- Search for weather by city name
- View temperature in Celsius
- Check humidity and wind speed
- View the feels-like temperature
- Display weather conditions and icons
- Handle invalid city names and connection errors

Technologies Used

- Python
- Streamlit
- Requests
- OpenWeatherMap API

Installation and Setup

1. Clone this repository.
2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.streamlit` folder in the project directory.
4. Inside it, create a `secrets.toml` file with your API key:

   ```toml
   OPENWEATHER_API_KEY = "your_api_key_here"
   ```

5. Start the application:

   ```bash
   streamlit run weatherDashboard.py
   ```

   Replace `weatherDashboard.py` with your actual Python filename if necessary.

Security

The API key is stored locally using Streamlit secrets.

Purpose

This project was built to practise Python, API integration, and building interactive web applications with Streamlit.
