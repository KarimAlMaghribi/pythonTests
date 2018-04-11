import psycopg2
import sys

dbname = "To_Do_Database"
user = "postgres"
password = "bitctrl"
host = "localhost"
port = "5433"



def changeItem(numberOfList, strToDo, dateToDo, booleanDone):

    try:

        connectionToDataBase = psycopg2.connect(
            host = host,
            port = port,
            database = dbname,
            user = user,
            password = password
        )

       

    except:

        print (" Can not connect to the database ' " + dbname + "'.")

    try:
    
        cursor = connectionToDataBase.cursor()
        cursor.execute("""UPDATE public."Items" SET "strToDo" = '""" + strToDo + """' WHERE id = """+ str( numberOfList ) + """;
                          UPDATE public."Items" SET "booleanDone" = '""" + str(booleanDone) + """' WHERE id = """+ str( numberOfList ) + """;
                          UPDATE public."Items" SET "toDoDate" = '"""+ dateToDo + """' WHERE id =""" + str( numberOfList ) + """;""" )
    
        connectionToDataBase.commit()

        cursor.close()
        connectionToDataBase.close()

    except:
        print("Unexpected error:", sys.exc_info()[0])

def uploadItem (strToDo, dateToDo):

      
    try:

        connectionToDataBase = psycopg2.connect(
            host = host,
            port = port,
            database = dbname,
            user = user,
            password = password
        )

        

    except:

        print (" Can not connect to the database ' " + dbname + "'.")
        print("Unexpected error:", sys.exc_info()[0])

    try:
    
        cursor = connectionToDataBase.cursor()
        cursor.execute("INSERT INTO public.\"Items\" VALUES ('" + strToDo + "', DEFAULT, '" + dateToDo + "');")
    
        connectionToDataBase.commit()

        cursor.close()
        connectionToDataBase.close()
        
        

    except:

        print("Es war nicht möglich diese Daten hochzuladen.")
        print("Unexpected error:", sys.exc_info()[0])
    
   
def downloadItem (numberOfList):

    try:

        connectionToDataBase = psycopg2.connect(
            host = host,
            port = port,
            database = dbname,
            user = user,
            password = password
        )

        print ( "Ich bin verbunden." )

    except:

        print (" Can not connect to the database ' " + dbname + "'.")
        print("Unexpected error:", sys.exc_info()[0])

    try:
    
        cursor = connectionToDataBase.cursor()

        cursor.execute('SELECT * FROM public."Items" WHERE id = ' + str( numberOfList ) + ';')
    
        downloadedItem = cursor.fetchall()

        cursor.close()
        connectionToDataBase.close()
        
        return downloadedItem   


    except:
        print("Unexpected error:", sys.exc_info()[0])
        print("Es war nicht möglich diese Daten herunterzuladen.")
    

def getLastID():

    try:

        connectionToDataBase = psycopg2.connect(
            host = host,
            port = port,
            database = dbname,
            user = user,
            password = password
        )

      

    except:

        print (" Can not connect to the database ' " + dbname + "'.")
        print("Unexpected error:", sys.exc_info()[0])

    try:
    
        cursor = connectionToDataBase.cursor()

        cursor.execute(' SELECT max(id) FROM public."Items" ')
    
        lastID = cursor.fetchone()

        cursor.close()
        connectionToDataBase.close()
        
        print(lastID[0])   

        return lastID[0]   


    except:
        print("Unexpected error:", sys.exc_info()[0])
        print("Es war nicht möglich die letzte ID zu bekommen.")     

def getallItemsForList():

    try:

        connectionToDataBase = psycopg2.connect(
            host = host,
            port = port,
            database = dbname,
            user = user,
            password = password
        )

        

    except:

        print (" Can not connect to the database ' " + dbname + "'.")
        print("Unexpected error:", sys.exc_info()[0])

    try:
    
        
        cursor = connectionToDataBase.cursor()

        cursor.execute(' SELECT * FROM public."Items" ORDER BY id ')
    
        allItems = cursor.fetchall()

        cursor.close()
        connectionToDataBase.close()
        
        return allItems   


    except:
        print("Unexpected error:", sys.exc_info()[0])
        print("Es war nicht möglich diese Daten herunterzuladen.")     
