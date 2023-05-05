import customtkinter as ctk
from random import *
import pyperclip
import csv


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

        nav = ctk.CTkFrame(container, fg_color="gray")
        nav.grid(row=0, column=0, sticky="nsew")

        label = ctk.CTkLabel(nav, text="NavigationPage")
        label.pack(side="top", padx=10, pady=10, fill="x")

        btn_Verifyer = ctk.CTkButton(nav, text="Verifyer Page", command=self.showVerifyer, fg_color="black")
        btn_CreatePasswords = ctk.CTkButton(
            nav, text="CreatePasswords Page", command=self.showCreatePasswords, fg_color="black"
        )
        btn_Pwds = ctk.CTkButton(nav, text="Passwords Page", command=self.showPasswords, fg_color="black")
        btn_Details = ctk.CTkButton(nav, text="Détails", command=self.showDetails, fg_color="black")
        btn_Verifyer.pack(side="top", pady=10)
        btn_CreatePasswords.pack(side="top", pady=10)
        btn_Pwds.pack(side="top", pady=10)
        btn_Details.pack(side="bottom", pady=10)
        self.frames = {}
        for F in (CreatePasswordsPage, VerifyerPage, PasswordsPage, Details, PresentationPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            # OR F.__name__ pour que _name_ ne dépende pas d'une instance
            print(F.__name__)
            self.frames[page_name] = frame
            frame.grid(row=0, column=1, sticky="nsew")

        self.showFrame(self.frames["PresentationPage"])

    def showFrame(self, frame):
        frame.tkraise()

    def showVerifyer(self):
        self.showFrame(self.frames["VerifyerPage"])

    def showCreatePasswords(self):
        self.showFrame(self.frames["CreatePasswordsPage"])

    def showPasswords(self):
        self.showFrame(self.frames["PasswordsPage"])

    def showDetails(self):
        self.showFrame(self.frames["Details"])



class PresentationPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.name = "PresentationPage"
        self.controller = controller
        self.label = ctk.CTkLabel(self, text="PresentationPage")
        self.label.pack(side="top", fill="x")
        self.presentation_label = ctk.CTkLabel(self, text="Génération, Vérification et Stockage de Mots de passe", font=("Calibri",35,"bold"))
        self.presentation_label.place(anchor=ctk.N, relx=0.5, rely=0.5)
        self.noms_label = ctk.CTkLabel(self, text="Par Paul Génin et Thomas Dolnet", font=("Calibri", 20, "bold"))
        self.noms_label.place(anchor=ctk.N, relx=0.8, rely=0.9)


class CreatePasswordsPage(ctk.CTkFrame):
    def __init__(self, parent, controller):

        ctk.CTkFrame.__init__(self, parent)
        self.name = "CreatePasswordPage"
        self.controller = controller
        self.label = ctk.CTkLabel(self, text="Page de création", font=("Arial", 25))
        self.label.pack(side="top", fill="x")
        self.btn_generate = ctk.CTkButton(
            self, text="Générer un mot de passe", command=self.Click_event_Dialog, fg_color="gray15"
        )
        self.btn_generate.place(anchor=ctk.N, relx=0.33, rely=0.5)
        self.labelMotDePasse = ctk.CTkLabel(self, text="", fg_color="black", width=500)
        self.labelMotDePasse.place(anchor=ctk.N, relx=0.5, rely=0.45)
        self.btn_copy = ctk.CTkButton(
            self, text="Copier le mot de passe", command=pyperclip.copy(''.join([str(i) for i in Mdp])), fg_color="gray15"
        )
        self.btn_copy.place(anchor=ctk.N, relx=0.675, rely=0.5)
        self.textgene = ctk.CTkLabel(self, text="Génération de mots de passe", font=("Calibri", 20, "bold"))
        self.textgene.place(anchor=ctk.N, relx=0.5, rely=0.41)
        
    def Click_event_Dialog(self):
        dialog = ctk.CTkInputDialog(text="Longueur du mot de passe", title="Password")
        MdpLongueur = int(dialog.get_input()) 
        self.labelMotDePasse.configure(text=mdp(MdpLongueur))



class VerifyerPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.name = "VerifyerPage"
        self.controller = controller
        label = ctk.CTkLabel(self, text="Page de vérification", font=("Arial", 25))
        label.pack(side="top", fill="x")
        self.entry_verif = ctk.CTkEntry(self, placeholder_text="Mot de passe à tester", fg_color="black", width=500)
        self.entry_verif.place(anchor=ctk.N, relx=0.5, rely=0.4)
        self.btn_verif = ctk.CTkButton(
            self, text="Vérifier", command=self.Click_event_Verif, width=500, fg_color="gray15"
        )
        self.btn_verif.place(anchor=ctk.N, relx=0.5, rely=0.5)
        self.progressbar_verif = ctk.CTkProgressBar(self, progress_color="red", width=500, height=23)
        self.progressbar_verif.place(anchor=ctk.N, relx=0.5, rely=0.45)
        self.progressbar_verif.set(value=0)
        self.label_verif = ctk.CTkLabel(self, text="", width=500)
        self.label_verif.place(anchor=ctk.N, relx=0.5, rely=0.6)
        self.btn_paste = ctk.CTkButton(
            self, text="Coller", command=self.Click_event_Paste, fg_color="gray15"
        )
        self.btn_paste.place(anchor=ctk.N, relx=0.1, rely=0.1)
        self.textverif_label = ctk.CTkLabel(self, text="Entrez le mot de passe à tester", font=("Calibri", 15, "bold"))
        self.textverif_label.place(anchor=ctk.N, relx=0.5, rely=0.36)

    def Click_event_Verif(self):
        verifmdp = self.entry_verif.get()
        s=verif(verifmdp)
        self.progressbar_verif.set(value=s)
        color(self, s)

    def Click_event_Paste(self):
        s=verif(pyperclip.paste())
        self.progressbar_verif.set(value=s)
        color(self, s)


class PasswordsPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.name = "PasswordsPage"
        self.controller = controller
        label = ctk.CTkLabel(self, text="Page des Mots de passe", font=("Arial", 25))
        label.pack(side="top", fill="x")
        self.btn_tableau = ctk.CTkButton(self,text="Tableau", command=self.tableau, width=350, fg_color="gray15")
        self.btn_tableau.place(anchor=ctk.N, relx=0.75, rely=0.16)
        self.identifiant = ctk.CTkEntry(self, placeholder_text="Numéro d'identifiant", fg_color="black", width=350)
        self.identifiant.place(anchor=ctk.N, relx=0.75, rely=0.2)
        self.label_ajout = ctk.CTkLabel(self, text="Ajout de données", font=("Calibri",25,"bold"))
        self.label_ajout.place(anchor=ctk.N, relx=0.5, rely=0.5)
        self.entry_numero = ctk.CTkEntry(self, placeholder_text="Numéro d'identifiant", fg_color="black", width=250)
        self.entry_numero.place(anchor=ctk.N, relx=0.15, rely=0.65)
        self.entry_id = ctk.CTkEntry(self, placeholder_text="Identifiant", fg_color="black", width=250)
        self.entry_id.place(anchor=ctk.N, relx=0.15, rely=0.7)
        self.entry_mdp = ctk.CTkEntry(self, placeholder_text="Mot de passe", fg_color="black", width=250)
        self.entry_mdp.place(anchor=ctk.N, relx=0.15, rely=0.75)
        self.entry_site = ctk.CTkEntry(self, placeholder_text="Site", fg_color="black", width=250)
        self.entry_site.place(anchor=ctk.N, relx=0.15, rely=0.8)
        self.btn_données = ctk.CTkButton(self, text="Valider", command=self.ajout, width=350, fg_color="gray15")
        self.btn_données.place(anchor=ctk.N, relx=0.6, rely=0.73)
        self.textdonnées_label = ctk.CTkLabel(self, text="Données enregistrées", font=("Calibri", 25, "bold" ))
        self.textdonnées_label.place(anchor=ctk.N, relx=0.5, rely=0.06)
        

        

    def tableau(self):
        identifiant_entry=self.identifiant.get()
        identifiant(identifiant_entry)
        self.textbox = ctk.CTkTextbox(self, width=500, state="normal", font=("Calibri", 18))
        self.textbox.place(anchor=ctk.N, relx=0.3, rely=0.1)
        self.textbox.delete("0.0", "end")
        self.textbox.insert("0.0", text='\n'.join(map(str, Liste_identifiant)))
        self.textbox.configure(state="disabled")

    def ajout(self):
        donnée_numéro = self.entry_numero.get()
        donnée_id = self.entry_id.get()
        donnée_mdp = self.entry_mdp.get()
        donnée_site = self.entry_site.get()
        f = open("données.csv","a", newline="")
        writer = csv.writer(f)
        data = [(donnée_numéro, donnée_id, donnée_mdp, donnée_site)]
        writer.writerows(data)
        f.close()





class Details(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.configure(fg_color="black")
        self.name = "Détails"
        self.controller = controller
        label = ctk.CTkLabel(self, text="Détails")
        label.pack(side="top", fill="x")
        self.textboxcarac = ctk.CTkTextbox(self, state="normal", font=("Calibri", 18))
        self.textboxcarac.pack(side="top", fill="x")
        self.textboxcarac.insert("0.0", text="Système de notation des mots de passe fondé sur des caractéristiques fixées.\n Mots de passe générés aléatoirement.\n Mots de passe sauvegardé de manière sécurisée hors ligne.\n")
        self.textboxcarac.configure(state="disabled")

#génération du mdp
a=0 #valeur ASCII du caractère
x=0 
Mdp=[] #Liste des caractères
def mdp(MdpLongueur):
    if MdpLongueur<8:
        return "Il est conseillé de choisir un mot de passe d'une longueur plus élevée que 7."
    else:
        Mdp=[]
        for i in range(MdpLongueur):
            a=randint(33,126)
            Mdp.append(chr(a))
        pyperclip.copy("".join(Mdp))
        return Mdp


#vérification du mdp
def verif(verifmdp):
    s=0 #score
    nb=0 
    maj=0
    min=0
    spe=0
    rep=0
    MM=0 #répétitions de maj et min
    NB=0 #répétitions de chiffres
    ch = list(verifmdp)
    CH=[]
    consecnb=0
    consecspe=0
    consecmin=0
    consecmaj=0
    s=3*len(ch)
#donner les points
    for i in range(len(ch)):
        CH.append(ord(ch[i]))
        if CH[i]>=48 and CH[i]<=57:
            nb=nb+1
        if CH[i]>=65 and CH[i]<=90:
            maj=maj+1
        if CH[i]>=97 and CH[i]<=122:
            min=min+1
        if CH[i]>=33 and CH[i]<=47 or CH[i]>=58 and CH[i]<=64 or CH[i]>=91 and CH[i]<=96 or CH[i]>=123 and CH[i]<=126:
            spe=spe+1
        else:
            s=s
#test des malus
    for y in range(33,126):
        if CH.count(y)>1:
            rep=rep+CH.count(y)-1
        if spe==0 and nb==0:
            MM=maj+min-2*(maj+min)
        if spe==0 and maj==0 and min==0:
            NB=nb-3*nb 
    for z in range(len(CH)-1):
        if CH[z]>=48 and CH[z]<=57 and CH[z+1]>=48 and CH[z+1]<=57:
            consecnb=consecnb+1
        if CH[z]>=65 and CH[z]<=90 and CH[z+1]>=65 and CH[z+1]<=90:
            consecmaj=consecmaj+1
        if CH[z]>=97 and CH[z]<=122 and CH[z+1]>=97 and CH[z+1]<=122:
            consecmin=consecmin+1
        if CH[z]>=33 and CH[z]<=47 or CH[z]>=58 and CH[z]<=64 or CH[z]>=91 and CH[z]<=96 or CH[z]>=123 and CH[z]<=126 and CH[z+1]>=33 and CH[z+1]<=47 or CH[z+1]>=58 and CH[z+1]<=64 or CH[z+1]>=91 and CH[z+1]<=96 or CH[z+1]>=123 and CH[z+1]<=126:
            consecspe=consecspe+1
        else:
            s=s
    s=((s+(nb*2)+maj+min+(spe*4)+MM+NB-(rep**2+consecmaj*2+consecmin*2+consecnb*2+consecspe*2))*100)/5000
    if s>=1:
        s=1
    else:
        if s<=0:
            s=0
        else:
            s=s
    return s


#association avec les couleurs
def color(self, s):
    if s<=0.25:
        self.progressbar_verif.configure(progress_color="red")
        self.label_verif.configure(text="L'utilisation du mot de passe est déconseillée.")
    if s>0.25 and s<=0.5:
        self.progressbar_verif.configure(progress_color="orange")
        self.label_verif.configure(text="Le mot de passe est peu solide.")
    if s>0.5 and s<=0.75:
        self.progressbar_verif.configure(progress_color="yellow")
        self.label_verif.configure(text="Le mot de passe est de solidité moyenne.")
    if s>0.75:
        self.progressbar_verif.configure(progress_color="green")
        self.label_verif.configure(text="Le mot de passe est solide.")


#affichage du csv dans le terminal
with open('données.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    list_of_rows = list(csv_reader)
    print(list_of_rows)


#génération du tableau
Liste_identifiant=[]
def identifiant(identifiant_entry):
    Liste_identifiant.clear()
    for l in range(len(list_of_rows)):
        if identifiant_entry==list_of_rows[l][0]:
            Liste_identifiant.append(list_of_rows[l])
            l=l+1
        else:
            l=l+1




app = App()
app.mainloop()


# https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter