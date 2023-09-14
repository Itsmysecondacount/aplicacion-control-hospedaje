from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import crud, models, database

app = FastAPI()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.post("/clientes/")
def create_cliente(cliente: models.Cliente, db: Session = Depends(get_db)):
    return crud.create_cliente(db, cliente)