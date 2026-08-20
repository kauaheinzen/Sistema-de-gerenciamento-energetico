from cadastrar import conectar
import os
from dotenv import load_dotenv
from google import genai
from google.genai.errors import APIError


def validar_ambiente():
    if not os.path.exists(".env"):
        return False, "Arquivo .env não encontrado no diretório do projeto."

    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key or api_key.strip() == "":
        return False, "A chave GEMINI_API_KEY não foi encontrada dentro do .env."

    try:
        client = genai.Client()
        client.models.generate_content(
            model="gemini-3.6-flash",
            contents="ping",
            config={"max_output_tokens": 1},
        )
        return True
    except APIError as e:
        return False, f"Chave de API inválida ou sem permissão: {e.message}"
    except Exception as e:
        return False, f"Erro ao conectar com a API: {str(e)}"


def validar_API_env():
    valido, mensagem = validar_ambiente()

    if not valido:
        return f"Erro de Configuração: {mensagem}"
    else:
        return False


def validar_pessoas(pessoas):
    try:
        pessoas = int(pessoas)

        if pessoas <= 0:
            return False, "A quantidade de pessoas deve ser maior do que zero"

        return True, pessoas

    except ValueError:
        return False, "A quantidade de pessoas deve ser um número inteiro"


def validar_nome(nome):
    if not nome or not nome.strip():
        return False, "O nome do eletrodoméstico não pode estar vazio"

    if len(nome.strip()) > 100:
        return False, "O nome deve possuir no máximo 100 caracteres"

    return True, nome.strip()


def validar_consumo(consumo):
    try:
        consumo = float(consumo)
        if consumo <= 0:
            return False, "O consumo deve ser maior que zero"
        return True, consumo

    except ValueError:
        return False, "O consumo deve ser um número."


def validar_horas(horas):
    try:
        horas = float(horas)
        if horas < 0:
            return False, "As horas diárias não podem ser negativas"
        if horas > 24:
            return False, "As horas diárias não podem ser maiores que 24"
        return True, horas

    except ValueError:
        return False, "As horas diárias devem ser um número."


def validar_familia(id_familia):
    try:
        id_familia = int(id_familia)
        if id_familia <= 0:
            return False, "ID da família inválido"

        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
            SELECT id_familia
            FROM familia
            WHERE id_familia = %s
        """

        cursor.execute(sql, (id_familia,))
        familia = cursor.fetchone()

        cursor.close()
        conexao.close()

        if familia is None:
            return False, "A família informada não existe"

        return True, id_familia

    except ValueError:
        return False, "O ID da família deve ser um número inteiro"
    

def validar_eletronico(id_eletronico):
    try:
        id_eletronico = int(id_eletronico)
        if id_eletronico <= 0:
            return False, "ID do eletrônico inválido"

        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
            SELECT id_eletronico
            FROM eletrodomesticos
            WHERE id_eletronico = %s
        """

        cursor.execute(sql, (id_eletronico,))
        eletronico = cursor.fetchone()

        cursor.close()
        conexao.close()

        if eletronico is None:
            return False, "O eletrônico informado não existe"

        return True, id_eletronico

    except ValueError:
        return False, "O ID do eletrônico deve ser um número inteiro"