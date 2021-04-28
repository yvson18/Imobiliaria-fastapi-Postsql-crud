from fastapi import FastAPI, HTTPException
from Modelos import Imobiliaria,Imobiliaria_User_Entry,Imovel_Delete,Imovel_Update
from PgDb import database,users
import uuid
import datetime


app = FastAPI()

#-------------------------------on_vent faz uma func rodar antes da app iniciar, porem n sei a utilidade aqui ---------------------------------------

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

#----------------------------------------------------------------------------------------------------------------------------------------------------

@app.get("/imoveis")
async def read_item():
    query = users.select()
    return await database.fetch_all(query)


@app.get("/imoveis/{user_ID}",response_model=Imobiliaria)
async def busca_imovel_pelo_id(imovel_id:str):
    query = users.select().where(users.c.imovel_id == imovel_id)
    return await database.fetch_one(query)


@app.post("/imovel-insert",response_model = Imobiliaria)
async def inserir_imovel(imovel: Imobiliaria_User_Entry):
    gID = str(uuid.uuid1())
    gDate = str(datetime.datetime.now())
    query = users.insert().values(
        imovel_id = gID,
        create_at = gDate,
        endereco  = imovel.endereco.dict(),
        anuncio = imovel.anuncio,
        area_construida = imovel.area_construida,
        num_de_quartos = imovel.num_de_quartos
    )

    await database.execute(query)

    return {
        "imovel_id":gID,
        "create_at": gDate,
        **imovel.dict()
    }


@app.put("/imoveis-update")
async def update_imoveis(imovel: Imovel_Update):
    gDate = str(datetime.datetime.now())
    query = users.update().\
        where(users.c.imovel_id == imovel.imovel_id).\
            values(
                endereco = imovel.endereco.dict(),
                anuncio = imovel.anuncio,
                area_construida = imovel.area_construida,
                num_de_quartos = imovel.num_de_quartos, 
            )
    await database.execute(query)
    return await busca_imovel_pelo_id(imovel.imovel_id)


@app.delete("/imoveis/{imovelId}",tags=["Imoveis"])
async def delete_imovel(imovel:Imovel_Delete):
    query = users.delete().where(users.c.imovel_id == imovel.imovel_id)
    await database.execute(query)

    return {
        "status" : True,
        "message": "Esse imovel foi deletado com sucesso." 
    }
