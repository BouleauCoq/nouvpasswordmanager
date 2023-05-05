import customtkinter as ctk
import csv

ctk.set_appearance_mode("dark")
class Table:
	
	def __init__(self,root):
		for i in range(lignestotales):
			for j in range(colonnestotales):
				self.entry = ctk.CTkEntry(root, width=200,fg_color="white", text_color="black", font=("Calibri",15,"bold"))
				self.entry.grid(row=i, column=j)
				self.entry.insert(ctk.END, list_of_rows[i][j])


with open('données.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    list_of_rows = list(csv_reader)
    print(list_of_rows)


lignestotales = len(list_of_rows)
colonnestotales = len(list_of_rows[0])

root = ctk.CTk()
t = Table(root)
root.mainloop()
