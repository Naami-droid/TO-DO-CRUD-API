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

@app.get("/task/{id}")
def return_task(id:int)->TaskSchema:
    task=tasks_db.get(id)
    if task:
        return task
    raise HTTPException(status_code=404, detail="Task not Found!")