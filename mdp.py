from random import *
import csv
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

f = open("données.csv","w", newline="")
writer = csv.writer(f)
data = [1,"un", "deux", "trois", "quatre"]
data2 = [1,"cinq","six","sept","huit"]
writer.writerow(data)
writer.writerow(data2)
f.close()

with open('données.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    list_of_rows = list(csv_reader)
    print(list_of_rows)
    print(*list_of_rows[0])
