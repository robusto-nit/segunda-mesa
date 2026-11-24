from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Archivo SQLite que se creará automáticamente en la carpeta backend
SQLALCHEMY_DATABASE_URL = "sqlite:///./segunda_mesa.db"

# check_same_thread=False permite que FastAPI maneje varias peticiones concurrentes en SQLite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependencia para abrir y cerrar la sesión de BD en cada endpoint
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()