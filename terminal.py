from cadastrar import *
from atualizar import *
from deletar import *
from ler import *
from validações import *
import os
from dotenv import load_dotenv
from google import genai


def menu():
    while True:  
        print("\n--- MENU PRINCIPAL ---")
        print("1 - Cadastrar")
        print("2 - Atualizar")
        print("3 - Deletar")
        print("4 - Visualizar (Ler)")
        print("5 - Prompt IA para economia de energia")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        
        if opcao == "0":
            print("Saindo do sistema... Até logo!")
            break

       
        elif opcao == "1":
            while True:
                print("\nO que você deseja \033[32mcadastrar\033[m?")
                print("1 - Cadastrar Família")
                print("2 - Cadastrar Eletrodoméstico")
                print("0 - Voltar ao início")

                opcao_cadastro = input("Escolha uma opção: ").strip()

                if opcao_cadastro == "1":
                    pessoas = input("Digite a quantidade de pessoas na família: ").strip()
                    numero = validar_pessoas(pessoas)
                    if numero[0]:
                        cadastrar_familia(numero[1])
                    else:
                        print(f"\033[31mErro: {numero[1]}\033[m")

                elif opcao_cadastro == "2":
                    nome = input("Digite o nome do eletrodoméstico: ").strip()
                    consumo = input("Digite o consumo do eletrodoméstico (em Wh): ").strip()
                    horas = input("Digite a quantidade de horas diárias de uso do eletrodoméstico: ").strip()

                    valida_nome = validar_nome(nome)
                    valida_consumo = validar_consumo(consumo)
                    valida_horas = validar_horas(horas)

                    if valida_nome[0] and valida_consumo[0] and valida_horas[0]:
                        id_familia = input("Digite o ID da família a qual o eletrodoméstico pertence: ").strip()
                        valida_familia = validar_familia(id_familia)

                        if valida_familia[0]:
                            cadastrar_eletrodomestico(valida_familia[1], valida_nome[1], valida_consumo[1], valida_horas[1])
                        else:
                            print(f"\033[31mErro: {valida_familia[1]}\033[m")
                    else:
                        if not valida_nome[0]:
                            print(f"\033[31mErro: {valida_nome[1]}\033[m")
                        if not valida_consumo[0]:
                            print(f"\033[31mErro: {valida_consumo[1]}\033[m")
                        if not valida_horas[0]:
                            print(f"\033[31mErro: {valida_horas[1]}\033[m")

                elif opcao_cadastro == "0":
                    break
                else:
                    print("\033[31mOpção inválida!\033[m")


        elif opcao == "2":
            while True:
                print("\nO que você deseja \033[32matualizar\033[m?")
                print("1 - Atualizar Família")
                print("2 - Atualizar Eletrodoméstico")
                print("0 - Voltar ao início")

                opcao_cadastro = input("Escolha uma opção: ").strip()

                if opcao_cadastro == "1":
                    print("Mostrando todas as famílias cadastradas")
                    familias = ler_familias()
                    for familia in familias:
                        print(f"ID: {familia[0]} | Número de pessoas: {familia[1]} | Consumo Total: {familia[2]}")

                    id = input("Digite o ID da família que deseja atualizar: ").strip()
                    valida_familia = validar_familia(id)

                    if valida_familia[0]:
                        pessoas = input("Digite a nova quantidade de pessoas na família: ").strip()
                        numero = validar_pessoas(pessoas)
                        if numero[0]:
                            atualizar_familia(numero[1], valida_familia[1])
                        else:
                            print(f"\033[31mErro: {numero[1]}\033[m")
                    else:
                        print(f"\033[31mErro: {valida_familia[1]}\033[m")

                elif opcao_cadastro == "2":
                    print("O que você gostaria de alterar:")
                    print(
                        """
                        1 - Nome do eletrodoméstico
                        2 - Consumo do eletrodoméstico
                        3 - Horas diárias de uso
                        0 - Voltar ao início
                        """)
                    item = input("Escolha uma opção: ").strip()

                    id_eletrodomestico = input("Digite o ID do eletrodoméstico que deseja atualizar: ").strip()
                    valida_eletronico = validar_eletronico(id_eletrodomestico)

                    if valida_eletronico[0]:
                        if item == "1":
                            nome = input("Digite o novo nome do eletrodoméstico: ").strip()
                            valida_nome = validar_nome(nome)
                            if valida_nome[0]:
                                atualizar_eletrodomestico(valida_eletronico[1], "nome_eletronico", valida_nome[1])
                            else:
                                print(f"\033[31mErro: {valida_nome[1]}\033[m")
                        
                        elif item == "2":
                            consumo = input("Digite o novo consumo do eletrodoméstico (em Wh): ").strip()
                            valida_consumo = validar_consumo(consumo)
                            if valida_consumo[0]:
                                atualizar_eletrodomestico(valida_eletronico[1], "consumo", valida_consumo[1])
                            else:
                                print(f"\033[31mErro: {valida_consumo[1]}\033[m")

                        elif item == "3":
                            horas = input("Digite a nova quantidade de horas diárias de uso: ").strip()
                            valida_horas = validar_horas(horas)
                            if valida_horas[0]:
                                atualizar_eletrodomestico(valida_eletronico[1], "horas_diarias", valida_horas[1])
                            else:
                                print(f"\033[31mErro: {valida_horas[1]}\033[m")
                        
                        elif item == "0":
                            break

                        else:
                            print("\033[31mOpção inválida!\033[m")
                    
                    else:
                        print(f"\033[31mErro: {valida_eletronico[1]}\033[m")

                elif opcao_cadastro == "0":
                    break

                else:
                    print("\033[31mOpção inválida!\033[m")
        

        elif opcao == "3":
            while True:
                print("\nConfirme se deseja \033[32mdeletar\033[m?")
                print("1 - Deletar Eletrodoméstico")
                print("0 - Cancelar e voltar ao início")

                opcao_deletar = input("Escolha uma opção: ").strip()

                if opcao_deletar == "1":
                    id_eletrodomestico = input("Digite o ID do eletrodoméstico que deseja deletar: ").strip()
                    valida_eletronico = validar_eletronico(id_eletrodomestico)
                    if valida_eletronico[0]:
                        deletar_eletrodomestico(valida_eletronico[1])
                        break
                    else:
                        print(f"\033[31mErro: {valida_eletronico[1]}\033[m")

                elif opcao_deletar == "0":
                    break

                else:
                    print("\033[31mOpção inválida!\033[m")

       
        elif opcao == "4":
            while True:
                print("\nO que você deseja \033[32mler\033[m?")
                print("1 - Ler Famílias")
                print("2 - Ler Eletrodomésticos")
                print("0 - Voltar ao início")

                opcao_ler = input("Escolha uma opção: ").strip()

                if opcao_ler == "1":
                    familias = ler_familias()
                    for familia in familias:
                        print(f"ID: {familia[0]} | Número de pessoas: {familia[1]} | Consumo Total: {familia[2]}")

                elif opcao_ler == "2":
                    familia = input("Digite o ID da família para ver seus eletrodomésticos: ").strip()
                    valida_familia = validar_familia(familia)

                    eletrodomesticos = ler_eletrodomesticos(valida_familia[1])
                    for eletrodomestico in eletrodomesticos:
                        print(f"ID: {eletrodomestico[0]} | Nome: {eletrodomestico[1]} | Consumo: {eletrodomestico[2]} Wh | Horas diárias: {eletrodomestico[3]}h")

                elif opcao_ler == "0":
                    break

                else:
                    print("\033[31mOpção inválida!\033[m")

        elif opcao == "5":
            familia = input("Digite o ID da família para a Inteligência Artificial analisar: ").strip()

            eletronicos = []

            casa = ler_casa(1)
            consumo_mensal = ler_consumo_total(1)

            for eletrodomestico in casa[1]:
                eletronicos.append(eletrodomestico)

            print("Enviando prompt... A Inteligência Artificial dará cerca de dez dicas e tabelas de antes e depois com a estimativa de consumo ao realizar as melhorias.")
            print("\033[33mAguarde alguns segundos, estamos processando...\033[m")

            try:
                load_dotenv()
                client = genai.Client()

                response = client.models.generate_content(
                    model="gemini-3.6-flash",
                    contents=f"Crie 10 soluções curtas para o problema de consumo excessivo de energia elétrica em uma residência, considerando que a família possui {casa[0][1]} integrantes e possui os seguintes eletrodomésticos com os respectivos parâmetros sendo eles: nome, consumo em Wh e horas utilizadas por dia, segue a lista de eletrônicos: {eletronicos}. O consumo total mensal é de {consumo_mensal[0]}W. Após as análises e dicas, faça uma tabela de antes e depois, sendo antes em cima e depois em baixo, com os eletrodomésticos, consumo em Wh, horas utilizadas por dia e o consumo total mensal de cada um deles após a aplicação dessas mudanças.",
                )

                print(response.text)
            except:
                load_dotenv()
                client = genai.Client()

                response = client.models.generate_content(
                    model="gemini-3.6-flash",
                    contents=f"Crie 10 soluções curtas para o problema de consumo excessivo de energia elétrica em uma residência, considerando que a família possui {casa[0][1]} integrantes e possui os seguintes eletrodomésticos com os respectivos parâmetros sendo eles: nome, consumo em Wh e horas utilizadas por dia, segue a lista de eletrônicos: {eletronicos}. O consumo total mensal é de {consumo_mensal[0]}W. Após as análises e dicas, faça uma tabela de antes e depois, sendo antes em cima e depois em baixo, com os eletrodomésticos, consumo em Wh, horas utilizadas por dia e o consumo total mensal de cada um deles após a aplicação dessas mudanças.",
                )

                print(response.text)
            
            print("Clique em qualquer tecla para continuar...")
            if os.name == 'nt':
                import msvcrt
                msvcrt.getch()
            

        else:
            print("\033[31mOpção inválida!\033[m Escolha entre \033[33m0\033[m, \033[33m1\033[m, \033[33m2\033[m ou \033[33m3\033[m.")


menu()