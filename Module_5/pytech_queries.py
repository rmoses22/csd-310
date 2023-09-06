import pymongo
from pymongo import MongoClient
url ="mongodb+srv://admin:admin@cluster0.kda0kcn.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
students = db["PyTech"]

records = students.find({})
print()
print(" -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY -- ")
for record in records:
    print("Student ID: " + str(record["student_id"]))
    print("First Name: " + str(record["first_name"]))
    print("Last Name: " + str(record["last_name"]))
    print()
print(" -- DISPLAYING STUDENTS DOCUMENTS FROM find_one() QUERY -- ")
print ()
doc = students.find_one({"student_id": "1007"})
print("Student ID: " + str(record["student_id"]))
print("First Name: " + str(record["first_name"]))
print("Last Name: " + str(record["last_name"]))
print ()
print("End of the program, press any key to contnue.....")
print()