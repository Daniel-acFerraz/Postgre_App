from pydantic import BaseModel, EmailStr,constr, field_validator
from datetime import date
class Client(BaseModel):
    cpf: str
    name: str
    dt_nascimento: date
    email: EmailStr
    telefone: constr(max_length=11)
    estado: constr(min_length=2, max_length=2)
    cidade: str
    rua: str
    numero: constr(max_length=10)
    complemento: str = None

    @field_validator("cpf")
    def validate_cpf(cls, value):
        if len(value) < 11:
            raise ValueError(f"CPF deve conter 11 digitos: {value}")
        return value
    