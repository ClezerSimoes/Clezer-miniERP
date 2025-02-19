from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
import files


id_selected = 15
def janela_client_list(root, janela_atualizar, janela_deletar):

    client_list_app = Toplevel(root)
    client_list_app.title("Lista de Clientes")
    client_list_app.geometry("1080x720")
    client_list_app.configure(background="#dde")
    client_list_app.grab_set()

    fr_titulo1 = Frame(client_list_app, background="#fff")
    fr_titulo1.place(x=0, y=10, width=1080, height=25)
    titulo= Label(fr_titulo1, text= "LISTA DE CLIENTES", background="#fff", foreground="#009", font= ("Arial", 12, "bold"))
    titulo.pack(expand=0)

    fr_list = Frame(client_list_app, background="#c8c8d9", borderwidth=2, relief="groove")
    fr_list.place(x=10, y=80, width=1060, height=580)

    def on_focus_in(event):
        if atualizar_busca.get() == "Digite aqui...":
            atualizar_busca.delete(0, END)
            atualizar_busca.config(fg="black")

    def on_focus_out(event):
        if atualizar_busca.get() == "":
            atualizar_busca.insert(0, "Digite aqui...")
            atualizar_busca.config(fg="gray")

    atualizar_busca= Entry(client_list_app, fg="gray")
    atualizar_busca.place(x=10, y=50, width=270, height=20)
    atualizar_busca.insert(0, "Digite aqui...")
    atualizar_busca.bind("<FocusIn>", on_focus_in)
    atualizar_busca.bind("<FocusOut>", on_focus_out)

    lista_opcao = ["Sem Filtro", "ID", "Documento", "Nome", "CEP"]
    atualizar_filtro= ttk.Combobox(client_list_app, values=lista_opcao, state="readonly")
    atualizar_filtro.place(x=285, y=50, width=90, height=20)
    atualizar_filtro.set("Sem Filtro")


    # Criação do Treeview para mostrar os dados
    tree = ttk.Treeview(fr_list, columns=('id', 'nome', 'documento', 'telefone', 'email', 'numero', 'cidade', 'estado', 'cep'), show="headings")
    tree.heading("id", text="ID")
    tree.heading("nome", text="Nome do cliente")
    tree.heading("documento", text="Documento")
    tree.heading("telefone", text="Telefone")
    tree.heading("email", text="E-mail")
    tree.heading("numero", text="Número")
    tree.heading("cidade", text="Cidade")
    tree.heading("estado", text="Estado")
    tree.heading("cep", text="CEP")

    tree.column("id", width=5)
    tree.column("nome", width=150)
    tree.column("documento", width=80)
    tree.column("telefone", width=60)
    tree.column("email", width=200)
    tree.column("numero", width=35)
    tree.column("cidade", width=100)
    tree.column("estado", width=100)
    tree.column("cep", width=50)

    # Estilo para simular bordas
    style = ttk.Style()
    style.configure("Treeview",
                    highlightthickness=0, 
                    bd=0, 
                    font=("Arial", 10))
    style.configure("Treeview.Heading", 
                    font=("Arial", 10, 'bold'))


    tree.tag_configure('oddrow', background='#f0f0f0')  # Cor para as linhas ímpares
    tree.tag_configure('evenrow', background='#e0e0e0')  # Cor para as linhas pares

    tree.pack(fill=BOTH, expand=True)

    # Função para listar os clientes
    # Aplicando as tags para simular as bordas

    def listar_clientes():
        pesquisa = atualizar_busca.get().strip()
        filtro = atualizar_filtro.get().lower()

        for i in tree.get_children():
            tree.delete(i)

        if filtro == "sem filtro":
            try:
                dt_base_path = files.sql_db_file()
                conn = sqlite3.connect(dt_base_path)
                cursor = conn.cursor()
                cursor.execute("SELECT id, nome, documento, telefone, email, numero, cidade, estado, cep FROM clientes")
                clientes = cursor.fetchall()
                conn.close()

                for index, cliente in enumerate(clientes):
                    tag = 'oddrow' if index % 2 == 0 else 'evenrow'  # Alterna entre as cores de fundo
                    tree.insert("", END, values=cliente, tags=(tag,))
            except sqlite3.Error as e:
                messagebox.showinfo("Erro", f"Erro no banco de dados: {e}")
        else:
            try:
                dt_base_path = files.sql_db_file()
                conn = sqlite3.connect(dt_base_path)
                cursor = conn.cursor()
                cursor.execute(f'SELECT id, nome, documento, telefone, email, numero, cidade, estado, cep FROM clientes WHERE {filtro} LIKE ?', (pesquisa,))
                clientes = cursor.fetchall()
                conn.close()

                for index, cliente in enumerate(clientes):
                    tag = 'oddrow' if index % 2 == 0 else 'evenrow'  # Alterna entre as cores de fundo
                    tree.insert("", END, values=cliente, tags=(tag,))
            except sqlite3.Error as e:
                messagebox.showinfo("Erro", f"Erro no banco de dados: {e}")

    listar_clientes()

    # MOUSE POPUP MENU 
    def teste():
        print("ok")

    def show_popup(event):
        global id_selected

        item = tree.identify_row(event.y)
        if item:
            tree.selection_set(item)
            menu_popup.post(event.x_root, event.y_root)
            
            for campo in tree.selection():
                coluna_id = tree.identify_column(event.x)  # Identifica a coluna
                coluna_index = int(coluna_id[1:]) - 1  # Converte para índice
                id_selected = tree.item(campo, "values")[0]  # Pega o ID do cliente

    menu_popup = Menu(client_list_app, tearoff=0)
    menu_popup.add_command(label="Visualizar",command=janela_deletar)
    menu_popup.add_command(label="Remover",command=janela_atualizar)
    
    tree.bind("<Button-3>", show_popup)

    # BUTTONS
    btn_listar = Button(client_list_app, text="Listar Clientes", bg="green", fg="white", font=("Arial", 9, "bold"), command=listar_clientes)
    btn_listar.place(x=380, y=50, width=90, height=20)

    def voltar():
        global id_selected
        id_selected = 0
        client_list_app.grab_release()
        client_list_app.destroy()

    btn_listar = Button(client_list_app, text="Voltar", command=voltar)
    btn_listar.place(x=990, y=670, width=80, height=20)

    # Rodando a interface
    client_list_app.mainloop()
