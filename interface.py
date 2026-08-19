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
    ctk.CTkLabel(frame_principal,text=" Sistema de Controle Energético",font=("Arial",35,"bold")).place(x=810,y=40)

    ctk.CTkButton(frame_principal,text="Cadastrar",width=300,height=50,fg_color=("#2563EB","#475569"),hover_color=("#1D4ED8","#334155"),command=tela_cadastrar).place(x=810,y=180)
    
    ctk.CTkButton(frame_principal,text="Listar",width=300,height=50,fg_color=("#2563EB","#475569"),hover_color=("#1D4ED8","#334155"),command=tela_listar).place(x=810,y=270)
    
    ctk.CTkButton(frame_principal,text="Atualizar",width=300,height=50,fg_color=("#2563EB","#475569"),hover_color=("#1D4ED8","#334155"), text_color="red",command=tela_atualizar).place(x=810,y=360)
    
    ctk.CTkButton(frame_principal,text="Deletar",width=300,height=50,fg_color=("#2563EB","#475569"),hover_color=("#1D4ED8","#334155"),command=tela_desativar).place(x=810,y=450)
    
    ctk.CTkButton(frame_principal,text="Prompt IA para economia de energia",width=300,height=50,fg_color=("#2563EB","#475569"),hover_color=("#1D4ED8","#334155"),command=tela_IA).place(x=810,y=540)
    
    
    ctk.CTkButton(frame_principal,text="☀️",width=50,command=mudar_tema).place(x=1840,y=20)


def tela_cadastrar():
    limpar_frame()
    titulo = ctk.CTkTextbox(
        app,
        width=300,
        height=40,
        activate_scrollbars=False,
        fg_color="transparent",
        border_width=0,
    )
    titulo.insert("1.0", "O que você deseja cadastrar?")
    titulo.pack(padx=20, pady=20)
    titulo.tag_config("destaque", foreground="yellow")

    titulo.tag_add("destaque", "1.18", "1.27")

    titulo.configure(state="disabled")


tela_cadastrar()
app.mainloop()