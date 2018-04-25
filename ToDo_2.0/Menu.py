import Picture
import sys
import DB_Connector
import CSV_Connector
import time
from datetime import datetime 
import ListItem

class Menu:
    def __init__( self ):
        self.listeners = { }

    def on( self, pStrMenuname, pStrEvent, pFunCallback ):
        key = pStrMenuname + ':' + pStrEvent # hauptmenu:q
        self.listeners[ key ] = pFunCallback

    def getUserInput( self, pStrMessage = None ):
        if pStrMessage != None:
            self.textOutPut_hack( pStrMessage )
        return input(">>> ")

    def textOutPut_hack(self, string):

        length_Of_String = len(string)
        
        i = 0
        while i < length_Of_String:
            print(string[i], end="")
            sys.stdout.flush()
            time.sleep(.035)
            i += 1
    
    def startMenu (self):

        pic = Picture.Picture.getPicture(self)
        
        welcome_string = " "*8 + "WILLKOMMEN ZURÜCK IN IHREM TO-DO-LISTEN-PROGRAMM" + " "*9
        print("┌" + "─" * 65 + "┐")
        self.textOutPut_hack("│" + welcome_string + "│\n")
        print("└" + "─" * 65 + "┘" ) 
        
        print (pic)

        print("┌" + "─" * 65 + "┐")
        self.textOutPut_hack("│" + " "*17 + "WELCHE DER OPTIONEN WÄHLEN SIE?" + " "*17 + "│\n")
        print("└" + "─" * 65 + "┘\n")

        choise = str( self.getUserInput( ) )
    
        if choise == "1" :
            if 'hauptmenu:1' in self.listeners:
            self.listeners[ 'hauptmenu:1' ]
            
            """self.textOutPut_hack( ">>>   SIE WERDEN ZUM CSV-MENU WEITERGELEITET .........\n\n" )
            connector = CSV_Connector.CSV_Connector()
            self.main_menu(connector, 1)"""

        elif choise == "2":
            if 'hauptmenu:2' in self.listeners:
            self.listeners[ 'hauptmenu:2' ]
            
            """self.textOutPut_hack( ">>>   SIE WERDEN ZUM DB-MENU WEITERGELEITET .........\n\n" )
            connector = DB_Connector.DB_Connector()
            self.main_menu(connector, 1)"""


        elif choise == "q" or choise == "Q" :
            if 'hauptmenu:q' in self.listeners:
                self.listeners[ 'hauptmenu:q' ]( )

            #self.textOutPut_hack( """>>>   DIE ANWENDUNG WIRD GESCHLOSSEN... \n\n 
            #                         >>>   WIR FREUEN UNS, SIE WIEDER ZU SEHEN.""" )

            #sys.exit()

        else: 

            print("\n!!!   WARNING: FALSCHE EINGABE. VERSUCHEN SIE ES NOCH EINMAL.")
            self.startMenu()
    

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

    
    def insertlistItems(self, number_selected_page, arrAllItems):

        length_of_list = len(arrAllItems)
        list_of_selected_page = []
        i =  10 * (number_selected_page - 1) -1
        
        max_page_number = length_of_list//10
        
        if length_of_list%10 > 0:
            max_page_number += 1

        pageReminder =  "*" * 25 + "  SEITE " + str(number_selected_page) + " VON " + str(max_page_number) + "  " + "*" * 25
        list_of_selected_page.append(pageReminder)

        while  i < 10 * number_selected_page - 1:
            if i == length_of_list:
                break
            if i < 0:
                i += 1
                continue
            list_of_selected_page.append( self.generateStringForList(arrAllItems[i]) )
            i += 1

        self.printlist(list_of_selected_page)


    def printlist(self, list_of_selected_page):

        for list_item in list_of_selected_page:
            print(list_item)


    def main_menu(self, connector, pageNumber):

        
        print( "*" * 27 + " TO_DO_LISTE  " + "*" * 26 )

        arrAllItems = connector.load_all()
        length_of_list = len(arrAllItems)

        max_page_number = length_of_list//10
            
        if length_of_list%10 > 0:
            max_page_number += 1 

        if pageNumber > max_page_number :
            pageNumber -= 1



        self.insertlistItems( pageNumber, arrAllItems )

        print ("*" * 67)
    
        self.textOutPut_hack("\n\nMENU:\nWÄHLEN SIE ZWISCHEN DEN FOLGENDEN OPTIONEN: \n")
            
        print("─" * 67 )
        print("s    ->      Statistik")
        print("n    ->      Neuer Listen - Eintrag")
        print("l    ->      Einen Eintrag lesen")
        print("a    ->      Status eines Eintrags ändern")
        print("t    ->      Nächste Seite der To - Do - Liste")
        print("p    ->      Vorrige Seite der To - Do - Liste")
        print("─" * 67 )

        command = self.getUserInput( "\nMEINE WAHL IST:\n" )
        
        if not command in ("s", "n", "l", "a", "t", "p"):

            self.textOutPut_hack("\n\n >>>   IHRE EINGABE WAR NICHT KORREKT.\n\n")
            self.main_menu(connector, pageNumber)

        self.main_menu_interaction(connector, command, pageNumber)

    def main_menu_interaction(self, connector, command, pageNumber):

        if command == "n" :
            
            newToDoData = self.getUserInput("WAS HABEN SIE VOR?\n")
            newToDoDate = self.getUserInput("\nAN WELCHEN DATUM? || dd.mm.yyyy\n")

            try:

                ToDoDate = datetime.strptime(newToDoDate, "%d.%m.%Y")

                if ToDoDate < datetime.now():
                    self.textOutPut_hack("\n\n>>>   DIESES DATUM LIEGT IN DER VERGANGENHEIT\n\n")
                    self.main_menu_interaction(connector, command, pageNumber)
                
            except:
                
                self.textOutPut_hack("\n\n >>>   IHRE EINGABE WAR NICHT KORREKT.\n\n")
                
                self.main_menu_interaction(connector, command, pageNumber)

            self.textOutPut_hack("\n\n>>>   WOLLEN SIE DIESEN EINTRAG SPEICHERN?   |||   ( Y ) OR ( N )\n\n")
            check_whether_save = input (">>>   ")

            if check_whether_save == "Y" or check_whether_save == "y":

                item = ListItem.ItemOfToDoList(newToDoData, ToDoDate)
                newItemforDB = item.getItem()

                connector.save()

                self.are_you_ready(connector, command, pageNumber)

            elif check_whether_save == "N" or check_whether_save == "n":

                self.are_you_ready(connector, command, pageNumber)

        elif command == "l" :
                
            self.textOutPut_hack(">>>   MIT DIESER OPTION KÖNNEN SIE EINES IHRER EINTRÄGE AUSLESEN.\n")
            self.textOutPut_hack(">>>   WELCHE NUMMER WOLLEN SIE AUSLESEN?   ") 
            numberOfList = input("\n>>>   ")   

            downloadedItem = connector.load_by_id(numberOfList)

            item = ListItem.ItemOfToDoList(downloadedItem[0][0], downloadedItem[0][2], downloadedItem[0][1])
            newItemforDB = item.getItem()

            strToDo         = newItemforDB[0]
            dateToDo        = newItemforDB[2].strftime("%d.%m.%y")
            checkDone       = newItemforDB[1]

            
            if checkDone == True:
                
                print("\n>>>   FÜR DEN   " + dateToDo + "   HABEN SIE FOLGENDES GEPLANT:\n\n" + strToDo + "\n\nSIE HABEN DIESE AUFGABE ERLEDIGT.")
                    
                self.are_you_ready(connector, command, pageNumber)
          
            else:

                print("\n>>>   FÜR DEN   " + dateToDo + "   HABEN SIE FOLGENDES GEPLANT:\n\n" + strToDo + "\n\nSIE HABEN DIESE AUFGABE NOCH NICHT ERLEDIGT.")
                
                self.are_you_ready(connector, command, pageNumber)

        elif command == "a" :
                
            self.textOutPut_hack("\n>>>   MIT DIESER OPTION KÖNNEN SIE IHRE EINTRÄGE BEARBEITEN.\n")
            self.textOutPut_hack(">>>   BEI WELCHER LISTEN-NUMMER SOLL DIES GESCHEHEN ?\n")
            numberOfList = int(input(">>>   ") )
            i = 1
            listOfNumbers = []
            number = connector.get_last_id()
            
            while i < number + 1 :
                listOfNumbers.append(i)
                i += 1

            if not numberOfList in listOfNumbers :

                self.textOutPut_hack("\n\n >>>   IHRE EINGABE WAR NICHT KORREKT.\n\n")
                self.are_you_ready(connector, command, pageNumber)
            

            downloadedItem = connector.load_by_id( numberOfList )

            item = ListItem.ItemOfToDoList(downloadedItem[0][0], downloadedItem[0][2], downloadedItem[0][1])
            newItemforDB = item.getItem()

            strToDo         = newItemforDB[0]
            dateToDo        = newItemforDB[2].strftime("%d.%m.%y")
            checkDone       = newItemforDB[1]  

            command_for_main_menu_UI =  self.main_menu_option_interaction()

            if command_for_main_menu_UI == "t" or command_for_main_menu_UI == "T":
                    

                self.textOutPut_hack(">>>   SIE WOLLEN DIE TÄTIGKEIT VOM  " + dateToDo + "  ÄNDERN.\n")
                self.textOutPut_hack(">>> GEBEN SIE EINEN NEUEN EINTRAG EIN:\n\n")
                
                stringInput = input (">>>   ")

                self.wanna_save_change_question(connector, command, stringInput, dateToDo, checkDone, numberOfList, pageNumber)
                self.are_you_ready(connector, command, pageNumber)
            
            elif command_for_main_menu_UI == "d" or command_for_main_menu_UI == "D":
                    
                self.textOutPut_hack(">>>   SIE WOLLEN DAS DATUM DER TÄTIGKEIT  " + strToDo[0:10] + "  ÄNDERN.\n")
                self.textOutPut_hack("GEBEN SIE EIN NEUES DATUM EIN:\n\n")    
                
                dateInput = input (">>>   ")

                self.wanna_save_change_question(connector, command, strToDo, dateInput, checkDone, numberOfList,pageNumber)
                self.are_you_ready(connector, command, pageNumber)
            
            elif command_for_main_menu_UI == "s" or command_for_main_menu_UI == "S":
                
                self.textOutPut_hack(">>>   SIE WOLLEN DEN STATUS DER TÄTIGKEIT  " + strToDo[0:10] + "... AM " + dateToDo +"  ÄNDERN.\n")
                
                        
                if checkDone == True:
                    self.textOutPut_hack(">>>   WOLLEN SIE DEN STATUS AUF 'NICHT ERLEDIGT' STELLEN? || ( Y ) OR ( N ) \n\n")
                    checkerStatusChange = input (">>>   ")
             
                else:
                    self.textOutPut_hack(">>>   WOLLEN SIE DEN STATUS AUF 'ERLEDIGT' STELLEN? || ( Y ) OR ( N ) \n\n")
                    checkerStatusChange = input(">>>   ")
                        

                if checkerStatusChange == "y" or checkerStatusChange == "Y":

                    booleanInput =  checkDone == False     

                    self.wanna_save_change_question(connector, command, strToDo, dateToDo, booleanInput, numberOfList, pageNumber)
                    self.are_you_ready(connector, command, pageNumber)
                
                else: 

                    self.are_you_ready(connector, command, pageNumber)
            
            elif command_for_main_menu_UI == "q" or command_for_main_menu_UI == "Q":

                self.are_you_ready(connector, command, pageNumber)

            else:

                self.textOutPut_hack("\n\n >>>   IHRE EINGABE WAR NICHT KORREKT.\n\n")
                self.are_you_ready(connector, command, pageNumber)

            
        elif command == "t" :
               
            pageNumber += 1
             #pageNumber = Math.max( 1, Math.min( max_page_number, pageNumber ) )
            self.main_menu( connector, pageNumber)

        elif command == "p" :

            pageNumber -=1
            self.main_menu( connector, pageNumber)

       """ elif command == "s" :
            
            arrOfAllElements = connector.load_all()

            arrayOf_DATE_Items= []

            for item in arrOfAllElements :
                    
                arrayOf_DATE_Items.append(item)

            all_Done_Array = connector.get_done_items( )
            length_Of_DONE_Array = len( all_Done_Array )

            self.textOutPut_hack(">>>\nSIE HABEN DIE OPTION 'STATISTIK' GEWÄHLT:\n\n")
            self.textOutPut_hack("SIE HABEN INSGESAMT " + str(len(arrOfAllElements)) +" ELEMENTE IN IHRER LISTE.\n" )
                
            self.textOutPut_hack("\nDAVON SIND " + str(length_Of_DONE_Array) + " ERLEDIGT:\n\n")
            
            for item in all_Done_Array:

                self.textOutPut_hack("Die Tätigkeit mit der id '" + str( item[0] ) + "'.\n")
            
            arrayOf_dates = []

            for item in arrayOf_DATE_Items :
                datetimes = datetime.combine( item[2], datetime.min.time())
                  
                if datetimes < datetime.now() :
                        
                    arrayOf_dates.append(item)

            lengthDateTime = len(arrayOf_dates)

            self.textOutPut_hack("\nDAVON LIEGEN " + str( lengthDateTime ) + " IN DER VERGANGENHEIT:\n ")
                    
            for itemDate in arrayOf_dates:

                strToDo = itemDate[0]
                self.textOutPut_hack("Die Tätigkeit '" + strToDo[0:15] + "' mit dem Index '" + str( itemDate[3] ) + "' liegt in der Vergangenheit.\n" )

            print("\n")
"""
            self.are_you_ready(connector, command, pageNumber)

    def wanna_save_change_question(self, connector, command, strToDo, dateToDo, checkDone, numberOfList, pageNumber):

        self.textOutPut_hack("EINTRAG SPEICHERN? || ( Y ) OR ( N )   ")
        checker = input("\n>>>   ")

                    
        if checker == "y" or checker == "Y":
                            
            item = ListItem.ItemOfToDoList(strToDo, dateToDo, checkDone)
            newItemforDB = item.getItem()
                        
            connector.update_item(newItemforDB, numberOfList)
                        
            self.are_you_ready(connector, command, pageNumber)

        elif checker == "n" or checker == "N" :
                            
            self.are_you_ready(connector, command, pageNumber)
                        
        else: 
                            
            self.textOutPut_hack("\n\n >>>   IHRE EINGABE WAR NICHT KORREKT.\n\n")
            self.are_you_ready(connector, command, pageNumber)

    def are_you_ready(self, connector, command, pageNumber):
                                
        check_string = " "*5 + "WOLLEN SIE DIESE OPTION NUN VERLASSEN? » Y « OR » N « " + " "*6
        print("┌" + "─" * 65 + "┐")
        self.textOutPut_hack("│" + check_string + "│\n")
        
        command_option = input("└" + "─" * 65 + "┘\n\n>>>  " )

        if command_option == "y" or command_option == "Y" :
            
            self.main_menu(connector, 1)

            
        elif command_option == "n" or command_option == "N":

            check_string = "  SIE WERDEN ZURÜCKGELEITET .................... "
            
            self.textOutPut_hack(">>>  " + check_string + "\n\n")

            self.main_menu_interaction(connector, command, pageNumber)
        
        else:
            self.textOutPut_hack(">>>  IHRE EINGABE WAR FALSCH...")
            
            self.main_menu_interaction(connector, command, pageNumber)
    
    def main_menu_option_interaction(self):

        print("─" * 67 )
        print("( t )  ||  Tätigkeit ändern ")
        print("( d )  ||  Datum ändern ")
        print("( s )  ||  Status ändern ")
        print("( q )  ||  Verlassen ")
        print("─" * 67 )
        command = input ("\nWAS IST IHR WUNSCH?>>>   ")
        print("\n")

        return command

    def printStatistic(self):
        
        arrOfAllElements = connector.load_all()

            arrayOf_DATE_Items= []

            for item in arrOfAllElements :
                    
                arrayOf_DATE_Items.append(item)

            all_Done_Array = connector.get_done_items( )
            length_Of_DONE_Array = len( all_Done_Array )

            self.textOutPut_hack(">>>\nSIE HABEN DIE OPTION 'STATISTIK' GEWÄHLT:\n\n")
            self.textOutPut_hack("SIE HABEN INSGESAMT " + str(len(arrOfAllElements)) +" ELEMENTE IN IHRER LISTE.\n" )
                
            self.textOutPut_hack("\nDAVON SIND " + str(length_Of_DONE_Array) + " ERLEDIGT:\n\n")
            
            for item in all_Done_Array:

                self.textOutPut_hack("Die Tätigkeit mit der id '" + str( item[0] ) + "'.\n")
            
            arrayOf_dates = []

            for item in arrayOf_DATE_Items :
                datetimes = datetime.combine( item[2], datetime.min.time())
                  
                if datetimes < datetime.now() :
                        
                    arrayOf_dates.append(item)

            lengthDateTime = len(arrayOf_dates)

            self.textOutPut_hack("\nDAVON LIEGEN " + str( lengthDateTime ) + " IN DER VERGANGENHEIT:\n ")
                    
            for itemDate in arrayOf_dates:

                strToDo = itemDate[0]
                self.textOutPut_hack("Die Tätigkeit '" + strToDo[0:15] + "' mit dem Index '" + str( itemDate[3] ) + "' liegt in der Vergangenheit.\n" )

            print("\n")