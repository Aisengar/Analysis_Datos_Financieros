from sqlalchemy import Column, Integer, String, Date, ForeignKey, Numeric, Text
from models.base import Base

"""
CREATE TABLE cuentas_bancarias (
    id_cuenta INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nombre_banco VARCHAR(50) NOT NULL,
    numero_cuenta VARCHAR(50) NOT NULL,
    tipo_cuenta VARCHAR(50) NOT NULL
)

CREATE TABLE transacciones_bancarias(
    id_transaccion INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    id_cuenta INTEGER,
    fecha DATE NOT NULL,
    concepto VARCHAR(255),
    metadata Text,
    cargo NUMERIC(13,2) NOT NULL DEFAULT 0.0,
    abono NUMERIC(13,2) NOT NULL DEFAULT 0.0,
    saldo NUMERIC(13,2)
    FOREIGN KEY (id_cuenta) REFERENSE cuentas_bancarias(id_cuentas)

)
"""

class CuentaBancaria(Base):
    __tablename__ = 'cuentas_bancarias' #nombre de la tabla
    id_cuenta = Column(Integer, autoincrement=True, primary_key= True, nullable=False)
    nombre_banco = Column(String(50),nullable=False)
    numero_cuenta = Column(String(50), nullable=False)
    tipo_cuenta = Column(String(50), nullable=False)

class Transaccion(Base):
    __tablename__ = "transacciones_bancarias"
    id_transaccion = Column(Integer, nullable=False,primary_key=True,autoincrement=True)
    id_cuenta = Column(Integer, ForeignKey("cuentas_bancarias.id_cuenta"))
    fecha = Column(Date, nullable=False)
    concepto = Column(String(255))
    metadata = Column(Text)
    cargo = Column(Numeric(13,2), nullable=False, default= 0.0)
    abono = Column(Numeric(13,2), nullable=False, default= 0.0)
    saldo = Column(Numeric(13,2), nullable=False, default= 0.0)

    
    
