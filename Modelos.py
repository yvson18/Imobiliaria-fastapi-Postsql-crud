from pydantic import BaseModel

class Endereco(BaseModel):
    rua: str = None
    cidade: str = None
    estado: str = None
    pais: str = None
    cep: str = None
    numero: str = None
    complemento: str = None

class Imobiliaria(BaseModel):
    endereco: Endereco
    anuncio: str = None
    area_construida: str = None
    num_de_quartos: str = None
    imovel_id: str
    create_at: str

class Imobiliaria_User_Entry(BaseModel):
    endereco: Endereco
    anuncio: str = None
    area_construida: str = None
    num_de_quartos: str = None

class Imovel_Delete(BaseModel):
    imovel_id: str

class Imovel_Update(BaseModel):
    imovel_id: str
    endereco: Endereco
    anuncio: str = None
    area_construida: str = None
    num_de_quartos: str = None

