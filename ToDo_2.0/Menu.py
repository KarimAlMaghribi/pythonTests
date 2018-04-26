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
        print(string)
        """length_Of_String = len(string)
        
        i = 0
        while i < length_Of_String:
            print(string[i], end="")
            sys.stdout.flush()
            time.sleep(.035)
            i += 1"""
    
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


    def main_menu(self, arrAllItems, pageNumber):

        
        print( "*" * 27 + " TO_DO_LISTE  " + "*" * 26 )

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
        
       
        self.main_menu_interaction(command, arrAllItems, pageNumber)

    def main_menu_interaction(self, command, arrAllItems,  pageNumber):
        

        if command == "n" :
            
            if 'itemmenu:n' in self.listeners:
                self.listeners[ 'itemmenu:n' ]( )
            
        elif command == "l" :
                
            if 'itemmenu:l' in self.listeners:
                self.listeners[ 'itemmenu:l' ]()   

        elif command == "a" :
                
            if 'itemmenu:a' in self.listeners:
                self.listeners[ 'itemmenu:a' ]() 
       
        elif command == "t" :

            if 'itemmenu:t' in self.listeners:
                self.listeners[ 'itemmenu:t' ](arrAllItems)

        elif command == "p" :

            if 'itemmenu:p' in self.listeners:
                self.listeners[ 'itemmenu:p' ](arrAllItems)



        else:
            self.startMenu()


   
    
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

    def printStatistic(self, arrOfAllElements,all_Done_Array):
        
    

        arrayOf_DATE_Items= []

        for item in arrOfAllElements :
                    
            arrayOf_DATE_Items.append(item)

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

    
    def createItem(self, strInput, dateInput ):
        
        item = ListItem.ItemOfToDoList(strInput,dateInput)
        newItemforDB = item.getItem()
        return newItemforDB


    def wanna_save_change_question(self, connector, command, strToDo, dateToDo, checkDone, numberOfList, pageNumber):

        self.textOutPut_hack("EINTRAG SPEICHERN? || ( Y ) OR ( N )   ")
        checker = input("\n>>>   ")

                    
        if checker == "y" or checker == "Y":

            item = ListItem.ItemOfToDoList(strToDo, dateToDo, checkDone)
            newItemforDB = item.getItem()

            if 'update_check:y' in self.listeners:
                self.listeners[ 'update_check:y' ]( newItemforDB, numberOfList )  
   

        elif checker == "n" or checker == "N" :
                            
            if 'update_check:n' in self.listeners:
                self.listeners[ 'update_check:n' ]( )  
          
                        
        else: 
                            
            self.textOutPut_hack("\n\n >>>   IHRE EINGABE WAR NICHT KORREKT.\n\n")
            if 'update_check:n' in self.listeners:
                self.listeners[ 'update_check:n' ]( )