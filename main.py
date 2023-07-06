from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException
from database import SessionLocal, engine
import crud, models, schemas


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

TIMEOUT = 20

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/provinces/", response_model=schemas.Province)
def create_province(prov: schemas.ProvinceCreate, db: Session = Depends(get_db)):
    return crud.create_province(db=db, prov=prov)

@app.get("/provinces/", response_model=list[schemas.Province])
def read_provinces(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    provs = crud.get_provinces(db, skip=skip, limit=limit)
    return provs

@app.get("/provinces/{code}", response_model=list[schemas.Province])
def read_province(code: str, db: Session = Depends(get_db)):
    db_prov = crud.get_province_by_code(db, code)
    if db_prov is None:
        raise HTTPException(status_code=404, detail="Province not found")
    return db_prov