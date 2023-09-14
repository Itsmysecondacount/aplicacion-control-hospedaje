from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Float, Date

SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://icarouscja:tokyo3@db:3306/hospedaje_db"

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