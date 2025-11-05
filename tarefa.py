from flask import jsonify
from conexao import get_conexao
from psycopg2.extras import RealDictCursor

def buscar_tarefas():
    #Conecta no banco de dados
    con = get_conexao()
    cursor = con.cursor(cursor_factory = RealDictCursor)
    cursor.execute(
        "SELECT id, name, description FROM todos;"
    )
    #Busca os dados e armazena na variável
    todos = cursor.fetchall()

    #Fecha as conexões
    cursor.close()
    con.close()

    return jsonify(todos)

def buscar_tarefa(id):
    #Conecta no banco de dados
    con = get_conexao()
    cursor = con.cursor(cursor_factory = RealDictCursor)
    cursor.execute(
        "SELECT id, name, description FROM todos WHERE id = %s;",
        (id,)
    )
    #Busca os dados e armazena na variável
    todo = cursor.fetchone()

    #Fecha as conexões
    cursor.close()
    con.close()

    return jsonify(todo)