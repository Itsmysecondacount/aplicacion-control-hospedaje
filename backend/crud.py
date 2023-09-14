from sqlalchemy.orm import Session
import models
import database

def create_cliente(db: Session, cliente: models.Cliente):
    copy_client = cliente
    db_cliente = database.Cliente(**cliente.dict())
    db.add(db_cliente)
    db.commit()
    db.refresh(cliente)
    return copy_client