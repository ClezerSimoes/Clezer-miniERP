## IMPORTS

from tkinter import *
from tkinter import messagebox
import os
import webbrowser

## IMPORT JANELAS

import about 
import cliente_novo
import cliente_delete
import cliente_update
import pedido_novo

## MAIN APP

main_app = Tk()
main_app.title ("Clezer - miniERP")
main_app.geometry ("1080x720")
main_app.configure(background="#dde")

main_app_Dir=os.path.dirname(__file__)

## FUNÇÕES MENU

def abrir_github():
    webbrowser.open("https://github.com/ClezerSimoes")

def fun_about():
    about.janela_about()

def semcomando():
    print("Teste funcionando")

def new_client():
    cliente_novo.janela_clienteNovo()

def update_client():
    cliente_update.janela_clienteUP()

def delete_client():
    cliente_delete.janela_deleteCliente()

def new_order():
    pedido_novo.janela_pedidoNovo()
## MENU

menu_bar = Menu(main_app)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New Flie", command=semcomando)
file_menu.add_command(label="Open Flie...", command=semcomando)
file_menu.add_command(label="Backup", command=semcomando)
file_menu.add_separator()
file_menu.add_command(label="Language", command=semcomando)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=semcomando)
menu_bar.add_cascade(label="File", menu=file_menu)

clients_menu = Menu(menu_bar, tearoff=0)
clients_menu.add_command(label="New Client", command=new_client)
clients_menu.add_command(label="Client List", command=semcomando)
clients_menu.add_command(label="Update Client", command=update_client)
clients_menu.add_separator()
clients_menu.add_command(label="Delete Client", command=delete_client)
menu_bar.add_cascade(label="Clients", menu=clients_menu)

orders_menu = Menu(menu_bar, tearoff=0)
orders_menu.add_command(label="New Order", command=new_order)
orders_menu.add_command(label="Order list", command=semcomando)
orders_menu.add_command(label="Update Order", command=semcomando)
orders_menu.add_separator()
orders_menu.add_command(label="Delete Order", command=semcomando)
menu_bar.add_cascade(label="Orders", menu=orders_menu)

help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="My Github Page", command=abrir_github)
help_menu.add_command(label="About the program...", command=fun_about)
menu_bar.add_cascade(label="Help", menu=help_menu)


main_app.config(menu=menu_bar)

## FRAME 

fr_window1= Frame(main_app, borderwidth=1, relief="groove")
fr_window1.place(width=1080, height=50)
fr_window1.place(x=((1080/2)-540), y=10)

Label(fr_window1, text= "GERENCIADOR DE CLIENTES E PEDIDOS", font=("Arial", 14, "bold")).pack(expand=True)
main_app.mainloop()