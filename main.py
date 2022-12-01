from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse
from starlette.requests import Request
from models import Animal
import models
from schemas import AnimalSchema
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
def hello_root():
    return {"message": "Hello World"}


@app.get("/animais/", response_model=List[AnimalSchema])
def lista_animais(db: Session = Depends(get_db)):
    animais = db.query(Animal).all()
    print(animais)
    return animais

@app.post("/animais/")
def adiciona_animal(animal: AnimalSchema, db: Session = Depends(get_db)):
    db_animal = Animal(nome= animal.nome, idade=animal.idade, especie = animal.especie, genero = animal.genero)
    db.add(db_animal)
    db.commit()
    # db.close()
    return animal.dict()
    # return {"animal adicionado com sucesso!"}
    

@app.delete("/animais/{animal_id}")
def deleta_animal(animal_id: int, db: Session = Depends(get_db)):
    db_animal = db.query(Animal).where(Animal.id == animal_id).delete()
    db.commit()
    return {"animal removido com sucesso!"}

# @app.put("/api/v1/animais/{animal_id}")
# async def atualiza_animal(animal_update: AnimalUpdateRequest, animal_id: UUID):
#     for animal in db:
#         if animal_update.nome is not None:
#             animal.nome = animal_update.nome
#         if animal_update.idade is not None:
#             animal.idade = animal_update.idade
#         if animal_update.genero is not None:
#             animal.genero = animal_update.genero
#         if animal_update.especie is not None:
#             animal.especie = animal_update.especie
#     raise HTTPException(
#         status_code=404,
#         detail=f"animal with id: {animal_id} does not exists"
#     )
#     return {"animal atualizado com sucesso!"}

# @app.delete("/api/v1/animais/{animal_id}")
# async def deleta_animal(animal_id: UUID):
#     for animal in db: 
#         if animal.id == animal_id:
#             db.remove(animal)
#             return 
#     raise HTTPException(
#         status_code = 404,
#         detail= f"animal with id {animal_id} does not exists"
#     )
#     # return {"animal removido com sucesso"}

