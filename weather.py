# Simple program in virtual environments used to pull the weather from a given city and returns the current weather for any location. We will use OpenWeather.org to do this.
# .env stores the API Key and these are NEVER included in any distributions of what you publish when building these. You can add these to the .gitignore

# This version of the file is used for posting to a website.

import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()


def get_current_weather(city="New York"):

    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={
        os.getenv("API_KEY")}&q={city}&units=imperial'

    weather_data = requests.get(request_url).json()

    return weather_data


if __name__ == "__main__":
    print('\n\n===== GET CURRENT WEATHER CONDITIONS =====\n\n')
    city = input('\nPlease enter a city name:\n')

    # Check for empty string or space only
    if not bool(city.strip()):
        city = "Cleveland"

    weather_data = get_current_weather(city)

    print("\n")
    pprint(weather_data)
