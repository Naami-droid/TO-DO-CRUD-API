from pydantic import BaseModel, Field

class TaskSchema(BaseModel):
    id: int =Field(description="A unique identifier for the task")
    title:str=Field(description="What is the task about, a short descriptive name")
    completed:bool=Field(default=False,description="Is the task completed or yet to be completed")