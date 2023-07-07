from pydantic import BaseModel


# Province
class ProvinceBase(BaseModel):
    name: str

    class Config:
        orm_mode = True

class ProvinceCreate(ProvinceBase):
    code: str
    country_code: str

class Province(ProvinceBase):
    id: int

    class Config:
        orm_mode = True

# Country
class CountryBase(BaseModel):
    name: str

class CountryCreate(CountryBase):
    code: str

class Country(CountryBase):
    id: int

    class Config:
        orm_mode = True

# Procedure
class ProcedureBase(BaseModel):
    type: str

class ProcedureCreate(ProcedureBase):
    province_code: str
    code_number: str

class Procedure(ProcedureBase):
    id: int

    class Config:
        orm_mode = True