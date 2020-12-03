import mysql.connector
import dbconfig as cfg


db = mysql.connector.connect(
    host=cfg.mysql['host'],
    user=cfg.mysql['user'],
    password=cfg.mysql['password'],
    database=cfg.mysql['database']
    )

mycursor = db.cursor()



sql = "CREATE TABLE states (name varchar(20) NOT NULL, abv varchar(2) NOT NULL, ecv int NOT NULL, tv int NOT NULL, bv int NOT NULL, tp varchar(5) NOT NULL, bp varchar(5) NOT NULL, stateID int NOT NULL AUTO_INCREMENT, PRIMARY KEY (stateID))"

mycursor.execute(sql)