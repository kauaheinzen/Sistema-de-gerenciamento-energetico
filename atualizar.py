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


def atualizar_eletrodomestico(id, item_atuaizar, novo_item):
    try:
        conn = conectar()
        cursor = conn.cursor()

        sql = f'UPDATE eletrodomesticos SET {item_atuaizar} = %s WHERE id_eletronico = %s'
        valores = (novo_item, id)
        cursor.execute(sql, valores)

        conn.commit()
        print("Eletrodoméstico atualizado")

        cursor.close()
        conn.close()

    except Error as e:
        conn.rollback()
        cursor.close()
        conn.close()
        print(f"Erro {e}. Atualização cancelada.")