from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
import files


id_selected = 15
def janela_order_list(root, janela_pedidos_deletar, janela_pedidos_atualizar):

    order_list_app = Toplevel(root)
    order_list_app.title("Lista de Pedidos")
    order_list_app.geometry("1080x720")
    order_list_app.configure(background="#dde")
    order_list_app.grab_set()

    fr_titulo1 = Frame(order_list_app, background="#fff")
    fr_titulo1.place(x=0, y=10, width=1080, height=25)
    titulo= Label(fr_titulo1, text= "LISTA DE PEDIDOS", background="#fff", foreground="#009", font= ("Arial", 12, "bold"))
    titulo.pack(expand=0)

    fr_list = Frame(order_list_app, background="#c8c8d9", borderwidth=2, relief="groove")
    fr_list.place(x=10, y=80, width=1060, height=580)

    def on_focus_in(event):
        if atualizar_busca.get() == "Digite aqui...":
            atualizar_busca.delete(0, END)
            atualizar_busca.config(fg="black")

    def on_focus_out(event):
        if atualizar_busca.get() == "":
            atualizar_busca.insert(0, "Digite aqui...")
            atualizar_busca.config(fg="gray")

    atualizar_busca= Entry(order_list_app, fg="gray")
    atualizar_busca.place(x=10, y=50, width=270, height=20)
    atualizar_busca.insert(0, "Digite aqui...")
    atualizar_busca.bind("<FocusIn>", on_focus_in)
    atualizar_busca.bind("<FocusOut>", on_focus_out)

    lista_opcao = ["Todos Pedidos", "ID Pedido", "ID Cliente"]
    atualizar_filtro= ttk.Combobox(order_list_app, values=lista_opcao, state="readonly")
    atualizar_filtro.place(x=285, y=50, width=100, height=20)
    atualizar_filtro.set("Todos Pedidos")


    # Criação do Treeview para mostrar os dados
    tree = ttk.Treeview(fr_list, columns=("id", "clienteID", "data", "valor", "prazo", "itens", "status", "obs"), show="headings")
    tree.heading("id", text="ID")
    tree.heading("clienteID", text="ID Cliente")
    tree.heading("data", text="Data")
    tree.heading("valor", text="Valor")
    tree.heading("prazo", text="Prazo")
    tree.heading("itens", text="Itens")
    tree.heading("status", text="Status")
    tree.heading("obs", text="OBS")

    tree.column("id", width=5)
    tree.column("clienteID", width=15)
    tree.column("data", width=30)
    tree.column("valor", width=60)
    tree.column("prazo", width=30)
    tree.column("itens", width=250)
    tree.column("status", width=50)
    tree.column("obs", width=150)

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
        filtro_orig = atualizar_filtro.get().lower()
        if filtro_orig =="id pedido":
            filtro = "id"
        elif filtro_orig =="id cliente":
            filtro = "clienteID"
        elif filtro_orig =="documento":
            filtro = "documento"

        for i in tree.get_children():
            tree.delete(i)

        if filtro_orig == "todos pedidos":
            try:
                dt_base_path = files.sql_db_file()
                conn = sqlite3.connect(dt_base_path)
                cursor = conn.cursor()
                cursor.execute("SELECT id, clienteID, data, valor, prazo, itens, status, obs FROM pedidos")
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
                cursor.execute(f"SELECT id, clienteID, data, valor, prazo, itens, status, obs FROM pedidos WHERE {filtro} LIKE ?", (pesquisa,))
                clientes = cursor.fetchall()
                conn.close()

                for index, cliente in enumerate(clientes):
                    tag = 'oddrow' if index % 2 == 0 else 'evenrow'  # Alterna entre as cores de fundo
                    tree.insert("", END, values=cliente, tags=(tag,))
            except sqlite3.Error as e:
                messagebox.showinfo("Erro", f"Erro no banco de dados: {e}")

    listar_clientes()

    # MOUSE POPUP MENU 
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

    def temporaria():
        print("ok")
    menu_popup = Menu(order_list_app, tearoff=0)
    menu_popup.add_command(label="Visualizar",command=janela_pedidos_atualizar)
    menu_popup.add_command(label="Remover",command=janela_pedidos_deletar)
    
    tree.bind("<Button-3>", show_popup)

    # BUTTONS
    btn_listar = Button(order_list_app, text="Listar Pedidos", bg="green", fg="white", font=("Arial", 9, "bold"), command=listar_clientes)
    btn_listar.place(x=390, y=50, width=90, height=20)

    def pedios_status(status):

        for i in tree.get_children():
            tree.delete(i)

        try:
            dt_base_path = files.sql_db_file()
            conn = sqlite3.connect(dt_base_path)
            cursor = conn.cursor()
            cursor.execute(f"SELECT id, clienteID, data, valor, prazo, itens, status, obs FROM pedidos WHERE status LIKE ?", (status,))
            clientes = cursor.fetchall()
            conn.close()

            for index, cliente in enumerate(clientes):
                tag = 'oddrow' if index % 2 == 0 else 'evenrow'  # Alterna entre as cores de fundo
                tree.insert("", END, values=cliente, tags=(tag,))
        except sqlite3.Error as e:
            messagebox.showinfo("Erro", f"Erro no banco de dados: {e}")
    
    btn_listar_aberto = Button(
        order_list_app, 
        text="Pedidos Abertos", 
        bg="green", fg="white", 
        font=("Arial", 9, "bold"), 
        command=lambda: pedios_status("Aberto")
        )
    btn_listar_aberto.place(x=840, y=50, width=100, height=20)

    btn_listar_concluido = Button(
        order_list_app, 
        text="Pedidos Concluidos", 
        bg="green", 
        fg="white", 
        font=("Arial", 9, "bold"), 
        command=lambda: pedios_status("Concluído")
        )
    btn_listar_concluido.place(x=950, y=50, width=120, height=20)

    def voltar():
        global id_selected
        id_selected = 0
        order_list_app.grab_release()
        order_list_app.destroy()

    btn_listar = Button(order_list_app, text="Voltar", command=voltar)
    btn_listar.place(x=990, y=670, width=80, height=20)

    # Rodando a interface
    order_list_app.mainloop()

