from sqlalchemy.orm import declarative_base
"""
Todas las clases de models van a tener a base como referencia 

base servira para reutilizar el llamado a sqlalchemy.orm - declarative_base
"""
Base = declarative_base()