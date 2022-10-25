#Human, ALive
#salva no Banco de dados
import requests
import sqlite3
from typing import List, Dict

def data_base(user:dict) -> None:
    """ Essa função tabalha com o banco de dados e persiste informações
    da função get_users()"""

    #TODO: Abrir ou criar banco
        # Criando a conexão bd/ cursor
    con = sqlite3.connect('user.db')
    cur = con.cursor()

    try:
        #criando tabela
        cur.execute('CREATE TABLE human_alive (id int, nome text);')
    except Exception:
        pass
    # inserindo
    id = user['id']
    nome = user['nome']
    cur.execute('INSERT INTO human_alive (id, nome) VALUES (?,?)',(id,nome))

    # salvar a conexão
    con.commit()
    print("Dados inseridos com sucesso")
    
    # fechando a conexão
    con.close()

def get_users() -> None:
    """Essa função coleta dados de users humanos e vivos da API Rick And Morty"""

    query = {"status": "Alive", "species": "Human"}
    # TODO: colete os dados da API com o json()
    r = requests.get('https://rickandmortyapi.com/api/character?page=1', params=query).json()
    user = dict()

    #TODO: salve os dados coletados em um banco de dados com o nome de user.db
    r = r['results']
    for item in r:
        user = {'id': item['id'], 'nome': item['name']}
        # TODO persistir os dados noo bd(user.db)
        data_base(user)


get_users()