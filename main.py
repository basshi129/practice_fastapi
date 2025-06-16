from fastapi import FastAPI
from pydantic import BaseModel

# class Item(BaseModel):


app = FastAPI()

@app.get("/test/{country}")
def get(country: str):
    return {"message": f"{country}"}