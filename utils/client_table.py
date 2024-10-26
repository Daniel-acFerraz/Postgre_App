from backend.database import db_interface
import psycopg2


def create_table():

    if not db_interface.myInterface.check_db_connection():
        return {"error": "Sem conexão com banco de dados"}
    try:
        with  db_interface.myInterface.db_connection.cursor() as cursor:
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
            db_interface.myInterface.db_connection.commit()
            return {"message": "Tabela criada com sucesso!"}
    except psycopg2.DatabaseError as e:
        print(f"Erro ao criar tabela: {repr(e)}")
        return {"error": "Falha ao criar tabela"}    
    finally:
        db_interface.myInterface.db_connection.close()  # Fecha a conexão ao final


create_table()