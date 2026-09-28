# 🌤️ Weather App

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/OpenWeatherMap-API-orange?style=for-the-badge" alt="OpenWeatherMap">
  <img src="https://img.shields.io/badge/Requests-HTTP-green?style=for-the-badge&logo=python&logoColor=white" alt="Requests">
  <img src="https://img.shields.io/badge/python--dotenv-Environment%20Config-3776AB?style=for-the-badge" alt="python-dotenv">
  <img src="https://img.shields.io/badge/CLI-Terminal-black?style=for-the-badge&logo=windowsterminal&logoColor=white" alt="CLI">
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" alt="Status">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License">
</p>

<p align="center">
  <b>🌦️ Real-Time Weather Information Using Python & OpenWeatherMap API</b>
</p>

<p align="center">
  A lightweight API-driven weather application that retrieves and displays real-time weather information for any city.
</p>

---

## 📌 Overview

**Weather App** is a Python-based real-time weather application that integrates with the **OpenWeatherMap REST API** to retrieve current weather information for a user-selected city.

The application accepts a city name, sends an HTTP request to the weather API, processes the returned JSON response, extracts relevant weather information, and displays the results through a clean command-line interface.

### 🎯 Project Objectives

- Build a practical Python-based API application
- Understand REST API integration
- Process JSON responses
- Handle API authentication securely
- Implement exception and network error handling
- Work with environment variables
- Build a clean command-line interface

---

## ✨ Features

- 🌍 Search weather by city name
- 🌡️ Display current temperature
- 🌡️ Display feels-like temperature
- ☁️ Display current weather condition
- 💧 Display humidity
- 🌬️ Display wind speed
- ⏱️ Display atmospheric pressure
- 🌅 Display sunrise time
- 🌇 Display sunset time
- 🔐 Secure API key configuration
- ⚠️ API and network error handling
- ⏳ Request timeout handling
- 🔄 Multiple city searches
- 🚪 Clean application exit
- 🕐 Local timestamp conversion

---

## 🛠️ Technology Stack

| Technology | Purpose |
|------------|---------|
| 🐍 Python | Core application development |
| 🌐 Requests | HTTP API communication |
| 🔐 python-dotenv | Environment variable management |
| ☁️ OpenWeatherMap API | Real-time weather data |
| 📦 JSON | API response processing |
| 🔧 Git | Version control |
| 🐙 GitHub | Source code hosting |
| 💻 VS Code | Development environment |

### Core Technology Flow

```text
Python
│
├── Requests
│   └── HTTP API Communication
│
├── python-dotenv
│   └── Environment Configuration
│
└── OpenWeatherMap API
    └── Real-Time Weather Data
```

---

# 🚀 Installation & Setup

Follow the steps below to install and run the Weather App locally.

## 📋 Prerequisites

Before running the project, make sure you have:

- 🐍 Python 3.x installed
- 📦 pip installed
- 🔑 OpenWeatherMap API key
- 🔧 Git installed
- 💻 VS Code or any Python-supported IDE

Check your Python version:

```bash
python --version
```

Check pip:

```bash
pip --version
```

---

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Lalithkrish06/weather-app.git
```

## 2️⃣ Navigate to the Project Directory

```bash
cd weather-app
```

## 3️⃣ Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate the virtual environment:

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 5️⃣ Configure the API Key

Create a `.env` file in the project root:

```env
OPENWEATHER_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual OpenWeatherMap API key.

> 🔐 Never commit your `.env` file or expose your API key publicly.

## 6️⃣ Run the Application

```bash
python weather.py
```

## 7️⃣ Example Output

```text
==================================================
             🌤️ WEATHER INFORMATION
==================================================

🌍 Location      : Erode, IN

🌡️ Temperature   : 29.4°C
🌡️ Feels Like    : 32.1°C

☁️ Condition     : Clear Sky

💧 Humidity      : 72%
🌬️ Wind Speed    : 3.2 m/s
⏱️ Pressure      : 1008 hPa

🌅 Sunrise       : 06:01
🌇 Sunset        : 18:12

==================================================
```

---

## 🔄 Complete Installation Flow

```text
┌──────────────────────────────┐
│     Clone GitHub Repository  │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│      Navigate to Project     │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│     Create Virtual Env       │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│     Activate Virtual Env     │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│     Install Dependencies     │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│      Create .env File        │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│   Add OpenWeatherMap API Key │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│       Run weather.py         │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│     🌤️ Get Weather Data      │
└──────────────────────────────┘
```

---

## 🔐 Security

Add the following to `.gitignore`:

```gitignore
.env
venv/
__pycache__/
*.pyc
```

This prevents your API key and virtual environment from being uploaded to GitHub.

---

## 🛑 Deactivate Virtual Environment

```bash
deactivate
```

---

## 🔁 Run the Project Again

### Windows

```bash
cd weather-app
venv\Scripts\activate
python weather.py
```

### Linux / macOS

```bash
cd weather-app
source venv/bin/activate
python3 weather.py
```

---

## ⚠️ Troubleshooting

### Python Not Recognized

If you see:

```text
'python' is not recognized as an internal or external command
```

Install Python and enable **Add Python to PATH** during installation.

### pip Not Recognized

Use:

```bash
python -m pip install -r requirements.txt
```

### Module Not Found

If you see:

```text
ModuleNotFoundError: No module named 'requests'
```

Run:

```bash
python -m pip install requests python-dotenv
```

### API Key Error

Check that:

1. `.env` exists in the project root.
2. The variable name is exactly:

```env
OPENWEATHER_API_KEY=your_api_key_here
```

3. Your API key is valid.
4. There are no unnecessary spaces around the API key.

---

## ✅ Installation Complete

Run:

```bash
python weather.py
```

🌤️ Enter a city name and get real-time weather information directly in your terminal.

---
### Example Application Output

```text
==================================================
             🌤️ WEATHER INFORMATION
==================================================

🌍 Location      : Erode, IN

🌡️ Temperature   : 29.4°C
🌡️ Feels Like    : 32.1°C

☁️ Condition     : Clear Sky

💧 Humidity      : 72%
🌬️ Wind Speed    : 3.2 m/s
⏱️ Pressure      : 1008 hPa

🌅 Sunrise       : 06:01
🌇 Sunset        : 18:12

==================================================

```

---
# 🐛 Issues & Suggestions

If you find a bug, encounter an issue, or have a feature suggestion, open an issue in the repository.

🔗 **GitHub Repository:**

https://github.com/Lalithkrish06/weather-app

---

# 📄 License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this project according to the terms of the license.

---

# 👨‍💻 Author

<p align="center">
  <b>Lalith Krish</b>
</p>

<p align="center">
  B.Tech Artificial Intelligence & Data Science
</p>

<p align="center">
  <a href="https://github.com/Lalithkrish06">
    <img src="https://img.shields.io/badge/GitHub-Lalithkrish06-181717?style=for-the-badge&logo=github" alt="GitHub">
  </a>
</p>

---

# ⭐ Support

If you found this project useful, consider giving the repository a ⭐ on GitHub.

<p align="center">
  <b>🌤️ Built with Python • REST APIs • OpenWeatherMap</b>
</p>

<p align="center">
  <i>Turning real-time weather data into simple, useful information.</i>
</p>
