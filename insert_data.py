import mysql.connector
import json

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1solari2",
    database="datarep"
    )







with open('states.json') as f:
    states = json.load(f)

for state in states:
    mycursor = db.cursor()
    sql = "insert into states (name,abv,electoral_votes,tv,bv,tp,bp) values  (%s,%s,%s,%s,%s,%s,%s)"
    values = (state['name'],state['abv'],state['ecv'],state['tv'],state['bv'],state['tp'],state['bp'])

    mycursor.execute(sql,values)
    db.commit()