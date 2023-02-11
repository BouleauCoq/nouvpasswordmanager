import tkinter as tk
import customtkinter as ctk
from random import *
Mdp=[]
class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        ctk.CTk.__init__(self, *args, **kwargs)
        self.geometry("1250x1080")
        container = ctk.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.grid_columnconfigure(1, weight=6)
        ctk.set_appearance_mode("dark")

        nav = ctk.CTkFrame(container, fg_color="red")
        nav.grid(row=0, column=0, sticky="nsew")

        label = ctk.CTkLabel(nav, text="NavigationPage")
        label.pack(side="top", padx=10, pady=10, fill="x")

        btn_Verifyer = ctk.CTkButton(nav, text="Verifyer Page", command=self.showVerifyer, fg_color="black")
        btn_CreatePasswords = ctk.CTkButton(
            nav, text="CreatePasswords Page", command=self.showCreatePasswords, fg_color="black"
        )
        btn_Pwds = ctk.CTkButton(nav, text="Passwords Page", command=self.showPasswords, fg_color="black")
        btn_Verifyer.pack(side="top", pady=10)
        btn_CreatePasswords.pack(side="top", pady=10)
        btn_Pwds.pack(side="top", pady=10)

        self.frames = {}
        for F in (CreatePasswordsPage, VerifyerPage, PasswordsPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            # OR F.__name__ pour que _name_ ne dépende pas d'une instance
            print(F.__name__)
            self.frames[page_name] = frame
            frame.grid(row=0, column=1, sticky="nsew")

        self.showFrame(self.frames["VerifyerPage"])

    def showFrame(self, frame):
        frame.tkraise()

    def showVerifyer(self):
        self.showFrame(self.frames["VerifyerPage"])

    def showCreatePasswords(self):
        self.showFrame(self.frames["CreatePasswordsPage"])

    def showPasswords(self):
        self.showFrame(self.frames["PasswordsPage"])



class CreatePasswordsPage(ctk.CTkFrame):
    def __init__(self, parent, controller):

        ctk.CTkFrame.__init__(self, parent)
        self.configure(fg_color="blue")
        self.name = "CreatePasswordPage"
        self.controller = controller
        self.label = ctk.CTkLabel(self, text="CreatePasswordsPage")
        self.label.pack(side="top", fill="x")
        self.btn = ctk.CTkButton(
            self, text="Generate a password", command=self.Click_event
        )
        self.btn.pack(side="top", fill="x")
        self.labelMotDePasse = ctk.CTkLabel(self, text="", fg_color="black")
        self.labelMotDePasse.pack(side="bottom", fill="x")
        
    def Click_event(self):
        dialog = ctk.CTkInputDialog(text="Longueur du mot de passe", title="Password")
        MdpLongueur = int(dialog.get_input()) 
        self.labelMotDePasse.configure(text=mdp(MdpLongueur))
    


class VerifyerPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.name = "VerifyerPage"
        self.controller = controller
        label = ctk.CTkLabel(self, text="VerifyerPage")
        label.pack(side="top", fill="x")


class PasswordsPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.configure(fg_color="green")
        self.name = "PasswordsPage"
        self.controller = controller
        label = ctk.CTkLabel(self, text="PasswordsPage")
        label.pack(side="top", fill="x")


a=0
x=0
Mdp=[]
def mdp(MdpLongueur):
    if MdpLongueur<8:
        return "Il est conseillé de choisir un mot de passe d'une longueur plus élevée que 7."
    else:
        Mdp=[]
        for i in range(MdpLongueur):
            a=randint(33,126)
            Mdp.append(chr(a))
        return Mdp


app = App()
app.mainloop()


# https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter