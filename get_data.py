import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1solari2",
    database="datarep"
    )

cursor = db.cursor()
sql="select * from states"

cursor.execute(sql)
result = cursor.fetchall()
for x in result:
    print(x)
