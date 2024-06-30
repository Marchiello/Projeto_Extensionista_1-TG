import os
import tkinter as tk
from tkinter import ttk
arquivo = open("cadastrados.txt", "r")


class Interface:
    def __init__(self, root):
        self.inscritos = []
        self.entry_numeroPassagens = None
        self.entry_numeroFilhos = None
        self.label_numeroPassagens = None
        self.root = root
        self.root.title("Cadastro Atiradores - TG")
        self.root.iconbitmap("icone.ico")

        # =========================================> Frames(Elementos Invisiveis pra alinhar a tela)

        self.frame = tk.Frame(root, width=150, height=90)
        self.frame.grid(row=6, column=0, padx=5, pady=5, sticky=tk.W)
        self.frame2 = tk.Frame(root, width=170, height=100)
        self.frame2.grid(row=6, column=1, padx=5, pady=5, sticky=tk.W)
        self.frame3 = tk.Frame(root, width=170, height=100)
        self.frame3.grid(row=6, column=2, padx=5, pady=5, sticky=tk.W)
        self.frame4 = tk.Frame(root, width=170, height=100)
        self.frame4.grid(row=6, column=4, padx=5, pady=5, sticky=tk.W)

        # ========================================> Funções Visuais

        def aptoServir():
            if self.souApto.get() == 1:
                self.vaiServir.configure(state=tk.NORMAL)
                self.preAceito.configure(state=tk.NORMAL)
            else:
                self.vaiServir.configure(state=tk.DISABLED)
                self.preAceito.configure(state=tk.DISABLED)

        def direcao():
            if self.preSelecionado.get() == 1:
                self.selecionado.set(0)
                self.dispensado.set(0)
            elif self.selecionado.get() == 1:
                self.dispensado.set(0)
                self.preSelecionado.set(0)
            elif self.dispensado.get() == 1:
                self.selecionado.set(0)
                self.preSelecionado.set(0)

        # ==================================================> Formação da Tela

        self.label_numeroFilhos = tk.Label(root, text="Número de Filhos:")
        self.label_numeroFilhos.grid(row=4, column=4, padx=15, pady=12, sticky=tk.W)
        self.entry_numeroFilhos = tk.Entry(root, font=("Helvetica", 10))
        self.entry_numeroFilhos.grid(row=4, column=5, padx=5, pady=15, sticky=tk.W)

        self.label_numeroPassagens = tk.Label(root, text="Nº de Passagens: ")
        self.label_numeroPassagens.grid(row=6, column=0, padx=15, pady=12, sticky=tk.W)
        self.entry_numeroPassagens = tk.Entry(root, font=("Helvetica", 10))
        self.entry_numeroPassagens.grid(row=6, column=1, padx=15, pady=12, sticky=tk.W)

        self.label_nome = tk.Label(root, text="Nome Completo:")
        self.label_nome.grid(row=1, column=0, padx=15, pady=12, sticky=tk.W)
        self.entry_nome = tk.Entry(root, width=38, font=("Helvetica", 10))  # Nome
        self.entry_nome.grid(row=1, column=1, padx=5, pady=15, sticky=tk.W)

        self.label_cadastrado = tk.Label(root, text="Cadastrado:")
        self.label_cadastrado.grid(row=1, column=2, padx=10, pady=5, sticky=tk.W)
        self.combo_cadastrado = ttk.Combobox(root, width=28, state="readonly")  # Cadastrado
        self.combo_cadastrado.grid(row=1, column=3, padx=5, pady=5, sticky=tk.W)

        self.carregar = tk.Button(root, text="Carregar", command=self.fullLoad)  # Carregar
        self.carregar.grid(row=1, column=4)

        self.label_dataNasc = tk.Label(root, text="Data de Nascimento:")
        self.label_dataNasc.grid(row=2, column=0, padx=15, pady=12, sticky=tk.W)  # Data de Nascimento
        self.entry_dataNasc = tk.Entry(root, font=("Helvetica", 10))
        self.entry_dataNasc.grid(row=2, column=1, padx=5, pady=15, sticky=tk.W)

        self.label_cpf = tk.Label(root, text="CPF:")
        self.label_cpf.grid(row=2, column=2, padx=15, pady=12, sticky=tk.W)  # CPF
        self.entry_cpf = tk.Entry(root, font=("Helvetica", 10))
        self.entry_cpf.grid(row=2, column=3, padx=5, pady=15, sticky=tk.W)

        self.label_rg = tk.Label(root, text="RG:")
        self.label_rg.grid(row=2, column=4, padx=15, pady=12, sticky=tk.W)  # RG
        self.entry_rg = tk.Entry(root, font=("Helvetica", 10))
        self.entry_rg.grid(row=2, column=5, padx=5, pady=15, sticky=tk.W)

        self.label_cityNatal = tk.Label(root, text="Cidade Natal:")
        self.label_cityNatal.grid(row=3, column=0, padx=15, pady=12, sticky=tk.W)  # Cidade Natal
        self.entry_cityNatal = tk.Entry(root, font=("Helvetica", 10))
        self.entry_cityNatal.grid(row=3, column=1, padx=5, pady=15, sticky=tk.W)

        self.label_altura = tk.Label(root, text="Altura:")
        self.label_altura.grid(row=3, column=2, padx=15, pady=12, sticky=tk.W)  # Altura
        self.entry_altura = tk.Entry(root, font=("Helvetica", 10))
        self.entry_altura.grid(row=3, column=3, padx=5, pady=15, sticky=tk.W)

        self.label_peso = tk.Label(root, text="Peso:")
        self.label_peso.grid(row=3, column=4, padx=15, pady=12, sticky=tk.W)  # Peso
        self.entry_peso = tk.Entry(root, font=("Helvetica", 10))
        self.entry_peso.grid(row=3, column=5, padx=5, pady=15, sticky=tk.W)

        self.label_escolaridade = tk.Label(root, text="Escolaridade:")
        self.label_escolaridade.grid(row=4, column=0, padx=15, pady=12, sticky=tk.W)  # Escolaridade
        escolaridade = ["Ensino Fundamental Incompleto", "Ensino Fundamental Completo", "Ensino Médio Incompleto",
                        "Ensino Médio Completo", "Ensino Superior Incompleto", "Ensino Superior"]
        self.entry_escolaridade = ttk.Combobox(root, width=30, values=escolaridade, state='readonly')
        self.entry_escolaridade.grid(row=4, column=1, padx=5, pady=15, sticky=tk.W)

        self.label_profissao = tk.Label(root, text="Profissão:")
        self.label_profissao.grid(row=4, column=2, padx=15, pady=12, sticky=tk.W)  # Profissão
        self.entry_profissao = tk.Entry(root, font=("Helvetica", 10))
        self.entry_profissao.grid(row=4, column=3, padx=5, pady=15, sticky=tk.W)

        self.souApto = tk.IntVar()
        self.Apto = tk.Checkbutton(root, text="Sou Apto a Servir.", variable=self.souApto, onvalue=1,
                                   # Apto a Servir
                                   offvalue=0, command=aptoServir)

        self.Apto.grid(row=5, column=0, columnspan=2, padx=15, pady=12, sticky=tk.W)

        self.preSelecionado = tk.IntVar()
        self.preAceito = tk.Checkbutton(root, text="Pré-Selecionado", variable=self.preSelecionado, onvalue=1,
                                        offvalue=0, command=direcao)
        self.preAceito.grid(row=8, column=1, columnspan=2, padx=15, pady=12, sticky=tk.W)  # Pré-Selecionado
        self.preAceito.configure(state=tk.DISABLED)

        self.selecionado = tk.IntVar()
        self.vaiServir = tk.Checkbutton(root, text="Selecionado", variable=self.selecionado, onvalue=1,
                                        offvalue=0, command=direcao)
        self.vaiServir.grid(row=8, column=3, columnspan=2, padx=15, pady=12, sticky=tk.W)  # Selecionado
        self.vaiServir.configure(state=tk.DISABLED)

        self.dispensado = tk.IntVar()
        self.goodEnd = tk.Checkbutton(root, text="Dispensado", variable=self.dispensado, onvalue=1,
                                      offvalue=0, command=direcao)
        self.goodEnd.grid(row=8, column=5, columnspan=2, padx=15, pady=12, sticky=tk.W)  # Dispensado

        self.salvar = tk.Button(root, text="Salvar", command=self.fullSave)
        self.salvar.grid(row=9, column=2, padx=15, pady=12, sticky=tk.W)  # Salvar

        self.limpar = tk.Button(root, text="Limpar", command=self.limpar_dados)
        self.limpar.grid(row=9, column=3, padx=15, pady=12, sticky=tk.W)  # Limpar

        self.excluir = tk.Button(root, text="Excluir", command=self.excluir_dados)
        self.excluir.grid(row=9, column=4, padx=15, pady=12, sticky=tk.W)  # Excluir

        # def limparDados():
        #     entries = [self.entry_nome, self.entry_profissao, self.entry_cpf, self.entry_altura, self.entry_cityNatal,
        #                self.entry_dataNasc, self.entry_enderecoAnterior, self.entry_rg, self.entry_peso]
        #     # noinspection PyTypeChecker
        #     for i in entries.__len__():
        #         print(entries[i])
        #         # self.entry_nome.delete(0, tk.END)
        #

        # ===================> Funcionamento do Programa

    # nome, cpf, RG, dataNascimento, cidadeNatal, enderecoAnterior, comprovanteEnderecoAnterior,
    # altura, enderecoAtual, peso, escolaridade, profissao, filhos, mudeiEmUmAno, passagemPolicia,
    # condicaoSaude

    def limpar_dados(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_cpf.delete(0, tk.END)
        self.entry_rg.delete(0, tk.END)
        self.entry_dataNasc.delete(0, tk.END)
        self.entry_cityNatal.delete(0, tk.END)
        self.entry_altura.delete(0, tk.END)
        self.souApto.set(0)
        self.entry_peso.delete(0, tk.END)
        self.entry_escolaridade.set('')
        self.entry_profissao.delete(0, tk.END)
        self.preSelecionado.set(0)
        self.selecionado.set(0)
        self.dispensado.set(0)
        self.entry_numeroPassagens.delete(0, tk.END)

    def salvar_dados(self):
        inscrito = {
            'nome': self.entry_nome.get(),
            'cpf': self.entry_cpf.get(),
            'RG': self.entry_rg.get(),
            'dataNascimento': self.entry_dataNasc.get(),
            'cidadeNatal': self.entry_cityNatal.get(),
            'altura': self.entry_altura.get(),
            'peso': self.entry_peso.get(),
            'escolaridade': self.entry_escolaridade.get(),
            'profissao': self.entry_profissao.get(),
            'souApto': self.souApto.get(),
            'preSelecionado': self.preSelecionado.get(),
            'selecionado': self.selecionado.get(),
            'dispensado': self.dispensado.get(),
            'numeroPassagens': self.entry_numeroPassagens.get(),
            'numeroFilhos': self.entry_numeroFilhos.get(),
        }
        self.inscritos.append(inscrito)
        self.combo_cadastrado['values'] = [insc['nome'] for insc in self.inscritos]
        self.limpar_dados()

    def excluir_dados(self):
        nome_selecionado = self.combo_cadastrado.get()
        self.inscritos = [insc for insc in self.inscritos if insc['nome'] != nome_selecionado]
        self.combo_cadastrado['values'] = [insc['nome'] for insc in self.inscritos]
        self.limpar_dados()

    def carregar_inscrito(self):
        nome_selecionado = self.combo_cadastrado.get()
        for inscrito in self.inscritos:
            if inscrito['nome'] == nome_selecionado:
                self.entry_nome.delete(0, tk.END)
                self.entry_nome.insert(0, inscrito['nome'])
                self.entry_cpf.delete(0, tk.END)
                self.entry_cpf.insert(0, inscrito['cpf'])
                self.entry_rg.delete(0, tk.END)
                self.entry_rg.insert(0, inscrito['RG'])
                self.entry_dataNasc.delete(0, tk.END)
                self.entry_dataNasc.insert(0, inscrito['dataNascimento'])
                self.entry_cityNatal.delete(0, tk.END)
                self.entry_cityNatal.insert(0, inscrito['cidadeNatal'])
                self.entry_altura.delete(0, tk.END)
                self.entry_altura.insert(0, inscrito['altura'])
                self.entry_peso.delete(0, tk.END)
                self.entry_peso.insert(0, inscrito['peso'])
                self.entry_escolaridade.set(inscrito['escolaridade'])
                self.entry_profissao.delete(0, tk.END)
                self.entry_profissao.insert(0, inscrito['profissao'])
                self.souApto.set(inscrito['souApto'])
                self.preSelecionado.set(inscrito['preSelecionado'])
                self.selecionado.set(inscrito['selecionado'])
                self.dispensado.set(inscrito['dispensado'])
                self.entry_numeroPassagens.delete(0, tk.END)
                self.entry_numeroPassagens.insert(0, inscrito['numeroPassagens'])
                self.entry_numeroFilhos.delete(0, tk.END)
                self.entry_numeroFilhos.insert(0, inscrito['numeroFilhos'])
                break

    def salvarDadosArquivo(self):
        with open("cadastrados.txt", "w") as file:
            for inscrito in self.inscritos:
                file.write(','.join([
                    inscrito['nome'],
                    inscrito['cpf'],
                    inscrito['RG'],
                    inscrito['dataNascimento'],
                    inscrito['cidadeNatal'],
                    inscrito['altura'],
                    inscrito['peso'],
                    inscrito['escolaridade'],
                    inscrito['profissao'],
                    str(inscrito['souApto']),
                    str(inscrito['preSelecionado']),
                    str(inscrito['selecionado']),
                    str(inscrito['dispensado']),
                    inscrito['numeroPassagens'],
                    inscrito['numeroFilhos']
                ]) + '\n')

    def carregarDadosArquivo(self):
        if os.path.exists("cadastrados.txt"):
            with open("cadastrados.txt", "r") as file:
                self.inscritos = []
                for line in file:
                    dados = line.strip().split(',')
                    inscrito = {
                        'nome': dados[0],
                        'cpf': dados[1],
                        'RG': dados[2],
                        'dataNascimento': dados[3],
                        'cidadeNatal': dados[4],
                        'altura': dados[5],
                        'peso': dados[6],
                        'escolaridade': dados[7],
                        'profissao': dados[8],
                        'souApto': int(dados[9]),
                        'preSelecionado': int(dados[10]),
                        'selecionado': int(dados[11]),
                        'dispensado': int(dados[12]),
                        'numeroPassagens': dados[13],
                        'numeroFilhos': dados[14]
                    }
                    self.inscritos.append(inscrito)
                self.combo_cadastrado['values'] = [insc['nome'] for insc in self.inscritos]

    def fullSave(self):
        self.salvar_dados()
        self.salvarDadosArquivo()

    def fullLoad(self):
        self.carregarDadosArquivo()
        self.carregar_inscrito()


root = tk.Tk()
app = Interface(root)
root.mainloop()
