from sqlalchemy.orm import Session
import models
import database

#Todos los métodos para crear

def create_cliente(db: Session, cliente: models.ClienteModel):
    db_cliente = database.Cliente(**cliente.dict())
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return models.ClienteModel(**db_cliente.__dict__)

def create_detalles_reporte(db: Session, detalles_reporte: models.DetallesReporteModel):
    db_detalles_reporte = database.DetallesReporte(**detalles_reporte.dict())
    db.add(db_detalles_reporte)
    db.commit()
    db.refresh(db_detalles_reporte)
    return models.DetallesReporteModel(**db_detalles_reporte.__dict__)

def create_habitacion(db: Session, habitacion: models.HabitacionesModel):
    db_habitacion = database.Habitaciones(**habitacion.dict())
    db.add(db_habitacion)
    db.commit()
    db.refresh(db_habitacion)
    return models.HabitacionesModel(**db_habitacion.__dict__)

def create_reserva(db: Session, reserva: models.ReservasModel):
    db_reserva = database.Reservas(**reserva.dict())
    db.add(db_reserva)
    db.commit()
    db.refresh(db_reserva)
    return models.ReservasModel(**db_reserva.__dict__)

def create_factura(db: Session, factura: models.FacturasModel):
    db_factura = database.Facturas(**factura.dict())
    db.add(db_factura)
    db.commit()
    db.refresh(db_factura)
    return models.FacturasModel(**db_factura.__dict__)

def create_pago(db: Session, pago: models.PagosModel):
    db_pago = database.Pagos(**pago.dict())
    db.add(db_pago)
    db.commit()
    db.refresh(db_pago)
    return models.PagosModel(**db_pago.__dict__)

def create_personal(db: Session, personal: models.PersonalModel):
    db_personal = database.Personal(**personal.dict())
    db.add(db_personal)
    db.commit()
    db.refresh(db_personal)
    return models.PersonalModel(**db_personal.__dict__)

def create_tarea(db: Session, tarea: models.TareasModel):
    db_tarea = database.Tareas(**tarea.dict())
    db.add(db_tarea)
    db.commit()
    db.refresh(db_tarea)
    return models.TareasModel(**db_tarea.__dict__)

def create_reporte(db: Session, reporte: models.ReportesModel):
    db_reporte = database.Reportes(**reporte.dict())
    db.add(db_reporte)
    db.commit()
    db.refresh(db_reporte)
    return models.ReportesModel(**db_reporte.__dict__)

#Todos los métodos para recuperar datos

def get_cliente(db: Session, cliente_id: int):
    return models.ClienteModel(db.query(database.Cliente).filter(database.Cliente.ClienteID == cliente_id).first().__dict__)

def get_clientes(db: Session, skip: int = 0, limit: int = 10):
    return models.ClienteModel(db.query(database.Cliente).offset(skip).limit(limit).all().__dict__)

