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
New_record = {
    "student_id": "1010",
    "first_name": "Harrison",
    "last_name": "Harris"
}
New_record_id = students.insert_one(New_record).inserted_id
print("-- INSERT STATEMENTS --")
print("  Inserted student record into the students collection with document_id " + str(New_record_id))
print("")
student_new_record = students.find_one({"student_id": "1010"})
print("-- DISPLAYING STUDENT NEW RECORD -- ")
print("  Student ID: " + student_new_record["student_id"] + 
      "\n  First Name: " + student_new_record["first_name"] + 
      "\n  Last Name: " + student_new_record["last_name"] + "\n")
deleted_student_new_record = students.delete_one({"student_id": "1010"})
updated_student_list = students.find({})
print ("")
print("--DISPLAYING STUDENTS DOCUMENTS FROM find( QUERY --")
for student in updated_student_list: 
    print("  Student ID: " + student["student_id"] + 
          "\n  First Name: " + student["first_name"] + 
          "\n  Last Name: " + student["last_name"] + "\n")

input("End of program press any key to continue...")
