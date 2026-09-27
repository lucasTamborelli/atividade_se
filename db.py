import sqlite3


class Database:
	def __init__(self):
		self.conexao = sqlite3.connect("xyz.db")
		self.create_table()
		self.seed_start()

	def create_table(self):
		c = self.conexao.cursor()
		c.execute("""create table if not exists accounts(
			number integer primary key,
			holder text,
			balance real)""")

		c.execute("""create table if not exists transactions(
			account integer,
			description text)""")
		self.conexao.commit()
		c.close()

	def seed_start(self):
		c = self.conexao.cursor()
		c.execute("SELECT COUNT(*) FROM accounts")
		if c.fetchone()[0] == 0:
			c.execute("INSERT INTO accounts VALUES (1, 'pessoa1', 100.0)")
			c.execute("INSERT INTO accounts VALUES (2, 'pessoa2', 200.0)")
			c.execute("INSERT INTO accounts VALUES (3, 'pessoa3', 300.0)")
			self.conexao.commit()
		c.close()

	def get_account(self, number):
		c = self.conexao.cursor()
		c.execute(
			"SELECT number, holder, balance FROM accounts WHERE number = ?",
			(number,),
		)
		row = c.fetchone()
		c.close()
		return row

	def get_all_accounts(self):
		c = self.conexao.cursor()
		c.execute("SELECT number, holder, balance FROM accounts")
		rows = c.fetchall()
		c.close()
		return rows

	def update_balance(self, number, balance):
		c = self.conexao.cursor()
		c.execute(
			"UPDATE accounts SET balance = ? WHERE number = ?",
			(balance, number),
		)
		self.conexao.commit()
		c.close()

	def add_transaction(self, account, description):
		c = self.conexao.cursor()
		c.execute(
			"INSERT INTO transactions VALUES (?, ?)",
			(account, description),
		)
		self.conexao.commit()
		c.close()

	def get_transactions(self, account):
		c = self.conexao.cursor()
		c.execute(
			"SELECT description FROM transactions WHERE account = ? ORDER BY rowid",
			(account,),
		)
		rows = c.fetchall()
		c.close()
		return [row[0] for row in rows]
