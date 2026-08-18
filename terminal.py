def menu():
    while True:  
        print("\n--- MENU PRINCIPAL ---")
        print("1 - Cadastrar")
        print("2 - Deletar")
        print("3 - Atualizar")
        print("4 - Visualizar (Ler)")
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
                    ...
                elif opcao_cadastro == "2":
                    ...
                elif opcao_cadastro == "0":
                    continue
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
                    ...
                elif opcao_cadastro == "2":
                    ...
                elif opcao_cadastro == "0":
                    continue
                else:
                    print("\033[31mOpção inválida!\033[m")
        

        elif opcao == "3":
            ...

       
        elif opcao == "4":
            while True:
                print("\nO que você deseja \033[32mler\033[m?")
                print("1 - Ler Família")
                print("2 - Ler Eletrodoméstico")
                print("0 - Voltar ao início")

                opcao_ler = input("Escolha uma opção: ").strip()

                if opcao_ler == "1":
                    ...
                elif opcao_ler == "2":
                    ...
                elif opcao_ler == "0":
                    continue
                else:
                    print("\033[31mOpção inválida!\033[m")
                    continue

        
        else:
            print("\033[31mOpção inválida!\033[m Escolha entre \033[33m0\033[m, \033[33m1\033[m, \033[33m2\033[m ou \033[33m3\033[m.")


menu()