## IMPORTS

from tkinter import *
import os
import webbrowser


def janela_about():
    about_app = Tk()
    about_app.title ("Clezer - miniERP")
    about_app.geometry ("1080x720")
    about_app.configure(background="#dde")

    def abrir_github():
        webbrowser.open("https://github.com/ClezerSimoes")

    def cursor_ao_passar(event):
        gh_page2.config(cursor="hand2")

    def cursor_normal(event):
        gh_page2.config(cursor="")

    texto = """
    Sobre o Clezer - miniERP

    Este software está sendo desenvolvido com o objetivo de aprender e aprimorar minhas 
    habilidades em Git, Python, Tkinter e SQLite. Trata-se de um gerenciador simples de pedidos 
    de vendas e cadastro de clientes.

    Além disso, também pretendo utilizá-lo em um dos programas de extensão da faculdade.

    Vale ressaltar que este é o primeiro software que desenvolvo sozinho e, certamente, 
    há maneiras mais eficientes de escrever o código. Estou trabalhando dentro das minhas 
    capacidades atuais, mas planejo continuar aprimorando o projeto.

    Sugestões de melhoria são sempre bem-vindas!
    """
    # Label(fr_atualizar1, text="Nome", background="#dde", foreground="#009", anchor=W).place(x=5, y=25, width=100, height=20)
    print(texto)

    sobre= Label (about_app, text=texto, background="#dde", font=("Arial", 12))
    sobre.pack()

    gh_page1= Label (about_app, text="link para minha page no Github:", background="#dde", font=("Arial", 12))
    gh_page1.place(x=330, y=271)

    gh_page2= Label (about_app, text="github.com/ClezerSimoes", background="#dde", fg="blue", font=("Arial", 12))
    gh_page2.place(x=560, y=271)

    gh_page2.bind("<Button-1>", lambda e: abrir_github())
    gh_page2.bind("<Enter>", cursor_ao_passar)
    gh_page2.bind("<Leave>", cursor_normal)

    about_app.mainloop()