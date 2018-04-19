from datetime import datetime
import ListItem
import SqlConnector
import Window
import SqlConnector
import ListItem
import unserinteraction


class dbInteraction:

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
                newItemforDB = item.getItem()

                connector.uploadNewItem(newItemforDB)

                window = Window.Window()
                connector = SqlConnector.SQLConnector()

                arrOfAllElements = connector.getallItemsForList()

                nextStep = window.initToDoList(arrOfAllElements, 0,index_Of_nxtStep)
        
                

                self.menuInteration(nextStep, arrOfAllElements, connector, window, index_Of_nxtStep)

            
            elif nextStep == "l" :
                
                print("Mit dieser Option, können Sie eines Ihrer Einträge auslesen.")
                numberOfList = input("Welche Nummer wollen Sie einlesen?   ")

                downloadedItem = connector.downloadItem(numberOfList)

                item = ListItem.ItemOfToDoList(downloadedItem[0][0], downloadedItem[0][2], downloadedItem[0][1])
                newItemforDB = item.getItem()

                strToDo         = newItemforDB[0]
                dateToDo        = newItemforDB[2].strftime("%d.%m.%y")
                checkDone       = newItemforDB[1]

            
                if checkDone == True:
                
                    print("Für den   " + dateToDo + "   haben Sie Folgendes geplant:\n\n" + strToDo + "\n\nSie haben diese Aufgabe erledigt.")
                    
                    window = Window.Window()
                    connector = SqlConnector.SQLConnector()

                    arrOfAllElements = connector.getallItemsForList()
            
                    nextStep = window.initToDoList(arrOfAllElements, 0, index_Of_nxtStep)
            
                    user = unserinteraction.Userinteraction(nextStep, arrOfAllElements, connector, window, index_Of_nxtStep)

                    self.menuInteration( nextStep, arrOfAllElements, connector, window, index_Of_nxtStep )

                else:

                    print("Für den   " + dateToDo + "   haben Sie Folgendes geplant:\n\n" + strToDo + "\n\nSie haben diese Aufgabe noch nicht erledigt.")
                
                    window = Window.Window()
                    connector = SqlConnector.SQLConnector()

                    arrOfAllElements = connector.getallItemsForList()
            
                    nextStep = window.initToDoList(arrOfAllElements, 0, index_Of_nxtStep)
            
                    user = unserinteraction.Userinteraction(nextStep, arrOfAllElements, connector, window, index_Of_nxtStep)

                    self.menuInteration( nextStep, arrOfAllElements, connector, window, index_Of_nxtStep )

            elif nextStep == "s" :
                
                print("Mit dieser Option, können Sie eines Ihrer Einträge ändern.")
                numberOfList = input("Welche Nummer in Ihrer Liste wollen Sie ändern?   ")  

                downloadedItem = connector.downloadItem(numberOfList)

                item = ListItem.ItemOfToDoList(downloadedItem[0][0], downloadedItem[0][2], downloadedItem[0][1])
                newItemforDB = item.getItem()

                strToDo         = newItemforDB[0]
                dateToDo        = newItemforDB[1].strftime("%d.%m.%y")
                checkDone       = newItemforDB[2]  

                command =  window.changingInteraction()

                if command == "t":
                    

                    print("Sie wollen die Tätigkeit vom " + dateToDo + " ändern.")
                    stringInput = input("Geben Sie den neuen Eintrag ein:\n\n")

                    checker = input("Eintrag speichern? || ( y ) OR ( n )   ")

                    
                    if checker == "y" :
                            
                        item = ListItem.ItemOfToDoList(stringInput, dateToDo, checkDone)
                        newItemforDB = item.getItem()
                        
                        connector.changeItem(newItemforDB, window)
                        
                        window = Window.Window()
                        connector = SqlConnector.SQLConnector()

                        arrOfAllElements = connector.getallItemsForList()
                
                        nextStep = window.initToDoList(arrOfAllElements, 0, index_Of_nxtStep)
                
                        user = unserinteraction.Userinteraction(nextStep, arrOfAllElements, connector, window, index_Of_nxtStep)

                        self.menuInteration( nextStep, arrOfAllElements, connector, window, index_Of_nxtStep )

                    elif checker == "n" :
                            
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