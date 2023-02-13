import customtkinter as ctk


ctk.set_appearance_mode("dark")
class Table:
	
	def __init__(self,root):
		for i in range(lignestotales):
			for j in range(colonnestotales):
				self.entry = ctk.CTkEntry(root, width=200,fg_color="white", text_color="black", font=("Calibri",15,"bold"))
				self.entry.grid(row=i, column=j)
				self.entry.insert(ctk.END, liste[i][j])

liste = [(1,"A","B"),
        (2,"C","D")]

lignestotales = len(liste)
colonnestotales = len(liste[0])

root = ctk.CTk()
t = Table(root)
root.mainloop()
