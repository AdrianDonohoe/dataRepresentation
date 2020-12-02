import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1solari2",
    database="datarep"
    )

mycursor = db.cursor()



sql = "CREATE TABLE states (name varchar(20) NOT NULL, abv varchar(2) NOT NULL, ecv int NOT NULL, tv int NOT NULL, bv int NOT NULL, tp varchar(5) NOT NULL, bp varchar(5) NOT NULL, stateID int NOT NULL AUTO_INCREMENT, PRIMARY KEY (stateID))"

mycursor.execute(sql)