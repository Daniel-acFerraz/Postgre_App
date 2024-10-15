import pandas as pd
import psycopg2
from fastapi import FastAPI
from models import Client

app = FastAPI()

db_connection = None

#REALIZAR CONEXÃO COM O DB
def connect_to_db():
    global db_connection
    host = "localhost"
    dbname="fakeapp"
    user="postgres" #usuario digitado pelo usuario
    password="Postx89f7+" #password digitado pelo usuario
    port="5432"
    try:
        db_connection = psycopg2.connect(host=f"{host}", dbname=f"{dbname}", user=f"{user}", password=f"{password}", port=f"{port}")
        print(f"Conexão com banco de dados bem sucedida: {db_connection}")
        return db_connection
    except(Exception, psycopg2.DatabaseError, psycopg2.OperationalError) as e:
        print(repr(e))
        if "senha falhou" in repr(e):
            db_connection = None
            print("Usuário ou senha incorretos")
            return {"error": "Usuário ou senha incorretos"}
        else:
            db_connection = None
            print("Falha no login, verifique sua conexão e tente novamente")
            return {"error": "Falha no login"}
    except Exception as e:
        db_connection = None
        print(f"Erro inesperado: {repr(e)}")
        return {"error": "Erro inesperado ao tentar se conectar ao banco"}

#CHECAR CONEXÃO COM DB   
def check_db_connection():
    global db_connection
    if db_connection is None or db_connection.closed !=0:
        print("Sem conexão com o banco de dados, tentando reestabelecer...")
        connect_to_db()
        if db_connection is None or db_connection.closed !=0:
            print("Falha ao restabelecer a conexão")
            return False
    print("Conectado!")
    return True

#CRIAR TABELA CLIENTES
@app.post('/create_table')
def create_table():
    if not check_db_connection():
        return {"error": "Sem conexão com banco de dados"}
    try:
        with  db_connection.cursor() as cursor:
            create_table_query = """
            CREATE TABLE IF NOT EXISTS clients (
                id SERIAL PRIMARY KEY,
                cpf VARCHAR(11) UNIQUE NOT NULL,
                name VARCHAR(100) NOT NULL,
                dt_nascimento DATE NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                telefone VARCHAR(15),
                estado CHAR(2) NOT NULL,
                cidade VARCHAR(100) NOT NULL,
                rua VARCHAR(100) NOT NULL,
                numero VARCHAR(10) NOT NULL,
                complemento VARCHAR(50)
            )
            """
            cursor.execute(create_table_query)
            db_connection.commit()
            return {"message": "Tabela criada com sucesso!"}
    except psycopg2.DatabaseError as e:
        print(f"Erro ao criar tabela: {repr(e)}")
        return {"error": "Falha ao criar tabela"}

CADASTRAR CLIENTES    
@app.post('/cadastrar_cliente')
def register_client(cpf: str, name: str, dt_nascimento: date, email: str, telefone: str, estado: str, cidade: str, rua:str, numero:str, complemento: str):
    if not check_db_connection():
        return {"error": "Sem conexão com banco de dados"}
    try:
        with db_connection.cursor() as cursor:
            client_registration = """INSERT 

            """
#     except 

                
    
    

connect_to_db()
create_table()

