# -*- coding: utf-8 -*-

import Window
import SqlConnector
import ListItem
import unserinteraction
import CSV_File
from datetime import datetime

class Launcher:
    def run( self ):
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
    
        user = unserinteraction.Userinteraction(nextStep, items_for_ToDoList, connector, window, index_Of_nxtStep)  

        user.menuInteration() 
    

l = Launcher( )
l.run( )
