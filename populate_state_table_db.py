# Created by Adrian Donohoe 20/11/2020
import mysql.connector
import csv

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="election",
)

cursor = db.cursor()

with open('my_states.csv', newline='') as f:
    reader = csv.reader(f)
    states = list(reader)

for state in states:
    sql="insert into states (name,abv,electoral_votes) values (%s,%s,%s)"
    values = (state[5],state[6],state[4])
    cursor.execute(sql,values)

db.commit()