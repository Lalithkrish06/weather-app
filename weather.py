"""
Weather App - Fetches current weather data from OpenWeatherMap API
Author: [Your Name]
"""

import os
import sys
import requests
from datetime import datetime
from typing import Dict, Optional
from dotenv import load_dotenv


# Load environment variables
load_dotenv()


class WeatherApp:
    """A simple weather application using OpenWeatherMap API."""
    
    BASE_URL = "https://api.openweather.org/data/2.5/weather"
    
    def __init__(self):
        """Initialize with API key from environment."""
        self.api_key = os.getenv("OPENWEATHER_API_KEY")
        if not self.api_key:
            raise ValueError("API key not found. Set OPENWEATHER_API_KEY in .env file.")
    
    def get_weather(self, city: str) -> Optional[Dict]:
        """
        Fetch weather data for a given city.
        
        Args:
            city: Name of the city
            
        Returns:
            Dictionary containing weather data or None if error occurs
        """
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"  # Use Celsius
        }
        
        try:
            response = requests.get(self.BASE_URL, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.HTTPError as http_err:
            if response.status_code == 404:
                print(f"❌ City '{city}' not found. Please check the spelling.")
            elif response.status_code == 401:
                print("❌ Invalid API key. Please check your credentials.")
            else:
                print(f"❌ HTTP error occurred: {http_err}")
            return None
            
        except requests.exceptions.ConnectionError:
            print("❌ Connection error. Please check your internet connection.")
            return None
            
        except requests.exceptions.Timeout:
            print("❌ Request timed out. Please try again.")
            return None
            
        except requests.exceptions.RequestException as err:
            print(f"❌ An error occurred: {err}")
            return None
    
    def display_weather(self, data: Dict) -> None:
        """
        Display formatted weather information.
        
        Args:
            data: Weather data dictionary from API
        """
        city = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        weather_desc = data["weather"][0]["description"].title()
        wind_speed = data["wind"]["speed"]
        sunrise = datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%H:%M")
        sunset = datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%H:%M")
        
        print("\n" + "=" * 50)
        print(f"🌍 Weather in {city}, {country}")
        print("=" * 50)
        print(f"🌡️  Temperature: {temp}°C (Feels like: {feels_like}°C)")
        print(f"☁️  Conditions:  {weather_desc}")
        print(f"💧 Humidity:    {humidity}%")
        print(f"🌬️  Wind Speed:  {wind_speed} m/s")
        print(f"⏱️  Pressure:    {pressure} hPa")
        print(f"🌅 Sunrise:     {sunrise}")
        print(f"🌇 Sunset:      {sunset}")
        print("=" * 50 + "\n")
    
    def run(self) -> None:
        """Main loop for the application."""
        print("🌤️  Welcome to the Weather App!\n")
        
        while True:
            city = input("Enter city name (or 'quit' to exit): ").strip()
            
            if city.lower() == 'quit':
                print("👋 Goodbye!")
                break
            
            if not city:
                print("⚠️  Please enter a valid city name.\n")
                continue
            
            # Fetch and display weather
            weather_data = self.get_weather(city)
            if weather_data:
                self.display_weather(weather_data)


def main():
    """Entry point for the application."""
    try:
        app = WeatherApp()
        app.run()
    except ValueError as e:
        print(f"Configuration Error: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n👋 Application closed by user.")
        sys.exit(0)


if __name__ == "__main__":
    main()
