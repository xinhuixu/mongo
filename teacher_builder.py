import csv
from pymongo import MongoClient

server = MongoClient('149.89.150.100')
db = server.XL
coll = db.coll.find()

#display name, id, average
for p in coll:
    courses =  p['courses']
    grade_sum = 0
    count = 0
    for c in courses:
        grade_sum += int( c['mark'] )
        count += 1
    average = grade_sum / (1.0 * count)
    print p['name'], p['id'], average

#declare teachers collection
teachers = db.teachers
td = csv.DictReader(open('teachers.csv'))
teacher_list = []
for t in td:
    dict = {}
    dict['name'] = t['teacher']
    dict['class'] = t['code']
    code = dict['class']
    dict['period'] = t['period']
    teacherstudents = []
    temp = db.coll.find()
    for item in temp:
        for cheat in item['courses']:
            if cheat['code'] == t['code']:
                teacherstudents.append(item['id'])
    dict['students'] = teacherstudents
    teacher_list.append(dict)

for item in teacher_list:
    teachers.insert_one(item)


#Each teacher document should contain their name, class, period and st\
#udents in that class
#The student data should be a list of ids that match the ids of studen\
#ts from the other collection.

#teacher = ...
#teachers.insert_one( teacher )

