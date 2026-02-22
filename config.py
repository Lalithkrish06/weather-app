"""
Configuration settings for the Weather App.
"""

import os
from dataclasses import dataclass


@dataclass
class Config:
    """Application configuration."""
    API_KEY: str = os.getenv("OPENWEATHER_API_KEY", "")
    BASE_URL: str = "https://api.openweathermap.org/data/2.5/weather"
    TIMEOUT: int = 10
    UNITS: str = "metric"  # metric (Celsius), imperial (Fahrenheit), standard (Kelvin)
    
    @classmethod
    def validate(cls) -> bool:
        """Validate configuration."""
        return bool(cls.API_KEY)
