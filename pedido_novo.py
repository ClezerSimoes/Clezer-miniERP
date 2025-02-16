from tkinter import *
from tkinter import messagebox, ttk
import datetime

pedidos_cadastrados=[]

def janela_pedidoNovo(root):
    app = Toplevel(root)
    app.title ("Clezer - miniERP")
    app.geometry ("1080x720")
    app.configure(background="#dde")

    lista_opcao= ["ID", "Documento", "Nome"]
    lista_status= ["Aberto","Concluído","Atrasado"]
    
    fr_titulo1 = Frame(app, background="#fff")
    fr_titulo1.place(x=0, y=10, width=1080, height=25)
    titulo= Label(fr_titulo1, text= "CADASTRO DE NOVO PEDIDO", background="#fff", foreground="#009", font= ("Arial", 12, "bold"))
    titulo.pack(expand=0)

    fr_cliente = Frame(app, background="#c8c8d9", borderwidth=2, relief="groove")
    fr_cliente.place(x=10, y=110, width=400, height=500)
    titulo_cliente= Label(app, text= "CLIENTE", background="#dde", foreground="#009", anchor=W, font= ("Arial", 11, "bold"))
    titulo_cliente.place(x=10, y=85, width=80,height=25)

    fr_pedido= Frame(app, background="#c8c8d9", borderwidth=2, relief="groove")
    fr_pedido.place(x=415, y=110, width=655, height=500)
    titulo_pedido= Label(app, text= "PEDIDO", background="#dde", foreground="#009", anchor=W, font= ("Arial", 11, "bold"))
    titulo_pedido.place(x=415, y=85, width=80,height=25)

    separador = "___________________________________________________________________________"

    ## CAMPO PESQUISA

    Label(app, text="Pesquisar Cliente:", background="#dde", foreground="#009", anchor=W).place(x=10, y=50, width=100, height=20)
    pedido_Pesquisa= Entry(app)
    pedido_Pesquisa.place(x=115, y=50, width=250, height=20)
    pesquisa_opcao= ttk.Combobox(app, values=lista_opcao)
    pesquisa_opcao.place(x=370, y=50, width=90, height=20)
    pesquisa_opcao.set("ID")

    btn_pesquisa = Button(app, text="Buscar")
    btn_pesquisa.place(x=465, y=50, width=90, height=20)

    ## CAMPO CLIENTE
     
    Label(fr_cliente, text="Cliente:", background="#c8c8d9", foreground="#009", anchor=E).place(x=5, y=5, width=60, height=20)
    cliente_Nome= Entry(fr_cliente)
    cliente_Nome.place(x=70, y=5, width=320, height=20)

    Label(fr_cliente, text="CPF/CNPJ:", background="#c8c8d9", foreground="#009", anchor=E).place(x=5, y=35, width=60, height=20)
    cliente_Documento= Entry(fr_cliente)
    cliente_Documento.place(x=70, y=35, width=320, height=20)

    Label(fr_cliente, text="Telefone:", background="#c8c8d9", foreground="#009", anchor=E).place(x=5, y=70, width=60, height=20)
    cliente_Fone= Entry(fr_cliente)
    cliente_Fone.place(x=70, y=70, width=320, height=20)

    Label(fr_cliente, text="E-mail:", background="#c8c8d9", foreground="#009", anchor=E).place(x=5, y=105, width=60, height=20)
    cliente_Email= Entry(fr_cliente)
    cliente_Email.place(x=70, y=105, width=320, height=20)

    Label(fr_cliente, text="Endereço:", background="#c8c8d9", foreground="#009", anchor=E).place(x=5, y=140, width=60, height=20)
    cliente_Rua= Entry(fr_cliente)
    cliente_Rua.place(x=70, y=140, width=320, height=20)

    Label(fr_cliente, text="Obs:", background="#c8c8d9", foreground="#009", anchor=E).place(x=5, y=175, width=60, height=20)
    cliente_Num= Entry(fr_cliente)
    cliente_Num.place(x=70, y=175, width=320, height=20)

    ## CAMPO PEDIDOS

    Label(fr_pedido, text="Data (DD-MM-YYYY):", background="#c8c8d9", foreground="#009", anchor=E).place(x=5, y=5, width=130, height=20)
    pedido_data= Entry(fr_pedido)
    pedido_data.place(x=140, y=5, width=320, height=20)

    Label(fr_pedido, text="Valor:", background="#c8c8d9", foreground="#009", anchor=E).place(x=5, y=35, width=130, height=20)
    pedido_valor= Entry(fr_pedido)
    pedido_valor.place(x=140, y=35, width=320, height=20)

    Label(fr_pedido, text="Prazo (DD-MM-YYYY):", background="#c8c8d9", foreground="#009", anchor=E).place(x=5, y=70, width=130, height=20)
    pedido_prazo= Entry(fr_pedido)
    pedido_prazo.place(x=140, y=70, width=320, height=20)

    Label(fr_pedido, text="Status:", background="#c8c8d9", foreground="#009", anchor=E).place(x=5, y=105, width=130, height=20)
    pedido_status= ttk.Combobox(fr_pedido, values=lista_status)
    pedido_status.place(x=140, y=105, width=320, height=20)
    pedido_status.set("Aberto")

    Label(fr_pedido, text="Itens:", background="#c8c8d9", foreground="#009", anchor=E).place(x=5, y=140, width=130, height=20)
    pedido_itens= Text(fr_pedido)
    pedido_itens.place(x=140, y=140, width=320, height=150)

    Label(fr_pedido, text="Obs:", background="#c8c8d9", foreground="#009", anchor=E).place(x=5, y=305, width=130, height=20)
    pedido_obs= Text(fr_pedido)
    pedido_obs.place(x=140, y=305, width=320, height=150)

    ## Botões

    def validar_Inteiro(valor):
        return valor.isdigit()

    def validar_data(data: str) -> bool:
        try:
            # Tenta converter a string para o formato DD-MM-YYYY
            datetime.datetime.strptime(data, '%d-%m-%Y')
            return True  # Se não lançar exceção, a data é válida
        except ValueError:
            return False  # Se lançar exceção, a data é inválida

    def gravar_Dados():
        global pedidos_cadastrados
        
        print ("Dados Salvos")
        cliente = "ID" # pegar do cliente 
        data= pedido_data.get().strip()
        valor= pedido_valor.get()
        prazo= pedido_prazo.get()
        status= pedido_status.get()
        itens= pedido_itens.get(1.0, END)
        obs= pedido_obs.get(1.0, END)

        dic_validacao = {
            "clienteID": lambda x: bool(x),
            "data": validar_data,
            "valor": validar_Inteiro,
            "prazo": validar_data,
            "itens": lambda x: bool(x)
        }

        dic_dados = {
            "clienteID": cliente,
            "data": data,
            "valor": valor,
            "prazo": prazo,
            "status": status,
            "itens": itens,
            "obs": obs
        }

        for campo, valor in dic_dados.items():
            if campo != "obs" and not dic_validacao[campo](valor):
                messagebox.showerror("Erro", f"Campo inválido: {campo}")
                return

        pedidos_cadastrados.append(dic_dados)
        print (f"Clientes cadastrados: {pedidos_cadastrados}")
        messagebox.showinfo("Cadastro", "Cliente cadastrado com sucesso!")

    btn_Salvar= Button(app, text="Salvar Pedido", command=gravar_Dados)
    btn_Salvar.place(x=970, y=620, width=100, height=20)


    def cancelar():
        messagebox.showwarning("Atenção","ATENÇÂO!!!\nTodo dado não salvo será perdido.")
        confirmar= messagebox.askyesno("Cancelar o Cadastro", "Deseja mesmo cancelar?")
        if confirmar == True:
            app.destroy()

    btn_Cancelar= Button(app, text="Cancelar", command=cancelar)
    btn_Cancelar.place(x=880, y=620, width=80, height=20)


    app.mainloop()
