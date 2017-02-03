import csv

po = open("peeps.csv")
pd = csv.DictReader(po)

co = open("courses.csv")
cd = csv.DictReader(pd)

for k in pd:
    print k

for k in cd:
    print k
