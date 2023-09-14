from sqlalchemy.orm import Session
from . import models

def create_cliente(db: Session, cliente: models.Cliente):
    db.add(cliente)
    db.commit()
    db.refresh(cliente)
    return cliente