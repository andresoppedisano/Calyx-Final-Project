from sqlalchemy import Column, ForeignKey, Integer, String
from database import Base


class Province(Base):
    __tablename__ = "provinces"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    code = Column(String)
    country_code = Column(String)