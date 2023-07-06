from pydantic import BaseModel


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