import os
from pathlib import Path
from openai import OpenAI

# Pega a pasta onde está este script .py
pasta = Path(__file__).parent.resolve()

chave_encontrada = None

# Procura qualquer arquivo na pasta que comece com .env (ex: .env, .env.txt)
for arquivo in pasta.iterdir():
    if arquivo.name.startswith(".env"):
        print(f"📄 Arquivo encontrado: '{arquivo.name}'")
        
        # Lê o conteúdo do arquivo linha por linha
        try:
            texto = arquivo.read_text(encoding="utf-8")
        except Exception:
            texto = arquivo.read_text(encoding="utf-16")

        for linha in texto.splitlines():
            linha = linha.strip()
            if linha.startswith("OPENAI_API_KEY="):
                chave_encontrada = linha.split("=", 1)[1].strip()
                # Remove aspas se você tiver colocado sem querer
                chave_encontrada = chave_encontrada.strip("'\"")

if not chave_encontrada:
    print("❌ AINDA NÃO LEU: O arquivo existe, mas a linha OPENAI_API_KEY=sk-... não foi lida corretamente.")
else:
    print(f"✅ CHAVE ENCONTRADA COM SUCESSO! ({chave_encontrada[:8]}...)")

    # Inicializa o cliente com a chave lida manualmente
    client = OpenAI(api_key=chave_encontrada)

    resposta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Olá, funcionou?"}]
    )

    print("\n🤖 Resposta da OpenAI:")
    print(resposta.choices[0].message.content)