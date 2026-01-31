from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey, Numeric, Text
from models.base import Base

"""
CREATE TABLE  proveedores(
    id_proveedor INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nombre_limpio VARCHAR(150) NOT NULL UNIC,
    nombre_original VARCHAR(150) NOT NULL,
    nit INTEGER
 );
 CREATE TABLE centros_de_costo(
    id_proyecto INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nombre_centro VARCHAR(150) NOT NULL
 );

 CREATE TABLE facturas(
    id_factura INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    id_proveedor INTEGER,
    id_proyecto INTEGER,
    numero_factura TEXT NOT NULL,
    fecha DATE NOT NULL,
    concepto_agrupado TEXT,
    total_valor DECIMAL(13,2) NOT NULL DEFAULT 0.0,
    impuesto DECIMAL(13,2) NOT NULL DEFAULT 0.0,
    retencion DECIMAL(13,2) NOT NULL DEFAULT 0.0,
    FOREIGN KEY (id_proveedor) REFERENCES proveedores(id_proveedor),
    FOREIGN KEY (id_proyecto) REFERENCES centros_de_costo(id_proyecto)

 );
"""
class Proveedor(Base):
    __tablename__ = "proveedores"
    id_proveedor = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    nombre_limpio = Column(String(150), unique=True, nullable=False)
    nombre_original = Column(String(150), nullable=False)
    nit = Column(Integer)
class CentroDeCostos(Base):
    __tablename__ = "centros_de_costo"
    id_proyecto = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    nombre_centro = Column(String(150), nullable=False)

class Factura(Base):
    __tablename__ = "facturas"
    id_factura = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    id_proveedor = Column(Integer, ForeignKey("proveedores.id_proveedor"))
    id_proyecto = Column(Integer, ForeignKey("centros_de_costo.id_proyecto"))
    numero_factura = Column(String(150), nullable=False)
    fecha = Column(Date, nullable=False)
    concepto_agrupado = Column(Text)
    impuesto = Column(Numeric(13,2), nullable=False, default=0.0)
    retencion = Column(Numeric(13,2), nullable=False, default=0.0)
    total_valor = Column(Numeric(13,2), nullable=False, default=0.0)


