from typing import Optional, List
from fastapi import FastAPI
from pydantic import BaseModel

class Endereco(BaseModel):
    rua: str = None
    cidade: str = None
    estado: str = None
    pais: str = None
    cep: str = None
    numero: int = None
    complemento: int = None

class Imobiliaria(BaseModel):
    endereco: Endereco
    anuncio: str = None
    area_construida: float = None
    num_de_quartos: int = None
    

imo1 = Imobiliaria(endereco = {'rua': 'banana',
                        'cidade': 'banana',
                        'estado': 'banana',
                        'pais': 'banana',
                        'cep': 'banana',
                        'numero': 95,},
                    anuncio = 'Casa da banana',
                    area_construida = 200,
                )

print(imo1.dict())

