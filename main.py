from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException


app = FastAPI()

tasks=[]

class Task_Dec(BaseModel):
    title : str
    done : bool=False

next_id=1


@app.get("/task",status_code=200)
def get_tasks():
    return tasks

@app.post("/task")
def create_tasks(task:Task_Dec):
    global next_id
    new_task={"id":next_id,"task":task.title,"done":task.done}
    tasks.append(new_task)
    next_id+=1
    return tasks

@app.delete("/task/{task_id}")
def delete_task(task_id:int):
    if task_id<1:
        raise HTTPException(status_code=400,detail="id doest exist")
    for x in tasks:
        if x["id"]==task_id:
            tasks.remove(x)
            return {"message":"Deleted"}
    raise HTTPException(status_code=404,detail="Task not found")


@app.put("/task/{task_id}")
def update_task(task_id:int,task:Task_Dec):
    if task_id<1:
        raise HTTPException(status_code=400,detail="bad request")
    for x in tasks:
        if x["id"]==task_id:
            x["done"]=task.done
            x["task"]=task.title
            return x
    raise HTTPException(status_code=404,detail="id doesnt exist")