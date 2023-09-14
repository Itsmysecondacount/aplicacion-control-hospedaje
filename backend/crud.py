from sqlalchemy.orm import Session
import models
import database

def create_cliente(db: Session, cliente: models.Cliente):
    db_cliente = database.Cliente(**cliente.dict())
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return cliente