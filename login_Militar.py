import tkinter as tk
from tkinter import ttk


class Login:

    def __init__(self, CPF, Id_militar, senha):
        self.cpf = CPF
        self.Id = Id_militar
        self.senha = senha


class Inter:

    def __init__(self, root):
        self.root = root
        self.login = []
        self.root.title("Login Militar")

        self.label_cpf = tk.Label(root, text="CPF")
        self.label_cpf.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

        self.entry_nome = tk.Entry(root)
        self.entry_nome.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

        self.label_cpf = tk.Label(root, text="Identidade Militar")
        self.label_cpf.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

        self.entry_nome = tk.Entry(root)
        self.entry_nome.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)

        self.label_cpf = tk.Label(root, text="Senha")
        self.label_cpf.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)

        self.entry_nome = tk.Entry(root)
        self.entry_nome.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)
        
        self.button_login = tk.Button(root, text="Login", command=self.login)
        self.button_login.grid(row=4, column=1, columnspan=2, padx=10, pady=5, sticky=tk.W)
            
root = tk.Tk()
app = Inter(root)
root.mainloop()
