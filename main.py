from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException

app=FastAPI()

tasks=[]
next_id=1
class Task(BaseModel):
    title : str
    done : bool

@app.get("/tasks")
def get_tasks():
    return tasks


@app.post("/tasks",status_code=201)
def add_task(task:Task):
    global next_id
    new_task={"id":next_id,"title":task.title, "done":task.done}
    tasks.append(new_task)
    next_id+=1
    return new_task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id<1:
        raise HTTPException(status_code=400 , detail="bad request")
    for x in tasks:
        if x["id"] == task_id:
            tasks.remove(x)
            return {"message": "deleted"}
    raise HTTPException (status_code="404" detail:"message not found")
    

