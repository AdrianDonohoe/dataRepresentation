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

trump_cid = '1' # candidateID on DB
biden_cid = '2'

sql = "select * from states"
cursor.execute(sql)
result = cursor.fetchall()

with open('my_states.csv', newline='') as f:
    reader = csv.reader(f)
    states = list(reader)

for state in states:
    sql="insert into votes (votes, candidateID,stateID,percent) values (%s,%s,%s,%s)"
    stateID = findStateID(state)
    values = (state[0],trump_cid,stateID,state[2])
#    cursor.execute(sql,values)

#db.commit()