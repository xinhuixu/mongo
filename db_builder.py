import csv
from pymongo import MongoClient

#csv parsing
po = open("peeps.csv")
peeps = csv.DictReader(po)
co = open("courses.csv")
courses = csv.DictReader(co)

#build peeps & courses data
students = []
# [ {'name': 'alison', 'id': '10', 'age': '23',
#   'courses': [
#               {'code': 'systems',
#               'mark': '85'},
#               {'code': 'softdev',
#               'mark': '80'}
#              ]
#   }, {'name': 'tINI'...}, {...} ]
for p in peeps:
    


#mongoz !!LOOPBACK FOR NOW CHANGE TO HOMER LATER
server = MongoClient('127.0.0.1')
#'declare' single database (db name = teamname)
db = server.XL
#'declare' single collection
coll = db.coll
#create a single document for each student
for doc in students:
    coll.insert_one(doc)
