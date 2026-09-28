# 🌤️ Weather App — Real-Time Weather Information

> A lightweight Python application that retrieves and displays real-time weather information for any city using the OpenWeatherMap API.

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![API](https://img.shields.io/badge/API-OpenWeatherMap-orange?style=for-the-badge)](https://openweathermap.org/api)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](#-license)

---

## 📌 Overview

**Weather App** is a Python-based real-time weather application that demonstrates practical **REST API integration, HTTP request handling, JSON data processing, environment-based configuration, exception handling, and object-oriented programming**.

Users can enter the name of a city and retrieve its current weather information through the OpenWeatherMap API.

### 🌍 The application provides:

- 🌡️ Current temperature
- 🌡️ Feels-like temperature
- ☁️ Weather conditions
- 💧 Humidity
- 🌬️ Wind speed
- ⏱️ Atmospheric pressure
- 🌅 Sunrise time
- 🌇 Sunset time
- 🌎 City and country information

---

## ✨ Features

### 🌍 City-Based Weather Search
Search for the current weather of any supported city.

### 🌡️ Real-Time Weather Data
Fetches live weather information directly from the OpenWeatherMap API.

### ☁️ Weather Conditions
Displays a readable description of the current weather condition.

### 💧 Humidity & Pressure
Shows humidity percentage and atmospheric pressure.

### 🌬️ Wind Information
Displays the current wind speed.

### 🌅 Sunrise & Sunset
Converts Unix timestamps returned by the API into readable time values.

### 🔐 Secure API-Key Handling
The API key is loaded from an environment variable instead of being hard-coded.

### ⚠️ Error Handling
Handles common problems such as:

- Invalid city
- Invalid API key
- Network errors
- Request timeout
- HTTP errors
- Empty input

### 🔄 Continuous Search
Users can search for multiple cities without restarting the application.

### 🚪 Clean Exit
Type `quit` to terminate the application safely.

---

## 🧠 How It Works

```text
                    ┌──────────────────┐
                    │    Start App     │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Load Environment │
                    │   Configuration  │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Enter City Name  │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Build API Query  │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Send HTTP GET    │
                    │     Request      │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Receive JSON     │
                    │    Response      │
                    └────────┬─────────┘
                             │
                    ┌────────┴─────────┐
                    │                  │
                    ▼                  ▼
              ┌───────────┐     ┌───────────────┐
              │   Error   │     │    Success    │
              └─────┬─────┘     └───────┬───────┘
                    │                   │
                    ▼                   ▼
              Display Error       Extract Data
                                        │
                                        ▼
                                Display Weather
                                        │
                                        ▼
                                  Search Again


