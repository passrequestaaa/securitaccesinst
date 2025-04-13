import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",     # ou o host do seu MySQL remoto
        user="seu_usuario",
        password="sua_senha",
        database="nome_do_banco"
    )