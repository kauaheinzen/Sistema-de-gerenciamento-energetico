from cadastrar import *
from atualizar import *
from deletar import *
from ler import *
from validações import *

import os
from dotenv import load_dotenv
from google import genai
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


app = ctk.CTk()
app.geometry("1280x720")
app.title("Sistema de Controle Energético")


frame_principal = ctk.CTkFrame(app)
frame_principal.pack(fill="both", expand=True)
frame_principal.grid_columnconfigure((0,1,2), weight=1)


def mudar_tema():
    if ctk.get_appearance_mode() == "Dark":
        ctk.set_appearance_mode("light")
    else:
        ctk.set_appearance_mode("dark")


def limpar_frame():
    for widget in frame_principal.winfo_children(): widget.destroy()


def menu_principal():
    limpar_frame()
    ctk.CTkLabel(frame_principal,text=" Sistema de Controle Energético",font=("Arial",35,"bold")).pack(pady=20)

    ctk.CTkButton(frame_principal,text="Cadastrar",width=300,height=50,fg_color=("#475569","#2563EB"), hover_color=("#334155","#1D4ED8"),command=tela_cadastrar).pack(pady=20)
    
    ctk.CTkButton(frame_principal,text="Listar",width=300,height=50,fg_color=("#475569","#2563EB"), hover_color=("#334155","#1D4ED8"),command=tela_listar).pack(pady=20)
    
    ctk.CTkButton(frame_principal,text="Atualizar",width=300,height=50,fg_color=("#475569","#2563EB"), hover_color=("#334155","#1D4ED8"),command=tela_atualizar).pack(pady=20)
    
    ctk.CTkButton(frame_principal,text="Deletar Eletrônico",width=300,height=50,fg_color=("#475569","#2563EB"), hover_color=("#334155","#1D4ED8"),command=tela_deletar).pack(pady=20)
    
    ctk.CTkButton(frame_principal,text="Prompt IA para economia de energia",width=300,height=50,fg_color=("#475569","#2563EB"), hover_color=("#334155","#1D4ED8"),command=tela_IA).pack(pady=20)
    
    
    ctk.CTkButton(frame_principal,text="☀️",width=50,command=mudar_tema).place(x=1220,y=20)


def tela_cadastrar():
    limpar_frame()
    titulo = ctk.CTkTextbox(
        frame_principal,
        width=300,
        height=40,
        activate_scrollbars=False,
        fg_color="transparent",
        border_width=0,
        font=("Arial", 20, "bold")
    )
    titulo.grid(row=0, column=1, padx=10, pady=(20, 10), sticky="n")
    titulo.insert("1.0", "O que você deseja cadastrar?")
    
    titulo.tag_config("destaque", foreground="blue")

    titulo.tag_add("destaque", "1.18", "1.27")

    titulo.configure(state="disabled")



    ctk.CTkButton(frame_principal,text="←",width=50,height=30,command=menu_principal).place(x=20,y=20)
    ctk.CTkButton(frame_principal,text="☀️",width=50,command=mudar_tema).place(x=1220,y=20)

    def tela_cadastrar_familia():
        limpar_frame()
        ctk.CTkLabel(frame_principal,text="Cadastrar Família",font=("Arial",25,"bold")).pack(pady=20)
        ctk.CTkButton(frame_principal,text="←",width=50,height=30,command=tela_cadastrar).place(x=20,y=20)
        ctk.CTkButton(frame_principal,text="☀️",width=50,command=mudar_tema).place(x=1220,y=20)

        try:
            entrar_pessoas = ctk.CTkEntry(frame_principal,placeholder_text="Número de Pessoas da Família",width=300, height=30); entrar_pessoas.pack(pady=10)
            ctk.CTkButton(frame_principal,text="Cadastrar",width=300,height=50,fg_color=("#475569","#2563EB"), hover_color=("#334155","#1D4ED8"),command=lambda: cadastra(entrar_pessoas)).pack(pady=10)
            def cadastra(pessoa):
                valida_pessoas = validar_pessoas(pessoa.get())

                if valida_pessoas[0]:
                    cadastrar_familia(valida_pessoas[1])
                    ctk.CTkLabel(frame_principal,text="Família cadastrada com sucesso!",text_color="green", font=("arial", 30, "bold")).pack(pady=20)
                    app.after(1500, tela_cadastrar)
                else:
                    ctk.CTkLabel(frame_principal,text=valida_pessoas[1],text_color="red", font=("arial", 30, "bold")).pack(pady=20)
                    app.after(1500, tela_cadastrar)
        except:
            ctk.CTkLabel(frame_principal,text="Erro ao cadastrar família, verifique se digitou um valor válido",text_color="red", font=("arial", 30, "bold")).pack(pady=20)
            app.after(1500, tela_cadastrar)
    
    def tela_cadastrar_eletrodomestico():
        limpar_frame()
        ctk.CTkLabel(frame_principal,text="Cadastrar Eletrodoméstico",font=("Arial",25,"bold")).pack(pady=20)
        ctk.CTkButton(frame_principal,text="←",width=50,height=30,command=tela_cadastrar).place(x=20,y=20)
        ctk.CTkButton(frame_principal,text="☀️",width=50,command=mudar_tema).place(x=1220,y=20)

        try:
            entrar_nome = ctk.CTkEntry(frame_principal,placeholder_text="Nome do Eletrodoméstico",width=300, height=30); entrar_nome.pack(pady=10)
            entrar_consumo = ctk.CTkEntry(frame_principal,placeholder_text="Consumo do Eletrodoméstico (Wh)",width=300, height=30); entrar_consumo.pack(pady=10)
            entrar_horas = ctk.CTkEntry(frame_principal,placeholder_text="Horas Diárias de Uso",width=300, height=30); entrar_horas.pack(pady=10)
            entrar_id = ctk.CTkEntry(frame_principal,placeholder_text="Digite o ID da Família",width=300, height=30); entrar_id.pack(pady=10)
            ctk.CTkButton(frame_principal,text="Cadastrar",width=300,height=50,fg_color=("#475569","#2563EB"), hover_color=("#334155","#1D4ED8"),command=lambda: cadastra(entrar_nome, entrar_consumo, entrar_horas, entrar_id)).pack(pady=10)
            def cadastra(nome, consumo, horas, id_familia):
                valida_nome = validar_nome(entrar_nome.get())
                valida_consumo = validar_consumo(entrar_consumo.get())
                valida_horas = validar_horas(entrar_horas.get())
                valida_familia = validar_familia(entrar_id.get())

                if valida_nome[0] and valida_consumo[0] and valida_horas[0] and valida_familia[0]:
                    cadastrar_eletrodomestico(valida_familia[1], valida_nome[1],valida_consumo[1],valida_horas[1])
                    ctk.CTkLabel(frame_principal,text="Eletrodoméstico cadastrado com sucesso!",text_color="green", font=("arial", 30, "bold")).pack(pady=40)
                    app.update()
                    app.after(1500, tela_cadastrar)
                else:
                    ctk.CTkLabel(frame_principal,text="Erro ao cadastrar eletrodoméstico, verifique se digitou valores válidos",text_color="red", font=("arial", 30, "bold")).pack(pady=40)
                    app.update()
                    app.after(1500, tela_cadastrar)
        
        except:
            ctk.CTkLabel(frame_principal,text="Erro ao cadastrar eletrodoméstico, verifique se digitou valores válidos",text_color="red", font=("arial", 30, "bold")).pack(pady=40)
            app.update()
            app.after(1500, tela_cadastrar)

    ctk.CTkButton(frame_principal,text="Cadastrar Família",width=300,height=50,fg_color=("#475569","#2563EB"), hover_color=("#334155","#1D4ED8"),command=tela_cadastrar_familia).grid(row=1, column=1, padx=10, pady=(40, 20), sticky="n")
    ctk.CTkButton(frame_principal,text="Cadastrar Eletrodoméstico",width=300,height=50,fg_color=("#475569","#2563EB"), hover_color=("#334155","#1D4ED8"),command=tela_cadastrar_eletrodomestico).grid(row=2, column=1, padx=10, pady=(40, 20), sticky="n")

def tela_listar():
    limpar_frame()
    def ler_opcao_1():
        saida.delete("1.0", "end")
        familias = ler_familias()
        for familia in familias:
            saida.insert("end", f"ID: {familia[0]} | Número de pessoas: {familia[1]} | Consumo Total: {familia[2]}\n")

    def ler_opcao_2():
        saida.delete("1.0", "end")
        familia = campo_id.get().strip()

        if not familia:
            saida.insert("end", "Opção inválida!\n")
            return

        valida_familia = validar_familia(familia)
        eletrodomesticos = ler_eletrodomesticos(valida_familia[1])
        for eletrodomestico in eletrodomesticos:
            saida.insert("end", f"ID: {eletrodomestico[0]} | Nome: {eletrodomestico[1]} | Consumo: {eletrodomestico[2]} Wh | Horas diárias: {eletrodomestico[3]}h\n")

    titulo = ctk.CTkTextbox(
        frame_principal,
        width=300,
        height=40,
        activate_scrollbars=False,
        fg_color="transparent",
        border_width=0,
        font=("Arial", 20, "bold")
    )

    titulo.pack(pady=20)
    titulo.insert("1.0", "      O que você deseja ler?")
    
    titulo.tag_config("destaque", foreground="blue")

    titulo.tag_add("destaque", "1.24", "1.27")

    titulo.configure(state="disabled")


    campo_id = ctk.CTkEntry(frame_principal, placeholder_text="Digite o ID da família caso queira ver os eletrodomésticos", width=365, height=30); campo_id.pack(pady=10)
    saida = ctk.CTkTextbox(frame_principal, width=450, height=300); saida.pack(pady=20)

    ctk.CTkButton(frame_principal, text="Ler Famílias",width=300,height=50, command=ler_opcao_1).pack(pady=20)
    ctk.CTkButton(frame_principal, text="Ler Eletrodomésticos",width=300,height=50, command=ler_opcao_2).pack(pady=20)
    
    ctk.CTkButton(frame_principal,text="←",width=50,height=30,command=menu_principal).place(x=20,y=20)
    ctk.CTkButton(frame_principal,text="☀️",width=50,command=mudar_tema).place(x=1220,y=20)


def tela_atualizar():
    limpar_frame()

    ctk.CTkLabel(frame_principal, text="O que você deseja atualizar?", font=("Arial", 20, "bold")).pack(pady=20)
    ctk.CTkButton(frame_principal, text="←", width=50, height=30, command=menu_principal).place(x=20, y=20)
    ctk.CTkButton(frame_principal, text="☀️", width=50, command=mudar_tema).place(x=1220, y=20)

    def preparar_sub_tela(titulo):
        limpar_frame()
        ctk.CTkLabel(frame_principal, text=titulo, font=("Arial", 25, "bold")).pack(pady=40)
        ctk.CTkButton(frame_principal, text="←", width=50, height=30, command=tela_atualizar).place(x=20, y=20)
        ctk.CTkButton(frame_principal, text="☀️", width=50, command=mudar_tema).place(x=1220, y=20)

    def tela_atualizar_familia():
        preparar_sub_tela("Atualizar Família")
        entrar_id = ctk.CTkEntry(frame_principal, placeholder_text="ID da Família", width=300, height=30)
        entrar_id.pack(pady=10)
        entrar_pessoas = ctk.CTkEntry(frame_principal, placeholder_text="Nova Quantidade de Pessoas", width=300, height=30)
        entrar_pessoas.pack(pady=10)

        def salvar_familia():
            valida_familia = validar_familia(entrar_id.get())
            valida_pessoas = validar_pessoas(entrar_pessoas.get())
            
            if valida_familia[0] and valida_pessoas[0]:
                atualizar_familia(valida_pessoas[1], valida_familia[1])
                mensagem, cor_texto = "Família atualizada com sucesso!", "green"
            else:
                mensagem_erro = valida_familia[1] if not valida_familia[0] else valida_pessoas[1]
                mensagem, cor_texto = f"Erro: {mensagem_erro}", "red"
            
            ctk.CTkLabel(frame_principal, text=mensagem, text_color=cor_texto, font=("Arial", 20, "bold")).pack(pady=20)
            app.after(1500, tela_atualizar)

        ctk.CTkButton(frame_principal, text="Atualizar", width=300, height=40, command=salvar_familia).pack(pady=20)

    def tela_atualizar_eletrodomestico():
        preparar_sub_tela("Atualizar Eletrodoméstico")
        entrar_id = ctk.CTkEntry(frame_principal, placeholder_text="ID do Eletrodoméstico", width=300, height=30)
        entrar_id.pack(pady=10)
        combo_opcoes = ctk.CTkOptionMenu(frame_principal, values=["Nome", "Consumo (Wh)", "Horas/Dia"], width=300, height=30,fg_color="#343638",button_color="#050505",button_hover_color="#565B5E", text_color="#DCE4EE").pack(pady=20)
        entrar_valor = ctk.CTkEntry(frame_principal, placeholder_text="Novo Valor", width=300, height=30).pack(pady=20)

        def salvar_eletrodomestico():
            valida_eletrodomestico = validar_eletronico(entrar_id.get())
            if not valida_eletrodomestico[0]:
                ctk.CTkLabel(frame_principal, text=f"Erro: {valida_eletrodomestico[1]}", text_color="red", font=("Arial", 20, "bold")).pack(pady=20)
                app.after(1500, tela_atualizar)
                return

            opcao_selecionada = combo_opcoes.get()
            novo_valor = entrar_valor.get()
            
            if opcao_selecionada == "Nome": 
                valida_campo, nome_coluna = validar_nome(novo_valor), "nome_eletronico"
            elif opcao_selecionada == "Consumo (Wh)": 
                valida_campo, nome_coluna = validar_consumo(novo_valor), "consumo"
            else: 
                valida_campo, nome_coluna = validar_horas(novo_valor), "horas_diarias"

            if valida_campo[0]:
                atualizar_eletrodomestico(valida_eletrodomestico[1], nome_coluna, valida_campo[1])
                mensagem, cor_texto = "Eletrodoméstico atualizado com sucesso!", "green"
            else:
                mensagem, cor_texto = f"Erro: {valida_campo[1]}", "red"
            
            ctk.CTkLabel(frame_principal, text=mensagem, text_color=cor_texto, font=("Arial", 20, "bold")).pack(pady=20)
            app.after(1500, tela_atualizar)

        ctk.CTkButton(frame_principal, text="Atualizar", width=300, height=40, command=salvar_eletrodomestico).pack(pady=20)

    ctk.CTkButton(frame_principal, text="Atualizar Família", width=300, height=50, command=tela_atualizar_familia).pack(pady=15)
    ctk.CTkButton(frame_principal, text="Atualizar Eletrodoméstico", width=300, height=50, command=tela_atualizar_eletrodomestico).pack(pady=15)



def tela_IA():
    def gerar_dicas(id):
        try:
            valida_id = validar_familia(id.get())
            if valida_id[0]:
                eletronicos = []

                casa = ler_casa(valida_id[1])
                consumo_mensal = ler_consumo_total(valida_id[1])

                for eletrodomestico in casa[1]:
                    eletronicos.append(eletrodomestico)

                ctk.CTkLabel(frame_principal,text="Enviando prompt... A Inteligência Artificial dará cerca de dez dicas e tabelas",font=("Arial",16)).pack(pady=10)
                ctk.CTkLabel(frame_principal, text="de antes e depois com a estimativa de consumo ao realizar as melhorias.",font=("Arial",16)).pack(padx=10,pady=2)
                ctk.CTkLabel(frame_principal,text="Isso pode levar alguns segundos... Por favor, não clique em nenhum botão", text_color="blue", font=("Arial",16)).pack(pady=10)
                
                app.update()
                load_dotenv()
                client = genai.Client()

                response = client.models.generate_content(
                    model="gemini-3.6-flash",
                    contents=f"Crie 10 soluções curtas para o problema de consumo excessivo de energia elétrica em uma residência, considerando que a família possui {casa[0][1]} integrantes e possui os seguintes eletrodomésticos com os respectivos parâmetros sendo eles: nome, consumo em Wh e horas utilizadas por dia, segue a lista de eletrônicos: {eletronicos}. O consumo total mensal é de {consumo_mensal[0]}W. Após as análises e dicas, faça uma tabela de antes e depois, sendo antes em cima e depois em baixo, com os eletrodomésticos, consumo em Wh, horas utilizadas por dia e o consumo total mensal de cada um deles após a aplicação dessas mudanças.",
                )
                
                saida.delete("1.0", "end")
                saida.insert("end", response.text)
        except:
            None

    limpar_frame()
    ctk.CTkLabel(frame_principal,text="Prompt IA para economia de energia",font=("Arial",25,"bold")).pack(pady=40)
    ctk.CTkButton(frame_principal,text="←",width=50,height=30,command=menu_principal).place(x=20,y=20)
    ctk.CTkButton(frame_principal,text="☀️",width=50,command=mudar_tema).place(x=1220,y=20)

    entrar_id = ctk.CTkEntry(frame_principal,placeholder_text="Digite o ID da Família que a Inteligência Artificial analisará",width=360, height=30); entrar_id.pack(pady=20)
    saida = ctk.CTkTextbox(frame_principal, width=550, height=300); saida.pack(pady=20) 

    ctk.CTkButton(frame_principal,text="Gerar Dicas",width=300,height=50,fg_color=("#475569","#2563EB"), hover_color=("#334155","#1D4ED8"),command=lambda: gerar_dicas(entrar_id)).pack(pady=10)
    
def tela_deletar():
    global saida
    def listar_eletrodomesticos(id):
        try:
            saida.delete("1.0", "end")
            print(id.get())
            valida_id = validar_familia(id.get())
            if valida_id[0]:
                eletrodomesticos = ler_eletrodomesticos(valida_id[1])
                saida.delete("1.0", "end")
                saida.insert("end", "Eletrodomésticos da família:\n")
                for eletrodomestico in eletrodomesticos:
                    saida.insert("end", f"ID: {eletrodomestico[0]} | Nome: {eletrodomestico[1]} | Consumo: {eletrodomestico[2]} Wh | Horas diárias: {eletrodomestico[3]}h\n")
            else:
                saida.insert("end", f"Erro: {valida_id[1]}\n")
                app.update()
        except:
            saida.insert("end", "Erro ao listar eletrodomésticos. Verifique se o ID da família é válido.\n", text_color="red")

    
    def preparar_sub_tela(titulo):
        limpar_frame()
        ctk.CTkLabel(frame_principal, text=titulo, font=("Arial", 25, "bold")).pack(pady=20)
        ctk.CTkButton(frame_principal, text="←", width=50, height=30, command=menu_principal).place(x=20, y=20)
        ctk.CTkButton(frame_principal, text="☀️", width=50, command=mudar_tema).place(x=1220, y=20)

    def tela_deletar_eletrodomestico():
        global saida
        preparar_sub_tela("Deletar Eletrodoméstico")

        entrar_id_familia = ctk.CTkEntry(frame_principal, placeholder_text="Digite o ID da família que possui o eletrodoméstico que você deseja deletar", width=460, height=30)
        entrar_id_familia.pack(pady=20)

        saida = ctk.CTkTextbox(frame_principal, width=450, height=300)
        saida.pack(pady=10)

        ctk.CTkButton(frame_principal, text="Listar Eletrodomésticos", width=300, height=50, command=lambda: listar_eletrodomesticos(entrar_id_familia)).pack(pady=20)

        entrar_id = ctk.CTkEntry(frame_principal, placeholder_text="ID do Eletrodoméstico", width=300, height=30)
        entrar_id.pack(pady=10)

        def salvar_delecao():
            valida_eletrodomestico = validar_eletronico(entrar_id.get())
            
            if valida_eletrodomestico[0]:
                deletar_eletrodomestico(valida_eletrodomestico[1])
                mensagem, cor_texto = "Eletrodoméstico deletado com sucesso!", "green"
            else:
                mensagem, cor_texto = f"Erro: {valida_eletrodomestico[1]}", "red"
            
            ctk.CTkLabel(frame_principal, text=mensagem, text_color=cor_texto, font=("Arial", 20, "bold")).pack(pady=20)
            app.after(1500, tela_deletar)


        ctk.CTkButton(
            frame_principal, 
            text="Deletar", 
            width=300, 
            height=40, 
            fg_color="#C62828", 
            hover_color="#B71C1C", 
            command=salvar_delecao
        ).pack(pady=10)

    tela_deletar_eletrodomestico()

menu_principal()
app.mainloop()
