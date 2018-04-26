from datetime import datetime
import ListItem
import sys
import time


class UserInteraction:
    
    def __init__( self ):
        self.listeners = { }
    

    def on( self, pStrMenuname, pStrEvent, pFunCallback):
     
            key = pStrMenuname + ':' + pStrEvent 
            self.listeners[ key ] = pFunCallback

    def textOutPut_hack(self, string):
        print(string)
        '''
        length_Of_String = len(string)
        
        i = 0
        while i < length_Of_String:
            print(string[i], end="")
            sys.stdout.flush()
            time.sleep(.035)
            i += 1
        '''
    def new_element_input(self, connector, command ):

        newToDoData = self.getUserInput("WAS HABEN SIE VOR?\n")
        newToDoDate = self.getUserInput("\nAN WELCHEN DATUM? || dd.mm.yyyy\n")
        newItem = None

        try:

            ToDoDate = datetime.strptime(newToDoDate, "%d.%m.%Y")
            
            if ToDoDate < datetime.now():
                self.textOutPut_hack("\n\n>>>   DIESES DATUM LIEGT IN DER VERGANGENHEIT\n\n")
                if 'ready_check:e' in self.listeners:
                    self.listeners[ 'ready_check:e' ](connector, command)
            
            else:
                
                item = ListItem.ItemOfToDoList(newToDoData,ToDoDate)
                newItem = item.getItem()
                
        except:
                
            self.textOutPut_hack("\n\n >>>   IHRE EINGABE WAR NICHT KORREKT.\n\n")    
            if 'ready_check:e' in self.listeners:
                self.listeners[ 'ready_check:e' ](connector, command)
        

        self.check_whether_save(newItem, connector, command)

    def change_item_by_number(self, connector, number, pageNumber):

        self.textOutPut_hack("\n>>>   MIT DIESER OPTION KÖNNEN SIE IHRE EINTRÄGE BEARBEITEN.\n")
          
            
        numberOfList = int( self.getUserInput(">>>   BEI WELCHER LISTEN-NUMMER SOLL DIES GESCHEHEN ?\n") ) 
        i = 1
        listOfNumbers = []
        number = connector.get_last_id()

        while i < number + 1 :
            listOfNumbers.append(i)
            i += 1

        if not numberOfList in listOfNumbers :

            self.textOutPut_hack("\n\n >>>   IHRE EINGABE WAR NICHT KORREKT.\n\n")
            self.are_you_ready(connector, "a", 1)
        
        self.get_Item_for_change(numberOfList, connector, pageNumber)


    def get_Item_for_change(self, numberOfList, connector, pageNumber):

        downloadedItem = connector.load_by_id( numberOfList )

        item = ListItem.ItemOfToDoList(downloadedItem[0][0], downloadedItem[0][2], downloadedItem[0][1])
        newItem = item.getItem()

        self.change_Interaction(newItem, connector, pageNumber, numberOfList)

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

    def change_Interaction(self, newItem, connector, pageNumber, numberOfList):

        strToDo         = newItem[0]
        dateToDo        = newItem[2].strftime("%d.%m.%y")
        checkDone       = newItem[1]  

        command_for_main_menu_UI =  self.main_menu_option_interaction()

        if command_for_main_menu_UI == "t" or command_for_main_menu_UI == "T":
                    

                self.textOutPut_hack(">>>   SIE WOLLEN DIE TÄTIGKEIT VOM  " + dateToDo + "  ÄNDERN.\n")
                stringInput = self.getUserInput(">>> GEBEN SIE EINEN NEUEN EINTRAG EIN:\n\n")
          
                if 'changingmenu:c' in self.listeners:
                    self.listeners[ 'changingmenu:c' ](stringInput, dateToDo, checkDone, numberOfList)

                self.are_you_ready(connector, "a", 1)
            
        elif command_for_main_menu_UI == "d" or command_for_main_menu_UI == "D":
                    
            self.textOutPut_hack(">>>   SIE WOLLEN DAS DATUM DER TÄTIGKEIT  " + strToDo[0:10] + "  ÄNDERN.\n")
            dateInput = self.getUserInput("GEBEN SIE EIN NEUES DATUM EIN:\n\n")    

            if 'changingmenu:c' in self.listeners:
                self.listeners[ 'changingmenu:c' ](strToDo, dateInput, checkDone, numberOfList)
    
            self.are_you_ready(connector, "a", 1)

            
        elif command_for_main_menu_UI == "s" or command_for_main_menu_UI == "S":
            self.textOutPut_hack(">>>   SIE WOLLEN DEN STATUS DER TÄTIGKEIT  " + strToDo[0:10] + "... AM " + dateToDo +"  ÄNDERN.\n")
                        
            if checkDone == True:
                    
                checkerStatusChange =  self.getUserInput(">>>   WOLLEN SIE DEN STATUS AUF 'NICHT ERLEDIGT' STELLEN? || ( Y ) OR ( N ) \n\n")
             
            else:
                    
                checkerStatusChange =  self.getUserInput(">>>   WOLLEN SIE DEN STATUS AUF 'ERLEDIGT' STELLEN? || ( Y ) OR ( N ) \n\n")
                        

            if checkerStatusChange == "y" or checkerStatusChange == "Y":
                booleanInput =  checkDone == False     
                    
                if 'changingmenu:c' in self.listeners:
                    self.listeners[ 'changingmenu:c' ](strToDo, dateToDo, booleanInput, numberOfList)

                self.are_you_ready(connector, "a", 1)
                
            else: 

                self.are_you_ready(connector, "a", 1)
            
        elif command_for_main_menu_UI == "q" or command_for_main_menu_UI == "Q":

            self.are_you_ready(connector, "a", 1)

        else:

            self.textOutPut_hack("\n\n >>>   IHRE EINGABE WAR NICHT KORREKT.\n\n")
            self.are_you_ready(connector, "a", 1 )

        
            

    def readListItem(self):

        self.textOutPut_hack(">>>   MIT DIESER OPTION KÖNNEN SIE EINES IHRER EINTRÄGE AUSLESEN.\n")
        numberOfList = self.getUserInput(">>>   WELCHE NUMMER WOLLEN SIE AUSLESEN?   ")
        return numberOfList

    def getSpecifiedItem(self, connector, downloadedItem):

        item = ListItem.ItemOfToDoList(downloadedItem[0][0], downloadedItem[0][2], downloadedItem[0][1])
        newItemforDB = item.getItem()

        strToDo         = newItemforDB[0]
        dateToDo        = newItemforDB[2].strftime("%d.%m.%y")
        checkDone       = newItemforDB[1]

            
        if checkDone == True:
                
            print("\n>>>   FÜR DEN   " + dateToDo + "   HABEN SIE FOLGENDES GEPLANT:\n\n" + strToDo + "\n\nSIE HABEN DIESE AUFGABE ERLEDIGT.")
                    
            self.are_you_ready(connector, "l", 1)
          
        else:

            print("\n>>>   FÜR DEN   " + dateToDo + "   HABEN SIE FOLGENDES GEPLANT:\n\n" + strToDo + "\n\nSIE HABEN DIESE AUFGABE NOCH NICHT ERLEDIGT.")
                
            self.are_you_ready(connector, "l", 1)

        

    def getUserInput( self, pStrMessage = None ):
        if pStrMessage != None:
            self.textOutPut_hack( pStrMessage )
        return input(">>> ")

    def check_whether_save(self, newItem, connector, command):

        self.textOutPut_hack("\n\n>>>   WOLLEN SIE DIESEN EINTRAG SPEICHERN?   |||   ( Y ) OR ( N )\n\n")
        check_whether_save = input (">>>   ")

        if check_whether_save == "y" or check_whether_save == "Y":
            if 'save_check:y' in self.listeners:
                self.listeners[ 'save_check:y' ](newItem)
                self.are_you_ready(connector, command, 1)
            
        elif check_whether_save == "n" or check_whether_save == "N":
            self.are_you_ready(connector, command, 1)

            
    def getItemMenuOption(self):

        choise = str( self.getUserInput( ) )
    
        if choise == "1" :
            if 'itemmenu:1' in self.listeners:
                self.listeners[ 'itemmenu:1' ]( )
         

        elif choise == "2":
            if 'hauptmenu:2' in self.listeners:
                self.listeners[ 'hauptmenu:2' ]( )
            

        elif choise == "q" or choise == "Q" :
            if 'hauptmenu:q' in self.listeners:
                self.listeners[ 'hauptmenu:q' ]( )

        else: 

            print("\n!!!   WARNING: FALSCHE EINGABE. VERSUCHEN SIE ES NOCH EINMAL.")
            if 'hauptmenu:e' in self.listeners:
                self.listeners[ 'hauptmenu:e' ]( )

    
    
    def are_you_ready(self, connector, command, pageNumber):
                                
        check_string = " "*5 + "WOLLEN SIE DIESE OPTION NUN VERLASSEN? » Y « OR » N « " + " "*6
        print("┌" + "─" * 65 + "┐")
        self.textOutPut_hack("│" + check_string + "│\n")
        
        command_option = input("└" + "─" * 65 + "┘\n\n>>>  " )

        if command_option == "y" or command_option == "Y" :
            
            if 'ready_check:y' in self.listeners:
                self.listeners[ 'ready_check:y' ](connector)

        elif command_option == "n" or command_option == "N":

            check_string = "  SIE WERDEN ZURÜCKGELEITET .................... "
            
            self.textOutPut_hack(">>>  " + check_string + "\n\n")

            if 'ready_check:n' in self.listeners:
                self.listeners[ 'ready_check:n' ](connector, command, pageNumber)
        
        else:
            
            self.textOutPut_hack(">>>  IHRE EINGABE WAR FALSCH...")
            
            if 'ready_check:e' in self.listeners:
                self.listeners[ 'ready_check:e' ](connector, command, pageNumber)
            