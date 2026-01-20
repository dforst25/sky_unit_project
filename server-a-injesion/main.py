from fastapi import FastAPI, HTTPException
from api_extractor import ingest_weather_for_location
import uvicorn

app = FastAPI()

@app.post("/ingest")
def extract_data(city: str):
    try:
        result = ingest_weather_for_location(city)
    except ValueError as e:
        raise HTTPException(status_code=404, detail="location not found")
    return result
    

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8080, reload=True)