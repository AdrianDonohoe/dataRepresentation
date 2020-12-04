import mysql.connector
import dbconfig as cfg

class StatesDAO:
    
    def initConnectToDB(self):
        db = mysql.connector.connect(
            host=       cfg.mysql['host'],
            user=       cfg.mysql['user'],
            password=   cfg.mysql['password'],
            database=   cfg.mysql['database'],
            pool_name='my_connection_pool',
            pool_size=4
        )
        return db

    def getConnection(self):
        db = mysql.connector.connect(
            pool_name='my_connection_pool'
        )
        return db

    def __init__(self): 
        db=self.initConnectToDB()
        db.close()
            

    def getAll(self):
        db = self.getConnection()
        cursor = db.cursor()
        sql="select * from states"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        
        for result in results:
            returnArray.append(self.convertToDictionary(result))
        db.close()
        return returnArray

    def findByAbv(self, abv):
        db = self.getConnection()
        cursor = db.cursor()
        sql="select * from states where  abv = %s"
        values = (abv,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        state=self.convertToDictionary(result)
        db.close()
        return state

    def update(self, values):
        db = self.getConnection()
        cursor = db.cursor()
        sql="update states set tv = %s, bv = %s, tp = %s, bp = %s where abv = %s"
        cursor.execute(sql, values)
        db.commit()
        db.close()


        

    def convertToDictionary(self, result):
        colnames=['name','abv','ecv', 'tv','bv','tp','bp']
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item

statesDAO = StatesDAO()