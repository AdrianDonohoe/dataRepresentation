import mysql.connector
import json
import dbconfig as cfg



class StatesDAO:
    db = ""
    def __init__(self): 
        self.db = mysql.connector.connect(
        host=cfg.mysql['host'],
        user=cfg.mysql['user'],
        password=cfg.mysql['password'],
        database=cfg.mysql['database']
        )

    def create(self):
        with open('../states.json') as f:
            states = json.load(f)

        for state in states:
            mycursor = self.db.cursor()
            sql = "insert into states (name,abv,ecv,tv,bv,tp,bp) values  (%s,%s,%s,%s,%s,%s,%s)"
            values = (state['name'],state['abv'],state['ecv'],state['tv'],state['bv'],state['tp'],state['bp'])

            mycursor.execute(sql,values)
            self.db.commit()

    def getAll(self):
        cursor = self.db.cursor()
        sql="select * from states"
        cursor.execute(sql)
        results = cursor.fetchall()

        returnArray = []
        
        for result in results:
            returnArray.append(self.convertToDictionary(result))

        return returnArray
        

    def update(self, values):
        cursor = self.db.cursor()
        sql="update states set tv = %s, bv = %s, tp = %s, bp = %s where abv = %s"
        cursor.execute(sql, values)
        self.db.commit()

    def findByAbv(self, abv):
        cursor = self.db.cursor()
        sql="select * from states where abv = %s"
        values = (abv,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDictionary(result)

    def convertToDictionary(self, result):
        colnames=['name','abv','ecv', 'tv','bv','tp','bp']
        
        states = {}
        
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                states[colName] = value
        
        return states

statesDAO = StatesDAO()