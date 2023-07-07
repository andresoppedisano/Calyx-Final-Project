from sqlalchemy.orm import Session
from sqlalchemy.sql import compiler
import models, schemas


# Province
def get_provinces(db: Session, skip: int = 0, limit: int = 100):
    query = db.query(models.Province).offset(skip).limit(limit)
    return query.all()

def get_province_by_code(db: Session, code: str):
    return db.query(models.Province).filter(models.Province.code == code).all()

def create_province(db: Session, prov: schemas.ProvinceCreate):
    db_prov = models.Province(name=prov.name, code=prov.code, country_code=prov.country_code)
    db.add(db_prov)
    db.commit()
    db.refresh(db_prov)
    return db_prov

# Country
def get_countries(db: Session, skip: int = 0, limit: int = 100):
    query = db.query(models.Country).offset(skip).limit(limit)
    return query.all()

def create_country(db: Session, coun: schemas.CountryCreate):
    db_coun = models.Country(name=coun.name, code=coun.code)
    db.add(db_coun)
    db.commit()
    db.refresh(db_coun)
    return db_coun

def get_country_by_code(db: Session, code: str):
    return db.query(models.Country).filter(models.Country.code == code).all()

# Procedure
def get_procedures(db: Session, skip: int = 0, limit: int = 100):
    query = db.query(models.Procedure).offset(skip).limit(limit)
    return query.all()

def create_procedure(db: Session, proced: schemas.ProcedureCreate):
    db_proced = models.Procedure(type=proced.type, province_code=proced.province_code, code_number=proced.code_number)
    db.add(db_proced)
    db.commit()
    db.refresh(db_proced)
    return db_proced

def get_procedure_by_code(db: Session, code: str):
    return db.query(models.Procedure).filter(models.Procedure.code_number == code).all()