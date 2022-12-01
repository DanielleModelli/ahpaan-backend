from pydantic import BaseModel
from models import Genero
from datetime import date



class AnimalSchema(BaseModel):
    nome: str 
    idade: date 
    especie: str 
    genero: str 

    class Config: 
        orm_mode = True