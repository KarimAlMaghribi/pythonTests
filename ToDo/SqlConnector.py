import psycopg2
import sys
import Window
from datetime import datetime

class SQLConnector:

    
    def __init__ (self):
        
        self.dbname     =   "To_Do_Database"
        self.user       =   "postgres"
        self.password   =   "bitctrl"
        self.host       =   "localhost"
        self.port       =   "5432"

    

    def connect(self):
        

        try:

            connectionToDataBase = psycopg2.connect(
               
                host        = self.host,
                port        = self.port,
                database    = self.dbname,
                user        = self.user,
                password    = self.password
            )

            return connectionToDataBase


        except:

            print (" Can not connect to the database ' " + self.dbname + "'.")
            print("Unexpected error:", sys.exc_info()[0])


    def uploadNewItem(self, item):

        self.strToDo = item[0]
        self.checkDone = item[1]
        self.dateToDo = item[2].strftime("%d.%m.%y")
        
        connectionToDataBase = self.connect()

        try:
    
            cursor = connectionToDataBase.cursor()

            cursor.execute("INSERT INTO public.\"to_do_db\" VALUES ('" + self.strToDo + "', DEFAULT, '" +  self.dateToDo + "');")
        
            connectionToDataBase.commit()

            cursor.close()
            connectionToDataBase.close()

        
        except:

            print("Unexpected error:", sys.exc_info()[0])


    def changeItem(self, item, window):

        self.strToDo = item[0]
        self.checkDone = item[1]
        timeItem = item[2]
        timeItem = timeItem[:6] + timeItem[6:]
        
  
        
        connectionToDataBase = self.connect()

        try:
            
            cursor = connectionToDataBase.cursor()
                
            cursor.execute("""UPDATE public."to_do_db" SET "strToDo" = '""" + self.strToDo + """' WHERE id = """+ str( self.numberOfList ) + """;
                                UPDATE public."to_do_db" SET "booleanDone" = '""" + str(self.checkDone) + """' WHERE id = """+ str( self.numberOfList ) + """;
                                UPDATE public."to_do_db" SET "toDoDate" = '"""+ timeItem + """' WHERE id =""" + str( self.numberOfList ) + """;""" )
            
            connectionToDataBase.commit()

            cursor.close()
            connectionToDataBase.close()

        except:
            print (" Can not change item in database ' " + self.dbname + "'.")
            print("Unexpected error:", sys.exc_info()[0])

       

    
    def downloadItem (self, numberOfList):

        self.numberOfList = numberOfList
         
        connectionToDataBase = self.connect()
        
        
        try:
        
            cursor = connectionToDataBase.cursor()

            cursor.execute('SELECT * FROM public."to_do_db" WHERE id = ' + str( self.numberOfList ) + ';')
        
            downloadedItem = cursor.fetchall()

            cursor.close()
            connectionToDataBase.close()
            
            return downloadedItem   


        except:
            print("Unexpected error:", sys.exc_info()[0])
            print("Es war nicht möglich diese Daten herunterzuladen.")
    



    def getallItemsForList(self):

        connectionToDataBase = self.connect()

        try:
        
            
            cursor = connectionToDataBase.cursor()

            cursor.execute(' SELECT * FROM public."to_do_db" ORDER BY id ')
        
            allItems = cursor.fetchall()

            cursor.close()
            connectionToDataBase.close()
            
            return allItems   


        except:
            print("Unexpected error:", sys.exc_info()[0])
            print("Es war nicht möglich diese Daten herunterzuladen.")    

    def addListItem(self, item, window ):

        self.uploadNewItem(item)
    


    def getLastID(self):

        connectionToDataBase = self.connect()

        try:
        
            cursor = connectionToDataBase.cursor()

            cursor.execute(' SELECT max(id) FROM public."to_do_db" ')
        
            lastID = cursor.fetchone()

            cursor.close()
            connectionToDataBase.close()
           
            return lastID[0]   


        except:
            print("Unexpected error:", sys.exc_info()[0])
            print("Es war nicht möglich die letzte ID zu bekommen.") 


    def getAllDone(self):

        connectionToDataBase = self.connect()

        try:

            cursor= connectionToDataBase.cursor()

            cursor.execute(' SELECT id FROM public.to_do_db where public.to_do_db."booleanDone" = TRUE ')   

            all_DONE_items = cursor.fetchall()

            cursor.close()
            connectionToDataBase.close()

            return all_DONE_items
        
        except:
            print("Unexpected error:", sys.exc_info()[0])
            print("\n\nEs konnte keine erledigten Items aus der DB geholt werden")
