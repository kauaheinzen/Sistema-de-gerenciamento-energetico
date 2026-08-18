from cadastrar import *

def ler_familias():
    try:
        conn = conectar()
        cursor = conn.cursor()

        sql = 'SELECT * FROM familia'
        cursor.execute(sql,)

        resultados = cursor.fetchall()
        return resultados
        
    except Error as e:
        conn.rollback()
        return f"Erro {e} ao procurar as famílias."
    
    finally:
        cursor.close()
        conn.close()


def ler_eletrodomesticos():
    try:
        conn = conectar()
        cursor = conn.cursor()

        sql = 'SELECT * FROM eletrodomesticos'
        cursor.execute(sql,)

        resultados = cursor.fetchall()
        return resultados

    except Error as e:
        conn.rollback()
        return f"Erro {e} ao procurar eletrodomésticos."
    
    finally:
        cursor.close()
        conn.close()