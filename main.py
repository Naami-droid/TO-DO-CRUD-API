from fastapi import FastAPI, HTTPException
import pydantic
from schema import XAITaskSchema
from tasks import tasks_db

app=FastAPI()

@app.get("/")
def read_root():
    return({"message":"A TO-DO list built with FastAPI"})

@app.get("/health")
def return_health():
    return({"status":"good"})

@app.get("/task/{id}")
def return_task(id:int)->XAITaskSchema:
    task=tasks_db.get(id)
    if task:
        return task
    raise HTTPException(status_code=404, detail="Task not Found!")


@app.post("/tasks", status_code=201)
def create_task(task:XAITaskSchema)->XAITaskSchema:
    tasks_db[task.id]=task
    return task

@app.put("/tasks/{id}")
def update_task(id:int,newTask:XAITaskSchema)->XAITaskSchema:
    task=tasks_db.get(id)
    if task:
        tasks_db[id]=newTask
        return newTask
    raise HTTPException(status_code=404, detail="TASK NOT FOUND!")


@app.delete("/tasks/{id}", status_code=204)
def delete_task(id:int):
    if id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task Not Found!")
    tasks_db.pop(id)
