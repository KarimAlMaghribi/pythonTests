import SqlConnector
import time
import sys
import Picture
import CSV_File

class Window:
    
    def textOutPut_hack(self, string):

        length_Of_String = len(string)
        
        i = 0
        while i < length_Of_String:
            print(string[i], end="")
            sys.stdout.flush()
            time.sleep(.035)
            i += 1

    def __init__(self):

        self.top =  "*" * 25 + " TO_DO_LISTE_DB  " + "*" * 25
        self.bottom = "*" * 67

    def initTop(self) :
        print(self.top)

    def initialiseStart(self, csvArray, dbArray):

        self.startWindow()
        choise = self.getStartChoise()
        index_for_nxtStep =self.choiseControl(choise)

        if index_for_nxtStep == "csv" :
            return "1"
            
        elif index_for_nxtStep == "db" :
            return "2"
        else: 
            self.initialiseStart(csvArray, dbArray)

    def startWindow(self):
        pic = Picture.Picture.getPicture(self)
        welcome_string = " "*8 + "WILLKOMMEN ZURÜCK IN IHREM TO-DO-LISTEN-PROGRAMM" + " "*9
        print("┌" + "─" * 65 + "┐")
        self.textOutPut_hack("│" + welcome_string + "│\n")
        print("└" + "─" * 65 + "┘" ) 
        print (pic)

    def getStartChoise(self):
        print("┌" + "─" * 65 + "┐")
        self.textOutPut_hack("│" + " "*17 + "WELCHE DER OPTIONEN WÄHLEN SIE?" + " "*17 + "│\n")   
        choise = str(input("└" + "─" * 65 + "┘\n >>>   "))
        return choise

    def choiseControl(self, choise):

        if choise == "1" :
            return "csv"
        elif choise == "2":
            return "db"
        else :
            return "false"

    def initBottom(self):
        print(self.bottom)

    def generateStringForList(self, item):
        
        self.strToDo = item[0]
        self.checkDone = item[1]
        self.dateToDo = item[2].strftime("%d.%m.%y")
        self.numberOfList = item[3]

        stringForList = "* " + str( self.numberOfList ) + " [ " + str(self.checkDone) + " ] " + self.strToDo +  ", am " + self.dateToDo + " *"
        stringOhneStrToDoForList = "* " + str( self.numberOfList ) + " [ " + str(self.checkDone) + " ] , am " + self.dateToDo + " *"
        
        lengthStringOhne= len(stringOhneStrToDoForList)
        lengthPreviousString = len(stringForList)

        if lengthPreviousString > 67:

            strToDo = self.strToDo[ 0 : 64 - lengthStringOhne ] + "..."

            stringForList = "* " + str( self.numberOfList ) + " [ " + str(self.checkDone) + " ] " + strToDo +  ", am " + self.dateToDo + " *"

            return stringForList
        
        else:

            starsForRemaingSpace = (67 - lengthPreviousString)//2
            starString = ( "." * starsForRemaingSpace )

            if  (67 - lengthPreviousString) % 2 == 1:

                stringForList = "* " + str( self.numberOfList ) + " [ " + str(self.checkDone) + " ] " + starString +  self.strToDo + starString + "." + ", am " + self.dateToDo + " *"
            
            else:
                
                stringForList = "* " + str( self.numberOfList ) + " [ " + str(self.checkDone) + " ] " + starString +  self.strToDo + starString + ", am " + self.dateToDo + " *"
        
            return stringForList


    def setWelcomeText(self):
        
        print("\n\nDie Organisation des Arbeitsablaufes durch Tätigkeitslisten in die noch unerledigte Aufgaben festgehalten werden," +
            "ist eine erfolgreiche Arbeitstechnik zur Strukturierung und Verwaltung anfallender Aufgaben. Dieses schriftliche Planen" +
            " hilft nicht nur seine Vergeßlichkeit in den Griff zu bekommen, sondern ist oftmals bereits der erste Schritt zur Bewältigung der Dinge. Los gehts!\n\n")

        print("Hier finden Sie Ihre To-Do-Liste:")


    def initMenu (self, arrAllItems_Index):
        
        if arrAllItems_Index == "1":

            print("Menu:\nWählen Sie zwischen den folgenden Optionen: ")
            print("?    ->      Statistik")
            print("n    ->      Neuer Listen - Eintrag")
            print("l    ->      Einen Eintrag lesen")
            print("s    ->      Status eines Eintrags ändern")
            print("t    ->      Nächste Seite der To - Do - Liste")
            print("p    ->      Vorrige Seite der To - Do - Liste")
            print("i    ->      CSV-Datei in DB importieren")

        else :

            print("Menu:\nWählen Sie zwischen den folgenden Optionen: ")
            print("?    ->      Statistik")
            print("n    ->      Neuer Listen - Eintrag")
            print("l    ->      Einen Eintrag lesen")
            print("s    ->      Status eines Eintrags ändern")
            print("t    ->      Nächste Seite der To - Do - Liste")
            print("p    ->      Vorrige Seite der To - Do - Liste")
            print("e    ->      Datensätze der DB in die CSV-Datei exportieren")

    def changingInteraction(self):

        print("Sie haben folgende Option zur Änderung Ihrer Eingaben:\n\n")
        
        print("( t )  ||  Tätigkeit ändern ")
        print("( d )  ||  Datum ändern ")
        print("( s )  ||  Status ändern ")
        print("( q )  ||  Verlassen \n\n")

        command = input ("Was ist Ihr Wunsch?   ")
        
        return command   


    def getCommand(self, arrAllItems_Index):

        if arrAllItems_Index == "1":
           
            command = input("Meine Wahl ist:   ")

            if command == "n" :            
                return "n"

            elif command == "l" :
                return "l"

            elif command == "s":
                
                #print("Mit dieser Option, können Sie eines Ihrer Einträge ändern.")
                #numberOfList = input("Welche Nummer in Ihrer Liste wollen Sie ändern?   ")
                
                #List.changeSpecifiedItemOfList(numberOfList)

                return "s"

            elif command == "t" :
                return "t"
            #   List.pageChanger("t")    
            #  print("")
            
            elif command == "p" :
                return "p"
        

        else :

            command = input("Meine Wahl ist:   ")

            if command == "n" :            
                return "n"

            elif command == "l" :
                return "l"

            elif command == "s":
                return "s"

            elif command == "t" :
                return "t"
                  
            elif command == "p" :
                return "p"
            

    def printListOfItems(self, items):
        
        for item in items:
            print(item)

    def getherListOfItems(self, arrAllItems, index, arrAllItems_Index):

        if arrAllItems_Index == "1":
            
            file = CSV_File.CSV_File()
            number = file.getNumberOfItems()

            listOf_ALL_Items = []
            listOf_LEFT_Items = []
            listOf_RIGHT_Items = []
            length_ALL_Items = len(arrAllItems)
            i = 0

            if index == 0:

                if number > 10:
                    
                    pageReminder =  "*" * 25 + "  SEITE 1 VON 2  " + "*" * 25
                    listOf_LEFT_Items.append( pageReminder )
                    
                    while i < 10:
                    
                        listOf_LEFT_Items.append(self.generateStringForList( arrAllItems[i] ))
                        i = i + 1
                    
                    return listOf_LEFT_Items
                
                else:

                    for item in arrAllItems:
                
                        listOf_ALL_Items.append( self.generateStringForList(item) )

                    return listOf_ALL_Items
            
            elif index == 1:

                if number > 10:
                    
                    pageReminder =  "*" * 25 + "  SEITE 2 VON 2  " + "*" * 25
                    listOf_RIGHT_Items.append( pageReminder )    

                    for i in range( 10, length_ALL_Items ):

                        listOf_RIGHT_Items.append(self.generateStringForList( arrAllItems[i] ))
                        i = i + 1
                    
                    return listOf_RIGHT_Items

                else:

                    for item in arrAllItems:
                
                        listOf_ALL_Items.append( self.generateStringForList(item) )

                    return listOf_ALL_Items


        else:

            connector = SqlConnector.SQLConnector()
            number = connector.getLastID()

            listOf_ALL_Items = []
            listOf_LEFT_Items = []
            listOf_RIGHT_Items = []
            length_ALL_Items = len(arrAllItems)
            i = 0

            if index == 0:

                if number > 10:
                    
                    pageReminder =  "*" * 25 + "  SEITE 1 VON 2  " + "*" * 25
                    listOf_LEFT_Items.append( pageReminder )
                    
                    while i < 10:
                    
                        listOf_LEFT_Items.append(self.generateStringForList( arrAllItems[i] ))
                        i = i + 1
                    
                    return listOf_LEFT_Items
                
                else:

                    for item in arrAllItems:
                
                        listOf_ALL_Items.append( self.generateStringForList(item) )

                    return listOf_ALL_Items
            
            elif index == 1:

                if number > 10:
                    
                    pageReminder =  "*" * 25 + "  SEITE 2 VON 2  " + "*" * 25
                    listOf_RIGHT_Items.append( pageReminder )    

                    for i in range( 10, length_ALL_Items ):

                        listOf_RIGHT_Items.append(self.generateStringForList( arrAllItems[i] ))
                        i = i + 1
                    
                    return listOf_RIGHT_Items

                else:

                    for item in arrAllItems:
                
                        listOf_ALL_Items.append( self.generateStringForList(item) )

                    return listOf_ALL_Items


    def initToDoList(self, arrAllItems, pageIndex, arrAllItems_Index):

        self.initTop()
        listOfItems = self.getherListOfItems(arrAllItems, pageIndex, arrAllItems_Index)
        self.printListOfItems(listOfItems)
        self.initBottom()
        self.initMenu(arrAllItems_Index)
        nxtStep = self.getCommand(arrAllItems_Index)

        return nxtStep
        

