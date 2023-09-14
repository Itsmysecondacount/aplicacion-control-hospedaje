from pydantic import BaseModel
from datetime import date
from typing import Optional

class ClienteModel(BaseModel):
    ClienteID: Optional[int] = None
    DNI: str
    Nombre: str
    Apellido: str
    Email: Optional[str] = None
    Telefono: Optional[str] = None
    Atributo1: Optional[str] = None
    Atributo2: Optional[str] = None

class DetallesReporteModel(BaseModel):
    DetalleID: Optional[int] = None
    ReporteID: int
    Descripcion: Optional[str] = None
    Datos: str
    Atributo1: Optional[str] = None
    Atributo2: Optional[str] = None

class HabitacionesModel(BaseModel):
    HabitacionID: int
    Tipo: str
    Estado: Optional[str] = None
    PrecioPorNoche: float
    Atributo1: Optional[str] = None
    Atributo2: Optional[str] = None

class ReservasModel(BaseModel):
    ReservaID: Optional[int] = None
    ClienteID: int
    HabitacionID: int
    FechaInicio: date
    FechaFin: Optional[date] = None
    Estado: str
    Atributo1: Optional[str] = None
    Atributo2: Optional[str] = None

class FacturasModel(BaseModel):
    FacturaID: Optional[int] = None
    ReservaID: int
    Fecha: date
    MontoTotal: float
    Estado: str
    Atributo1: Optional[str] = None
    Atributo2: Optional[str] = None

class PagosModel(BaseModel):
    PagoID: Optional[int] = None
    FacturaID: int
    Fecha: date
    Monto: float
    Metodo: str
    Atributo1: Optional[str] = None
    Atributo2: Optional[str] = None

class PersonalModel(BaseModel):
    PersonalID: Optional[int] = None
    Nombre: str
    Puesto: str
    Horario: Optional[str] = None
    Atributo1: Optional[str] = None
    Atributo2: Optional[str] = None

class TareasModel(BaseModel):
    TareaID: Optional[int] = None
    PersonalID: int
    Descripcion: str
    Estado: str
    Atributo1: Optional[str] = None
    Atributo2: Optional[str] = None

class ReportesModel(BaseModel):
    ReporteID: Optional[int] = None
    Tipo: str
    FechaGenerado: date
    Atributo1: Optional[str] = None
    Atributo2: Optional[str] = None