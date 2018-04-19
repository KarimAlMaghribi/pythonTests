from datetime import datetime
import ListItem
import SqlConnector
import Window
import SqlConnector
import ListItem
import dbInteraction
import csvInteraction
import sys
import time
import CSV_File


class Userinteraction: 

    def __init__ (self, nextStep, arrOfAllElements, connector, window, index_Of_nxtStep):

        self.nextStep = nextStep
        self.arrOfAllElements = arrOfAllElements
        self.connector = connector
        self.window = window
        self.index_Of_nxtStep = index_Of_nxtStep

 
    def db_interaction(self):
        db_Interaction = dbInteraction.dbInteraction()
        db_Interaction.menuInteration(self.nextStep, self.arrOfAllElements, self.connector, self.window, self.index_Of_nxtStep)

    def csv_interaction(self):
        csv_interaction = csvInteraction.csvInteraction()
        csv_interaction.menuInteration(self.nextStep, self.arrOfAllElements, self.connector, self.window, self.index_Of_nxtStep)

    def menuInteration(self):
            
        if self.index_Of_nxtStep == '1':
            self.csv_interaction()
        else:
            self.db_interaction()

    def are_you_ready(self):
                                
        check_string = " "*5 + "WOLLEN SIE DIESE OPTION NUN VERLASSEN? » Y « OR » N « " + " "*6
        print("┌" + "─" * 65 + "┐")
        self.textOutPut_hack("│" + check_string + "│\n")
        
        command = input("└" + "─" * 65 + "┘\n\n>>>  " )

        if command == "y" or command == "Y" :

            window = Window.Window()
            connector = SqlConnector.SQLConnector()
            csv_file = CSV_File.CSV_File()
            
            arrOfAll_DB_Elements = connector.getallItemsForList()
            arrOfAll_CSV_Elements = csv_file.readFile()

            index_Of_nxtStep = window.initialiseStart(arrOfAll_CSV_Elements, arrOfAll_DB_Elements)

            if index_Of_nxtStep == "1":
                items_for_ToDoList = arrOfAll_CSV_Elements
            
            else:
                items_for_ToDoList = arrOfAll_DB_Elements
            
            nextStep = window.initToDoList(items_for_ToDoList, 0, index_Of_nxtStep)
        
            user = Userinteraction(nextStep, items_for_ToDoList, connector, window, index_Of_nxtStep)  

            user.menuInteration()
        
        elif command == "n" or command == "N":

            check_string = "  SIE WERDEN ZURÜCKGELEITET .................... "
            
            self.textOutPut_hack(">>>  " + check_string + "\n\n")

            return False
        
        else:
            self.textOutPut_hack(">>>  IHRE EINGABE WAR FALSCH...")
            
            return False

    def textOutPut_hack(self, string):

        length_Of_String = len(string)
        
        i = 0
        while i < length_Of_String:
            print(string[i], end="")
            sys.stdout.flush()
            time.sleep(.035)
            i += 1
