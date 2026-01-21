from fastapi import FastAPI, HTTPException
from db_contactor import *


app = FastAPI()

DB_connector = DbConnection(
    host=SQL_HOST,
    port=SQL_PORT,
    user=SQL_USER,
    password=SQL_PASSWORD
)

@app.post("/records")
def records(records_list: list):
    try:
        DB_connector.create_table()
        DB_connector.insert_records(records_list)
    except ConnectionError as e:
        raise HTTPException(status_code=500, detail={' Database  Connection Error':str(e)})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))