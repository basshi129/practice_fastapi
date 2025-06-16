from fastapi import FastAPI
from pydantic import BaseModel

class Data(BaseModel):
    x: float
    y: float

app = FastAPI()

@app.post("/")
def calc(data: Data):
    return data.x * data.y

@app.get("/")
def get():
    return {"message": "testtest"}