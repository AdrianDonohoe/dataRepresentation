import mysql.connector
import dbconfig as cfg


db = mysql.connector.connect(
    host=cfg.mysql['host'],
    user=cfg.mysql['user'],
    password=cfg.mysql['password'],
    database=cfg.mysql['database']
)

cursor = db.cursor()
sql="update states set tv = %s, bv = %s, tp = %s, bp = %s where abv = %s"
values = (10,11,55.34,33.3, "AL")

cursor.execute(sql,values)
db.commit()
print('update done')