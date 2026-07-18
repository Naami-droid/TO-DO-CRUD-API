from fastapi import FastAPI, HTTPException
import pydantic
from schema import TaskSchema
from tasks import tasks_db

app=FastAPI()

@app.get("/")
def read_root():
    return({"message":"A TO-DO list built with FastAPI"})

@app.get("/health")
def return_health():
    return({"status":"good"})