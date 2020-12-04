import mysql.connector
import json
import dbconfig as cfg



class StatesDAO:
    
    

    def initConnectToDB(self):
        
        
            try:
                conn = mysql.connector.connect(
                    host=cfg.mysql['host'],
                    user=cfg.mysql['user'],
                    password=cfg.mysql['password'],
                    database=cfg.mysql['database'],
                    
                )
                print('CONNECTED from initConnectToDB')
                print('returning from intConn()')
                print(conn)
                return conn
        
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print("Something is wrong with your user name or password")
                elif err.errno == errorcode.ER_BAD_DB_ERROR:
                    print("Database does not exist")
                else:
                    print(err)
            else:
                conn.close()
        
    
#    def getConnection(self):
#        try:
#            db = mysql.connector.connect(
#            pool_name='my_connection_pool'
#       )
#            return db
#        except mysql.connector.Error as err:
#            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#                print("Something is wrong with your user name or password")
#            elif err.errno == errorcode.ER_BAD_DB_ERROR:
#                print("Database does not exist")
#            else:
#                print(err)
#        else:
#            db.close()
    
    def __init__(self): 
        
        print('Conecting.......')
        self.conn=self.initConnectToDB()
        print(' Connected from __init__')
        
        

    

#    def create(self):
        
#        with open('../states.json') as f:
#            states = json.load(f)

#        for state in states:
#            try:
#                db = self.getConnection()
#                cursor = db.cursor()
#                sql = "insert into states (name,abv,ecv,tv,bv,tp,bp) values  (%s,%s,%s,%s,%s,%s,%s)"
#                values = (state['name'],state['abv'],state['ecv'],state['tv'],state['bv'],state['tp'],state['bp'])
#
#                cursor.execute(sql,values)
#                db.commit()
#            except:
#                print('something wrong !!!')
#            finally:
#                db.close()

    def getAll(self):
        
        #print(f'Conn from getAll {self.conn}')
        #print(self.conn)
        if (not self.conn):
            #print('Connecting from getAll')
            initConnectToDB()
        else:
            pass
        
        sql="select * from states"
        
        try:
            with self.conn:
                #print(f"inside try: {self.conn}")
                cursor = self.conn.cursor()
                #print(f"cursor {cursor}")
                cursor.execute(sql)
                results = cursor.fetchall()

                returnArray = []
        
                for result in results:
                    returnArray.append(self.convertToDictionary(result))
        except:
            print('something wrong !!!')
        finally:
            print('finally!!')
        if (cursor):
            print('closing cursor')
            cursor.close()
        return returnArray
        

    def update(self, values):
        #print(f'Conn from Update {self.conn}')
        if (not self.conn):
            #print('Connecting from update')
            initConnectToDB()
        else:
            pass
        
        sql="update states set tv = %s, bv = %s, tp = %s, bp = %s where abv = %s"
        try:
            with self.conn:
                #print(f"inside update try: {self.conn}")
                cursor = self.conn.cursor()
                #print(f"cursor {cursor}")
                cursor.execute(sql, values)
                self.conn.commit()
        except:
            print('something wrong !!!')
        finally:
            print('finally!!')
        if (cursor):
            print('closing cursor')
            cursor.close()
        
    def findByAbv(self, abv):
        if (not self.conn):
            initConnectToDB()
        else:
            pass
        
        sql="select * from states where abv = %s"

        try:
            with self.conn:
                cursor = self.conn.cursor()
            
                values = (abv,)

                cursor.execute(sql, values)
                result = cursor.fetchone()
        except:
            print('something wrong !!!')
        finally:
            print('finally')    
        if (cursor):
            print('closing cursor')
            cursor.close()
        return self.convertToDictionary(result)

    def convertToDictionary(self, result):
        colnames=['name','abv','ecv', 'tv','bv','tp','bp']
        
        states = {}
        
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                states[colName] = value
        
        return states

    def closeConnection(self):
        if self.conn:
            print('closing Conn')
            self.conn.close()

#statesDAO = StatesDAO()