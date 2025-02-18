## IMPORTS

from tkinter import *
from tkinter import messagebox
import os
import json
import webbrowser

## IMPORT JANELAS

import about 
import files
import cliente_novo
import cliente_lista
import cliente_delete
import cliente_update
import pedido_novo
import pedido_lista
import pedido_update
import pedido_cancelar

## MAIN APP

main_app = Tk()
main_app.title ("Clezer - miniERP")
main_app.geometry ("1080x720")
main_app.configure(background="#dde")

main_app_Dir=os.path.dirname(__file__)
dt_base_name = "arquivo.db aqui"
dt_base_path= os.path.join(main_app_Dir, dt_base_name)

config_file_name= "config.json"
config_file_path= os.path.join(main_app_Dir, config_file_name)

## CONFIG VERIFICATION
def verify():
    if os.path.exists(config_file_path):
        return
    else:
        files.file_config_verify(main_app, config_file_path)


## ABOUT MENU FUNCTIONS

def abrir_github():
    webbrowser.open("https://github.com/ClezerSimoes")

def fun_about():
    about.janela_about(main_app)

def semcomando():
    print("Teste funcionando")

## FILE MENU FUNCTIONS

def file_exit():
    confirmar= messagebox.askyesno("Exit", "Deseja mesmo sair?")
    if confirmar == True:
        main_app.quit()
        main_app.destroy()

def overwrite_db_path():
    with open(config_file_path, 'r', encoding='utf-8') as config_file:
        config_data = json.load(config_file)
    
    lng = config_data.get("language")
    
    with open(config_file_path, 'w', encoding='utf-8') as config_file:
        json.dump({"db_path": files.db_file_path, "language": lng}, config_file, indent=4)

    messagebox.showinfo("Sucesso", "Configurações salvas com sucesso")
    print(f"Configuração salva em: {files.db_file_path}")

def file_new():
    files.new_file()
    
    overwrite_db_path()
 

def file_open():
    files.open_file()

    overwrite_db_path()

def language():
    files.janela_language(main_app)

## CLIENT MENU FUNCTIONS

def client_new():
    cliente_novo.janela_clienteNovo(main_app)

def client_list():
    cliente_lista.janela_client_list(main_app)

def client_update():
    cliente_update.janela_clienteUP(main_app)

def client_delete():
    cliente_delete.janela_deleteCliente(main_app)

## ORDERS MENU FUNCTIONS

def order_new():
    pedido_novo.janela_pedidoNovo(main_app)

def order_list():
    pedido_lista.janela_pedidoLista(main_app)

def order_update():
    pedido_update.janela_pedidoUP(main_app)

def order_cancel():
    pedido_cancelar.janela_pedidoCancelar(main_app)


## MENU

menu_bar = Menu(main_app)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New Flie", command=file_new)
file_menu.add_command(label="Open Flie...", command=file_open)
file_menu.add_command(label="Backup", command=semcomando)
file_menu.add_separator()
file_menu.add_command(label="Language", command=language)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=file_exit)
menu_bar.add_cascade(label="File", menu=file_menu)

clients_menu = Menu(menu_bar, tearoff=0)
clients_menu.add_command(label="New Client", command=client_new)
clients_menu.add_command(label="Client List", command=client_list)
clients_menu.add_command(label="Update Client", command=client_update)
clients_menu.add_separator()
clients_menu.add_command(label="Delete Client", command=client_delete)
menu_bar.add_cascade(label="Clients", menu=clients_menu)

orders_menu = Menu(menu_bar, tearoff=0)
orders_menu.add_command(label="New Order", command=order_new)
orders_menu.add_command(label="Order list", command=order_list)
orders_menu.add_command(label="Update Order", command=order_update)
orders_menu.add_separator()
orders_menu.add_command(label="Cancel Order", command=order_cancel)
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

verify()

Label(fr_window1, text= "GERENCIADOR DE CLIENTES E PEDIDOS", font=("Arial", 14, "bold")).pack(expand=True)
main_app.protocol("WM_DELETE_WINDOW", file_exit)
main_app.mainloop()