from tkinter import *
from tkinter import messagebox
import files
import os
import json


def janela_clienteNovo(root):
    new_client_app = Toplevel(root)
    new_client_app.title ("Clezer - miniERP")
    new_client_app.geometry ("1080x720")
    new_client_app.configure(background="#dde")
    new_client_app.grab_set()

    clientes_cadastrados= []

    ## INTERFACE Cliente

    """ anchor =>   N = North 
                    S = South
                    E = East
                    W = West
    """
    ## Campos 

    fr_titulo1 = Frame(new_client_app, background="#fff")
    fr_titulo1.place(x=0, y=10, width=1080, height=25)
    titulo= Label(fr_titulo1, text= "CADASTRO DE CLIENTES", background="#fff", foreground="#009", font= ("Arial", 12, "bold"))
    titulo.pack(expand=0)

    titulo_cliente= Label(new_client_app, text= "DADOS DO CLIENTE", background="#dde", foreground="#009", font= ("Arial", 12, "bold"))
    titulo_cliente.place(x=10, y=55)

    titulo_endereco= Label(new_client_app, text= "DADOS DO ENDEREÇO", background="#dde", foreground="#009", font= ("Arial", 12, "bold"))
    titulo_endereco.place(x=515, y=55)

    fr_cliente = Frame(new_client_app, background="#c8c8d9", borderwidth=2, relief="groove")
    fr_cliente.place(x=10, y=80, width=500, height=500)

    fr_endereco= Frame(new_client_app, background="#c8c8d9", borderwidth=2, relief="groove")
    fr_endereco.place(x=515, y=80, width=555, height=500)


    separador = "___________________________________________________________________________"
    ## CAMPO CLIENTE

    Label(fr_cliente, text="Nome:", background="#c8c8d9", foreground="#009", anchor=E).place(x=5, y=5, width=165, height=20)
    interface_Nome= Entry(fr_cliente)
    interface_Nome.place(x=175, y=5, width=310, height=20)

    Label(fr_cliente, text="CPF/CNPJ (Apenas Números):", background="#c8c8d9", foreground="#009", anchor=E).place(x=5, y=35, width=165, height=20)
    interface_Documento= Entry(fr_cliente)
    interface_Documento.place(x=175, y=35, width=310, height=20)

    Label(fr_cliente, text="Telefone (Apenas Números):", background="#c8c8d9", foreground="#009", anchor=E).place(x=5, y=70, width=165, height=20)
    interface_Fone= Entry(fr_cliente)
    interface_Fone.place(x=175, y=70, width=310, height=20)

    Label(fr_cliente, text="E-mail:", background="#c8c8d9", foreground="#009", anchor=E).place(x=5, y=105, width=165, height=20)
    interface_Email= Entry(fr_cliente)
    interface_Email.place(x=175, y=105, width=310, height=20)

    Label(fr_cliente, text="Obs:", background="#c8c8d9", foreground="#009", anchor=E).place(x=5, y=140, width=165, height=20)
    interface_Obs= Text(fr_cliente)
    interface_Obs.place(x=175, y=140, width=310, height=100)

    ## CAMPO ENDEREÇO

    Label(fr_endereco, text="Rua:", background="#c8c8d9", foreground="#009", anchor=E).place(x=5, y=5, width=140, height=20)
    interface_Rua= Entry(fr_endereco)
    interface_Rua.place(x=150, y=5, width=250, height=20)

    Label(fr_endereco, text="Num (Apenas Números):", background="#c8c8d9", foreground="#009", anchor=E).place(x=5, y=35, width=140, height=20)
    interface_Num= Entry(fr_endereco)
    interface_Num.place(x=150, y=35, width=50, height=20)

    Label(fr_endereco, text="Cidade:", background="#c8c8d9", foreground="#009", anchor=E).place(x=5, y=70, width=140, height=20)
    interface_Cidade= Entry(fr_endereco)
    interface_Cidade.place(x=150, y=70, width=250, height=20)

    Label(fr_endereco, text="Estado:", background="#c8c8d9", foreground="#009", anchor=E).place(x=5, y=105, width=140, height=20)
    interface_Estado= Entry(fr_endereco)
    interface_Estado.place(x=150, y=105, width=250, height=20)

    Label(fr_endereco, text="CEP (Apenas Números):", background="#c8c8d9", foreground="#009", anchor=E).place(x=5, y=140, width=140, height=20)
    interface_CEP= Entry(fr_endereco)
    interface_CEP.place(x=150, y=140, width=250, height=20)

    ## Botões

    def validar_Inteiro(valor):
        return valor.isdigit()

    def validar_email(valor):
        return "@" in valor and "." in valor

    def gravar_Dados():
        print ("Dados Salvos")
        nome= interface_Nome.get().strip()
        documento= interface_Documento.get()
        telefone= interface_Fone.get()
        email= interface_Email.get()
        rua= interface_Rua.get()
        numero= interface_Num.get()
        cidade= interface_Cidade.get()
        estado= interface_Estado.get()
        cep= interface_CEP.get()
        obs= interface_Obs.get(1.0, END)

        dic_validacao = {
            "nome": lambda x: bool(x),
            "documento": validar_Inteiro,
            "telefone": validar_Inteiro,
            "email": validar_email,
            "rua": lambda x: bool(x),
            "numero": validar_Inteiro,
            "cidade": lambda x: bool(x),
            "estado": lambda x: bool(x),
            "cep": validar_Inteiro
        }

        dic_dados = {
            "nome": nome,
            "documento": documento,
            "telefone": telefone,
            "email": email,
            "rua": rua,
            "numero": numero,
            "cidade": cidade,
            "estado": estado,
            "cep": cep,
            "obs": obs
        }

        for campo, valor in dic_dados.items():
            if campo != "obs" and not dic_validacao[campo](valor):
                messagebox.showerror("Erro", f"Campo inválido: {campo}")
                return

        root_path = os.path.dirname(__file__)
        config_path = os.path.join(root_path, "config.json")

        with open(config_path,"r", encoding="utf-8") as config_file:
            config_list = json.load(config_file)
        dt_base_path = config_list.get("db_path")

        files.Tabela_cliente_insert(dt_base_path, nome, documento, telefone, email, rua, numero, cidade, estado, cep, obs)
        messagebox.showinfo("Cadastro", "Cliente cadastrado com sucesso!")

    btn_Salvar= Button(new_client_app, text="Cadastrar Cliente", command=gravar_Dados)
    btn_Salvar.place(x=970, y=650, width=100, height=20)


    def cancelar():
        confirmar= messagebox.askyesno("Cancelar o Cadastro", "Deseja mesmo cancelar o cadastro?")
        if confirmar == True:
            new_client_app.grab_release()
            new_client_app.destroy()

    btn_Cancelar= Button(new_client_app, text="Cancelar", command=cancelar)
    btn_Cancelar.place(x=880, y=650, width=80, height=20)


    new_client_app.mainloop()
