import Connector
import sys
import psycopg2

class DB_Connector(Connector.Connector):
   
    def __init__ (self):
        
        self.dbname     =   "To_Do_Database"
        self.user       =   "postgres"
        self.password   =   "bitctrl"
        self.host       =   "localhost"
        self.port       =   "5432"

        self.connection = self.connect()

    
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

            print ("!!!   CAN NOT CONNECT TO DATABASE ' " + self.dbname + "'.")
            print("!!!   Unexpected error:", sys.exc_info()[0])
    

    def save(self, item):
        
        self.strToDo = item[0]
        self.checkDone = item[1]
        self.dateToDo = item[2].strftime("%d.%m.%y")
        

        try:
    
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO public.\"to_do_db\" VALUES ('" + self.strToDo + "', DEFAULT, '" +  self.dateToDo + "');")
            self.connection.commit()
            cursor.close()
            
        except:

            print("Unexpected error:", sys.exc_info()[0]) 
    

    def load_all(self):
        
        try:
        
            cursor = self.connection.cursor()
            cursor.execute(' SELECT * FROM public."to_do_db" ORDER BY id ')
            allItems = cursor.fetchall()
            cursor.close()
            
            return allItems   


        except:
            print("Unexpected error:", sys.exc_info()[0])
            print("Es war nicht möglich diese Daten herunterzuladen.")    
    
    
    def load_by_id(self, id_of_item):
        
        numberOfList = id_of_item

        try:
        
            cursor = self.connection.cursor()
            cursor.execute('SELECT * FROM public."to_do_db" WHERE id = ' + str( numberOfList ) + ';')
            downloadedItem = cursor.fetchall()
            cursor.close()
            
            return downloadedItem   


        except:
            print ("!!!   CAN NOT LOAD THIS ITEM IN ' " + self.dbname + "'.")
            print("!!!   Unexpected error:", sys.exc_info()[0])

    
    def update_item(self, item, id_of_item):
        
        numberOfList = id_of_item
        strToDo = item[0]
        checkDone = item[1]
        timeItem = item[2]
        timeItem = timeItem[:6] + timeItem[6:]
        

        try:
            
            cursor = self.connection.cursor()
                
            cursor.execute("""UPDATE public."to_do_db" SET "strToDo" = '""" + strToDo + """' WHERE id = """+ str( numberOfList ) + """;
                                UPDATE public."to_do_db" SET "booleanDone" = '""" + str(checkDone) + """' WHERE id = """+ str( numberOfList ) + """;
                                UPDATE public."to_do_db" SET "toDoDate" = '"""+ timeItem + """' WHERE id =""" + str( numberOfList ) + """;""" )
            
            self.connection.commit()

            cursor.close()
            

        except:
            print ("!!!   CAN NOT UPDATE THIS ITEM IN ' " + self.dbname + "'.")
            print("!!!   Unexpected error:", sys.exc_info()[0])

    def get_last_id(self):
        
        try:
        
            cursor = self.connection.cursor()
            cursor.execute(' SELECT max(id) FROM public."to_do_db" ')
            lastID = cursor.fetchone()
            cursor.close()
                       
            return lastID[0]   


        except:
            print (" CAN NOT GET LAST_ID FROM LIST OF ' " + self.dbname + "'.")
            print("Unexpected error:", sys.exc_info()[0]) 


    def get_done_items(self):
        
        try:

            cursor= self.connection.cursor()

            cursor.execute(' SELECT id FROM public.to_do_db where public.to_do_db."booleanDone" = TRUE ')   

            all_DONE_items = cursor.fetchall()

            cursor.close()
          
            return all_DONE_items
        
        except:  
            print (" CAN NOT GET DONE ITEMS FROM LIST OF ' " + self.dbname + "'.")
            print("Unexpected error:", sys.exc_info()[0]) 

    def close(self):
        
        try:

            self.connection.close()

        except:
            print (" CAN NOT CLOSE DB - CONNECTION FROM ' " + self.dbname + "'.")
            print("Unexpected error:", sys.exc_info()[0]) 

      