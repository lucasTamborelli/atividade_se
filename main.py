import tkinter as tk

from bank import Bank
from gui import Window

def main():
	bank = Bank()

	root = tk.Tk()
	root.title("Banco-xyz")
	root.geometry("500x650")

	Window(root, bank)
	root.mainloop()


if __name__ == "__main__":
	main()
