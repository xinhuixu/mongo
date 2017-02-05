import csv
#from pymongo import MongoClient

#mongoz !!LOOPBACK FOR NOW CHANGE TO HOMER LATER
#server = MongoClient('127.0.0.1')
#'declare' single database (db name = teamname)
#db = server.XL
#'declare' single collection
#coll = db.coll


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
for item in peeps:
    dict = {}
    dict['name'] = item['name']
    dict['id'] = item['id']
    dict['age'] = item['age']
    student_courses = []
    dict['courses'] = student_courses
    students.append(dict)
for c in courses:
    for item in students:
        if c['id'] == item['id']:
            courses_dict = {}
            courses_dict['code'] = c['code']
            courses_dict['mark'] = c['mark']
            item['courses'].append(courses_dict)
print students

#create a single document for each student
#for doc in students:
 #   coll.insert_one(doc)