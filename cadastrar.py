from conectar import *

def cadastrar_familia(pessoas):
    try:
        conn = conectar()
        cursor = conn.cursor()

        sql = 'INSERT INTO familia (pessoas) VALUES (%s)'
        cursor.execute(sql, (pessoas,))

        conn.commit()
        print("Família cadastrada")

        cursor.close()
        conn.close()
        
    except Error as e:
        conn.rollback()
        cursor.close()
        conn.close()
        return f"Erro {e}. Cadastro cancelado."


def cadastrar_eletrodomestico(familia, nome, consumo, horas):
    try:
        conn = conectar()
        cursor = conn.cursor()

        sql = 'INSERT INTO eletrodomesticos (nome_eletronico, consumo, horas_diarias, fk_id_familia) VALUES (%s, %s, %s, %s)'
        valores = (nome, consumo, horas, familia)
        cursor.execute(sql, valores)

        conn.commit()
        print("Eletrodoméstico cadastrado")

        cursor.close()
        conn.close()

    except Error as e:
        conn.rollback()
        cursor.close()
        conn.close()
        print(f"Erro {e}. Cadastro cancelado.")