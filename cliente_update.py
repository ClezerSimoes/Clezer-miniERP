from tkinter import *
from tkinter import messagebox
from tkinter import ttk


def janela_clienteUP(root):
    app = Toplevel(root)
    app.title ("Clezer - miniERP")
    app.geometry ("550x550")
    app.configure(background="#dde")

    clientes_cadastrados= []
    lista_opcao= ["ID", "Documento", "Nome"]

    def sobrescrever():
        print ("Contato Atualizado")

    ## Campos 

    separador = "_____________________________________________________________________________________________________________________"

    atualizar_titulo= Label(app, text= "ATUALIZAR CADASTRO CLIENTE", background="#fff", foreground="#009", anchor=N, font= ("Arial", 12, "bold"))
    atualizar_titulo.place(x=0, y=10, width=550, height=25)

    Label(app, text="Filtrar por:", background="#dde", foreground="#009", anchor=W).place(x=10, y=50, width=60, height=20)
    atualizar_opcao= ttk.Combobox(app, values=lista_opcao)
    atualizar_opcao.place(x=70, y=50, width=90, height=20)
    atualizar_opcao.set("ID")

    def on_focus_in(event):
        if atualizar_busca.get() == "Digite aqui...":
            atualizar_busca.delete(0, END)
            atualizar_busca.config(fg="black")

    def on_focus_out(event):
        if atualizar_busca.get() == "":
            atualizar_busca.insert(0, "Digite aqui...")
            atualizar_busca.config(fg="gray")

    atualizar_busca= Entry(app, fg="gray")
    atualizar_busca.place(x=165, y=50, width=270, height=20)
    atualizar_busca.insert(0, "Digite aqui...")
    atualizar_busca.bind("<FocusIn>", on_focus_in)
    atualizar_busca.bind("<FocusOut>", on_focus_out)

    atualizar_button= Button(app, text="Buscar", command=sobrescrever)
    atualizar_button.place(x=440, y=50, width=100, height=20)

    fr_atualizar1= Frame(app, background="#c8c8d9", borderwidth=2, relief="groove")
    fr_atualizar1.place(x=10, y=80, width=530, height=300)



    Label(fr_atualizar1, text="Dados do Cliente", background="#dee", foreground="#009", anchor=W, relief="groove").place(x=5, y=2, width=110, height=20)
    Label(fr_atualizar1, text="Descrição", background="#dee", foreground="#009", anchor=W, relief="groove").place(x=109, y=2, width=400, height=20)
    Label(fr_atualizar1, text="Atualizar", background="#dee", foreground="#009", anchor=W, relief="groove").place(x=398, y=2, width=125, height=20)

    Label(fr_atualizar1, text="Nome", background="#c8c8d9", foreground="#009", anchor=W).place(x=5, y=25, width=100, height=20)
    Label(fr_atualizar1, text="Documentos", background="#c8c8d9", foreground="#009", anchor=W).place(x=5, y=50, width=100, height=20)
    Label(fr_atualizar1, text="Telefone", background="#c8c8d9", foreground="#009", anchor=W).place(x=5, y=75, width=100, height=20)
    Label(fr_atualizar1, text="E-mail", background="#c8c8d9", foreground="#009", anchor=W).place(x=5, y=100, width=100, height=20)
    Label(fr_atualizar1, text="Rua", background="#c8c8d9", foreground="#009", anchor=W).place(x=5, y=135, width=100, height=20)
    Label(fr_atualizar1, text="Numero", background="#c8c8d9", foreground="#009", anchor=W).place(x=5, y=160, width=100, height=20)
    Label(fr_atualizar1, text="Cidade", background="#c8c8d9", foreground="#009", anchor=W).place(x=5, y=185, width=100, height=20)
    Label(fr_atualizar1, text="Estado", background="#c8c8d9", foreground="#009", anchor=W).place(x=5, y=210, width=100, height=20)
    Label(fr_atualizar1, text="CEP", background="#c8c8d9", foreground="#009", anchor=W).place(x=5, y=235, width=100, height=20)

    Label(fr_atualizar1, text= separador, background="#c8c8d9", foreground="#009", anchor=W).place(x=0, y=115, width=520, height=15)

    Label(fr_atualizar1, text="Nome", background="#fff", foreground="#009", anchor=W).place(x=109, y=25, width=285, height=20)
    Label(fr_atualizar1, text="Documentos", background="#fff", foreground="#009", anchor=W).place(x=109, y=50, width=285, height=20)
    Label(fr_atualizar1, text="Telefone", background="#fff", foreground="#009", anchor=W).place(x=109, y=75, width=285, height=20)
    Label(fr_atualizar1, text="E-mail", background="#fff", foreground="#009", anchor=W).place(x=109, y=100, width=285, height=20)
    Label(fr_atualizar1, text="Rua", background="#fff", foreground="#009", anchor=W).place(x=109, y=135, width=285, height=20)
    Label(fr_atualizar1, text="Numero", background="#fff", foreground="#009", anchor=W).place(x=109, y=160, width=285, height=20)
    Label(fr_atualizar1, text="Cidade", background="#fff", foreground="#009", anchor=W).place(x=109, y=185, width=285, height=20)
    Label(fr_atualizar1, text="Estado", background="#fff", foreground="#009", anchor=W).place(x=109, y=210, width=285, height=20)
    Label(fr_atualizar1, text="CEP", background="#fff", foreground="#009", anchor=W).place(x=109, y=235, width=285, height=20)


    def janela_sobrescrever():
        sobres = Toplevel(app)
        sobres.title ("Atualizar Nome")
        sobres.geometry ("320x200")
        sobres.configure(background="#dde")


        Label(sobres, text="Digite o novo nome:", background="#dde", foreground="#009", anchor=W).place(x=10, y=60, width=150, height=20)
        atualizar_busca= Entry(sobres)
        atualizar_busca.place(x=10, y=80, width=300, height=20)

        confirmar= Button(sobres, text="Atualizar Nome", command=sobrescrever)
        confirmar.place(x=190, y=150, width=120, height=20)

        cancelar= Button(sobres, text="Cancelar", command=sobrescrever)
        cancelar.place(x=10, y=150, width=80, height=20)

    
    atualizar_nome= Button(fr_atualizar1, text="Atualizar Nome", command=janela_sobrescrever)
    atualizar_nome.place(x=400, y=25, width=120, height=20)

    atualizar_doc= Button(fr_atualizar1, text="Atualizar Documento", command=janela_sobrescrever)
    atualizar_doc.place(x=400, y=50, width=120, height=20)

    atualizar_fone= Button(fr_atualizar1, text="Atualizar Telefone", command=sobrescrever)
    atualizar_fone.place(x=400, y=75, width=120, height=20)

    atualizar_email= Button(fr_atualizar1, text="Atualizar E-mail", command=sobrescrever)
    atualizar_email.place(x=400, y=100, width=120, height=20)

    atualizar_endereco= Button(fr_atualizar1, text="Atualizar Rua", command=sobrescrever)
    atualizar_endereco.place(x=400, y=135, width=120, height=20)

    atualizar_endereco= Button(fr_atualizar1, text="Atualizar Número", command=sobrescrever)
    atualizar_endereco.place(x=400, y=160, width=120, height=20)

    atualizar_endereco= Button(fr_atualizar1, text="Atualizar Cidade", command=sobrescrever)
    atualizar_endereco.place(x=400, y=185, width=120, height=20)

    atualizar_endereco= Button(fr_atualizar1, text="Atualizar Estado", command=sobrescrever)
    atualizar_endereco.place(x=400, y=210, width=120, height=20)

    atualizar_endereco= Button(fr_atualizar1, text="Atualizar CEP", command=sobrescrever)
    atualizar_endereco.place(x=400, y=235, width=120, height=20)

    def voltar():
        confirmar= messagebox.askyesno("Cancelar", "Deseja mesmo cancelar e voltar?")
        if confirmar == True:
            app.destroy()

    atualizar_fone= Button(app, text="Voltar", command=voltar)
    atualizar_fone.place(x=460, y=500, width=80, height=20)


    app.mainloop()
    