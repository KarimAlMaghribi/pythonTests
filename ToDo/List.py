# -*- coding: utf-8 -*-
import UserInteraction
import SqlConnector


class ItemOfToDoList:
    
    def __init__ (self, booleanDone, strToDo, dateToDo):

        self.booleanDone = booleanDone
        self.strToDo = strToDo
        self.dateToDo = dateToDo

    














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

    
