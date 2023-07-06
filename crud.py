from sqlalchemy.orm import Session
from sqlalchemy.sql import compiler
import models, schemas

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