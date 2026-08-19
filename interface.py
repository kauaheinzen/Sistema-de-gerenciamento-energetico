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
    
    ctk.CTkButton(frame_principal,text="Listar",width=300,height=50,fg_color=("#2563EB","#475569"),hover_color=("#1D4ED8","#334155"),command=tela_listar).pack(pady=20)
    
    ctk.CTkButton(frame_principal,text="Atualizar",width=300,height=50,fg_color=("#2563EB","#475569"),hover_color=("#1D4ED8","#334155"), text_color="red",command=tela_atualizar).pack(pady=20)
    
    ctk.CTkButton(frame_principal,text="Deletar",width=300,height=50,fg_color=("#2563EB","#475569"),hover_color=("#1D4ED8","#334155"),command=tela_desativar).pack(pady=20)
    
    ctk.CTkButton(frame_principal,text="Prompt IA para economia de energia",width=300,height=50,fg_color=("#2563EB","#475569"),hover_color=("#1D4ED8","#334155"),command=tela_IA).pack(pady=20)
    
    
    ctk.CTkButton(frame_principal,text="☀️",width=50,command=mudar_tema).place(x=1840,y=20)


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
    
    titulo.tag_config("destaque", foreground="yellow")

    titulo.tag_add("destaque", "1.18", "1.27")

    titulo.configure(state="disabled")



    ctk.CTkButton(frame_principal,text="←",width=50,height=30,command=menu_principal).place(x=20,y=20)
    ctk.CTkButton(frame_principal,text="☀️",width=50,command=mudar_tema).place(x=1840,y=20)

    def tela_cadastrar_familia():
        limpar_frame()
        ctk.CTkLabel(frame_principal,text="Cadastrar Família",font=("Arial",25,"bold")).pack(pady=20)
        ctk.CTkButton(frame_principal,text="←",width=50,height=30,command=tela_cadastrar).place(x=20,y=20)
        ctk.CTkButton(frame_principal,text="☀️",width=50,command=mudar_tema).place(x=1840,y=20)

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
        ctk.CTkButton(frame_principal,text="☀️",width=50,command=mudar_tema).place(x=1840,y=20)

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

    ctk.CTkLabel(app, text="O que você deseja ler?", font=("Arial", 16, "bold")).pack(pady=10)

    ctk.CTkButton(app, text="1 - Ler Famílias", command=ler_opcao_1).pack(pady=5)

    campo_id = ctk.CTkEntry(app, placeholder_text="Digite o ID da família")
    campo_id.pack(pady=5)

    ctk.CTkButton(app, text="2 - Ler Eletrodomésticos", command=ler_opcao_2).pack(pady=5)

    saida = ctk.CTkTextbox(app, width=400, height=200)
    saida.pack(pady=10)

    ctk.CTkButton(app, text="0 - Voltar ao início", fg_color="gray", command=app.destroy).pack(pady=5)




tela_cadastrar()
app.mainloop()
