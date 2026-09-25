import tkinter as tk
from tkinter import messagebox

from commands import *


class Window:
	def __init__(self, root, bank):
		self.root = root
		self.bank = bank
		self.entry_conta = tk.Entry(root)
		self.entry_destino = tk.Entry(root)
		self.entry_valor = tk.Entry(root)

		# -
		tk.Label(root, text="Banco XYZ").grid(row=0, column=0, columnspan=4, pady=20)
		tk.Label(root, text="Conta:").grid(row=1, column=0, sticky="e")
		self.entry_conta.grid(row=1, column=1)
		tk.Label(root, text="Conta destino:").grid(row=2, column=0, sticky="e")
		self.entry_destino.grid(row=2, column=1)
		tk.Label(root, text="Valor:").grid(row=3, column=0, sticky="e")
		self.entry_valor.grid(row=3, column=1)
		# ---
		tk.Button(root, text="Saldo", command=self.balance).grid(row=4, column=0, pady=10)
		tk.Button(root, text="Extrato", command=self.statement).grid(row=4, column=1, pady=10)
		tk.Button(root, text="Transferir", command=self.tarnsfer).grid(row=4, column=2, pady=10)
		tk.Button(root, text="Listar Contas", command=self.list_accounts).grid(row=4, column=3, pady=10)
		# ---
		tk.Label(root, text="Historico das Operações:").grid(row=5, column=0, sticky="w", padx=5)
		self.lista = tk.Listbox(root, width=70, height=10)
		self.lista.grid(row=6, column=0, columnspan=4, sticky="ew", padx=5, pady=5)

	def balance(self):
		try:
			conta = int(self.entry_conta.get())
			saldo = SeeBalance(self.bank, conta).execute()
		except ValueError as e:
			messagebox.showerror("Error", str(e))
			return
		messagebox.showinfo("Saldo", f"Conta {conta}: {saldo:.2f}")
		self.lista.insert(tk.END, f"Saldo da conta {conta}")

	def statement(self):
		try:
			conta = int(self.entry_conta.get())
			extrato = Statement(self.bank, conta).execute()
		except ValueError as e:
			messagebox.showerror("Error", str(e))
			return
		messagebox.showinfo("Extrato", extrato)
		self.lista.insert(tk.END, f"Extrato da conta {conta}")

	def tarnsfer(self):
		try:
			origem = int(self.entry_conta.get())
			destino = int(self.entry_destino.get())
			valor = float(self.entry_valor.get())
			msg = Transfer(self.bank, origem, destino, valor).execute()
		except ValueError as e:
			messagebox.showerror("Error", str(e))
			return
		messagebox.showinfo("OK", msg)
		self.lista.insert(tk.END, f"Transferencia {origem} -> {destino}: {valor:.2f}")

	def list_accounts(self):
		contas = ListAccounts(self.bank).execute()
		messagebox.showinfo("Contas", contas)
		self.lista.insert(tk.END, "Listou as contas")
