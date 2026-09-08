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
		self.accounts = {
			1: Account(1, "Amadeu", 100.0),
			2: Account(2, "Bruno", 200.0),
			3: Account(3, "Carlos", 300.0),
		}

	def aux_account(self, accountNumber):
		account = self.accounts.get(accountNumber)
		if account is None:
			raise ValueError(f"{accountNumber} nao existe :O")
		return account

	def get_balance(self, accountNumber):
		return self.aux_account(accountNumber).balance

	def transfer(self, source, destination, amount):
		if amount <= 0:
			raise ValueError("valor deve ser maior que zero :P")

		source_account = self.aux_account(source)
		destination_account = self.aux_account(destination)

		source_account.debit(amount, f"Transferencia para {destination}")
		destination_account.credit(amount, f"Transferencia de {source}")
