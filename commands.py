class Command:
	def execute(self):
                pass


class SeeBalance(Command):
	def __init__(self, bank, accountNumber):
		self.bank = bank
		self.accountNumber = accountNumber

	def execute(self):
		return self.bank.get_balance(self.accountNumber)


class Transfer(Command):
	def __init__(self, bank, source, destination, amount):
		self.bank = bank
		self.source = source
		self.destination = destination
		self.amount = amount

	def execute(self):
		self.bank.transfer(self.source, self.destination, self.amount)
		return f"=) Transferencia {self.source} -> {self.destination}: {self.amount:.2f}"


class Statement(Command):
	def __init__(self, bank, accountNumber):
		self.bank = bank
		self.accountNumber = accountNumber

	def execute(self):
		return self.bank.get_statement(self.accountNumber)
