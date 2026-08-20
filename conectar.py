import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        conexao = mysql.connector.connect(
                host = '127.0.0.1',
                user = 'root',
                password = 'Senac2026',
                database = 'sistema_controle_energetico'
        )
        return conexao
    except Error as e:
        print(f"Erro ao conectar no MySQL: {e}.")
        return None