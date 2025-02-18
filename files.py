import sqlite3
from tkinter import *
from tkinter import filedialog, messagebox, ttk
import shutil
import os
import json
from datetime import datetime

language_list= ["Portuguese-BR", "Only PT-BR"]
db_file_path = ""
    
def sql_db_file():
    ## Path's
    root_path = os.path.dirname(__file__)
    config_json = os.path.join(root_path, "config.json")

    with open (config_json, "r", encoding="utf-8") as config_file:
        config_dict = json.load(config_file)
    
    return config_dict.get("db_path")

## NEW FILE FUNCTION

def new_file():
    global db_file_path

    # Abre uma caixa de diálogo para o usuário escolher o local e nome do arquivo
    db_file = filedialog.asksaveasfilename(defaultextension=".db", filetypes=[("SQLite Database", "*.db")])
    db_file_path= db_file
    
    if db_file:  # Se o usuário selecionou um arquivo
        try:
            # Conectar ao banco de dados (se não existir, será criado)
            conn = sqlite3.connect(db_file)
            cursor = conn.cursor()
            
            # Criando a tabela de clientes
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS clientes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    documento INTEGER NOT NULL,
                    telefone INTEGER NOT NULL,
                    email TEXT NOT NULL,
                    rua TEXT NOT NULL,
                    numero INTEGER NOT NULL,
                    cidade TEXT NOT NULL,
                    estado TEXT NOT NULL,
                    cep INTEGER NOT NULL,
                    obs TEXT NOT NULL
                )
                ''')
            
            # Criando a tabela de pedidos
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS pedidos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    clienteID INTEGER NOT NULL,
                    data TEXT NOT NULL,
                    valor INTEGER NOT NULL,
                    prazo TEXT NOT NULL,
                    itens TEXT NOT NULL,
                    status TEXT NOT NULL,
                    obs TEXT NOT NULL,
                    FOREIGN KEY (clienteID) REFERENCES clientes(id)
                )
                ''')

            # Commitando as mudanças
            conn.commit()
            conn.close()

            # Mostra uma mensagem de sucesso
            messagebox.showinfo("Sucesso", f"Bando de dados {db_file} criado com sucesso!")
        except sqlite3.Error as e:
            messagebox.showerror("Erro", f"Erro ao criar o banco de dados: {e}")
    else:
        db_file_path = sql_db_file()
        messagebox.showwarning("Aviso", "Nenhum arquivo foi selecionado.")

## OPEN FILE FUNCTION 

def open_file():
    global db_file_path

    # Abre uma caixa de diálogo para o usuário escolher o arquivo .db
    db_file = filedialog.askopenfilename(defaultextension=".db", filetypes=[("SQLite Database", "*.db")])
    db_file_path= db_file

    if db_file:  # Se o usuário selecionou um arquivo
        try:
            # Conectar ao banco de dados existente
            conn = sqlite3.connect(db_file)
            cursor = conn.cursor()

            # A partir daqui, você pode executar comandos SQL no banco de dados aberto.
            # Exemplo: Consultar clientes
            cursor.execute("SELECT * FROM clientes")
            clientes = cursor.fetchall()
            print("Clientes:", clientes)  # Apenas para ver os dados retornados

            # Fecha a conexão
            conn.close()
            
            # Mostra uma mensagem de sucesso
            messagebox.showinfo("Sucesso", f"Bando de dados {db_file} aberto com sucesso!")
        except sqlite3.Error as e:
            messagebox.showerror("Erro", f"Erro ao abrir o banco de dados: {e}")
    else:
        db_file_path = sql_db_file()
        messagebox.showwarning("Aviso", "Nenhum arquivo foi selecionado.")
                               
## BACKUP FUNCTION
 
def file_backup(db_file):
    # Pergunta onde o usuário deseja salvar o backup
    backup_dir = filedialog.askdirectory(title="Escolha a pasta para salvar o backup")

    if backup_dir:
        try:
            # Cria o nome do backup com data/hora para evitar sobrescritas
            backup_name = f"backup_{os.path.basename(db_file)}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.db"
            backup_path = os.path.join(backup_dir, backup_name)

            # Copia o banco de dados para o diretório de backup com o novo nome
            shutil.copy(db_file, backup_path)

            # Exibe uma mensagem de sucesso
            messagebox.showinfo("Sucesso", f"Backup criado com sucesso!\nLocal: {backup_path}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao criar o backup: {e}")
    else:
        messagebox.showwarning("Aviso", "Nenhuma pasta foi selecionada para salvar o backup.")
        
## VERIFY IF CONFIG FILE EXISTS, IF NOT CREATES

def file_config_verify(root, file_path):
    if os.path.exists(file_path):
        return
    else:
        inicialization_app = Toplevel(root)
        inicialization_app.title ("Clezer - miniERP")
        inicialization_app.geometry ("580x720")
        inicialization_app.configure(background="#dde")
        
        fr_titulo1 = Frame(inicialization_app, background="#fff")
        fr_titulo1.place(x=0, y=10, width=580, height=25)
        titulo= Label(fr_titulo1, text= "CONFIGURAÇÕES PRIMEIRA INÍCIALIZAÇÃO", background="#fff", foreground="#009", font= ("Arial", 12, "bold"))
        titulo.pack(expand=0)

        fr_init = Frame(inicialization_app, background="#c8c8d9", borderwidth=2, relief="groove")
        fr_init.place(x=10, y=80, width=560, height=500)

        inicializcao = Label(
            fr_init,
            text="Parece que essa é a primeira vez que você inicializa o Clezer - miniERP ",
            background="#c8c8d9", 
            foreground="#009", 
            anchor=W, 
            font=("Arial", 10)
        )
        inicializcao.place(x=10, y=10, width=500, height=25)

        language = Label(
            fr_init, 
            text="Selecione sua língua", 
            background="#c8c8d9", 
            foreground="#009", 
            anchor=W, 
            font=("Arial", 10)
        )
        language.place(x=10, y=40, width=500, height=25)

        language_box = ttk.Combobox(fr_init, values=language_list)
        language_box.place(x=150, y=40, width=130, height=25)
        language_box.set("Portuguese-BR")

        data_base1 = Label(
            fr_init, 
            text="Caso você ja tenha utilizado o Clezer - miniERP, pode carregar uma banco de dados", 
            background="#c8c8d9", 
            foreground="#009", 
            anchor=W, 
            font=("Arial", 10)
        )
        data_base1.place(x=10, y=70, width=530, height=20)

        data_base2 = Label(
            fr_init,
            text="salvo anteriormente. Clique em \"Carregar\" se deseja carregar um banco de dados existente.",
            background="#c8c8d9", 
            foreground="#009", 
            anchor=W, 
            font=("Arial", 10)
        )
        data_base2.place(x=10, y=90, width=530, height=20)

        data_base3 = Label(
            fr_init,
            text="Clique em \"Criar\" se é um novo usuário ou deseja criar um novo banco de dados.",
            background="#c8c8d9", 
            foreground="#009", 
            anchor=W, 
            font=("Arial", 10)
        )
        data_base3.place(x=10, y=110, width=530, height=20)

        ## BUTTONS

        def config_save():
            file= os.path.dirname(__file__)
            lng = language_box.get()  # Obtém o idioma da interface
            config_path = os.path.join(file, "config.json")  # Forma segura de criar o caminhow
    
            try:
                with open(config_path, 'w', encoding='utf-8') as config_file:
                    json.dump({"db_path": db_file_path, "language": lng}, config_file, indent=4)
                messagebox.showinfo("Sucesso", "Configurações salvas com sucesso")
                print(f"Configuração salva em: {config_path}")  # Mensagem de depuração
                inicialization_app.destroy()
            except Exception as e:
                messagebox.showerror("Erro", "Erro ao salvar as configurações!!!")
                print(f"Erro ao salvar o arquivo de configuração: {e}")  # Tratamento de erro


        def config_cancel():
            confirmar= messagebox.askyesno("Cancelar Configuração", "Deseja mesmo cancelar e fechar o programa?")
            if confirmar == True:
                inicialization_app.destroy()

        btn_create = Button(fr_init, text="Criar novo BC", command=new_file)
        btn_create.place(x=440, y=200, width=100, height=20)
        create_path = Entry(fr_init)
        create_path.place(x=10, y=200, width=420, height=20)
    
        btn_load = Button(fr_init, text="Carregar BC", command=open_file)
        btn_load.place(x=440, y=230, width=100, height=20)
        load_path = Entry(fr_init)
        load_path.place(x=10, y=230, width=420, height=20)

        btn_cancel = Button(fr_init, text="Cancelar", command=config_cancel)
        btn_cancel.place(x=10, y=400, width=100, height=20)
                         
        btn_create = Button(fr_init, text="Salvar Configurações", command=config_save)
        btn_create.place(x=390, y=400, width=150, height=20)



        inicialization_app.mainloop()

## INSERT

def Tabela_cliente_insert(dt_base_path, tb_nome, tb_documento, tb_telefone, tb_email, tb_rua, tb_numero, tb_cidade, tb_estado, tb_cep, tb_obs):
    conn = sqlite3.connect(dt_base_path)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO clientes (nome, documento, telefone, email, rua, numero, cidade, estado, cep, obs)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (tb_nome, tb_documento, tb_telefone, tb_email, tb_rua, tb_numero, tb_cidade, tb_estado, tb_cep, tb_obs)) 

    conn.commit()
    conn.close()


def Tabela_pedido_insert(dt_base_path, tb_client_id, tb_data, tb_valor, tb_prazo, tb_itens, tb_status, tb_obs):
    conn = sqlite3.connect(dt_base_path)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO pedidos (clienteID, data, valor, prazo, itens, status, obs)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (tb_client_id, tb_data, tb_valor, tb_prazo, tb_itens, tb_status, tb_obs))

    conn.commit()
    conn.close()

## LANGUAGE

def janela_language(root):
    language_app = Toplevel(root)
    language_app.title ("Clezer - miniERP")
    language_app.geometry ("420x300")
    language_app.configure(background="#dde")
    
    fr_titulo1 = Frame(language_app, background="#fff")
    fr_titulo1.place(x=0, y=10, width=420, height=25)
    titulo= Label(fr_titulo1, text= "ALTERAR IDIOMA", background="#fff", foreground="#009", font= ("Arial", 12, "bold"))
    titulo.pack(expand=0)

    fr_init = Frame(language_app, background="#c8c8d9", borderwidth=2, relief="groove")
    fr_init.place(x=10, y=80, width=400, height=200)

    language = Label(
            fr_init, 
            text="Selecione seu idioma:", 
            background="#c8c8d9", 
            foreground="#009", 
            anchor=W, 
            font=("Arial", 10)
        )
    language.place(x=50, y=40, width=160, height=25)

    language_box1 = ttk.Combobox(fr_init, values=language_list)
    language_box1.place(x=200, y=40, width=120, height=25)
    language_box1.set("Portuguese-BR")

    def config_save():
        file= os.path.dirname(__file__)
        lng = language_box1.get()  # Obtém o idioma da interface
        config_path = os.path.join(file, "config.json")  # Forma segura de criar o caminhow

        try:
            with open(config_path, 'r', encoding='utf-8') as config_file:
                config_data = json.load(config_file)

            db_file_path = config_data.get("db_path")

            with open(config_path, 'w', encoding='utf-8') as config_file:
                json.dump({"db_path": db_file_path, "language": lng}, config_file, indent=4)

            messagebox.showinfo("Sucesso", "Configurações salvas com sucesso")
            print(f"Configuração salva em: {config_path}")  # Mensagem de depuração
            language_app.destroy()
        except Exception as e:
            messagebox.showerror("Erro", "Erro ao salvar as configurações!!!")
            print(f"Erro ao salvar o arquivo de configuração: {e}")  # Tratamento de erro


    def config_cancel():
        confirmar= messagebox.askyesno("Cancelar Configuração", "Deseja mesmo cancelar?")
        if confirmar == True:
            language_app.destroy()

    btn_cancel = Button(fr_init, text="Cancelar", command=config_cancel)
    btn_cancel.place(x=50, y=120, width=100, height=20)
                        
    btn_create = Button(fr_init, text="Salvar Idioma", command=config_save)
    btn_create.place(x=220, y=120, width=100, height=20)

    language_app.mainloop()
