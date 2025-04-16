import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import Integer, String, create_engine, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

load_dotenv()

DATABASE_URL = os.environ.get("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

## ----------------Model------------------------
class NameModel(Base):
    __tablename__ = "names"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

Base.metadata.create_all(bind=engine)

## ----------------Pydantic Model Schema------------------------

class NameCreate(BaseModel):
    name: str

class NameResponse(BaseModel):
    id:int
    name: str

    class Config:
        orm_mode = True

## ----------------FastAPI App------------------------

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

## ----------------CRUD Routes Endpoints------------------------

## Create Name
@app.post("/names/", response_model=NameResponse)
def create_name(name_in: NameCreate, db: Session = Depends(get_db)):
    db_name = db.query(NameModel).filter(NameModel.name == name_in.name).first()
    if db_name:
        raise HTTPException(status_code=400, detail="Name already exists")
    new_name = NameModel(name=name_in.name)
    db.add(new_name)
    db.commit()
    db.refresh(new_name)
    return new_name

## Get All Names
@app.get("/names/", response_model=list[NameResponse])
def get_all_names(db: Session = Depends(get_db)):
    return db.query(NameModel).all()

## Update Name
@app.put("/names/{name_id}", response_model=NameResponse)
def update_name(name_id: int, name_in: NameCreate, db: Session = Depends(get_db)):
    db_name = db.query(NameModel).filter(NameModel.id == name_id).first()
    if not db_name:
        raise HTTPException(status_code=404, detail="Name not found")
    db_name.name = name_in.name
    db.commit()
    db.refresh(db_name)
    return db_name

## Delete Name
@app.delete("/names/{name_id}")
def delete_name(name_id: int, db: Session = Depends(get_db)):
    db_name = db.query(NameModel).filter(NameModel.id == name_id).first()
    if not db_name:
        raise HTTPException(status_code=404, detail="Name not found")
    db.delete(db_name)
    db.commit()
    return {"detail": "Name deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
