import mysql.connector
import json
import dbconfig as cfg



class StatesDAO:
    
    def initConnectToDB(self):
        
        db = mysql.connector.connect(
            host=cfg.mysql['host'],
            user=cfg.mysql['user'],
            password=cfg.mysql['password'],
            database=cfg.mysql['database'],
            pool_name='my_connection_pool',
            pool_size=3
        )
        
        return db
    
    def getConnection(self):
        db = mysql.connector.connect(
            pool_name='my_connection_pool'
        )
        return db
    
    def __init__(self): 
        try:
            db=self.initConnectToDB()
        except e:
            print(e)
        finally:
            db.close()

    

    def create(self):
        
        with open('../states.json') as f:
            states = json.load(f)

        for state in states:
            try:
                db = self.getConnection()
                cursor = db.cursor()
                sql = "insert into states (name,abv,ecv,tv,bv,tp,bp) values  (%s,%s,%s,%s,%s,%s,%s)"
                values = (state['name'],state['abv'],state['ecv'],state['tv'],state['bv'],state['tp'],state['bp'])

                cursor.execute(sql,values)
                db.commit()
            except e:
                print(e)
            finally:
                db.close()

    def getAll(self):
        try:
            db = self.getConnection()
            cursor = db.cursor()
            sql="select * from states"
            cursor.execute(sql)
            results = cursor.fetchall()

            returnArray = []
        
            for result in results:
                returnArray.append(self.convertToDictionary(result))
        except e:
            print(e)
        finally:
            db.close()
        return returnArray
        

    def update(self, values):
        try:
            db = self.getConnection()
            cursor = db.cursor()
            sql="update states set tv = %s, bv = %s, tp = %s, bp = %s where abv = %s"
            cursor.execute(sql, values)
            db.commit()
        except e:
            print(e)
        finally:
            db.close()

    def findByAbv(self, abv):
        try:
            db = self.getConnection()
            cursor = db.cursor()
            sql="select * from states where abv = %s"
            values = (abv,)

            cursor.execute(sql, values)
            result = cursor.fetchone()
        except e:
            print(e)
        finally:
            db.close()
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