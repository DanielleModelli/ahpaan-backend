from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Date, Enum
from database import Base
import enum

class Genero(str, enum.Enum):
    macho = "Macho"
    femea = "Femea"

class Animal(Base):
    __tablename__ = "animais"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), index=True)
    idade = Column(Date)
    especie = Column(String)
    # genero = Column(Enum(Genero))
    genero = Column(String)

# from typing import Optional
# from uuid import UUID, uuid4
# from pydantic import BaseModel
# from enum import Enum


# class Genero(str, Enum): 
#     macho = "macho"
#     femea = "femea"

# class Especie(str, Enum):
#     cachorro = "cachorro"
#     gato = "gato"

# class Animal(BaseModel):
#     id: Optional(UUID) = uuid4()
#     nome: str
#     idade: str
#     especie: Especie
#     genero: Genero

# class AnimalUpdateRequest(BaseModel):
#     nome: Optional[str]
#     idade: Optional[str]
#     especie: Optional[Especie]
#     genero: Optional[Genero]

#     # def __init__(self, nome, idade, especie, sexo):
#     #     self.nome = nome
#     #     self.idade = idade
#     #     self.especie = especie
#     #     self.sexo = sexo