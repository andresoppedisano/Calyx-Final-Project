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

# Province
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

# Country
@app.post("/countries/", response_model=schemas.Country)
def create_country(coun: schemas.CountryCreate, db: Session = Depends(get_db)):
    return crud.create_country(db=db, coun=coun)

@app.get("/countries/", response_model=list[schemas.Country])
def read_countries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    countrs = crud.get_countries(db, skip=skip, limit=limit)
    return countrs

@app.get("/countries/{code}", response_model=list[schemas.Country])
def read_country(code: str, db: Session = Depends(get_db)):
    db_coun = crud.get_country_by_code(db, code)
    if db_coun is None:
        raise HTTPException(status_code=404, detail="Country not found")
    return db_coun

# Procedure
@app.get("/procedures/", response_model=list[schemas.Procedure])
def read_procedures(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    proceds = crud.get_procedures(db, skip=skip, limit=limit)
    return proceds

@app.post("/procedures/", response_model=schemas.Procedure)
def create_procedure(proced: schemas.ProcedureCreate, db: Session = Depends(get_db)):
    return crud.create_procedure(db=db, proced=proced)

@app.get("/procedures/{code}", response_model=list[schemas.Procedure])
def read_procedure(code: str, db: Session = Depends(get_db)):
    db_proceds = crud.get_procedure_by_code(db, code)
    if db_proceds is None:
        raise HTTPException(status_code=404, detail="Procedure not found")
    return db_proceds