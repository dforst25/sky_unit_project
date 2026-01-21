from fastapi import FastAPI

app = FastAPI()



@app.post("/records")
def records(records_list: list):
    pass
    