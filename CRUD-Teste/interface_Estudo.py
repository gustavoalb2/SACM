import tkinter as tk
from tkinter import messagebox
import bd
import ttkbootstrap as ttk


class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title('Sistema')
        self.janela.geometry('500x400')

        menubar = ttk.Menu(app)
        app.config(menu=menubar)

        produto_menu = ttk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Produto", menu=produto_menu)
        produto_menu.add_command(label="Cadastrar Droga", command=self.cadastrar_droga)
        produto_menu.add_command(label="Cadastrar Arma", command=self.cadastrar_arma)
        produto_menu.add_command(label="Listar Drogas", command=self.listar_drogas)
        produto_menu.add_command(label="Listar Armas", command=self.listar_armas)

    def cadastrar_droga(self):
        self.top_cadastroDroga = tk.Toplevel(self.janela)
        self.lbl_nome = ttk.Label(self.top_cadastroDroga, text='Nome: ')
        self.lbl_nome.grid(row=0, column=0, padx=(5, 2))
        self.ent_nome = ttk.Entry(self.top_cadastroDroga)
        self.ent_nome.grid(row=0, column=1, padx=(5, 2))

        self.lbl_quantidade = ttk.Label(self.top_cadastroDroga, text='Quantidade: ')
        self.lbl_quantidade.grid(row=1, column=0, padx=(5, 2))
        self.ent_quantidade = ttk.Entry(self.top_cadastroDroga)
        self.ent_quantidade.grid(row=1, column=1, padx=(5, 2))

        self.lbl_preco = ttk.Label(self.top_cadastroDroga, text='Preço: ')
        self.lbl_preco.grid(row=2, column=0, padx=(5, 2))
        self.ent_preco = ttk.Entry(self.top_cadastroDroga)
        self.ent_preco.grid(row=2, column=1, padx=(5, 2))

        self.btn_confirmar = ttk.Button(self.top_cadastroDroga, text='Confirmar',
                                        command=self.salvar_droga)
        self.btn_confirmar.grid(row=3, column=0, columnspan=2, pady=10)

    def salvar_droga(self):
        nome = self.ent_nome.get()
        quantidade = self.ent_quantidade.get()
        preco = self.ent_preco.get()
        bd.inserir_droga(nome, quantidade, preco)
        self.top_cadastroDroga.destroy()

    def cadastrar_arma(self):
        self.top_cadastroArma = tk.Toplevel(self.janela)
        self.lbl_nome = ttk.Label(self.top_cadastroArma, text='Nome: ')
        self.lbl_nome.grid(row=0, column=0, padx=(5, 2))
        self.ent_nome = ttk.Entry(self.top_cadastroArma)
        self.ent_nome.grid(row=0, column=1, padx=(5, 2))

        self.lbl_tipo = ttk.Label(self.top_cadastroArma, text='Tipo: ')
        self.lbl_tipo.grid(row=1, column=0, padx=(5, 2))
        self.ent_tipo = ttk.Entry(self.top_cadastroArma)
        self.ent_tipo.grid(row=1,column=1, padx=(5, 2))

        self.lbl_calibre = ttk.Label(self.top_cadastroArma, text='Calibre: ')
        self.lbl_calibre.grid(row=2, column=0, padx=(5, 2))
        self.ent_calibre = ttk.Entry(self.top_cadastroArma)
        self.ent_calibre.grid(row=2,column=1, padx=(5, 2))

        self.btn_confirmar = ttk.Button(self.top_cadastroArma, text='Confirmar',
                                        command=self.salvar_arma)
        self.btn_confirmar.grid(row=3, column=0, columnspan=2, pady=10)

    def salvar_arma(self):
        nome = self.ent_nome.get()
        tipo = self.ent_tipo.get()
        calibre = self.ent_calibre.get()
        bd.inserir_arma(nome, tipo, calibre)
        self.tvw_atualizarArma()
        self.top_cadastroArma.destroy()

    def listar_drogas(self):
        self.top_listarDroga = tk.Toplevel(self.janela)
        colunas = ['id', 'nome', 'quantidade', 'preco']
        self.tvw_droga = ttk.Treeview(self.top_listarDroga, columns=colunas, show='headings')
        self.tvw_droga.heading('id', text='ID')
        self.tvw_droga.heading('nome', text='Nome')
        self.tvw_droga.heading('quantidade', text='Quantidade')
        self.tvw_droga.heading('preco', text='Preço')
        self.tvw_droga.pack()

        for droga in bd.listar_drogas():
            self.tvw_droga.insert('', 'end', values=droga)

    def listar_armas(self):
        self.top_listarArma = tk.Toplevel(self.janela)
        self.frame_tvw = tk.Frame(self.top_listarArma)
        self.frame_tvw.pack()
        colunas = ['id', 'nome', 'tipo', 'calibre']
        self.tvw_arma = ttk.Treeview(self.frame_tvw, columns=colunas, show='headings')
        self.tvw_arma.heading('id', text='ID')
        self.tvw_arma.heading('nome', text='Nome')
        self.tvw_arma.heading('tipo', text='Tipo')
        self.tvw_arma.heading('calibre', text='Calibre')
        self.tvw_arma.pack()

        self.frame_btn = tk.Frame(self.top_listarArma)
        self.frame_btn.pack()
        self.btn_inserir = tk.Button(self.frame_btn, text="INSERIR", command=self.cadastrar_arma)
        self.btn_inserir.grid(column=3,row=0)

        self.btn_excloi = tk.Button(self.frame_btn, text="EXCLUIR", command=self.excluir_arma)
        self.btn_excloi.grid(column=2,row=0)


        self.btn_edita = tk.Button(self.frame_btn, text="EDTIA", command=self.editar_arma)
        self.btn_edita.grid(column=1,row=0)

        self.tvw_atualizarArma()

    def tvw_atualizarArma(self):
        for i in self.tvw_arma.get_children():
            self.tvw_arma.delete(i)
        for arma in bd.listar_armas():
            self.tvw_arma.insert('', 'end', values=arma)

    def excluir_arma(self):
        selecionado = self.tvw_arma.selection()
        lista = self.tvw_arma.item(selecionado, "values")
        if selecionado != ():
            print(lista)
            sql = f'DELETE FROM Arma WHERE id={lista[0]};'
            bd.excluir_armas(sql)
            messagebox.showinfo("Excluído", "Candidato excluído com sucesso")
            self.tvw_atualizarArma()

    def editar_arma(self):
        selecionado = self.tvw_arma.selection()
        lista = self.tvw_arma.item(selecionado, "values")
        if selecionado != ():
            self.top_cadastroArma = tk.Toplevel(self.janela)
            self.lbl_nome = ttk.Label(self.top_cadastroArma, text='Nome: ')
            self.lbl_nome.grid(row=0, column=0, padx=(5, 2))
            self.ent_nome = ttk.Entry(self.top_cadastroArma)
            self.ent_nome.grid(row=0, column=1, padx=(5, 2))
            self.ent_nome.insert(0,lista[1])

            self.lbl_tipo = ttk.Label(self.top_cadastroArma, text='Tipo: ')
            self.lbl_tipo.grid(row=1, column=0, padx=(5, 2))
            self.ent_tipo = ttk.Entry(self.top_cadastroArma)
            self.ent_tipo.grid(row=1, column=1, padx=(5, 2))
            self.ent_tipo.insert(0,lista[2])

            self.lbl_calibre = ttk.Label(self.top_cadastroArma, text='Calibre: ')
            self.lbl_calibre.grid(row=2, column=0, padx=(5, 2))
            self.ent_calibre = ttk.Entry(self.top_cadastroArma)
            self.ent_calibre.grid(row=2, column=1, padx=(5, 2))
            self.ent_calibre.insert(0,lista[3])

            self.btn_confirmar = ttk.Button(self.top_cadastroArma, text='Confirmar',
                                            command=self.confirmar_edit_arma)
            self.btn_confirmar.grid(row=3, column=0, columnspan=2, pady=10)

    def confirmar_edit_arma(self):
        selecionado = self.tvw_arma.selection()
        lista = self.tvw_arma.item(selecionado, "values")
        nome = self.ent_nome.get()
        tipo = self.ent_tipo.get()
        calibre = self.ent_calibre.get()
        sql = f'UPDATE Arma SET nome="{nome}", tipo="{tipo}", calibre="{calibre}" WHERE id={lista[0]};'
        bd.atualizar_arma(sql)
        self.tvw_atualizarArma()
        self.top_cadastroArma.destroy()


bd.criar_banco_de_dados()
app = tk.Tk()
Tela(app)
app.mainloop()
