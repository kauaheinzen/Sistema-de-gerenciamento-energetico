from cadastrar import *

def atualizar_familia(pessoas, id):
    try:
        conn = conectar()
        cursor = conn.cursor()

        sql = 'UPDATE familia SET pessoas = %s WHERE id_familia = %s'
        cursor.execute(sql, (pessoas, id))

        conn.commit()
        print("Família atualizada")

        cursor.close()
        conn.close()
        
    except Error as e:
        conn.rollback()
        cursor.close()
        conn.close()
        return f"Erro {e}. Atualização cancelada."


def atualizar_eletrodomestico(familia, item_atuaizar, novo_item):
    try:
        conn = conectar()
        cursor = conn.cursor()

        sql = 'UPDATE eletrodomesticos SET %s = %s WHERE fk_id_familia = %s'
        valores = (item_atuaizar, novo_item, familia)
        cursor.execute(sql, valores)

        conn.commit()
        print("Eletrodoméstico atualizado")

        cursor.close()
        conn.close()

    except Error as e:
        conn.rollback()
        cursor.close()
        conn.close()
        return f"Erro {e}. Atualização cancelada."