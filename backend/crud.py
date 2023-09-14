from sqlalchemy.orm import Session
import database

def create_cliente(db: Session, cliente: database.Cliente):
    db.add(cliente)
    db.commit()
    db.refresh(cliente)
    return cliente