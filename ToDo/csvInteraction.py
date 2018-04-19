from datetime import datetime
import ListItem
import SqlConnector
import Window
import SqlConnector
import ListItem
import unserinteraction
import CSV_File
import sys
import time


class csvInteraction:

    def menuInteration(self, nextStep, arrOfAllElements, connector, window, index_Of_nxtStep): 


            if nextStep == "n" :
                newToDoData = input("Was haben Sie vor?   " )
                newToDoDate = input("Und an welchem Datum? || dd.mm.yyyy   ")

                try:

                    ToDoDate = datetime.strptime(newToDoDate, "%d.%m.%Y")

                    if ToDoDate < datetime.now():
                        print("\n\n > > > Dieses Datum liegt in der Vergangenheit\n\n")
                        self.menuInteration(nextStep, arrOfAllElements, connector, window, index_Of_nxtStep)
                
                except:

                    print("Ihre Eingabe war nicht korrekt!")
                    self.menuInteration( nextStep, arrOfAllElements, connector, window, index_Of_nxtStep )




                item = ListItem.ItemOfToDoList(newToDoData, ToDoDate)
                newItemforCSV = item.getItem()

                file = CSV_File.CSV_File ()
                file.uploadItem(newItemforCSV)

                window = Window.Window()
                
                arrOfAllElements = file.readFile()

                nextStep = window.initToDoList(arrOfAllElements, 0,index_Of_nxtStep)

                self.menuInteration(nextStep, arrOfAllElements, connector, window, index_Of_nxtStep)

            
            elif nextStep == "l" :
                
                print("Mit dieser Option, können Sie eines Ihrer Einträge auslesen.")
                numberOfListItem = input("Welche Nummer wollen Sie einlesen?   ")

                file = CSV_File.CSV_File()
                csv_item = file.getSpecificItem(numberOfListItem)

                

                strToDo         = csv_item[0]
                dateToDo        = csv_item[2].strftime("%d.%m.%y")
                checkDone       = csv_item[1]

            
                if checkDone == True:
                
                    print("Für den   " + dateToDo + "   haben Sie Folgendes geplant:\n\n" + strToDo + "\n\nSie haben diese Aufgabe erledigt.")
                    
                    ui = unserinteraction.Userinteraction(nextStep, arrOfAllElements, connector, window, index_Of_nxtStep)
                    
                    command = ui.are_you_ready()
                    
                    if command == False:

                        self.menuInteration(nextStep, arrOfAllElements, connector, window, index_Of_nxtStep)

                else:

                    print("Für den   " + dateToDo + "   haben Sie Folgendes geplant:\n\n" + strToDo + "\n\nSie haben diese Aufgabe noch nicht erledigt.")

                    ui = unserinteraction.Userinteraction(nextStep, arrOfAllElements, connector, window, index_Of_nxtStep)
                    
                    command = ui.are_you_ready()
                    
                    if command == False:

                        self.menuInteration(nextStep, arrOfAllElements, connector, window, index_Of_nxtStep)


            elif nextStep == "s" :
                
                check_string = " "*13 + "» S «  SIE WOLLEN EINEN EINTRAG ÄNDERN" + " "*14
                print("┌" + "─" * 65 + "┐")
                self.textOutPut_hack("│" + check_string + "│\n\n") 

                
                numberOfList = int(input(">>>   Welche Nummer in Ihrer Liste wollen Sie ändern?\n\n>>>   ")  )

                file = CSV_File.CSV_File()
                item_to_change = file.getSpecificItem(numberOfList-1)


                strToDo         = item_to_change[0]
                dateToDo        = item_to_change[2].strftime("%d.%m.%y")
                checkDone       = item_to_change[1]  
                id_number       = item_to_change[3]
                
                command =  window.changingInteraction()

                if command == "t":
                    
                    print(">>>   Sie wollen die Tätigkeit vom " + dateToDo + " ändern.\n")
                    stringInput = input(">>>   Geben Sie den neuen Eintrag ein:\n\n>>>   ")

                    check_string = " "*5 + "WOLLEN SIE DEN EINTRAG NUN SPEICHERN ? » Y « OR » N « " + " "*6
                    print("\n\n┌" + "─" * 65 + "┐")
                    self.textOutPut_hack("│" + check_string + "│\n\n") 
                    checker = input( ">>>   " )
                    
                    if checker == "y" or check_string == "Y" :
                            
                        item = ListItem.ItemOfToDoList(stringInput, item_to_change[2], checkDone)
                        newItemforCSV = item.getItem()
                        itemArray= []
                        itemArray.append("strToDo,booleanToDo,dateToDo")
                        all_itemArray = file.readFile()
                        
                        for item in all_itemArray:
                            itemArray.append(item[0])
                        
                        itemArray[id_number-1] = newItemforCSV

                        file.changeItem(itemArray)
                        
                        #connector.changeItem(newItemforDB, window)
                        
                        #window = Window.Window()
                        #connector = SqlConnector.SQLConnector()

                        #arrOfAllElements = connector.getallItemsForList()
                
                        #nextStep = window.initToDoList(arrOfAllElements, 0, index_Of_nxtStep)
                
                        #user = unserinteraction.Userinteraction(nextStep, arrOfAllElements, connector, window, index_Of_nxtStep)

                        #self.menuInteration( nextStep, arrOfAllElements, connector, window, index_Of_nxtStep )

                    elif checker == "n" or check_string == "N" :
                            
                        window.initToDoList( connector.getallItemsForList() )
                        
                        window = Window.Window()
                        connector = SqlConnector.SQLConnector()

                        arrOfAllElements = connector.getallItemsForList()
                
                        nextStep = window.initToDoList(arrOfAllElements, 0, index_Of_nxtStep)
                
                        user = unserinteraction.Userinteraction(nextStep, arrOfAllElements, connector, window, index_Of_nxtStep)

                        self.menuInteration( nextStep, arrOfAllElements, connector, window, index_Of_nxtStep )
                        
                    else: 
                            
                        print("Ihre Eingabe war nicht korrekt")
                        window.initToDoList( connector.getallItemsForList() )    
                        
                        window = Window.Window()
                        connector = SqlConnector.SQLConnector()

                        arrOfAllElements = connector.getallItemsForList()
                
                        nextStep = window.initToDoList(arrOfAllElements, 0, index_Of_nxtStep)
                
                        user = unserinteraction.Userinteraction(nextStep, arrOfAllElements, connector, window, index_Of_nxtStep)

                        self.menuInteration( nextStep, arrOfAllElements, connector, window, index_Of_nxtStep )
            
                elif command == "d":
                    
                    
                    print("Sie wollen das Datum, der Tätigkeit ' " + strToDo[0:10] + "..."+ " ' ändern.")
                    dateInput = input("Geben Sie hierfür ein neues Datum ein:\n\n")

                    

                    checker = input("Eintrag speichern? || ( y ) OR ( n )   ")
                    
                    if checker == "y" :
                                
                        item = ListItem.ItemOfToDoList(strToDo, dateInput, checkDone)
                        newItemforDB = item.getItem()
                        connector.changeItem(newItemforDB, window)
                        window.initToDoList( connector.getallItemsForList() )
                            
                        window = Window.Window()
                        connector = SqlConnector.SQLConnector()

                        arrOfAllElements = connector.getallItemsForList()
                
                        nextStep = window.initToDoList(arrOfAllElements, 0, index_Of_nxtStep)
                
                        user = unserinteraction.Userinteraction(nextStep, arrOfAllElements, connector, window, index_Of_nxtStep)

                        self.menuInteration( nextStep, arrOfAllElements, connector, window, index_Of_nxtStep )
                        

                    elif checker == "n" :
                
                        window.initToDoList( connector.getallItemsForList )
                        
                        window = Window.Window()
                        connector = SqlConnector.SQLConnector()

                        arrOfAllElements = connector.getallItemsForList()
                
                        nextStep = window.initToDoList(arrOfAllElements, 0, index_Of_nxtStep)
                
                        user = unserinteraction.Userinteraction(nextStep, arrOfAllElements, connector, window, index_Of_nxtStep)

                        self.menuInteration( nextStep, arrOfAllElements, connector, window, index_Of_nxtStep )
                            
                    else: 
                                
                        print("Ihre Eingabe war nicht korrekt")
                        window.initToDoList( connector.getallItemsForList )
                            
                        window = Window.Window()
                        connector = SqlConnector.SQLConnector()

                        arrOfAllElements = connector.getallItemsForList()
                
                        nextStep = window.initToDoList(arrOfAllElements, 0, index_Of_nxtStep)
                
                        user = unserinteraction.Userinteraction(nextStep, arrOfAllElements, connector, window, index_Of_nxtStep)

                        self.menuInteration( nextStep, arrOfAllElements, connector, window, index_Of_nxtStep )
            
                elif command == "s":
            
                    print(" Sie wollen den Status, der Tätigkeit ' " + strToDo[0:10] + "..."+ " am " + dateToDo +" ändern.")
                        
                    if checkDone == True:

                        checkerStatusChange = input("Wollen Sie den auf 'NICHT ERLEDIGT' stellen? ||  ( y ) OR ( n )   ")
                        
                    else:

                        checkerStatusChange = input("Wollen Sie den auf 'ERLEDIGT' stellen? ||  ( y ) OR ( n )  ")
                        
                    

                    if checkerStatusChange == "y":

                        booleanInput =  checkDone == False     
                                
                        item = ListItem.ItemOfToDoList(strToDo, dateToDo, booleanInput)
                        newItemforDB = item.getItem()
                        connector.changeItem(newItemforDB, window)
                                
                        window = Window.Window()
                        connector = SqlConnector.SQLConnector()

                        arrOfAllElements = connector.getallItemsForList()
                    
                        nextStep = window.initToDoList(arrOfAllElements, 0, index_Of_nxtStep)
                    
                        user = unserinteraction.Userinteraction(nextStep, arrOfAllElements, connector, window, index_Of_nxtStep)

                        self.menuInteration( nextStep, arrOfAllElements, connector, window, index_Of_nxtStep )
                                

                    elif checkerStatusChange == "n" :

                        window.initToDoList(connector.getallItemsForList)

                        window = Window.Window()
                        connector = SqlConnector.SQLConnector()

                        arrOfAllElements = connector.getallItemsForList()
                    
                        nextStep = window.initToDoList(arrOfAllElements, 0, index_Of_nxtStep)
                    
                        user = unserinteraction.Userinteraction(nextStep, arrOfAllElements, connector, window, index_Of_nxtStep)

                        self.menuInteration( nextStep, arrOfAllElements, connector, window, index_Of_nxtStep )

                    else : 

                        print("Sie haben eine falsche Angabe gemacht.")
                        window.initToDoList(connector.getallItemsForList)
                            
                        window = Window.Window()
                        connector = SqlConnector.SQLConnector()

                        arrOfAllElements = connector.getallItemsForList()
                    
                        nextStep = window.initToDoList(arrOfAllElements, 0, index_Of_nxtStep)
                    
                        user = unserinteraction.Userinteraction(nextStep, arrOfAllElements, connector, window, index_Of_nxtStep)

                        self.menuInteration( nextStep, arrOfAllElements, connector, window, index_Of_nxtStep )
            
            elif nextStep == "t" :
                
                window = Window.Window()
                connector = SqlConnector.SQLConnector()
                arrOfAllElements = connector.getallItemsForList()
                
                nextStep = window.initToDoList(arrOfAllElements, 1, index_Of_nxtStep)
                user = unserinteraction.Userinteraction(nextStep, arrOfAllElements, connector, window, index_Of_nxtStep)
                self.menuInteration( nextStep, arrOfAllElements, connector, window, index_Of_nxtStep )

            elif nextStep == "p" :

                window = Window.Window()
                connector = SqlConnector.SQLConnector()
                arrOfAllElements = connector.getallItemsForList()

                nextStep = window.initToDoList(arrOfAllElements, 0, index_Of_nxtStep)
                user = unserinteraction.Userinteraction(nextStep, arrOfAllElements, connector, window, index_Of_nxtStep)
                self.menuInteration( nextStep, arrOfAllElements, connector, window, index_Of_nxtStep )

            elif nextStep == "?" :
                
                window = Window.Window()
                connector = SqlConnector.SQLConnector()
                arrOfAllElements = connector.getallItemsForList()

                arrayOf_DATE_Items= []

                for item in arrOfAllElements :
                    
                    arrayOf_DATE_Items.append(item)

                all_Done_Array = connector.getAllDone()
                length_Of_DONE_Array = len( all_Done_Array )

                print("\nSie haben die Option 'Statistik' gewählt.")
                print("Sie haben insgesamt " + str(len(arrOfAllElements)) +" Elemente in Ihrer Liste." )
                
                print("\nDavon sind " + str(length_Of_DONE_Array) + " erledigt:")
                for item in all_Done_Array:

                    print("Die Tätigkeit mit der ID '" + str( item[0] ) + "'.")
            
                print("\n")
                arrayOf_dates = []
                for item in arrayOf_DATE_Items :
                    datetimes = datetime.combine( item[2], datetime.min.time())
                    
                    
                    
                    if datetimes < datetime.now() :
                        
                        arrayOf_dates.append(item)

                lengthDateTime = len(arrayOf_dates)

                print("Davon liegen " + str( lengthDateTime ) + " in der Vergangenheit: ")
                    
                for itemDate in arrayOf_dates:

                    strToDo = itemDate[0]
                    print("Die Tätigkeit '" + strToDo[0:15] + "' mit dem Index '" + str( itemDate[3] ) + "' liegt in der Vergangenheit." )


                nextStep = window.initToDoList(arrOfAllElements, 0, index_Of_nxtStep)
                user = unserinteraction.Userinteraction(nextStep, arrOfAllElements, connector, window, index_Of_nxtStep)
                self.menuInteration( nextStep, arrOfAllElements, connector, window, index_Of_nxtStep )
    
    def textOutPut_hack(self, string):

        length_Of_String = len(string)
        
        i = 0
        while i < length_Of_String:
            print(string[i], end="")
            sys.stdout.flush()
            time.sleep(.035)
            i += 1

        