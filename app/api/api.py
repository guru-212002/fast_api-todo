from fastapi import FastAPI, Depends
from app.schemas.schemas import Form as FormRes
from app.schemas.schemas import FormCreate
from sqlalchemy.orm import Session 
from app.db.db import session_local
from app.models.models import Form

app = FastAPI()


# dependancy for .post()
def get_db():
    db = session_local()

    try:
        yield db
    finally:
        db.close()


@app.post("/form", response_model=FormRes)
def create_form(form: FormCreate, db: Session = Depends(get_db)):
    
    db_form = Form(**form.dict())
    db.add(db_form)
    db.commit()
    db.refresh(db_form)
    return db_form
