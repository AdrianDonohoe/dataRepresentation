import mysql.connector
import json
import dbconfig as cfg

db = mysql.connector.connect(
    host=cfg.mysql['host'],
    user=cfg.mysql['user'],
    password=cfg.mysql['password'],
    database=cfg.mysql['database']
)







with open('../states.json') as f:
    states = json.load(f)

for state in states:
    mycursor = db.cursor()
    sql = "insert into states (name,abv,electoral_votes,tv,bv,tp,bp) values  (%s,%s,%s,%s,%s,%s,%s)"
    values = (state['name'],state['abv'],state['ecv'],state['tv'],state['bv'],state['tp'],state['bp'])

    mycursor.execute(sql,values)
    db.commit()