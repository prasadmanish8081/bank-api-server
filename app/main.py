from fastapi import FastAPI
from app.database import engine
from app.models import Base
from app.routers import bank, branch

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Bank API Server")

app.include_router(bank.router)
app.include_router(branch.router)



@app.get("/")
def root():
    return {"message": "Bank API is running!"}