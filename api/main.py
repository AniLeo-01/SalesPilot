from fastapi import FastAPI
from api.web.controllers.controllers import router
from api.web.db import disconnect_db, init_db

app = FastAPI(title = "Sales Pilot API", version = "1.0.0")

@app.on_event("startup")
async def on_startup():
    print("Sales Pilot API started.....")
    await init_db()

@app.on_event("shutdown")
async def shutdown():
    print("Sales Pilot API shutdown....")
    await disconnect_db()

app.include_router(router, tags=['Sales Pilot'])
