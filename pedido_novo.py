from tkinter import *
from tkinter import messagebox, ttk
import datetime
import sqlite3
import files
import os
import json

pedidos_cadastrados=[]

client_id = 0
nome = ""
documento = 0
telefone = 0
email = ""
endereço = ""
obs = ""
def janela_pedidoNovo(root):
    app = Toplevel(root)
    app.title ("Clezer - miniERP")
    app.geometry ("1080x720")
    app.configure(background="#dde")
    app.grab_set()

    lista_opcao= ["ID", "Documento"]
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

    ## CAMPO PESQUISA

    Label(app, text="Selecione o Cliente:", background="#dde", foreground="#009", anchor=W).place(x=10, y=50, width=110, height=20)
    pedido_Pesquisa= Entry(app)
    pedido_Pesquisa.place(x=125, y=50, width=284, height=20)
    filtro_pesquisa= ttk.Combobox(app, values=lista_opcao)
    filtro_pesquisa.place(x=415, y=50, width=90, height=20)
    filtro_pesquisa.set("ID")

    ## CAMPO CLIENTE
     
    Label(fr_cliente, text="ID:", background="#c8c8d9", foreground="#009", anchor=E).place(x=5, y=5, width=60, height=20)

    Label(fr_cliente, text="Cliente:", background="#c8c8d9", foreground="#009", anchor=E).place(x=5, y=35, width=60, height=20)

    Label(fr_cliente, text="CPF/CNPJ:", background="#c8c8d9", foreground="#009", anchor=E).place(x=5, y=70, width=60, height=20)

    Label(fr_cliente, text="Telefone:", background="#c8c8d9", foreground="#009", anchor=E).place(x=5, y=105, width=60, height=20)

    Label(fr_cliente, text="E-mail:", background="#c8c8d9", foreground="#009", anchor=E).place(x=5, y=140, width=60, height=20)

    Label(fr_cliente, text="Enderço:", background="#c8c8d9", foreground="#009", anchor=E).place(x=5, y=175, width=60, height=20)

    Label(fr_cliente, text="Obs:", background="#c8c8d9", foreground="#009", anchor=E).place(x=5, y=220, width=60, height=20)
    
    def campos_branco():
        Label(fr_cliente, text="", background="#fff", foreground="#009", anchor=W).place(x=70, y=5, width=320, height=20)

        Label(fr_cliente, text="", background="#fff", foreground="#009", anchor=W).place(x=70, y=35, width=320, height=20)

        Label(fr_cliente, text="", background="#fff", foreground="#009", anchor=W).place(x=70, y=70, width=320, height=20)

        Label(fr_cliente, text="", background="#fff", foreground="#009", anchor=W).place(x=70, y=105, width=320, height=20)

        Label(fr_cliente, text="", background="#fff", foreground="#009", anchor=W).place(x=70, y=140, width=320, height=20)

        Label(fr_cliente, text="", background="#fff", foreground="#009", anchor=W).place(x=70, y=175, width=320, height=40)

        Label(fr_cliente, text="", background="#fff", foreground="#009", wraplength= 310, anchor=W).place(x=70, y=220, width=320, height=150)
    
    def campos_atualizados():
        Label(fr_cliente, text=client_id, background="#fff", foreground="#009", anchor=W).place(x=70, y=5, width=320, height=20)

        Label(fr_cliente, text=nome, background="#fff", foreground="#009", anchor=W).place(x=70, y=35, width=320, height=20)

        Label(fr_cliente, text=documento, background="#fff", foreground="#009", anchor=W).place(x=70, y=70, width=320, height=20)

        Label(fr_cliente, text=telefone, background="#fff", foreground="#009", anchor=W).place(x=70, y=105, width=320, height=20)

        Label(fr_cliente, text=email, background="#fff", foreground="#009", anchor=W).place(x=70, y=140, width=320, height=20)

        Label(fr_cliente, text=endereço, background="#fff", foreground="#009", wraplength= 310, justify= "left", anchor=NW).place(x=70, y=175, width=320, height=40)

        Label(fr_cliente, text=obs, background="#fff", foreground="#009", wraplength= 310, justify= "left", anchor=NW).place(x=70, y=220, width=320, height=150)

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

    def buscar():

        global client_id, nome, documento, telefone, email, endereço, rua, numero, cidade, estado, cep, obs
        
        dt_base_path = files.sql_db_file()
        pesquisa = pedido_Pesquisa.get().strip()
        filtro = filtro_pesquisa.get().lower()
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
            endereço = (f"Rua {rua}, n° {numero}, {cidade}-{estado}, CEP: {cep}")
            obs = cliente_select[0][10]

            campos_atualizados()

            conn.close()
        except sqlite3.Error as e:
            campos_branco()
            messagebox.showinfo("Erro", f"Erro no banco de dados: {e}")
        except:
            campos_branco()
            messagebox.showinfo("Erro", "Cliente não encontrado.")

    def validar_Inteiro(valor):
        return valor.isdigit()

    def validar_texto(texto):
        return len(texto) > 1
    
    def validar_data(data: str) -> bool:
        try:
            # Tenta converter a string para o formato DD-MM-YYYY
            datetime.datetime.strptime(data, '%d-%m-%Y')
            return True  # Se não lançar exceção, a data é válida
        except ValueError:
            return False  # Se lançar exceção, a data é inválida

    def gravar_dados():
        global pedidos_cadastrados
        global client_id

        if client_id == 0:
            messagebox.showinfo("ERRO", "Nenhum cliente Selecionado!!")
        else:
            cliente_id_pedido = client_id
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
                "itens": validar_texto,
                "status": lambda x: bool(x)
            }

            dic_dados = {
                "clienteID": cliente_id_pedido,
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

            root_path = os.path.dirname(__file__)
            config_path = os.path.join(root_path, "config.json")

            with open(config_path,"r", encoding="utf-8") as config_file:
                config_list = json.load(config_file)
            dt_base_path = config_list.get("db_path")

            pedido_data.delete(0, END)
            pedido_valor.delete(0, END)
            pedido_prazo.delete(0, END)
            pedido_status.set("Aberto")
            pedido_itens.delete(1.0, END)
            pedido_obs.delete(1.0, END)

            files.Tabela_pedido_insert(dt_base_path, client_id, data, valor, prazo, itens, status, obs)
            messagebox.showinfo("Cadastro", "Pedido cadastrado com sucesso!")

    btn_Salvar= Button(app, text="Salvar Pedido", command=gravar_dados)
    btn_Salvar.place(x=970, y=620, width=100, height=20)

    def cancelar():
        global client_id
        client_id = 0
        confirmar= messagebox.askyesno("Cancelar o Cadastro", "ATENÇÂO!!! Todo dado não salvo será perdido.\nDeseja mesmo cancelar?")
        if confirmar == True:
            app.grab_release()
            app.destroy()

    campos_branco()

    btn_Cancelar= Button(app, text="Cancelar", command=cancelar)
    btn_Cancelar.place(x=880, y=620, width=80, height=20)

    btn_pesquisa = Button(app, text="Buscar", command=buscar)
    btn_pesquisa.place(x=510, y=50, width=90, height=20)


    app.mainloop()
