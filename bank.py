from db import Database


class Account:
	def __init__(self, accountNumber, holder, balance = 0.00):
		self.accountNumber = accountNumber
		self.holder = holder
		self.balance = balance
		self.transactions = []

	def credit(self, amount, description):
		self.balance = self.balance + amount
		self.transactions.append(f"{description} :)  +{amount:.2f}")

	def debit(self, amount, description):
		if amount > self.balance:
			raise ValueError(f"Voce nao tem saldo suficiente :( {self.accountNumber}.")
		self.balance = self.balance - amount
		self.transactions.append(f"{description} :/ -{amount:.2f}")


class Bank:
	def __init__(self):
		self.db = Database()

	def aux_account(self, accountNumber):
		row = self.db.get_account(accountNumber)
		if row is None:
			raise ValueError(f"{accountNumber} nao existe :O")
		return Account(row[0], row[1], row[2])

	def get_balance(self, accountNumber):
		return self.aux_account(accountNumber).balance

	def transfer(self, source, destination, amount):
		if amount <= 0:
			raise ValueError("valor deve ser maior que zero :P")

		source_account = self.aux_account(source)
		destination_account = self.aux_account(destination)

		source_account.debit(amount, f"Transferencia para {destination}")
		destination_account.credit(amount, f"Transferencia de {source}")

		self.db.update_balance(source, source_account.balance)
		self.db.update_balance(destination, destination_account.balance)
