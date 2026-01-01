from pydantic import BaseModel

class FormBase(BaseModel):
    name:str
    email:str
    address:str | None = None
    phone:str

class FormCreate(FormBase):
    pass

class Form(FormBase):
    id:int
    class Config:
        orm_mode= True
