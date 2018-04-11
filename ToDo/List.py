# -*- coding: utf-8 -*-
import UserInteraction
import SqlConnector


class ItemOfToDoList:
    
    def __init__ (self, booleanDone, strToDo, dateToDo):

        self.booleanDone = booleanDone
        self.strToDo = strToDo
        self.dateToDo = dateToDo
'''
maTodoList = MyToDoList( 'database=mydb, user=bla, pass=bla, host=localhost' )
if ( maTodoList.connect() )
    maTodoList.printList()

    while( cmd = maTodoList.getCMD( ) !== 'q' )
        if( cmd === 'n' )

        else if (cmd === 'l' )
            maTodoList.startRead( )
        else
            print( 'Wow, den Befehl kenne ich nicht' )

else 
    print( 'UPS. Ich kann nicht zu DB Verbindung aufbauen' )


newItem = ItemOfToDoList()
newItem.setToDO( 'Muss noch was erledigen' )
newItem.setDate( time( ) + 2T )
'''

def generateStringForList(numberOfList, checkDone, strToDo, dateToDo):
    
    stringForList = "* " + str(numberOfList) + " [ " + str(checkDone) + " ] " + strToDo +  ", am " + dateToDo + " *"
    stringOhneStrToDoForList = "* " + str(numberOfList) + " [ " + str(checkDone) + " ] , am " + dateToDo + " *"
    
    lengthStringOhne= len(stringOhneStrToDoForList)
    lengthPreviousString = len(stringForList)

    if lengthPreviousString > 67:

        strToDo = strToDo[ 0 : 64 - lengthStringOhne ] + "..."

        stringForList = "* " + str(numberOfList) + " [ " + str(checkDone) + " ] " + strToDo +  ", am " + dateToDo + " *"

        return stringForList
    
    else:

        starsForRemaingSpace = (67 - lengthPreviousString)//2
        starString = ( "." * starsForRemaingSpace )

        if  (67 - lengthPreviousString) % 2 == 1:

            stringForList = "* " + str(numberOfList) + " [ " + str(checkDone) + " ] " + starString + strToDo + starString + "." + ", am " + dateToDo + " *"
        
        else:
            
            stringForList = "* " + str(numberOfList) + " [ " + str(checkDone) + " ] " + starString + strToDo + starString + ", am " + dateToDo + " *"
       
        return stringForList

def pageChanger(command):
    
    initTop()
       
    listOfItems = []

    arrAllItems = SqlConnector.getallItemsForList()

    for item in arrAllItems:
        
        strToDo = item[0]
        checkDone = item[1]
        dateToDo = item[2]
        numberOfList = item[3]

        
        listOfItems.append( generateStringForList(numberOfList, checkDone, strToDo, dateToDo) )
    
    if command == "t":
        
        if len(listOfItems) > 10:

            firstTenItems = listOfItems[:10]
            lastItems =  listOfItems[10:]

            for item in lastItems:
                print(item)
   
        
        else:
            for item in listOfItems:
                print(item)


       

    elif command == "p" :
        
        if len(listOfItems) > 10:

            firstTenItems = listOfItems[:10]
            lastItems =  listOfItems[10:]

            for item in firstTenItems:
                print(item)
   
        
        else:
            for item in listOfItems:
                print(item)

    
    initBottom()
    UserInteraction.initMenu()
    UserInteraction.getCommand()


def initListOfItems():

    listOfItems = []

    arrAllItems = SqlConnector.getallItemsForList()

    for item in arrAllItems:
        
        strToDo = item[0]
        checkDone = item[1]
        dateToDo = item[2]
        numberOfList = item[3]

        
        listOfItems.append( generateStringForList(numberOfList, checkDone, strToDo, dateToDo) )
    
    
    for item in listOfItems:
        print(item)

def initTop() :
   
        print("*" * 25 + " TO - DO - LISTE " + "*" * 25)

def initBottom():
        print("*" * 67)

def addListItem( strToDo, dateToDo ):

    SqlConnector.uploadItem(strToDo, dateToDo)
    
    #arrAllItems = SqlConnector.getallItemsForList()

   # initListOfItems()

    initToDoList()


def initToDoList():
    
    initTop()
    initListOfItems()
    initBottom()
    UserInteraction.initMenu()
    UserInteraction.getCommand()

def putOutSpecifiedItemOfList(numberOfList):
    
    downloadedItem = SqlConnector.downloadItem(numberOfList)

           
    strToDo = downloadedItem[0][0]
    checkDone = downloadedItem[0][1]
    dateToDo = downloadedItem[0][2]
    numberOfList = downloadedItem[0][3]

    if checkDone == True:
    
        print("Für den   " + dateToDo + "   haben Sie Folgendes geplant:\n\n" + strToDo + "\n\nSie haben diese Aufgabe erledigt.")

    else:

         print("Für den   " + dateToDo + "   haben Sie Folgendes geplant:\n\n" + strToDo + "\n\nSie haben diese Aufgabe noch nicht erledigt.")

    UserInteraction.checkIfReady()


def changeSpecifiedItemOfList(numberOfList):

    downloadedItem = SqlConnector.downloadItem(numberOfList)
    
    strToDo = downloadedItem[0][0]
    checkDone = downloadedItem[0][1]
    dateToDo = downloadedItem[0][2]
    numberOfList = downloadedItem[0][3]

    command = UserInteraction.changingInteraction()

    if command == "t":
        print("Sie wollen die Tätigkeit vom " + dateToDo + " ändern.")
        stringInput = input("Geben Sie den neuen Eintrag ein:\n\n")

        checker = input("Eintrag speichern? || ( y ) OR ( n )   ")

        
        if checker == "y" :
            
            SqlConnector.changeItem(numberOfList, stringInput, dateToDo, checkDone)
            initToDoList()

        elif checker == "n" :
            
             command = UserInteraction.changingInteraction()
        
        else: 
            
            print("Ihre Eingabe war nicht korrekt")
            command = UserInteraction.changingInteraction()
    
    elif command == "d":
        
        print("Sie wollen das Datum, der Tätigkeit ' " + strToDo[0:10] + "..."+ " ' ändern.")
        dateInput = input("Geben Sie hierfür ein neues Datum ein:\n\n")

        checker = input("Eintrag speichern? || ( y ) OR ( n )   ")
        
        if checker == "y" :
            SqlConnector.changeItem(numberOfList, strToDo, dateInput, checkDone)
            initToDoList()
        
        elif checker == "n" :
             command = UserInteraction.changingInteraction()
        
        else: 
            print("Ihre Eingabe war nicht korrekt")
            command = UserInteraction.changingInteraction()
    
    elif command == "s":

        print(" Sie wollen den Status, der Tätigkeit ' " + strToDo[0:10] + "..."+ " am " + dateToDo +" ändern.")
        
        if checkDone == True:

            checkerStatusChange = input("Wollen Sie den auf 'NICHT ERLEDIGT' stellen? ||  ( y ) OR ( n )   ")
        
        else:

            checkerStatusChange = input("Wollen Sie den auf 'ERLEDIGT' stellen? ||  ( y ) OR ( n )  ")
        
        if checkerStatusChange == "y":

            booleanInput =  checkDone == False     
            SqlConnector.changeItem(numberOfList, strToDo, dateToDo, booleanInput)
            initToDoList()

        elif checkerStatusChange == "n" :

             initToDoList()

        else : 

            print("Sie haben eine falsche Angabe gemacht.")
            initToDoList()

    
