from sqlalchemy import Column, Integer, String, Float, DateTime, func
from .database import Base

class Coleta(Base):
    __tablename__ = "coletas"

    id = Column(Integer, primary_key=True, index=True)
    data_coleta = Column(DateTime, default=func.now())
    tipo_combustivel = Column(String, index=True)
    volume_litros = Column(Float)
    preco_venda = Column(Float)
    cpf_motorista = Column(String, index=True)
    cidade = Column(String, index=True)
    tipo_veiculo = Column(String, index=True)
