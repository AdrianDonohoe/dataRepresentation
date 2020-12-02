import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1solari2"
    )

mycursor = db.cursor()

mycursor.execute("CREATE DATABASE datarep")

mycursor.execute(sql)