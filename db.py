import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    password="@Lifechoices1234",
    user="lifechoices",
    database="students",
    auth_plugin = "mysql_native_password",
)


mycursor = mydb.cursor()
ab = mycursor.execute("Select * from Login")
for i in mycursor:
    print(i)

print(mydb)
