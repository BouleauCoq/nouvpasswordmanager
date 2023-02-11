from random import *
a=0
x=0
Mdp=[]

def mdp(n):
    if n<8:
        print("Il est conseillé de choisir un mot de passe d'une longueur plus élevée que 7.")
    else:
        Mdp=[]
        for i in range(n):
            a=randint(33,126)
            Mdp.append(a)
            print(chr(a), end="")