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