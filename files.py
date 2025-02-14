import sqlite3
from tkinter import filedialog, messagebox
import shutil
import os
from datetime import datetime

# Função para criar o banco de dados

def new_file():
    # Abre uma caixa de diálogo para o usuário escolher o local e nome do arquivo
    db_file = filedialog.asksaveasfilename(defaultextension=".db", filetypes=[("SQLite Database", "*.db")])
    
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
                    email TEXT NOT NULL
                )
            ''')
            
            # Criando a tabela de pedidos
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS pedidos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cliente_id INTEGER,
                    data_pedido TEXT NOT NULL,
                    valor REAL NOT NULL,
                    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
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
        messagebox.showwarning("Aviso", "Nenhum arquivo foi selecionado.")

# Alterando o comando do "New File" para criar o banco de dados


def open_file():
    # Abre uma caixa de diálogo para o usuário escolher o arquivo .db
    db_file = filedialog.askopenfilename(defaultextension=".db", filetypes=[("SQLite Database", "*.db")])
    
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
        messagebox.showwarning("Aviso", "Nenhum arquivo foi selecionado.")
                               


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