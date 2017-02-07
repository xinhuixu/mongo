import csv
from pymongo import MongoClient

server = MongoClient('149.89.150.100')
db = server.XL
coll = db.coll.find()

for p in coll:
    courses =  p['courses']    
    for c in courses:
        print c



#teachers = db.teachers

