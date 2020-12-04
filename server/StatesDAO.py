# Created by Adrian Donohoe 20/11/2020
import mysql.connector
import dbconfig as cfg

class StatesDAO:  # Class for DB object
    
    # Initialise pool connection
    def initConnectToDB(self):
        db = mysql.connector.connect(
            host=       cfg.mysql['host'],
            user=       cfg.mysql['user'],
            password=   cfg.mysql['password'],
            database=   cfg.mysql['database'],
            pool_name='my_connection_pool',
            pool_size=2   # pythonanywhere doesnt like too many connections. App should work ok with 2.
        )
        return db

    def getConnection(self): # get a pool connection
        db = mysql.connector.connect(
            pool_name='my_connection_pool'
        )
        return db

    def __init__(self): # initialise pool connection when constructing class object
        db=self.initConnectToDB()
        db.close()
            

    def getAll(self): # Method to get All from DB
        db = self.getConnection() # get a connection
        cursor = db.cursor()   # make cursor
        sql="select * from states"
        cursor.execute(sql) # run the sql 
        results = cursor.fetchall()  # get results from cursor
        cursor.close() # Close the cursor
        returnArray = [] # an array for the results
        
        for result in results:  # iterate over results
            returnArray.append(self.convertToDictionary(result))  # append to return array
        db.close() # close DB connection
        return returnArray  

    def findByAbv(self, abv):  # Method to find state by ABV
        db = self.getConnection() # get a connection
        cursor = db.cursor() # make cursor
        sql="select * from states where  abv = %s"
        values = (abv,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        cursor.close()
        state=self.convertToDictionary(result)
        db.close() # close connection
        return state

    def update(self, values): # Method to find state by ABV
        db = self.getConnection()  # get a connection
        cursor = db.cursor() # make cursor
        sql="update states set tv = %s, bv = %s, tp = %s, bp = %s where abv = %s"
        cursor.execute(sql, values)
        db.commit() # Commit the update
        cursor.close()
        db.close() # close connection


        

    def convertToDictionary(self, result): # Method to convert cursor results to a dictionary
        colnames=['name','abv','ecv', 'tv','bv','tp','bp']
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item

statesDAO = StatesDAO() # Make a StatesDAO object