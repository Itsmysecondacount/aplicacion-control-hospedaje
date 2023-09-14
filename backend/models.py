from pydantic import BaseModel
from datetime import date
from typing import Optional

class Reserva(BaseModel):
    reserva_id: Optional[int] = None
    cliente_id: Optional[int] = None
    habitacion_id: Optional[int] = None
    fecha_inicio: Optional[date] = None
    fecha_fin: Optional[date] = None
    estado: Optional[str] = None
    atributo1: Optional[str] = None
    atributo2: Optional[str] = None

class Cliente(BaseModel):
    Dni: Optional[str] = None
    Nombre: Optional[str] = None
    Apellido: Optional[str] = None
    Email: Optional[str] = None
    Telefono: Optional[str] = None
    Atributo1: Optional[str] = None
    Atributo2: Optional[str] = None

class DetalleReporte(BaseModel):
    reporte_id: Optional[int] = None
    descripcion: Optional[str] = None
    datos: Optional[str] = None
    atributo1: Optional[str] = None
    atributo2: Optional[str] = None

class Factura(BaseModel):
    factura_id: Optional[int] = None  # Este campo se autoincrementará en la base de datos
    reserva_id: Optional[int] = None
    fecha: Optional[date] = None
    monto_total: Optional[float] = None
    estado: Optional[str] = None
    atributo1: Optional[str] = None
    atributo2: Optional[str] = None

class Habitacion(BaseModel):
    habitacion_id: int
    tipo: Optional[str] = None
    estado: Optional[str] = None
    precio_por_noche: Optional[float] = None
    atributo1: Optional[str] = None
    atributo2: Optional[str] = None

class Pago(BaseModel):
    pago_id: Optional[int] = None
    factura_id: Optional[int] = None
    fecha: Optional[date] = None
    monto: Optional[float] = None
    metodo: Optional[str] = None
    atributo1: Optional[str] = None
    atributo2: Optional[str] = None

class Personal(BaseModel):
    personal_id: Optional[int] = None
    nombre: Optional[str] = None
    puesto: Optional[str] = None
    horario: Optional[str] = None
    atributo1: Optional[str] = None
    atributo2: Optional[str] = None

class Reporte(BaseModel):
    reporte_id: Optional[int] = None
    tipo: Optional[str] = None
    fecha_generado: Optional[date] = None
    atributo1: Optional[str] = None
    atributo2: Optional[str] = None

class Tarea(BaseModel):
    tarea_id: Optional[int] = None
    personal_id: Optional[int] = None
    descripcion: Optional[str] = None
    estado: Optional[str] = None
    atributo1: Optional[str] = None
    atributo2: Optional[str] = None