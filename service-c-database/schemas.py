from pydantic import BaseModel


class Record(BaseModel):
    timestamp: str
    location_name: str
    country: str
    latitude: float
    longitude: float
    temperature: float
    wind_speed: float
    humidity: int
    temperature_category: str
    wind_category: str