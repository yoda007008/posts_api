from fastapi import FastAPI
from app.models.router import router as routers



app = FastAPI()
app.include_router(routers)

@app.get("/")
async def read_root():
    return {"Hello": "World"}




    
