from fastapi import FastAPI
from database import create_table
from routers.tasks import router

app= FastAPI()



@app.on_event("startup")
def on_startup():
    create_table()


app.include_router(router)


