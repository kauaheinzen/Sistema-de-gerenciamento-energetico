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


def ler_eletrodomesticos(id_familia):
    try:
        conn = conectar()
        cursor = conn.cursor()

        sql = 'SELECT * FROM eletrodomesticos WHERE fk_id_familia = %s'
        cursor.execute(sql, (id_familia,))

        resultados = cursor.fetchall()
        return resultados

    except Error as e:
        conn.rollback()
        return f"Erro {e} ao procurar eletrodomésticos."
    
    finally:
        cursor.close()
        conn.close()


def ler_consumo_total(familia):
    try:
        conn = conectar()
        cursor = conn.cursor()

        sql = 'SELECT consumo_total FROM familia WHERE id_familia = %s'
        cursor.execute(sql, (familia,))

        resultado = cursor.fetchone()
        return resultado

    except Error as e:
        conn.rollback()
        return f"Erro {e} ao procurar o consumo total da família."
    
    finally:
        cursor.close()
        conn.close()


def ler_casa(id_familia):
    try:
        conn = conectar()
        cursor = conn.cursor()

        sql = 'SELECT * FROM familia WHERE id_familia = %s'
        cursor.execute(sql, (id_familia,))

        resultado_familia = cursor.fetchone()

        sql = 'SELECT nome_eletronico, consumo, horas_diarias FROM eletrodomesticos WHERE fk_id_familia = %s'
        cursor.execute(sql, (id_familia,))

        resultado_eletrodomesticos = cursor.fetchall()

        return resultado_familia, resultado_eletrodomesticos

    except Error as e:
        conn.rollback()
        return f"Erro {e} ao procurar a casa."
    
    finally:
        cursor.close()
        conn.close()