import pymongo
from pymongo import MongoClient
url ="mongodb+srv://admin:admin@cluster0.kda0kcn.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
students = db["PyTech"]

records = students.find({})
print()
print(" -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY -- ")
print ("")
for record in records:
    print (" Student ID: " + record["student_id"] + 
           "\n  First Name: " + record["first_name"] + 
           "\n  Last Name: " + record["last_name"] + "\n")
outcome = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Thomas"}})
fred = students.find_one({"student_id": "1007"})
print("--DISPLAYING STUDENT DOCUMENT 1007 --")
print("")
print(" Student ID: " + fred["student_id"] + 
      "\n First Name: " + fred["first_name"] + 
      "\n Last Name: " + fred["last_name"] + "\n")
print()
print("End of the program, press any key to contnue.....")
print("")