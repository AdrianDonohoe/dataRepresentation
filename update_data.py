import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1solari2",
    database="datarep"
    )

cursor = db.cursor()
sql="update states set tv = %s, bv = %s, tp = %s, bp = %s where abv = %s"
values = (10,11,55.34,33.3, "AL")

cursor.execute(sql,values)
db.commit()
print('update done')