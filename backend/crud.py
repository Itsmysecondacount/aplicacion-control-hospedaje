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

#Tabla Clientes

def get_cliente(db: Session, cliente_id: int):
    return db.query(database.Cliente).filter(database.Cliente.ClienteID == cliente_id).first()

def get_clientes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(database.Cliente).offset(skip).limit(limit).all()

def search_cliente_by_name(db: Session, name: str):
    return db.query(database.Cliente).filter(database.Cliente.Nombre.ilike(f"%{name}%")).limit(10).all()

#Tabla para Personal
# Recuperar un registro específico
def get_personal(db: Session, personal_id: int):
    return db.query(database.Personal).filter(database.Personal.PersonalID == personal_id).first()

# Recuperar todos los registros ordenados por fecha
def get_all_personal(db: Session, skip: int = 0, limit: int = 10):
    return db.query(database.Personal).offset(skip).limit(limit).all()

#Tabla para Tareas
# Recuperar un registro específico
def get_tarea(db: Session, tarea_id: int):
    return db.query(database.Tareas).filter(database.Tareas.TareaID == tarea_id).first()

# Recuperar todos los registros ordenados por fecha
def get_all_tareas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(database.Tareas).offset(skip).limit(limit).all()

##Agregar los métodos para tareas según el tipo "estado" completado o no

# DetallesReporte
def get_detalle_reporte(db: Session, detalle_reporte_id: int):
    return db.query(database.DetallesReporte).filter(database.DetallesReporte.DetalleID == detalle_reporte_id).first()

def get_all_detalles_reporte(db: Session):
    return db.query(database.DetallesReporte).all()

# Facturas
def get_factura(db: Session, factura_id: int):
    return db.query(database.Facturas).filter(database.Facturas.FacturaID == factura_id).first()

def get_all_facturas_ordered_by_date(db: Session):
    return db.query(database.Facturas).order_by(database.Facturas.Fecha).all()

# Habitaciones
def get_habitacion(db: Session, habitacion_id: int):
    return db.query(database.Habitaciones).filter(database.Habitaciones.HabitacionID == habitacion_id).first()

def get_all_habitaciones(db: Session):
    return db.query(database.Habitaciones).all()

# Pagos
def get_pago(db: Session, pago_id: int):
    return db.query(database.Pagos).filter(database.Pagos.PagoID == pago_id).first()

def get_all_pagos_ordered_by_date(db: Session):
    return db.query(database.Pagos).order_by(database.Pagos.Fecha).all()

# Reportes
def get_reporte(db: Session, reporte_id: int):
    return db.query(database.Reportes).filter(database.Reportes.ReporteID == reporte_id).first()

def get_all_reportes_ordered_by_date(db: Session):
    return db.query(database.Reportes).order_by(database.Reportes.FechaGenerado).all()

# Reservas
def get_reserva(db: Session, reserva_id: int):
    return db.query(database.Reservas).filter(database.Reservas.ReservaID == reserva_id).first()

def get_all_reservas_ordered_by_date(db: Session):
    return db.query(database.Reservas).order_by(database.Reservas.FechaInicio).all()