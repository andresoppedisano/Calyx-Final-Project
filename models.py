from sqlalchemy import Column, ForeignKey, Integer, String
from database import Base


class Province(Base):
    __tablename__ = "provinces"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    code = Column(String)
    country_code = Column(String, ForeignKey("countries.id"))

class Country(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True)
    code = Column(String)
    name = Column(String)

class Procedure(Base):
    __tablename__ = "procedures"

    id = Column(Integer, primary_key=True, index=True)
    code_number = Column(String)
    type = Column(String)
    province_code = Column(String, ForeignKey("provinces.id"))