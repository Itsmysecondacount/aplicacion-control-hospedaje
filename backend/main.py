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
def create_cliente(cliente: models.ClienteModel, db: Session = Depends(get_db)):
    return crud.create_cliente(db, cliente)

@app.post("/detalles-reporte/")
def create_detalles_reporte(detalles_reporte: models.DetallesReporteModel, db: Session = Depends(get_db)):
    return crud.create_detalles_reporte(db, detalles_reporte)

@app.post("/habitaciones/")
def create_habitacion(habitacion: models.HabitacionesModel, db: Session = Depends(get_db)):
    return crud.create_habitacion(db, habitacion)

@app.post("/reservas/")
def create_reserva(reserva: models.ReservasModel, db: Session = Depends(get_db)):
    return crud.create_reserva(db, reserva)

@app.post("/facturas/")
def create_factura(factura: models.FacturasModel, db: Session = Depends(get_db)):
    return crud.create_factura(db, factura)

@app.post("/pagos/")
def create_pago(pago: models.PagosModel, db: Session = Depends(get_db)):
    return crud.create_pago(db, pago)

@app.post("/personal/")
def create_personal(personal: models.PersonalModel, db: Session = Depends(get_db)):
    return crud.create_personal(db, personal)

@app.post("/tareas/")
def create_tarea(tarea: models.TareasModel, db: Session = Depends(get_db)):
    return crud.create_tarea(db, tarea)

@app.post("/reportes/")
def create_reporte(reporte: models.ReportesModel, db: Session = Depends(get_db)):
    return crud.create_reporte(db, reporte)

#Endpoints para recuperar datos

#Tabla Clientes
@app.get("/clientes/{cliente_id}")
def read_cliente(cliente_id: int, db: Session = Depends(get_db)):
    db_cliente = crud.get_cliente(db, cliente_id=cliente_id)
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return db_cliente

@app.get("/clientes/")
def read_clientes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    clientes = crud.get_clientes(db, skip=skip, limit=limit)
    return clientes

@app.get("/clientes/search/")
def search_cliente(name: str, db: Session = Depends(get_db)):
    clientes = crud.search_cliente_by_name(db, name)
    return clientes

#Tabla para Personal
@app.get("/personal/{personal_id}")
def read_personal(personal_id: int, db: Session = Depends(get_db)):
    personal = crud.get_personal(db, personal_id)
    return personal

@app.get("/personal/")
def read_all_personal(db: Session = Depends(get_db)):
    personal_all = crud.get_all_personal(db)
    return personal_all

#Tabla Tareas
@app.get("/tareas/{tarea_id}")
def read_tarea(tarea_id: int, db: Session = Depends(get_db)):
    tarea = crud.get_tarea(db, tarea_id)
    return tarea

@app.get("/tareas/")
def read_all_tareas(db: Session = Depends(get_db)):
    tareas = crud.get_all_tareas(db)
    return tareas

# Para DetallesReporte
@app.get("/detalles_reporte/{detalle_reporte_id}")
def read_detalle_reporte(detalle_reporte_id: int, db: Session = Depends(get_db)):
    return crud.get_detalle_reporte(db, detalle_reporte_id)

@app.get("/detalles_reporte/")
def read_all_detalles_reporte(db: Session = Depends(get_db)):
    return crud.get_all_detalles_reporte(db)

# Para Facturas
@app.get("/facturas/{factura_id}")
def read_factura(factura_id: int, db: Session = Depends(get_db)):
    return crud.get_factura(db, factura_id)

@app.get("/facturas/")
def read_all_facturas(db: Session = Depends(get_db)):
    return crud.get_all_facturas_ordered_by_date(db)

# Para Habitaciones
@app.get("/habitaciones/{habitacion_id}")
def read_habitacion(habitacion_id: int, db: Session = Depends(get_db)):
    return crud.get_habitacion(db, habitacion_id)

@app.get("/habitaciones/")
def read_all_habitaciones(db: Session = Depends(get_db)):
    return crud.get_all_habitaciones(db)

# Para Pagos
@app.get("/pagos/{pago_id}")
def read_pago(pago_id: int, db: Session = Depends(get_db)):
    return crud.get_pago(db, pago_id)

@app.get("/pagos/")
def read_all_pagos(db: Session = Depends(get_db)):
    return crud.get_all_pagos_ordered_by_date(db)

# Para Reportes
@app.get("/reportes/{reporte_id}")
def read_reporte(reporte_id: int, db: Session = Depends(get_db)):
    return crud.get_reporte(db, reporte_id)

@app.get("/reportes/")
def read_all_reportes(db: Session = Depends(get_db)):
    return crud.get_all_reportes_ordered_by_date(db)

# Para Reservas
@app.get("/reservas/{reserva_id}")
def read_reserva(reserva_id: int, db: Session = Depends(get_db)):
    return crud.get_reserva(db, reserva_id)

@app.get("/reservas/")
def read_all_reservas(db: Session = Depends(get_db)):
    return crud.get_all_reservas_ordered_by_date(db)
    