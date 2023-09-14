from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Text, Float, Date, ForeignKey

SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:tokyo3@db:3306/hospedaje_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'Clientes'

    ClienteID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    DNI = Column(String(20), unique=True, index=True)
    Nombre = Column(String(50))
    Apellido = Column(String(50))
    Email = Column(String(50))
    Telefono = Column(String(20))
    Atributo1 = Column(String(50))
    Atributo2 = Column(String(50))

class DetallesReporte(Base):
    __tablename__ = 'DetallesReporte'
    
    DetalleID = Column(Integer, primary_key=True, autoincrement=True)
    ReporteID = Column(Integer, ForeignKey('Reportes.ReporteID'))
    Descripcion = Column(String(200))
    Datos = Column(Text)
    Atributo1 = Column(String(50))
    Atributo2 = Column(String(50))

class Habitaciones(Base):
    __tablename__ = 'Habitaciones'
    
    HabitacionID = Column(Integer, primary_key=True)
    Tipo = Column(String(20))
    Estado = Column(String(20))
    PrecioPorNoche = Column(Float)
    Atributo1 = Column(String(50))
    Atributo2 = Column(String(50))

class Reservas(Base):
    __tablename__ = 'Reservas'
    
    ReservaID = Column(Integer, primary_key=True, autoincrement=True)
    ClienteID = Column(Integer, ForeignKey('Clientes.ClienteID'))
    HabitacionID = Column(Integer, ForeignKey('Habitaciones.HabitacionID'))
    FechaInicio = Column(Date)
    FechaFin = Column(Date)
    Estado = Column(String(20))
    Atributo1 = Column(String(50))
    Atributo2 = Column(String(50))

class Facturas(Base):
    __tablename__ = 'Facturas'
    
    FacturaID = Column(Integer, primary_key=True, autoincrement=True)
    ReservaID = Column(Integer, ForeignKey('Reservas.ReservaID'))
    Fecha = Column(Date)
    MontoTotal = Column(Float)
    Estado = Column(String(20))
    Atributo1 = Column(String(50))
    Atributo2 = Column(String(50))

class Pagos(Base):
    __tablename__ = 'Pagos'
    
    PagoID = Column(Integer, primary_key=True, autoincrement=True)
    FacturaID = Column(Integer, ForeignKey('Facturas.FacturaID'))
    Fecha = Column(Date)
    Monto = Column(Float)
    Metodo = Column(String(20))
    Atributo1 = Column(String(50))
    Atributo2 = Column(String(50))

class Personal(Base):
    __tablename__ = 'Personal'
    
    PersonalID = Column(Integer, primary_key=True, autoincrement=True)
    Nombre = Column(String(50))
    Puesto = Column(String(20))
    Horario = Column(String(50))
    Atributo1 = Column(String(50))
    Atributo2 = Column(String(50))

class Tareas(Base):
    __tablename__ = 'Tareas'
    
    TareaID = Column(Integer, primary_key=True, autoincrement=True)
    PersonalID = Column(Integer, ForeignKey('Personal.PersonalID'))
    Descripcion = Column(String(200))
    Estado = Column(String(20))
    Atributo1 = Column(String(50))
    Atributo2 = Column(String(50))

class Reportes(Base):
    __tablename__ = 'Reportes'
    
    ReporteID = Column(Integer, primary_key=True, autoincrement=True)
    Tipo = Column(String(50))
    FechaGenerado = Column(Date)
    Atributo1 = Column(String(50))
    Atributo2 = Column(String(50))