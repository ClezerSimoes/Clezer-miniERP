from tkinter import *
from tkinter import messagebox
from tkinter import ttk


clientes_cadastrados= []

def janela_deleteCliente(root):
    app = Toplevel(root)
    app.title ("Clezer - miniERP")
    app.geometry ("500x450")
    app.configure(background="#dde")

    
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
    atualizar_filtro= ttk.Combobox(app, values=lista_filtro)
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

    atualizar_button= Button(app, text="Buscar", command=sobrescrever)
    atualizar_button.place(x=410, y=50, width=80, height=20)

    # fr_delete1= Frame(app, background= "#c8c8d9")
    # fr_delete1.place(x=10, y=80, width=550, height=500)

    fr_delete1 = Frame(app, background="#c8c8d9", borderwidth=2, relief="groove")
    fr_delete1.place(x=10, y=80, width=480, height=280)



    Label(fr_delete1, text="Dados do Cliente", background="#dee", foreground="#009", anchor=W, relief="groove").place(x=5, y=2, width=110, height=20)
    Label(fr_delete1, text="Descrição", background="#dee", foreground="#009", anchor=W, relief="groove").place(x=109, y=2, width=341, height=20)
    # Label(fr_atualizar1, text="Atualizar", background="#dee", foreground="#009", anchor=W, relief="groove").place(x=398, y=2, width=125, height=20)

    Label(fr_delete1, text="Nome", background="#c8c8d9", foreground="#009", anchor=W).place(x=5, y=25, width=100, height=20)
    Label(fr_delete1, text="Documentos", background="#c8c8d9", foreground="#009", anchor=W).place(x=5, y=50, width=100, height=20)
    Label(fr_delete1, text="Telefone", background="#c8c8d9", foreground="#009", anchor=W).place(x=5, y=75, width=100, height=20)
    Label(fr_delete1, text="E-mail", background="#c8c8d9", foreground="#009", anchor=W).place(x=5, y=100, width=100, height=20)
    Label(fr_delete1, text="Rua", background="#c8c8d9", foreground="#009", anchor=W).place(x=5, y=135, width=100, height=20)
    Label(fr_delete1, text="Numero", background="#c8c8d9", foreground="#009", anchor=W).place(x=5, y=160, width=100, height=20)
    Label(fr_delete1, text="Cidade", background="#c8c8d9", foreground="#009", anchor=W).place(x=5, y=185, width=100, height=20)
    Label(fr_delete1, text="Estado", background="#c8c8d9", foreground="#009", anchor=W).place(x=5, y=210, width=100, height=20)
    Label(fr_delete1, text="CEP", background="#c8c8d9", foreground="#009", anchor=W).place(x=5, y=235, width=100, height=20)

    Label(fr_delete1, text= separador, background="#c8c8d9", foreground="#009", anchor=W).place(x=0, y=115, width=450, height=15)

    Label(fr_delete1, text="Nome", background="#fff", foreground="#009", anchor=W).place(x=109, y=25, width=341, height=20)
    Label(fr_delete1, text="Documentos", background="#fff", foreground="#009", anchor=W).place(x=109, y=50, width=341, height=20)
    Label(fr_delete1, text="Telefone", background="#fff", foreground="#009", anchor=W).place(x=109, y=75, width=341, height=20)
    Label(fr_delete1, text="E-mail", background="#fff", foreground="#009", anchor=W).place(x=109, y=100, width=341, height=20)
    Label(fr_delete1, text="Rua", background="#fff", foreground="#009", anchor=W).place(x=109, y=135, width=341, height=20)
    Label(fr_delete1, text="Numero", background="#fff", foreground="#009", anchor=W).place(x=109, y=160, width=341, height=20)
    Label(fr_delete1, text="Cidade", background="#fff", foreground="#009", anchor=W).place(x=109, y=185, width=341, height=20)
    Label(fr_delete1, text="Estado", background="#fff", foreground="#009", anchor=W).place(x=109, y=210, width=341, height=20)
    Label(fr_delete1, text="CEP", background="#fff", foreground="#009", anchor=W).place(x=109, y=235, width=341, height=20)


    def deletar():
        cliente = atualizar_busca.get().strip()
        filtro = atualizar_filtro.get()

        if filtro == "ID":
            print("minha nossa")
            
        elif filtro == "Documento":
            print("oloco meu")
            
        elif filtro == "Nome":
            print("ok")
        
        else: 
            print("Deu erro")

    def cancelar():
        confirmar= messagebox.askyesno("Cancelar", "Deseja mesmo cancelar e voltar?")
        if confirmar == True:
            app.destroy()


    atualizar_doc= Button(app, text="Deletar", command=deletar)
    atualizar_doc.place(x=400, y=400, width=80, height=20)

    atualizar_fone= Button(app, text="Voltar", command=cancelar)
    atualizar_fone.place(x=10, y=400, width=80, height=20)


    app.mainloop()

