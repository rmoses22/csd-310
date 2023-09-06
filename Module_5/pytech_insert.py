
import pymongo
from pymongo import MongoClient
url ="mongodb+srv://admin:admin@cluster0.kda0kcn.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
students = db["PyTech"]

Fred= {
        "student_id": "1007",
        "first_name": "Fred",
        "last_name": "Robert"
    }
Romeo = {
        "student_id": "1008",
        "first_name": "Romeo",
        "last_name": "Ramond"
    }
Emmanuel = {
        "student_id": "1009",
        "first_name": "Emmanuel",
        "last_name": "Johnson"
    }
stud1 = students.insert_one(Fred).inserted_id
stud2 = students.insert_one(Romeo).inserted_id
stud3 = students.insert_one(Emmanuel).inserted_id
print("")
print("--INSERT STATEMENTS--")
print("")
print("Inserted student record " + Fred["first_name"] + " " + Fred["last_name"] + " into the students collection with document_id " + str(stud1))
print("Inserted student record " + Romeo["first_name"] + " " + Romeo["last_name"] + " into the students collection with document_id " + str(stud2))
print("Inserted student record " + Emmanuel["first_name"] + " " + Emmanuel["last_name"] + " into the students collection with document_id " + str(stud3))
print("")
print ("End of program, press any key to exit....")
print("")