from fastapi import FastAPI, HTTPException
from data_cleaning import basic_cleaning, add_categiries
from service import send_data_to_service_c
import os



service_c_url = os.getenv("SERVICE_C_URL", 'http://localhost:8003/records')

app = FastAPI()


@app.get("/health")
def health_check():
    return {"status": "server is healthy"}



@app.post("/clean")
def clean_data(raw_data: list[dict]):
    try:
        cleaned_data = basic_cleaning(raw_data)
        categorized_data = add_categiries(cleaned_data)
        is_saved = send_data_to_service_c(service_c_url, categorized_data.to_dict(orient='records'))


    except Exception as e:
        raise HTTPException(status_code=422, detail={"error": str(e)})


    return is_saved





if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app="main:app",
        host="0.0.0.0",
        port=8002,
        reload=True
    )

