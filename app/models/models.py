from sqlalchemy import Column, Integer, String
from app.db.db import Base


class Form(Base):
    __tablename__ = "fast_api"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String,nullable=False)
    email = Column(String,nullable=False)
    address = Column(String,nullable=False)
    phone = Column(String,nullable=False)

