# Sistema de gerenciamento energetico
Trabalho de escola feito por 3 alunos do primeiro ano do ensino médio + técnico SENAC
## Autores
 
- Filipe Rocha
- Kauã Heinzen
- Caio Adada
 
---

# Descrição
Nós criamos um sistema inteligente para monitorar, controlar e otimizar o consumo de energia, ajudando a reduzir gastos, evitar desperdícios e promover o uso mais eficiente e sustentável dos recursos energéticos.

# Manual de Instalação e Execução do Sistema de gerenciamento energetico

Olá! Neste guia será mostrado como instalar e executar o Sistema Escolar.

## Passo a passo

**1.** Instale o Visual Studio Code (VS Code), caso ainda não tenha:
https://code.visualstudio.com/

**2.** Instale o Python:
https://www.python.org/downloads/

**3.** Abra o VS Code, vá até a aba **Extensões** e instale a extensão **Python**.

**4.** Abra o terminal do VS Code utilizando Ctrl + J e execute os seguintes comandos:

```bash
pip install -r .\requirements.txt
```

**5.** Abra o MySQL Workbench e copie o código presente no arquivo **codigo.sql**, colando-o na área de consultas.

Caso ainda não tenha o MySQL Workbench instalado, faça o download em:
https://www.mysql.com/products/workbench/

**Importante:** defina a senha do usuário **root** como **Senac2026**. Caso prefira utilizar outra senha, altere o valor da variável **Password** no arquivo **conectar.py** para a senha escolhida.

**6.** No MySQL Workbench, clique no botão de **Executar** (ícone de raio) para criar o banco de dados e as tabelas.


**Importante:** Coloque sua API KEY da Gemini no arquivo **.env.example** no local indicado e o renomeie para ".env". Caso não tenha uma API KEY da Gemini, crie uma em: https://aistudio.google.com/api-keys , clicando no botão "Criar chave API" no canto superior direito, e se cadastre no site.

**7.** Para iniciar o sistema, execute no terminal do VS Code:

```bash
python interface.py
```

Ou simplesmente clique no botão **Run Python** do VS Code.

Pronto! O Sistema de gerenciamento energetico estará em funcionamento.
