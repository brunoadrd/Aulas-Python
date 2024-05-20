import psycopg2
import os
from dotenv import load_dotenv
from contextlib import contextmanager

load_dotenv()

DATABASE = os.getenv('DATABASE')
HOST = os.getenv('HOST')
USERSERVER = os.getenv('USERSERVER')
PASSWORD = os.getenv('PASSWORD')
PORT = os.getenv('PORT')

@contextmanager
def instance_cursor():
    connection = psycopg2.connect(database = DATABASE, host = HOST, user = USERSERVER, password = PASSWORD, port = PORT)
    cursor = connection.cursor()
    try:
        yield cursor
    finally:
        if connection:
            cursor.close()
            connection.close()
            print('Conexão com o PostgreSQL finalizada.')

def general_query():
    with instance_cursor() as cursor:
        query = '''
            SELECT * FROM REGISTROS
        '''
        cursor.execute(query)
        request = cursor.fetchall()
        
        return request
    
def user_query(user):
    print(user)
    with instance_cursor() as cursor:
        query = '''
            SELECT nome, usuario, senha FROM REGISTROS WHERE usuario = %s
        '''
        cursor.execute(query, (user, ))
        request = cursor.fetchall()
        
        return request

def create_table():
    connection = psycopg2.connect(database = DATABASE, host = HOST, user = USERSERVER, password = PASSWORD, port = PORT)
    cursor = connection.cursor()

    query = '''
        CREATE TABLE REGISTROS (
            nome varchar(255),
            usuario varchar(50),
            senha varchar(255)
        )
    '''
    cursor.execute(query)
    connection.commit()

    print('Tabela REGISTROS criada com sucesso!')

    if connection:
            cursor.close()
            connection.close()
            print('Conexão com o PostgreSQL finalizada.')

def register_user(name, user, password):
    connection = psycopg2.connect(database = DATABASE, host = HOST, user = USERSERVER, password = PASSWORD, port = PORT)
    cursor = connection.cursor()

    query = f'''
        INSERT INTO REGISTROS VALUES {name, user, password}
    '''
    cursor.execute(query)
    connection.commit()

    print(f'Usuário {user} criado com sucesso!')

    if connection:
            cursor.close()
            connection.close()
            print('Conexão com o PostgreSQL finalizada.')