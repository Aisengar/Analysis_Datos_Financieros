
from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey, Numeric, Text
from models.base import Base
"""
CREATE TABLE empleados (
    id_empleado INTEGER PRIMARY KEY AUTOINCREMENT,
    cedula INTEGER NOT NULL UNIQUE,
    nombre_completo VARCHAR(150) NOT NULL,
    cargo VARCHAR(150),
    activo BOOLEAN NOT NULL DEFAULT 1
);

CREATE TABLE pagos_nomina (
    id_pago INTEGER PRIMARY KEY AUTOINCREMENT,
    id_empleado INTEGER,
    fecha_pago DATE NOT NULL,
    periodo TEXT,
    total_pago DECIMAL(13,2),
    detalles_json TEXT,
    FOREIGN KEY (id_empleado) REFERENCES empleados(id_empleado)
);
"""
class Empleado(Base):
    """
    Modelo de la tabla para SQL que se creara para empleados
    """
    __tablename__ = "empleados"
    id_empleado = Column(Integer,primary_key=True, autoincrement=True)
    cedula = Column(Integer, nullable=False, unique=True)
    nombre_completo = Column(String(150), nullable=False)
    cargo = Column(String(150))
    activo = Column(Boolean, nullable=False)

class PagosNomina(Base):
    """
    Modelo de la tabla para SQL que se creara para pagos_nomina
    """
    __tablename__ = "pagos_nomina"
    id_pago = Column(Integer,primary_key=True, autoincrement=True)
    id_empleado = Column(Integer,ForeignKey('empleados.id_empleado'), nullable=False)
    fecha_pago = Column(Date, nullable=False)
    periodo = Column(Text)
    total_pago = Column(Numeric(13,2),nullable=False)
    detalles_json = Column(Text)


