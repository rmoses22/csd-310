import mysql.connector
from mysql.connector import errorcode
config = {
<<<<<<< HEAD
    "user": "root21",
    "password": "ChangeMe21",
=======
    "user": "root",
    "password": "ChangeMe21!",
>>>>>>> c19b6c8e92d95cd8cafdf9de0fc14a8e4fdb687a
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_Warnings": True
}
try:
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    input("\n\n Press any key to continue....")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")
    else:
        print(err)
finally:
    db.close()

