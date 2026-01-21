from sqlalchemy import Table, Column, Integer, Float, String, DateTime, MetaData
from typing import Optional, Annotated
from datetime import datetime


# class Record(Table):
#     id: Optional[int] = Column(default=None, primary_key=True)
#     timestamp: Annotated[datetime, Column(...)]
#     location_name: Annotated[str, Column(...)]
#     country: Annotated[str, Column(...)]
#     latitude: Annotated[float, Column(...)]
#     longitude: Annotated[float, Column(...)]
#     temperature: Annotated[float, Column(...)]
#     wind_speed: Annotated[float, Column(...)]
#     humidity: Annotated[int, Column(...)]
#     temperature_category: Annotated[str, Column(...)]
#     wind_category: Annotated[str, Column(...)]


# r = Record('26.1.15', 'tel aviv', 'israel', 34.5, 25.7, 8.4, 11.1, 5, 'cold', 'windy')
# print(str(r), r)