from sqlalchemy import create_engine,inspect
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models import nomina,bancos,facturas

engine = create_engine("sqlite:///contabilidad.db")
SesionMk = sessionmaker(engine)
sesion = SesionMk()

def init_db():
    Base.metadata.drop_all(engine)
    print("Inicialisando db")
    Base.metadata.create_all(engine)
    print("Db inicialisada correctamente")
def inspeccionar_db():
    # 1. Conectamos de nuevo a la base de datos
    engine = create_engine("sqlite:///contabilidad.db")
    
    # 2. Creamos el inspector (nuestro "detector")
    inspector = inspect(engine)
    
    # 3. Obtenemos las tablas
    tablas = inspector.get_table_names()
    print(f"📂 Tablas encontradas: {tablas}\n")
    
    # 4. Revisamos las columnas de cada tabla
    for tabla in tablas:
        print(f"--- Estructura de: {tabla.upper()} ---")
        columnas = inspector.get_columns(tabla)
        for col in columnas:
            # Imprimimos nombre, tipo de dato y si acepta nulos
            print(f"  • {col['name']}: {col['type']} (Nullable: {col['nullable']}, private_key = {col['primary_key']})")
        print("") # Espacio para sepa

if __name__ == "__main__":
    #init_db()
    inspeccionar_db()