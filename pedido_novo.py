from tkinter import *
from tkinter import messagebox, ttk

pedidos_cadastrados= []

def janela_pedidoNovo():
    app = Tk()
    app.title ("Clezer - miniERP")
    app.geometry ("1080x720")
    app.configure(background="#dde")

    lista_opcao= ["ID", "Documento", "Nome"]
    
    fr_titulo = Frame(app, background="#fff")
    fr_titulo.place(x=0, y=10, width=1080, height=25)
    titulo= Label(fr_titulo, text= "CADASTRO DE NOVO PEDIDO", background="#fff", foreground="#009", font= ("Arial", 12, "bold")).pack(expand=0)
    separador = "___________________________________________________________________________"

    Label(app, text="Pesquisar Cliente:", background="#dde", foreground="#009", anchor=W).place(x=10, y=50, width=100, height=20)
    pedido_Pesquisa= Entry(app)
    pedido_Pesquisa.place(x=115, y=50, width=250, height=20)
    pesquisa_opcao= ttk.Combobox(app, values=lista_opcao)
    pesquisa_opcao.place(x=370, y=50, width=90, height=20)
    pesquisa_opcao.set("ID")

    btn_pesquisa = Button(app, text="Buscar")
    btn_pesquisa.place(x=465, y=50, width=90, height=20)

    Label(app, text="Cliente:", background="#dde", foreground="#009", anchor=W).place(x=10, y=80, width=100, height=20)
    interface_Nome= Entry(app)
    interface_Nome.place(x=13, y=100, width=250, height=20)

    Label(app, text="Documento CPF/CNPJ:", background="#dde", foreground="#009", anchor=W).place(x=10, y=130, width=250, height=20)
    interface_Documento= Entry(app)
    interface_Documento.place(x=13, y=150, width=250, height=20)

    Label(app, text="Número do Pedido:", background="#dde", foreground="#009", anchor=W).place(x=10, y=180, width=200, height=20)
    interface_Fone= Entry(app)
    interface_Fone.place(x=13, y=200, width=250, height=20)

    Label(app, text="Ítens:", background="#dde", foreground="#009", anchor=W).place(x=10, y=230, width=100, height=20)
    interface_Email= Entry(app)
    interface_Email.place(x=13, y=250, width=250, height=20)

    # Label(app, text= separador, background="#dde", foreground="#009", anchor=W).place(x=10, y=200, width=250, height=20)

    Label(app, text="Valor:", background="#dde", foreground="#009", anchor=W).place(x=10, y=280, width=100, height=20)
    interface_Rua= Entry(app)
    interface_Rua.place(x=13, y=300, width=250, height=20)

    Label(app, text="Prazo:", background="#dde", foreground="#009", anchor=W).place(x=10, y=330, width=200, height=20)
    interface_Num= Entry(app)
    interface_Num.place(x=13, y=350, width=50, height=20)

    ## Botões

    def validar_Inteiro(valor):
        return valor.isdigit()

    def validar_email(valor):
        return "@" in valor and "." in valor

    def gravar_Dados():
        global pedidos_cadastrados

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

janela_pedidoNovo()