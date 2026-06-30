

from fastapi import HTTPException, APIRouter,Depends
from database import create_session
from models import Task
from sqlmodel import Session,select


router=APIRouter() 


@router.get("/task")
def get_task(session:Session=Depends(create_session)):
    return session.exec(select(Task)).all()


@router.post("/task",status_code=201)
def post_task(task:Task,session:Session=Depends(create_session)):
    session.add(task)
    session.commit()
    session.refresh(task)
    return task 

@router.delete("/task/{task_id}")
def delete_task(task_id:int,session:Session=Depends(create_session)):
    task=session.get(Task,task_id)
    if not task:
        raise HTTPException(status_code=404,detail="task not found")
    session.delete(task)
    session.commit()
    return {"message":"task deleted"}

@router.put("/task/{task_id}")
def update_task(task_id:int,new_task:Task,session:Session=Depends(create_session)):
    task=session.get(Task,task_id)
    if not task:
        raise HTTPException(status_code=404,detail="task not found")
    task.title=new_task.title
    task.done=new_task.done
    session.add(task)
    session.commit()
    return {"message":"updated"}


    