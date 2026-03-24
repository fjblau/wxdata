from pydantic import BaseModel
from datetime import datetime


class WeatherReading(BaseModel):
    location: str
    timestamp: datetime
    temperature: float
    humidity: float
    description: str
    raw: dict = {}
