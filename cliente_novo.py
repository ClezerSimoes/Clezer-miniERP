from tkinter import *
from tkinter import messagebox


def janela_clienteNovo():
    app = Tk()
    app.title ("Clezer - miniERP")
    app.geometry ("1080x720")
    app.configure(background="#dde")

    clientes_cadastrados= []

    ## INTERFACE Cliente

    """ anchor =>   N = North 
                    S = South
                    E = East
                    W = West
    """
    ## Campos 

    separador = "___________________________________________________________________________"

    Label(app, text="Nome:", background="#dde", foreground="#009", anchor=W).place(x=10, y=10, width=100, height=20)
    interface_Nome= Entry(app)
    interface_Nome.place(x=13, y=30, width=250, height=20)

    Label(app, text="Documento CPF/CNPJ (Apenas Números):", background="#dde", foreground="#009", anchor=W).place(x=10, y=60, width=250, height=20)
    interface_Documento= Entry(app)
    interface_Documento.place(x=13, y=80, width=250, height=20)

    Label(app, text="Telefone (Apenas Números):", background="#dde", foreground="#009", anchor=W).place(x=10, y=110, width=200, height=20)
    interface_Fone= Entry(app)
    interface_Fone.place(x=13, y=130, width=250, height=20)

    Label(app, text="E-mail:", background="#dde", foreground="#009", anchor=W).place(x=10, y=160, width=100, height=20)
    interface_Email= Entry(app)
    interface_Email.place(x=13, y=180, width=250, height=20)

    Label(app, text= separador, background="#dde", foreground="#009", anchor=W).place(x=10, y=200, width=250, height=20)

    Label(app, text="Endereço", background="#dde", foreground="#009", anchor=W).place(x=10, y=225, width=100, height=20)

    Label(app, text="Rua:", background="#dde", foreground="#009", anchor=W).place(x=10, y=250, width=100, height=20)
    interface_Rua= Entry(app)
    interface_Rua.place(x=13, y=270, width=250, height=20)

    Label(app, text="Num (Apenas Números):", background="#dde", foreground="#009", anchor=W).place(x=10, y=300, width=200, height=20)
    interface_Num= Entry(app)
    interface_Num.place(x=13, y=320, width=50, height=20)

    Label(app, text="Cidade:", background="#dde", foreground="#009", anchor=W).place(x=10, y=350, width=100, height=20)
    interface_Cidade= Entry(app)
    interface_Cidade.place(x=13, y=370, width=250, height=20)

    Label(app, text="Estado:", background="#dde", foreground="#009", anchor=W).place(x=10, y=400, width=100, height=20)
    interface_Estado= Entry(app)
    interface_Estado.place(x=13, y=420, width=250, height=20)

    Label(app, text="CEP (Apenas Números):", background="#dde", foreground="#009", anchor=W).place(x=10, y=450, width=200, height=20)
    interface_CEP= Entry(app)
    interface_CEP.place(x=13, y=470, width=250, height=20)

    Label(app, text= separador, background="#dde", foreground="#009", anchor=W).place(x=10, y=490, width=250, height=20)

    Label(app, text="Obs:", background="#dde", foreground="#009", anchor=W).place(x=10, y=510, width=100, height=20)
    interface_Obs= Text(app)
    interface_Obs.place(x=13, y=530, width=250, height=100)

    ## Botões

    def validar_Inteiro(valor):
        return valor.isdigit()

    def validar_email(valor):
        return "@" in valor and "." in valor

    def gravar_Dados():
        global clientes_cadastrados

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

        clientes_cadastrados.append(dic_dados)
        print (f"Clientes cadastrados: {clientes_cadastrados}")
        messagebox.showinfo("Cadastro", "Cliente cadastrado com sucesso!")

    btn_Salvar= Button(app, text="Salvar Cliente", command=gravar_Dados)
    btn_Salvar.place(x=160, y=650, width=100, height=20)


    def cancelar():
        messagebox.showwarning("Atenção","ATENÇÂO!!!\nTodo dado não salvo será perdido.")
        confirmar= messagebox.askyesno("Cancelar o Cadastro", "Deseja mesmo cancelar?")
        if confirmar == TRUE:
            app.quit()

    btn_Cancelar= Button(app, text="Cancelar", command=cancelar)
    btn_Cancelar.place(x=13, y=650, width=80, height=20)


    app.mainloop()