from fastapi import FastAPI, HTTPException
from api_extractor import ingest_weather_for_location
from service import send_records_to_service_b
import uvicorn

app = FastAPI()

@app.post("/ingest")
def extract_data(city: str):
    try:
        result = ingest_weather_for_location(city)
    
    except ValueError as e:
        raise HTTPException(status_code=404, detail={"Error":"location not found", "detail": str(e)})
    
    try:
        data_sent = send_records_to_service_b(result)
        return data_sent
    
    except Exception as e:
        raise HTTPException(status_code=500, detail={"Error": str(e)})
    

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", port=8001, reload=True)