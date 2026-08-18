from cadastrar import *

def deletar_eletrodomestico(id):
    try:
        conn = conectar()
        cursor = conn.cursor()

        sql = 'DELETE FROM eletrodomesticos WHERE id_eletrodomestico = %s'
        valor = (id,)
        cursor.execute(sql, valor)

        conn.commit()
        print("Eletrodoméstico deletado")

        cursor.close()
        conn.close()

    except Error as e:
        conn.rollback()
        cursor.close()
        conn.close()
        return f"Erro {e}. Eletrodoméstico não deletado."
