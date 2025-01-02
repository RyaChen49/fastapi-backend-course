from fastapi import FastAPI
from .database import Base, engine
from .routers import router
#Initialize Fasapi
app = FastAPI()

#Initialize Database's Table
#Base.metadata.create_all(bind=engine)
#Resister Router
app.include_router(router=router,prefix="/api",tags=["todos"])
app.include_router(auth_router)