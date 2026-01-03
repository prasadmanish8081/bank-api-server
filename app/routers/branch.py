from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models

router = APIRouter(prefix="/branches", tags=["Branches"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{ifsc}")
def get_branch(ifsc: str, db: Session = Depends(get_db)):
    return db.query(models.Branch).filter(models.Branch.ifsc == ifsc).first()


@router.get("/")
def get_all_branches(db: Session = Depends(get_db)):
    return db.query(models.Branch).limit(10).all()
