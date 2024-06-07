import tkinter
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk


class Interface:
    def __init__(self, root):
        self.root = root
        self.clientes = []
        self.root.title("Cadastro Atiradores - TG")
        self.root.iconbitmap("icone.ico")

        self.frame = tk.Frame(root, width=150, height=90)
        self.frame.grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)
        self.frame2 = tk.Frame(root, width=170, height=100)
        self.frame2.grid(row=5, column=1, padx=5, pady=5, sticky=tk.W)
        self.frame3 = tk.Frame(root, width=170, height=100)
        self.frame3.grid(row=5, column=2, padx=5, pady=5, sticky=tk.W)
        self.frame4 = tk.Frame(root, width=170, height=100)
        self.frame4.grid(row=5, column=4, padx=5, pady=5, sticky=tk.W)

        def tivePassagem():
            if self.existePassagem.get() == 1:
                if self.checkbox.get() == 0:
                    self.label_numeroPassagens = tk.Label(root, text="Número de Passagens: ")
                    self.label_numeroPassagens.grid(row=5, column = 0, padx=15, pady=12, sticky=tk.W)
                    self.entry_numeroPassagens = tk.Entry(root, font=("Helvetica", 10))
                    self.entry_numeroPassagens.grid(row=5, column=1, padx=15, pady=12, sticky=tk.W)
                else:
                    self.label_numeroPassagens = tk.Label(root, text="Número de Passagens: ")
                    self.label_numeroPassagens.grid(row=6, column=0, padx=15, pady=12, sticky=tk.W)
                    self.entry_numeroPassagens = tk.Entry(root, font=("Helvetica", 10))
                    self.entry_numeroPassagens.grid(row=6, column=1, padx=15, pady=12, sticky=tk.W)

            else:
                self.label_numeroPassagens.destroy()
                self.entry_numeroPassagens.destroy()

        def check():
            if self.checkbox.get() == 1:
                if self.existePassagem.get() == 1:
                    self.label_enderecoAnterior = tk.Label(root, text="Endereço Anterior :")
                    self.label_enderecoAnterior.grid(row=6, column=0, padx=15, pady=12, sticky=tk.W)
                    self.entry_enderecoAnterior = tk.Entry(root, font=("Helvetica", 10))
                    self.entry_enderecoAnterior.grid(row=6, column=1, padx=5, pady=15, sticky=tk.W)
                    self.label_enderecoComprovante = tk.Label(root, text="Comprovante de Endereço")
                    self.label_enderecoComprovante.grid(row=6, column=2, padx=15, pady=12, sticky=tk.W)
                    self.entry_enderecoComprovante = tk.Entry(root, font=("Helvetica", 10))
                    self.entry_enderecoComprovante.grid(row=6, column=3, padx=5, pady=15, sticky=tk.W)
                    self.enviarComprovante = tk.Button(root, text="Selecionar Arquivo", command='')
                    self.enviarComprovante.grid(row=6, column=4, padx=20, pady=0, sticky=tk.W)
                else:
                    self.label_enderecoAnterior = tk.Label(root, text="Endereço Anterior :")
                    self.label_enderecoAnterior.grid(row=5, column=0, padx=15, pady=12, sticky=tk.W)
                    self.entry_enderecoAnterior = tk.Entry(root, font=("Helvetica", 10))
                    self.entry_enderecoAnterior.grid(row=5, column=1, padx=5, pady=15, sticky=tk.W)
                    self.label_enderecoComprovante = tk.Label(root, text="Comprovante de Endereço")
                    self.label_enderecoComprovante.grid(row=5, column=2, padx=15, pady=12, sticky=tk.W)
                    self.entry_enderecoComprovante = tk.Entry(root, font=("Helvetica", 10))
                    self.entry_enderecoComprovante.grid(row=5, column=3, padx=5, pady=15, sticky=tk.W)
                    self.enviarComprovante = tk.Button(root, text="Selecionar Arquivo", command='')
                    self.enviarComprovante.grid(row=5, column=4, padx=20, pady=0, sticky=tk.W)
            else:
                self.label_enderecoAnterior.destroy()
                self.entry_enderecoAnterior.destroy()
                self.enviarComprovante.destroy()
                self.entry_enderecoComprovante.destroy()
                self.label_enderecoComprovante.destroy()

        self.label_nome = tk.Label(root, text="Nome Completo:")
        self.label_nome.grid(row=1, column=0, padx=15, pady=12, sticky=tk.W)
        self.entry_nome = tk.Entry(root, font=("Helvetica", 10))
        self.entry_nome.grid(row=1, column=1, padx=5, pady=15, sticky=tk.W)

        self.label_cadastrado = tk.Label(root, text="Cadastrado:")
        self.label_cadastrado.grid(row=1, column=2, padx=10, pady=5, sticky=tk.W)
        self.combo_cadastrado = ttk.Combobox(root, state="readonly")
        self.combo_cadastrado.grid(row=1, column=3, padx=5, pady=5, sticky=tk.W)

        self.carregar = tk.Button(root, text="Carregar", command='')
        self.carregar.grid(row=1, column=4)

        self.label_dataNasc = tk.Label(root, text="Data de Nascimento:")
        self.label_dataNasc.grid(row=2, column=0, padx=15, pady=12, sticky=tk.W)
        self.entry_dataNasc = tk.Entry(root, font=("Helvetica", 10))
        self.entry_dataNasc.grid(row=2, column=1, padx=5, pady=15, sticky=tk.W)

        self.label_cpf = tk.Label(root, text="CPF:")
        self.label_cpf.grid(row=2, column=2, padx=15, pady=12, sticky=tk.W)
        self.entry_cpf = tk.Entry(root, font=("Helvetica", 10))
        self.entry_cpf.grid(row=2, column=3, padx=5, pady=15, sticky=tk.W)

        self.label_rg = tk.Label(root, text="RG:")
        self.label_rg.grid(row=2, column=4, padx=15, pady=12, sticky=tk.W)
        self.entry_rg = tk.Entry(root, font=("Helvetica", 10))
        self.entry_rg.grid(row=2, column=5, padx=5, pady=15, sticky=tk.W)

        self.label_enderecoAnterior = tk.Label(root, text="Endereço :")
        self.label_enderecoAnterior.grid(row=3, column=0, padx=15, pady=12, sticky=tk.W)
        self.entry_enderecoAnterior = tk.Entry(root, font=("Helvetica", 10))
        self.entry_enderecoAnterior.grid(row=3, column=1, padx=5, pady=15, sticky=tk.W)

        self.label_cityNatal = tk.Label(root, text="Cidade Natal:")
        self.label_cityNatal.grid(row=3, column=0, padx=15, pady=12, sticky=tk.W)
        self.entry_cityNatal = tk.Entry(root, font=("Helvetica", 10))
        self.entry_cityNatal.grid(row=3, column=1, padx=5, pady=15, sticky=tk.W)

        self.label_altura = tk.Label(root, text="Altura:")
        self.label_altura.grid(row=3, column=2, padx=15, pady=12, sticky=tk.W)
        self.entry_altura = tk.Entry(root, font=("Helvetica", 10))
        self.entry_altura.grid(row=3, column=3, padx=5, pady=15, sticky=tk.W)

        self.label_peso = tk.Label(root, text="Peso:")
        self.label_peso.grid(row=3, column=4, padx=15, pady=12, sticky=tk.W)
        self.entry_peso = tk.Entry(root, font=("Helvetica", 10))
        self.entry_peso.grid(row=3, column=5, padx=5, pady=15, sticky=tk.W)

        self.label_profissao = tk.label(root, te)

        self.existePassagem = tk.IntVar()
        self.tenhoPassagem = tk.Checkbutton(root, text="Tenho passagem pela polícia", variable=self.existePassagem, onvalue=1,
                                    offvalue=0, command=tivePassagem)
        self.tenhoPassagem.grid(row=4, column=0, columnspan=2, padx=15, pady=12, sticky=tk.W)




        self.checkbox = tk.IntVar()
        self.caixa = tk.Checkbutton(root, text="Me mudei de casa à no máximo um ano", variable=self.checkbox, onvalue=1,
                                    offvalue=0, command=check)
        self.caixa.grid(row=4, column=2, columnspan=2, padx=15, pady=12, sticky=tk.W)

        self.salvar = tk.Button(root, text="Salvar", command="")
        self.salvar.grid(row=9, column=1, padx=15, pady=12, sticky=tk.W)

        self.limpar = tk.Button(root, text="Limpar", command="")
        self.limpar.grid(row=9, column=2, padx=15, pady=12, sticky=tk.W)

        self.excluir = tk.Button(root, text="Excluir", command="")
        self.excluir.grid(row=9, column=3, padx=15, pady=12, sticky=tk.W)


class Inscrito:
    def __int__(self, nome, cpf, RG, dataNascimento, enderecoAnterior, dataEnderecoAnterior, enderecoAtual, altura,
                peso, passagemPolicia, condicaoSaude):
        self.nome = nome
        self.cpf = cpf
        self.RG = RG
        self.dataNascimento = dataNascimento
        self.enderecoAnterior = enderecoAnterior
        self.dataEnderecoAnterior = dataEnderecoAnterior
        self.enderecoAtual = enderecoAtual
        self.altura = altura
        self.peso = peso
        self.passagemPolicia = passagemPolicia
        self.condicaoSaude = condicaoSaude


root = tk.Tk()
app = Interface(root)
root.mainloop()
