from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import files
import sqlite3


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

def janela_clienteUP(root):
    global updt_app
    updt_app = Toplevel(root)
    updt_app.title ("Clezer - miniERP")
    updt_app.geometry ("550x550")
    updt_app.configure(background="#dde")
    updt_app.grab_set()

    def fechar_janela():
        updt_app.grab_release()
        updt_app.destroy()

    clientes_cadastrados= []
    lista_opcao= ["ID", "Documento", "Nome"]

    ## Campos 

    separador = "_____________________________________________________________________________________________________________________"

    atualizar_titulo= Label(updt_app, text= "ATUALIZAR CADASTRO CLIENTE", background="#fff", foreground="#009", anchor=N, font= ("Arial", 12, "bold"))
    atualizar_titulo.place(x=0, y=10, width=550, height=25)

    Label(updt_app, text="Filtrar por:", background="#dde", foreground="#009", anchor=W).place(x=10, y=50, width=60, height=20)
    atualizar_filtro= ttk.Combobox(updt_app, values=lista_opcao, state="readonly")
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

    atualizar_busca= Entry(updt_app, fg="gray")
    atualizar_busca.place(x=165, y=50, width=270, height=20)
    atualizar_busca.insert(0, "Digite aqui...")
    atualizar_busca.bind("<FocusIn>", on_focus_in)
    atualizar_busca.bind("<FocusOut>", on_focus_out)

    fr_atualizar1= Frame(updt_app, background="#c8c8d9", borderwidth=2, relief="groove")
    fr_atualizar1.place(x=10, y=80, width=530, height=400)



    Label(fr_atualizar1, text="Dados do Cliente", background="#dee", foreground="#009", anchor=W, relief="groove").place(x=5, y=2, width=110, height=20)
    Label(fr_atualizar1, text="Descrição", background="#dee", foreground="#009", anchor=W, relief="groove").place(x=109, y=2, width=400, height=20)
    Label(fr_atualizar1, text="Atualizar", background="#dee", foreground="#009", anchor=W, relief="groove").place(x=398, y=2, width=125, height=20)

    Label(fr_atualizar1, text="ID", background="#c8c8d9", foreground="#009", anchor=W).place(x=5, y=25, width=100, height=20)
    Label(fr_atualizar1, text="Nome", background="#c8c8d9", foreground="#009", anchor=W).place(x=5, y=50, width=100, height=20)
    Label(fr_atualizar1, text="Documentos", background="#c8c8d9", foreground="#009", anchor=W).place(x=5, y=75, width=100, height=20)
    Label(fr_atualizar1, text="Telefone", background="#c8c8d9", foreground="#009", anchor=W).place(x=5, y=100, width=100, height=20)
    Label(fr_atualizar1, text="E-mail", background="#c8c8d9", foreground="#009", anchor=W).place(x=5, y=125, width=100, height=20)
    Label(fr_atualizar1, text="Rua", background="#c8c8d9", foreground="#009", anchor=W).place(x=5, y=160, width=100, height=20)
    Label(fr_atualizar1, text="Numero", background="#c8c8d9", foreground="#009", anchor=W).place(x=5, y=185, width=100, height=20)
    Label(fr_atualizar1, text="Cidade", background="#c8c8d9", foreground="#009", anchor=W).place(x=5, y=210, width=100, height=20)
    Label(fr_atualizar1, text="Estado", background="#c8c8d9", foreground="#009", anchor=W).place(x=5, y=235, width=100, height=20)
    Label(fr_atualizar1, text="CEP", background="#c8c8d9", foreground="#009", anchor=W).place(x=5, y=260, width=100, height=20)
    Label(fr_atualizar1, text="Observação", background="#c8c8d9", foreground="#009", anchor=W).place(x=5, y=285, width=100, height=20)

    Label(fr_atualizar1, text= separador, background="#c8c8d9", foreground="#009", anchor=W).place(x=0, y=140, width=520, height=15)

    def campo_branco():
        Label(fr_atualizar1, text="", background="#fff", foreground="#009", anchor=W).place(x=109, y=25, width=50, height=20)
        Label(fr_atualizar1, text="", background="#fff", foreground="#009", anchor=W).place(x=109, y=50, width=285, height=20)
        Label(fr_atualizar1, text="", background="#fff", foreground="#009", anchor=W).place(x=109, y=75, width=285, height=20)
        Label(fr_atualizar1, text="", background="#fff", foreground="#009", anchor=W).place(x=109, y=100, width=285, height=20)
        Label(fr_atualizar1, text="", background="#fff", foreground="#009", anchor=W).place(x=109, y=125, width=285, height=20)
        Label(fr_atualizar1, text="", background="#fff", foreground="#009", anchor=W).place(x=109, y=160, width=285, height=20)
        Label(fr_atualizar1, text="", background="#fff", foreground="#009", anchor=W).place(x=109, y=185, width=285, height=20)
        Label(fr_atualizar1, text="", background="#fff", foreground="#009", anchor=W).place(x=109, y=210, width=285, height=20)
        Label(fr_atualizar1, text="", background="#fff", foreground="#009", anchor=W).place(x=109, y=235, width=285, height=20)
        Label(fr_atualizar1, text="", background="#fff", foreground="#009", anchor=W).place(x=109, y=260, width=285, height=20)
        Label(fr_atualizar1, text="", background="#fff", foreground="#009", anchor=W).place(x=109, y=285, width=285, height=100)

    campo_branco()

    def func_atualizar_campos():
        Label(fr_atualizar1, text=client_id, background="#fff", foreground="#009", anchor=W).place(x=109, y=25, width=50, height=20)
        Label(fr_atualizar1, text=nome, background="#fff", foreground="#009", anchor=W).place(x=109, y=50, width=285, height=20)
        Label(fr_atualizar1, text=documento, background="#fff", foreground="#009", anchor=W).place(x=109, y=75, width=285, height=20)
        Label(fr_atualizar1, text=telefone, background="#fff", foreground="#009", anchor=W).place(x=109, y=100, width=285, height=20)
        Label(fr_atualizar1, text=email, background="#fff", foreground="#009", anchor=W).place(x=109, y=125, width=285, height=20)
        Label(fr_atualizar1, text=rua , background="#fff", foreground="#009", anchor=W).place(x=109, y=160, width=285, height=20)
        Label(fr_atualizar1, text=numero, background="#fff", foreground="#009", anchor=W).place(x=109, y=185, width=285, height=20)
        Label(fr_atualizar1, text=cidade, background="#fff", foreground="#009", anchor=W).place(x=109, y=210, width=285, height=20)
        Label(fr_atualizar1, text=estado, background="#fff", foreground="#009", anchor=W).place(x=109, y=235, width=285, height=20)
        Label(fr_atualizar1, text=cep, background="#fff", foreground="#009", anchor=W).place(x=109, y=260, width=285, height=20)
        Label(fr_atualizar1, text=obs, background="#fff", foreground="#009", anchor=NW, wraplength=275, justify="left").place(x=109, y=285, width=285, height=100)

    def buscar():
        global client_id, nome, documento, telefone, email, rua, numero, cidade, estado, cep, obs
        
        dt_base_path = files.sql_db_file()
        pesquisa = atualizar_busca.get().strip()
        filtro = atualizar_filtro.get().lower()
        print(dt_base_path)
        
        try:
            conn = sqlite3.connect(dt_base_path)
            cursor = conn.cursor()
            cursor.execute(f'SELECT * FROM clientes WHERE {filtro} = ?', (pesquisa,))
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

            func_atualizar_campos()

            conn.close()
        except sqlite3.Error as e:
            campo_branco()
            messagebox.showinfo("Erro", f"Erro no banco de dados: {e}")
        except:
            campo_branco()
            messagebox.showinfo("Erro", "Cliente não encontrado.")

    def janela_sobrescrever(campo_tb):
        global sobres
        sobres = Toplevel(updt_app)
        sobres.title (f"Atualizar {campo_tb}")
        sobres.geometry ("320x200")
        sobres.configure(background="#dde")
        sobres.grab_set()

        def fechar_janela_sobres():
            confirmar= messagebox.askyesno("Cancelar", "Deseja mesmo cancelar e voltar?")
            if confirmar == True:
                sobres.grab_release()
                sobres.destroy()
                updt_app.grab_set()


        Label(sobres, text=f"Digite o novo {campo_tb}:", background="#dde", foreground="#009", anchor=W).place(x=10, y=60, width=150, height=20)
        atualizar_campo= Entry(sobres)
        atualizar_campo.place(x=10, y=80, width=300, height=20)
        campo_atualizar = campo_tb

        def validar_email(valor):
            return "@" in valor and "." in valor

        def sobrescrever():

            global client_id
            dt_base_path = files.sql_db_file()
            campo_novo = atualizar_campo.get().strip()

            def sobrescrever_campos():
                try:
                    conn = sqlite3.connect(dt_base_path)
                    cursor = conn.cursor()
                    cursor.execute(f'UPDATE clientes SET {campo_atualizar} = ? WHERE id = ?', (campo_novo, client_id,))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Sucesso", f"Campo {campo_atualizar} atualizado com sucesso!")
                    func_atualizar_campos()
                    sobres.grab_release()
                    sobres.destroy()
                    updt_app.grab_set()

                except sqlite3.Error as e:
                    campo_branco()
                    messagebox.showinfo("Erro", f"Erro no banco de dados: {e}")

            if len(campo_novo) != 0:
                if campo_tb == "documento" or campo_tb == "telefone" or campo_tb == "numero" or campo_tb == "cep":
                    if campo_novo.isdigit():
                        sobrescrever_campos()
                    else:
                        messagebox.showinfo("Erro", "Campo inválido para esse dado, digite apenas números.")
                elif campo_tb == "email":
                    if validar_email(campo_novo):
                        sobrescrever_campos()
                    else:
                        messagebox.showinfo("Erro", "Campo inválido para esse dado, digite um e-mail.")
                else:
                    sobrescrever_campos()
            else:
                messagebox.showinfo("Erro", "O campo está vazio.")

        confirmar= Button(sobres, text=f"Atualizar {campo_tb}", command=sobrescrever)
        confirmar.place(x=190, y=150, width=120, height=20)

        cancelar= Button(sobres, text="Cancelar", command=fechar_janela_sobres)
        cancelar.place(x=10, y=150, width=80, height=20)

        #sobres.mainloop()

    atualizar_button= Button(updt_app, text="Buscar", command=buscar)
    atualizar_button.place(x=440, y=50, width=100, height=20)

    def overwrite_nome():
        if client_id!= 0:
            janela_sobrescrever("nome")
        else:
            messagebox.showinfo("Erro", "Você precisa selecionar um cliente!")

    def overwrite_doc():
        if client_id!= 0:
            janela_sobrescrever("documento")
        else:
            messagebox.showinfo("Erro", "Você precisa selecionar um cliente!")

    def overwrite_fone():
        if client_id!= 0:
            janela_sobrescrever("telefone")
        else:
            messagebox.showinfo("Erro", "Você precisa selecionar um cliente!")

    def overwrite_email():
        if client_id!= 0:
            janela_sobrescrever("email")
        else:
            messagebox.showinfo("Erro", "Você precisa selecionar um cliente!")

    def overwrite_rua():
        if client_id!= 0:
            janela_sobrescrever("rua")
        else:
            messagebox.showinfo("Erro", "Você precisa selecionar um cliente!")

    def overwrite_numero():
        if client_id!= 0:
            janela_sobrescrever("numero")
        else:
            messagebox.showinfo("Erro", "Você precisa selecionar um cliente!")

    def overwrite_cidade():
        if client_id!= 0:
            janela_sobrescrever("cidade")
        else:
            messagebox.showinfo("Erro", "Você precisa selecionar um cliente!")

    def overwrite_estado():
        if client_id!= 0:
            janela_sobrescrever("estado")
        else:
            messagebox.showinfo("Erro", "Você precisa selecionar um cliente!")

    def overwrite_cep():
        if client_id!= 0:
            janela_sobrescrever("cep")
        else:
            messagebox.showinfo("Erro", "Você precisa selecionar um cliente!")

    def overwrite_obs():
        if client_id!= 0:
            janela_sobrescrever("obs")
        else:
            messagebox.showinfo("Erro", "Você precisa selecionar um cliente!")

    atualizar_nome= Button(fr_atualizar1, text="Atualizar Nome", command=overwrite_nome)
    atualizar_nome.place(x=400, y=50, width=120, height=20)

    atualizar_doc= Button(fr_atualizar1, text="Atualizar Documento", command=overwrite_doc)
    atualizar_doc.place(x=400, y=75, width=120, height=20)

    atualizar_fone= Button(fr_atualizar1, text="Atualizar Telefone", command=overwrite_fone)
    atualizar_fone.place(x=400, y=100, width=120, height=20)

    atualizar_email= Button(fr_atualizar1, text="Atualizar E-mail", command=overwrite_email)
    atualizar_email.place(x=400, y=125, width=120, height=20)

    atualizar_endereco= Button(fr_atualizar1, text="Atualizar Rua", command=overwrite_rua)
    atualizar_endereco.place(x=400, y=160, width=120, height=20)

    atualizar_endereco= Button(fr_atualizar1, text="Atualizar Número", command=overwrite_numero)
    atualizar_endereco.place(x=400, y=185, width=120, height=20)

    atualizar_endereco= Button(fr_atualizar1, text="Atualizar Cidade", command=overwrite_cidade)
    atualizar_endereco.place(x=400, y=210, width=120, height=20)

    atualizar_endereco= Button(fr_atualizar1, text="Atualizar Estado", command=overwrite_estado)
    atualizar_endereco.place(x=400, y=235, width=120, height=20)

    atualizar_endereco= Button(fr_atualizar1, text="Atualizar CEP", command=overwrite_cep)
    atualizar_endereco.place(x=400, y=260, width=120, height=20)

    atualizar_endereco= Button(fr_atualizar1, text="Atualizar Obs.", command=overwrite_obs)
    atualizar_endereco.place(x=400, y=285, width=120, height=20)

    def voltar():
        confirmar= messagebox.askyesno("Cancelar", "Deseja mesmo cancelar e voltar?")
        if confirmar == True:
            fechar_janela()

    atualizar_fone= Button(updt_app, text="Voltar", command=voltar)
    atualizar_fone.place(x=460, y=500, width=80, height=20)


    updt_app.mainloop()
    