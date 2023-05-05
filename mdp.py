import csv

f = open("données.csv","w", newline="")
writer = csv.writer(f)
data = [(1,"identifiant1", "1234aze", "Mozilla"), (2,"identifiant2","nbvc?6","Google")]
writer.writerows(data)
f.close()
