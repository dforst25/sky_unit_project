from fastapi import FastAPI, HTTPException
from db_contactor import *
from schemas import Record
import os
import uvicorn

SQL_HOST = os.getenv("SQL_HOST", 'localhost')
SQL_PORT = os.getenv("SQL_PORT", 3307)
SQL_USER = os.getenv("SQL_USER", 'root')
SQL_PASSWORD = os.getenv("SQL_PASSWORD", '')
SQL_DATABASE = os.getenv("SQL_DATABASE", 'weather')

app = FastAPI()

DB_connector = DbConnection(
    host=SQL_HOST,
    port=SQL_PORT,
    user=SQL_USER,
    password=SQL_PASSWORD,
    database=SQL_DATABASE
)



@app.post("/records")
def records(records_list: list[Record]):
    try:
        DB_connector.create_table()
        DB_connector.insert_records([record.model_dump() for record in records_list])
    
    except ConnectionError as e:
        raise HTTPException(status_code=500, detail={' Database  Connection Error':str(e)})
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.get("/records/count")
def records_count():
    try:
        return DB_connector.get_records_count()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.get("/records/avg-temperature")
def avg_temp():
    try:
        return DB_connector.get_avg_temperature()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.get('/records/max-wind')
def max_wind():
    try:
        return DB_connector.get_max_wind_speed()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    


@app.get('/records/extreme')
def extreme():
    try:
        return DB_connector.get_extreme_records()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




if __name__ == "__main__":
    uvicorn.run(
        app="main:app", 
        host="0.0.0.0", 
        port=8000, 
        reload=True
        )
