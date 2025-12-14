from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime

from . import models, schemas
from .database import SessionLocal, engine

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Fuel Monitoring System API",
    description="API for collecting and analyzing fuel data for the Ministry of Transportation.",
    version="1.0.0"
)

# CORS Configuration
origins = [
    "http://localhost",
    "http://localhost:3000",  # Frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Utility function for CPF masking
def mask_cpf(cpf: str) -> str:
    """Masks the CPF for display purposes (LGPD compliance)."""
    if len(cpf) == 11:
        return f"{cpf[:3]}.***.***-{cpf[-2:]}"
    return cpf

# --- CRUD Routes ---

@app.post("/coletas/", response_model=schemas.ColetaResponse, status_code=201)
def create_coleta(coleta: schemas.ColetaCreate, db: Session = Depends(get_db)):
    db_coleta = models.Coleta(**coleta.model_dump())
    db.add(db_coleta)
    db.commit()
    db.refresh(db_coleta)
    
    # Apply masking before returning
    response_data = schemas.ColetaResponse.model_validate(db_coleta)
    response_data.masked_cpf_motorista = mask_cpf(db_coleta.cpf_motorista)
    
    return response_data

@app.get("/coletas/", response_model=List[schemas.ColetaResponse])
def read_coletas(
    db: Session = Depends(get_db),
    cidade: Optional[str] = None,
    tipo_combustivel: Optional[str] = None,
    data_inicio: Optional[datetime] = None,
    data_fim: Optional[datetime] = None,
    skip: int = 0,
    limit: int = 100
):
    query = db.query(models.Coleta)
    
    if cidade:
        query = query.filter(models.Coleta.cidade == cidade)
    if tipo_combustivel:
        query = query.filter(models.Coleta.tipo_combustivel == tipo_combustivel)
    if data_inicio:
        query = query.filter(models.Coleta.data_coleta >= data_inicio)
    if data_fim:
        query = query.filter(models.Coleta.data_coleta <= data_fim)
        
    coletas = query.offset(skip).limit(limit).all()
    
    # Apply masking for all results
    response_list = []
    for coleta in coletas:
        response_data = schemas.ColetaResponse.model_validate(coleta)
        response_data.masked_cpf_motorista = mask_cpf(coleta.cpf_motorista)
        response_list.append(response_data)
        
    return response_list

# --- KPI Routes (Placeholder for now, will be detailed in a later commit) ---

@app.get("/kpi/volume-veiculo/")
def kpi_volume_veiculo(db: Session = Depends(get_db)):
    # Placeholder for KPI logic
    return {"message": "KPI Volume by Vehicle Type endpoint is a placeholder."}

@app.get("/kpi/evolucao-preco/")
def kpi_evolucao_preco(db: Session = Depends(get_db)):
    # Placeholder for KPI logic
    return {"message": "KPI Price Evolution endpoint is a placeholder."}
