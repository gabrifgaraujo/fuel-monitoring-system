from datetime import datetime
from pydantic import BaseModel, field_validator
from validate_docbr import CPF

class ColetaBase(BaseModel):
    tipo_combustivel: str
    volume_litros: float
    preco_venda: float
    cpf_motorista: str
    cidade: str
    tipo_veiculo: str

    @field_validator('cpf_motorista')
    @classmethod
    def validate_cpf(cls, value):
        if not CPF().validate(value):
            raise ValueError('CPF inválido')
        return value

class ColetaCreate(ColetaBase):
    pass

class ColetaResponse(ColetaBase):
    id: int
    data_coleta: datetime
    masked_cpf_motorista: str

    class Config:
        from_attributes = True
