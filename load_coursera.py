from faker import Faker
from pymongo import MongoClient
import uuid
import random
import json
#import pymongo
from pymongo.errors import BulkWriteError

from random import randint

# MongoClient
try:
    conn = MongoClient('mongodb://localhost:27017')
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")

# MongoClient
db = MongoClient('mongodb://localhost:27017')['adbs2019']
db.drop_collection('course')
db.drop_collection('category')
db.drop_collection('session')
db.drop_collection('instructor')
db.drop_collection('university')
db.drop_collection('student')
db.drop_collection('course_taken')

fake = Faker()

# =============================================================================
# def fetch_courses():
#
#
# 	#courses = filter_english_courses(data['elements'])
# 	universities = university_list #data['linked']['universities']
# 	#categories = data['linked']['categories']
# 	#instructors = data['linked']['instructors']
# 	#sessions = data['linked']['sessions']
#
# 	print("Fetched: ")
# 	#print(str(len(courses)) + " courses")
# 	print(str(len(universities)) + " universities")
# 	#print(str(len(categories)) + " categories")
# 	#print(str(len(instructors)) + " instructors")
# 	#print(str(len(sessions)) + " sessions")
#
# 	for c in categories:
# 		c['_id'] = "category" + str(c['id'])
# 		#c['category_id'] = "category" + str(c['id'])
#
# 	for u in universities:
# 		u['_id'] = "university" + str(u['id'])
# 		#u['university_id'] = "university" + str(u['id'])
#
# 	for i in instructors:
# 		i['_id'] = "instructor" + str(i['id'])
# 		#i['instructor_id'] = "instructor" + str(i['id'])
#
# 	insert_mongo(categories, "category")
# 	insert_mongo(universities, "university")
# 	insert_mongo(instructors, "instructor")
#
# 	for c in categories:
# 		#c['_id'] = "category" + str(c['id'])
# 		c['category_id'] = "category" + str(c['id'])
# 		c.pop('_id', None)
#
# 	for u in universities:
# 		#u['_id'] = "university" + str(u['id'])
# 		u['university_id'] = "university" + str(u['id'])
# 		u.pop('_id', None)
#
# 	for i in instructors:
# 		#i['_id'] = "instructor" + str(i['id'])
# 		i['instructor_id'] = "instructor" + str(i['id'])
# 		i.pop('_id', None)
#
# 	for course in courses:
# 		new_categories = []
# 		new_universities = []
# 		new_instructors = []
#
# 		if 'categories' in course['links'].keys():
# 			for category_id in course['links']['categories']:
# 				category = find_by_id(categories, category_id)
# 				#category.pop('_id', None)
# 				new_categories.append(category)
#
# 		if 'universities' in course['links'].keys():
# 			for university_id in course['links']['universities']:
# 				univ = find_by_id(universities, university_id)
# 				#univ.pop('_id', None)
# 				new_universities.append(univ)
#
# 		if 'instructors' in course['links'].keys():
# 			for instructor_id in course['links']['instructors']:
# 				instructor = find_by_id(instructors, instructor_id)
# 				#instructor.pop('_id', None)
# 				new_instructors.append(instructor)
#
#
# 		course['categories'] = new_categories
# 		course['universities'] = new_universities
# 		course['instructors'] = new_instructors
# 		course.pop('links', None)
#
# 	return courses, categories, universities, instructors
# =============================================================================


def find_random_course_id():
   	return db.course.find().limit(1).skip(int(random.random() * db.course.estimated_document_count()))[0]['_id']

def new_student():
	student = {}
	student['_id'] = str(randint(50,100))
	student['name'] = fake.name()
	student['address'] = fake.address()
	student['phone'] = fake.phone_number()
	return student


def add_fake_students(num=5, d=2):
  students = []
  student_sessions = []

  my_grade_list = ['A','B','C','D','E','F']

  for i in range(num):
    students.append(new_student())
    for s in students:
      for e in range(int(random.random() * d)):
        session = {}
        session['student_id'] = s['_id']
        session['student_name'] = s['name']
        session['course_id'] = courses_dic[randint(0,len(courses_dic)-1)]['_id']
        session['grade'] = random.choice(my_grade_list)
        student_sessions.append(session)
  return students, student_sessions


def insert_mongo(docs, collection_name):
	collection = db[collection_name]
	collection.insert_many(docs)

if __name__ == "__main__":

  # connect to the MongoDB: adbs2019)
  db = conn.adbs2019

  # Inserting courses
  with open('courses.json') as f:
    courses_dic = json.load(f)
    insert_mongo(courses_dic, "course")

  # Creating fake students
  students, course_taken = add_fake_students()

  # Inserting fake students to MongoDB
  try:
    insert_mongo(students, "student")
    insert_mongo(course_taken, "course_taken")
  except BulkWriteError as exc:
    print ("%%%%% Insertion Unsuccessful %%%%")
    print (exc.details)
