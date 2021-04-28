import databases, sqlalchemy

usuario_posgre = "userimob"
senha = "userimob1337"
ip = "localhost" # deixa localhost para ficar nao dar ruim
porta = "5432"

DATABASE_URL = f"postgresql://{usuario_posgre}:{senha}@{ip}:{porta}/dbproimob"
database = databases.Database(DATABASE_URL) #Acho que se usa a url para fazer as devidas conexoes com o banco
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "Tabela_Imo",
    metadata,
    sqlalchemy.Column("imovel_id"   , sqlalchemy.String,primary_key= True),
    sqlalchemy.Column("create_at"   ,sqlalchemy.String),
    sqlalchemy.Column("endereco"    ,sqlalchemy.JSON),
    sqlalchemy.Column("anuncio"    ,sqlalchemy.String),
    sqlalchemy.Column("area_construida"  ,sqlalchemy.String),
    sqlalchemy.Column("num_de_quartos"   ,sqlalchemy.String),
    
)

engine = sqlalchemy.create_engine(DATABASE_URL) # The Engine is the starting point for any SQLAlchemy application.

metadata.create_all(engine)
