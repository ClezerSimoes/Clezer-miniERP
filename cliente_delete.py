from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import json
import os
import files


clientes_cadastrados= []

client_id = 0
nome = ""
documento = 0
telefone = 0
email = ""
rua = ""
numero = 0
cidade = ""
estado = ""
cep = 0
obs = ""

def janela_deleteCliente(root):
    app = Toplevel(root)
    app.title ("Clezer - miniERP")
    app.geometry ("500x450")
    app.configure(background="#dde")
    app.grab_set()

    
    lista_filtro= ["ID", "Documento", "Nome"]

    def sobrescrever():
        print ("Contato Atualizado")

    ## INTERFACE DELETE CLIENT

    ## Campos 

    separador = "_____________________________________________________________________________________________________________________"

    atualizar_titulo= Label(app, text= "DELETAR CADASTRO DO CLIENTE", background="#fff", foreground="#009", anchor=N, font= ("Arial", 12, "bold"))
    atualizar_titulo.place(x=0, y=10, width=550, height=25)
    # Label(app, text= separador, background="#dde", foreground="#009", anchor=W).place(x=10, y=490, width=250, height=20)

    Label(app, text="Filtrar por:", background="#dde", foreground="#009", anchor=W).place(x=10, y=50, width=60, height=20)
    atualizar_filtro= ttk.Combobox(app, values=lista_filtro, state="readonly")
    atualizar_filtro.place(x=70, y=50, width=90, height=20)
    atualizar_filtro.set("ID")

    def on_focus_in(event):
        if atualizar_busca.get() == "Digite aqui...":
            atualizar_busca.delete(0, END)
            atualizar_busca.config(fg="black")

    def on_focus_out(event):
        if atualizar_busca.get() == "":
            atualizar_busca.insert(0, "Digite aqui...")
            atualizar_busca.config(fg="gray")

    atualizar_busca= Entry(app, fg="gray")
    atualizar_busca.place(x=165, y=50, width=240, height=20)
    atualizar_busca.insert(0, "Digite aqui...")
    atualizar_busca.bind("<FocusIn>", on_focus_in)
    atualizar_busca.bind("<FocusOut>", on_focus_out)

    # fr_delete1= Frame(app, background= "#c8c8d9")
    # fr_delete1.place(x=10, y=80, width=550, height=500)

    fr_delete1 = Frame(app, background="#c8c8d9", borderwidth=2, relief="groove")
    fr_delete1.place(x=10, y=80, width=480, height=290)



    Label(fr_delete1, text="Dados do Cliente", background="#dee", foreground="#009", anchor=W, relief="groove").place(x=5, y=2, width=110, height=20)
    Label(fr_delete1, text="Descrição", background="#dee", foreground="#009", anchor=W, relief="groove").place(x=109, y=2, width=341, height=20)
    # Label(fr_atualizar1, text="Atualizar", background="#dee", foreground="#009", anchor=W, relief="groove").place(x=398, y=2, width=125, height=20)

    Label(fr_delete1, text="ID", background="#c8c8d9", foreground="#009", anchor=W).place(x=5, y=25, width=100, height=20)
    Label(fr_delete1, text="Nome", background="#c8c8d9", foreground="#009", anchor=W).place(x=5, y=50, width=100, height=20)
    Label(fr_delete1, text="Documentos", background="#c8c8d9", foreground="#009", anchor=W).place(x=5, y=75, width=100, height=20)
    Label(fr_delete1, text="Telefone", background="#c8c8d9", foreground="#009", anchor=W).place(x=5, y=100, width=100, height=20)
    Label(fr_delete1, text="E-mail", background="#c8c8d9", foreground="#009", anchor=W).place(x=5, y=125, width=100, height=20)
    Label(fr_delete1, text="Rua", background="#c8c8d9", foreground="#009", anchor=W).place(x=5, y=160, width=100, height=20)
    Label(fr_delete1, text="Numero", background="#c8c8d9", foreground="#009", anchor=W).place(x=5, y=185, width=100, height=20)
    Label(fr_delete1, text="Cidade", background="#c8c8d9", foreground="#009", anchor=W).place(x=5, y=210, width=100, height=20)
    Label(fr_delete1, text="Estado", background="#c8c8d9", foreground="#009", anchor=W).place(x=5, y=235, width=100, height=20)
    Label(fr_delete1, text="CEP", background="#c8c8d9", foreground="#009", anchor=W).place(x=5, y=260, width=100, height=20)

    Label(fr_delete1, text= separador, background="#c8c8d9", foreground="#009", anchor=W).place(x=0, y=140, width=450, height=15)

    def campo_branco():
        Label(fr_delete1, text="", background="#fff", foreground="#009", anchor=W).place(x=109, y=25, width=341, height=20)
        Label(fr_delete1, text="", background="#fff", foreground="#009", anchor=W).place(x=109, y=50, width=341, height=20)
        Label(fr_delete1, text="", background="#fff", foreground="#009", anchor=W).place(x=109, y=75, width=341, height=20)
        Label(fr_delete1, text="", background="#fff", foreground="#009", anchor=W).place(x=109, y=100, width=341, height=20)
        Label(fr_delete1, text="", background="#fff", foreground="#009", anchor=W).place(x=109, y=125, width=341, height=20)
        Label(fr_delete1, text="", background="#fff", foreground="#009", anchor=W).place(x=109, y=160, width=341, height=20)
        Label(fr_delete1, text="", background="#fff", foreground="#009", anchor=W).place(x=109, y=185, width=341, height=20)
        Label(fr_delete1, text="", background="#fff", foreground="#009", anchor=W).place(x=109, y=210, width=341, height=20)
        Label(fr_delete1, text="", background="#fff", foreground="#009", anchor=W).place(x=109, y=235, width=341, height=20)
        Label(fr_delete1, text="", background="#fff", foreground="#009", anchor=W).place(x=109, y=260, width=341, height=20)
    
    campo_branco()

    ## BUTTONS

    def deletar():
        dt_base_path = files.sql_db_file()
        pesquisa = atualizar_busca.get().strip()
        filtro = atualizar_filtro.get()
        print(dt_base_path)

        if len(pesquisa) != 0 and pesquisa != "Digite aqui...":
            confirmar = messagebox.askyesno("Deleta", "Deseja mesmo deletar esse cliente?")
            if confirmar == True:
                if filtro == "ID":
                    conn = sqlite3.connect(dt_base_path)
                    cursor = conn.cursor()
                    cursor.execute('DELETE FROM clientes WHERE id = ?', (pesquisa,))

                    conn.commit()
                    conn.close()
                    campo_branco()

                elif filtro == "Documento":
                    conn = sqlite3.connect(dt_base_path)
                    cursor = conn.cursor()
                    cursor.execute('DELETE FROM clientes WHERE documento = ?', (pesquisa,))

                    conn.commit()
                    conn.close()
                    campo_branco()

                elif filtro == "Nome":
                    conn = sqlite3.connect(dt_base_path)
                    cursor = conn.cursor()
                    cursor.execute('DELETE FROM clientes WHERE nome = ?', (pesquisa,))

                    conn.commit()
                    conn.close()
                    campo_branco()
        else:
            messagebox.showinfo("Erro", "Selecione um cliente para deletar.")

    def voltar():
        app.grab_release()
        app.destroy()

    def atualizar_campos():
        Label(fr_delete1, text= client_id, background="#fff", foreground="#009", anchor=W).place(x=109, y=25, width=341, height=20)
        Label(fr_delete1, text= nome, background="#fff", foreground="#009", anchor=W).place(x=109, y=50, width=341, height=20)
        Label(fr_delete1, text= documento, background="#fff", foreground="#009", anchor=W).place(x=109, y=75, width=341, height=20)
        Label(fr_delete1, text= telefone, background="#fff", foreground="#009", anchor=W).place(x=109, y=100, width=341, height=20)
        Label(fr_delete1, text= email, background="#fff", foreground="#009", anchor=W).place(x=109, y=125, width=341, height=20)
        Label(fr_delete1, text= rua, background="#fff", foreground="#009", anchor=W).place(x=109, y=160, width=341, height=20)
        Label(fr_delete1, text= numero, background="#fff", foreground="#009", anchor=W).place(x=109, y=185, width=341, height=20)
        Label(fr_delete1, text= cidade, background="#fff", foreground="#009", anchor=W).place(x=109, y=210, width=341, height=20)
        Label(fr_delete1, text= estado, background="#fff", foreground="#009", anchor=W).place(x=109, y=235, width=341, height=20)
        Label(fr_delete1, text= cep, background="#fff", foreground="#009", anchor=W).place(x=109, y=260, width=341, height=20)

    def buscar():
        global client_id, nome, documento, telefone, email, rua, numero, cidade, estado, cep, obs
        
        dt_base_path = files.sql_db_file()
        pesquisa = atualizar_busca.get().strip()
        filtro = atualizar_filtro.get()
        print(dt_base_path)
        
        if filtro.lower() == "id":
            try:
                conn = sqlite3.connect(dt_base_path)
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM clientes WHERE id = ?', (pesquisa,))
                cliente_select = cursor.fetchall()

                client_id = cliente_select[0][0]
                nome = cliente_select[0][1]
                documento = cliente_select[0][2]
                telefone = cliente_select[0][3]
                email = cliente_select[0][4]
                rua = cliente_select[0][5]
                numero = cliente_select[0][6]
                cidade = cliente_select[0][7]
                estado = cliente_select[0][8]
                cep = cliente_select[0][9]
                obs = cliente_select[0][10]

                atualizar_campos()

                conn.close()
            except sqlite3.Error as e:
                campo_branco()
                messagebox.showinfo("Erro", f"Erro no banco de dados: {e}")
            except:
                campo_branco()
                messagebox.showinfo("Erro", "Cliente não encontrado.")

        elif filtro.lower() == "documento":
            try:
                conn = sqlite3.connect(dt_base_path)
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM clientes WHERE documento = ?', (pesquisa,))
                cliente_select = cursor.fetchall()

                client_id = cliente_select[0][0]
                nome = cliente_select[0][1]
                documento = cliente_select[0][2]
                telefone = cliente_select[0][3]
                email = cliente_select[0][4]
                rua = cliente_select[0][5]
                numero = cliente_select[0][6]
                cidade = cliente_select[0][7]
                estado = cliente_select[0][8]
                cep = cliente_select[0][9]
                obs = cliente_select[0][10]

                atualizar_campos()

                conn.close()
            except sqlite3.Error as e:
                campo_branco()
                messagebox.showinfo("Erro", f"Erro no banco de dados: {e}")
            except:
                campo_branco()
                messagebox.showinfo("Erro", "Cliente não encontrado.")

        elif filtro.lower() == "nome":
            try:
                conn = sqlite3.connect(dt_base_path)
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM clientes WHERE nome = ?', (pesquisa,))
                cliente_select = cursor.fetchall()

                client_id = cliente_select[0][0]
                nome = cliente_select[0][1]
                documento = cliente_select[0][2]
                telefone = cliente_select[0][3]
                email = cliente_select[0][4]
                rua = cliente_select[0][5]
                numero = cliente_select[0][6]
                cidade = cliente_select[0][7]
                estado = cliente_select[0][8]
                cep = cliente_select[0][9]
                obs = cliente_select[0][10]

                atualizar_campos() 

                conn.close()
            except sqlite3.Error as e:
                campo_branco()
                messagebox.showinfo("Erro", f"Erro no banco de dados: {e}")
            except:
                campo_branco()
                messagebox.showinfo("Erro", "Cliente não encontrado.")


    atualizar_button= Button(app, text="Buscar", command=buscar)
    atualizar_button.place(x=410, y=50, width=80, height=20)


    atualizar_doc= Button(app, text="Deletar", command=deletar)
    atualizar_doc.place(x=400, y=400, width=80, height=20)

    atualizar_fone= Button(app, text="Voltar", command=voltar)
    atualizar_fone.place(x=10, y=400, width=80, height=20)


    app.mainloop()

