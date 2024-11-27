from fastapi import FastAPI
from app.models.router import router as routers



app = FastAPI()
router = app.router
app.include_router(routers)




    
