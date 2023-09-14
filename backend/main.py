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