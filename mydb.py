import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='marko'

)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE crm")

print("All done!")