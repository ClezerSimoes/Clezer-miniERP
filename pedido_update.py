from tkinter import *
from tkinter import messagebox, ttk
import datetime
import sqlite3
import files
import os
import json

pedidos_cadastrados=[]

cliente_id = 0
nome = ""
documento = 0
telefone = 0
email = ""
endereço = ""
obs_cliente = ""

pedido_id = 0
data=""
valor=0
prazo=""
status=""
itens=""
obs_pedido = ""

def janela_pedidoUP(root, list_id):
    app = Toplevel(root)
    app.title ("Clezer - miniERP")
    app.geometry ("1080x720")
    app.configure(background="#dde")
    app.grab_set()
    
    fr_titulo1 = Frame(app, background="#fff")
    fr_titulo1.place(x=0, y=10, width=1080, height=25)
    titulo= Label(fr_titulo1, text= "ATUALIZAR PEDIDO", background="#fff", foreground="#009", font= ("Arial", 12, "bold"))
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

    Label(app, text="ID do Pedido:", background="#dde", foreground="#009", anchor=W).place(x=10, y=50, width=100, height=20)
    pedido_Pesquisa= Entry(app)
    pedido_Pesquisa.place(x=115, y=50, width=250, height=20)

    ## CAMPO CLIENTE
     
    Label(fr_cliente, text="ID:", background="#c8c8d9", foreground="#009", anchor=E).place(x=5, y=5, width=60, height=20)

    Label(fr_cliente, text="Nome:", background="#c8c8d9", foreground="#009", anchor=E).place(x=5, y=35, width=60, height=20)

    Label(fr_cliente, text="CPF/CNPJ:", background="#c8c8d9", foreground="#009", anchor=E).place(x=5, y=70, width=60, height=20)

    Label(fr_cliente, text="Telefone:", background="#c8c8d9", foreground="#009", anchor=E).place(x=5, y=105, width=60, height=20)

    Label(fr_cliente, text="E-mail:", background="#c8c8d9", foreground="#009", anchor=E).place(x=5, y=140, width=60, height=20)

    Label(fr_cliente, text="Enderço:", background="#c8c8d9", foreground="#009", anchor=E).place(x=5, y=175, width=60, height=20)

    Label(fr_cliente, text="Obs:", background="#c8c8d9", foreground="#009", anchor=E).place(x=5, y=220, width=60, height=20)

    
    def campos_clientes_branco():
        Label(fr_cliente, text="", background="#fff", foreground="#009", anchor=W).place(x=70, y=5, width=320, height=20)

        Label(fr_cliente, text="", background="#fff", foreground="#009", anchor=W).place(x=70, y=35, width=320, height=20)

        Label(fr_cliente, text="", background="#fff", foreground="#009", anchor=W).place(x=70, y=70, width=320, height=20)

        Label(fr_cliente, text="", background="#fff", foreground="#009", anchor=W).place(x=70, y=105, width=320, height=20)

        Label(fr_cliente, text="", background="#fff", foreground="#009", anchor=W).place(x=70, y=140, width=320, height=20)

        Label(fr_cliente, text="", background="#fff", foreground="#009", anchor=W).place(x=70, y=175, width=320, height=40)

        Label(fr_cliente, text="", background="#fff", foreground="#009", wraplength= 310, anchor=W).place(x=70, y=220, width=320, height=150)
    
    
    def campos_clientes_atualizar():
        Label(fr_cliente, text=cliente_id, background="#fff", foreground="#009", anchor=W).place(x=70, y=5, width=320, height=20)

        Label(fr_cliente, text=nome, background="#fff", foreground="#009", anchor=W).place(x=70, y=35, width=320, height=20)

        Label(fr_cliente, text=documento, background="#fff", foreground="#009", anchor=W).place(x=70, y=70, width=320, height=20)

        Label(fr_cliente, text=telefone, background="#fff", foreground="#009", anchor=W).place(x=70, y=105, width=320, height=20)

        Label(fr_cliente, text=email, background="#fff", foreground="#009", anchor=W).place(x=70, y=140, width=320, height=20)

        Label(fr_cliente, text=endereço, background="#fff", foreground="#009", wraplength= 310, justify= "left", anchor=NW).place(x=70, y=175, width=320, height=40)

        Label(fr_cliente, text=obs_cliente, background="#fff", foreground="#009", wraplength= 310, justify= "left", anchor=NW).place(x=70, y=220, width=320, height=150)

    ## CAMPO PEDIDOS

    Label(fr_pedido, text="Data (DD-MM-YYYY):", background="#c8c8d9", foreground="#009", anchor=E).place(x=5, y=5, width=130, height=20)
    Label(fr_pedido, text="Valor:", background="#c8c8d9", foreground="#009", anchor=E).place(x=5, y=35, width=130, height=20)
    Label(fr_pedido, text="Prazo (DD-MM-YYYY):", background="#c8c8d9", foreground="#009", anchor=E).place(x=5, y=70, width=130, height=20)
    Label(fr_pedido, text="Status:", background="#c8c8d9", foreground="#009", anchor=E).place(x=5, y=105, width=130, height=20)
    Label(fr_pedido, text="Itens:", background="#c8c8d9", foreground="#009", anchor=E).place(x=5, y=140, width=130, height=20)
    Label(fr_pedido, text="Obs:", background="#c8c8d9", foreground="#009", anchor=E).place(x=5, y=305, width=130, height=20)

    def campos_pedidos_atualizar():
        pedido_data = Label(fr_pedido, text=data, background="#fff", foreground="#009", anchor=W)
        pedido_data.place(x=140, y=5, width=320, height=20)

        pedido_valor = Label(fr_pedido, text=valor, background="#fff", foreground="#009", anchor=W)
        pedido_valor.place(x=140, y=35, width=320, height=20)

        pedido_prazo = Label(fr_pedido, text=prazo, background="#fff", foreground="#009", anchor=W)
        pedido_prazo.place(x=140, y=70, width=320, height=20)

        pedido_status = Label(fr_pedido, text=status, background="#fff", foreground="#009", anchor=W)
        pedido_status.place(x=140, y=105, width=320, height=20)

        pedido_itens= Label(fr_pedido, text=itens, background="#fff", foreground="#009", anchor=NW)
        pedido_itens.place(x=140, y=140, width=320, height=150)

        pedido_obs = Label(fr_pedido, text=obs_pedido, background="#fff", foreground="#009", anchor=NW)
        pedido_obs.place(x=140, y=305, width=320, height=150)

    def campos_pedidos_branco():
        Label(fr_pedido, text="", background="#fff", foreground="#009", anchor=W).place(x=140, y=5, width=320, height=20)
        Label(fr_pedido, text="", background="#fff", foreground="#009", anchor=W).place(x=140, y=35, width=320, height=20)
        Label(fr_pedido, text="", background="#fff", foreground="#009", anchor=W).place(x=140, y=70, width=320, height=20)
        Label(fr_pedido, text="", background="#fff", foreground="#009", anchor=W).place(x=140, y=105, width=320, height=20)
        Label(fr_pedido, text="", background="#fff", foreground="#009", anchor=W).place(x=140, y=140, width=320, height=150)
        Label(fr_pedido, text="", background="#fff", foreground="#009", anchor=W).place(x=140, y=305, width=320, height=150)

    ## Botões

    def validar_data(data: str) -> bool:
        try:
            # Tenta converter a string para o formato DD-MM-YYYY
            datetime.datetime.strptime(data, '%d-%m-%Y')
            return True  # Se não lançar exceção, a data é válida
        except ValueError:
            return False  # Se lançar exceção, a data é inválida

    def pesquisar():

        global cliente_id, nome, documento, telefone, email, endereço, rua, numero, cidade, estado, cep, obs_cliente

        global pedido_id, data, valor, prazo, status, itens, obs_pedido
        
        dt_base_path = files.sql_db_file()
        pesquisa = pedido_Pesquisa.get().strip()
        print(dt_base_path)

        try:
            conn = sqlite3.connect(dt_base_path)
            cursor = conn.cursor()
            cursor.execute(f'SELECT * FROM pedidos WHERE id = ?', (pesquisa,))
            pedido_select = cursor.fetchall()

            pedido_id = pedido_select[0][0]
            cliente_id = pedido_select[0][1]
            data = pedido_select[0][2]
            valor = pedido_select[0][3]
            prazo = pedido_select[0][4]
            itens = pedido_select[0][5]
            status = pedido_select[0][6]
            obs_pedido = pedido_select[0][7]

            cursor.execute(f'SELECT * FROM clientes WHERE id = ?', (cliente_id,))
            cliente_select = cursor.fetchall()

            cliente_id = cliente_select[0][0]
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
            obs_cliente = cliente_select[0][10]

            campos_clientes_atualizar()
            campos_pedidos_atualizar()

            conn.close()
        except sqlite3.Error as e:
            pedido_id=0
            campos_pedidos_branco()
            messagebox.showinfo("Erro", f"Erro no banco de dados: {e}")
        except:
            pedido_id=0
            campos_pedidos_branco()
            messagebox.showinfo("Erro", "Pedido não encontrado.")

    def janela_overwrite(campo_tb):
        global over_w

        over_w = Toplevel(app)
        over_w.title (f"Atualizar {campo_tb}")
        over_w.geometry ("320x200")
        over_w.configure(background="#dde")
        over_w.grab_set()

        def fechar_janela_overw():
            confirmar= messagebox.askyesno("Cancelar", "Deseja mesmo cancelar e voltar?")
            if confirmar == True:
                over_w.grab_release()
                over_w.destroy()
                app.grab_set()


        Label(over_w, text=f"Digite o novo(a) {campo_tb}:", background="#dde", foreground="#009", anchor=W).place(x=10, y=60, width=150, height=20)
        atualizar_campo= Entry(over_w)
        atualizar_campo.place(x=10, y=80, width=300, height=20)
        campo_atualizar = campo_tb

        def overwrite():

            global pedido_id
            dt_base_path = files.sql_db_file()
            campo_novo = atualizar_campo.get().strip()

            def sobrescrever_campos():
                try:
                    conn = sqlite3.connect(dt_base_path)
                    cursor = conn.cursor()
                    cursor.execute(f'UPDATE pedidos SET {campo_atualizar} = ? WHERE id = ?', (campo_novo, pedido_id,))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Sucesso", f"Campo {campo_atualizar} atualizado com sucesso!")

                    over_w.grab_release()
                    over_w.destroy()
                    app.grab_set()

                except sqlite3.Error as e:
                    campos_clientes_branco()
                    campos_pedidos_branco()
                    messagebox.showinfo("Erro", f"Erro no banco de dados: {e}")

            lista_status= ["aberto","concluído","atrasado"]

            if len(campo_novo) != 0:
                if campo_tb == "valor":
                    if campo_novo.isdigit():
                        sobrescrever_campos()
                        campos_pedidos_atualizar()
                    else:
                        messagebox.showinfo("Erro", "Campo inválido para esse dado, digite apenas números.")

                elif campo_tb == "data" or campo_tb == "prazo":
                    if validar_data(campo_novo):
                        sobrescrever_campos()
                        campos_pedidos_atualizar()
                    else:
                        messagebox.showinfo("Erro", "Campo inválido, digite uma data no formato DD-MM-AAAA.")
                elif campo_tb == "status":
                    if campo_novo.lower() in lista_status:
                        sobrescrever_campos()
                        campos_pedidos_atualizar()
                    else:
                        messagebox.showinfo("Erro", "Campo inválido. Tipos de status aceitos:\n-Aberto\n-Atrasado\n-Concluído.")

                else:
                    sobrescrever_campos()
            else:
                messagebox.showinfo("Erro", "O campo está vazio.")

        confirmar= Button(over_w, text=f"Atualizar {campo_tb}", command=overwrite)
        confirmar.place(x=190, y=150, width=120, height=20)

        cancelar= Button(over_w, text="Cancelar", command=fechar_janela_overw)
        cancelar.place(x=10, y=150, width=80, height=20)

        over_w.protocol("WM_DELETE_WINDOW", fechar_janela_overw)

    def overwrite_geral(campo):
        if pedido_id != 0:
            janela_overwrite(campo)
            campos_pedidos_atualizar()
        else:
            messagebox.showinfo("Erro", "Você precisa selecionar um pedido!")

    def voltar():
        global pedido_id
        confirmar= messagebox.askyesno("Cancelar o Cadastro", "ATENÇÂO!!! Todo dado não salvo será perdido.\nDeseja mesmo cancelar?")
        pedido_id=0
        if confirmar == True:
            app.grab_release()
            app.destroy()

    btn_Cancelar= Button(app, text="Voltar", command=voltar)
    btn_Cancelar.place(x=990, y=620, width=80, height=20)

    btn_pesquisa = Button(app, text="Pesquisar", command=pesquisar)
    btn_pesquisa.place(x=370, y=50, width=90, height=20)

    atualizar_data= Button(fr_pedido, text="Atualizar Data", command=lambda: overwrite_geral("data"))
    atualizar_data.place(x=470, y=5, width=100, height=20)

    atualizar_valor= Button(fr_pedido, text="Atualizar Valor", command=lambda: overwrite_geral("valor"))
    atualizar_valor.place(x=470, y=35, width=100, height=20)

    atualizar_prazo= Button(fr_pedido, text="Atualizar Prazo", command=lambda: overwrite_geral("prazo"))
    atualizar_prazo.place(x=470, y=70, width=100, height=20)

    atualizar_status= Button(fr_pedido, text="Atualizar Status", command=lambda: overwrite_geral("status"))
    atualizar_status.place(x=470, y=105, width=100, height=20)

    atualizar_itens= Button(fr_pedido, text="Atualizar Itens", command=lambda: overwrite_geral("itens"))
    atualizar_itens.place(x=470, y=140, width=100, height=20)

    atualizar_obs= Button(fr_pedido, text="Atualizar Obs", command=lambda: overwrite_geral("obs"))
    atualizar_obs.place(x=470, y=305, width=100, height=20)

    if list_id == None:
        campos_clientes_branco()
        campos_pedidos_branco()
    else:
        global cliente_id, nome, documento, telefone, email, endereço, rua, numero, cidade, estado, cep, obs_cliente

        global pedido_id, data, valor, prazo, status, itens, obs_pedido
        
        dt_base_path = files.sql_db_file()
        pesquisa = list_id
        pedido_Pesquisa.delete(0, END)
        pedido_Pesquisa.insert(0, list_id)
        print(dt_base_path)
        
        try:
            conn = sqlite3.connect(dt_base_path)
            cursor = conn.cursor()
            cursor.execute(f'SELECT * FROM pedidos WHERE id = ?', (pesquisa,))
            pedido_select = cursor.fetchall()

            pedido_id = pedido_select[0][0]
            cliente_id = pedido_select[0][1]
            data = pedido_select[0][2]
            valor = pedido_select[0][3]
            prazo = pedido_select[0][4]
            itens = pedido_select[0][5]
            status = pedido_select[0][6]
            obs_pedido = pedido_select[0][7]

            cursor.execute(f'SELECT * FROM clientes WHERE id = ?', (cliente_id,))
            cliente_select = cursor.fetchall()

            cliente_id = cliente_select[0][0]
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
            obs_cliente = cliente_select[0][10]

            campos_clientes_atualizar()
            campos_pedidos_atualizar()

            conn.close()
        except sqlite3.Error as e:
            campos_clientes_branco()
            campos_pedidos_branco()
            messagebox.showinfo("Erro", f"Erro no banco de dados: {e}")
            
    app.protocol("WM_DELETE_WINDOW", voltar)
    app.mainloop()
