
import Menu
import sys
import CSV_Connector
import DB_Connector
import ListItem
import UserInteraction

class Main:
    def __init__( self ):
        self.menu       = Menu.Menu( )
        self.connector  = None
        self.userinteractor = UserInteraction.UserInteraction()
        self.command = None
        self.pageNumber = 1

    def __initActions( self ):
        
        # init Menü 1 (Hauptmenü)
        self.userinteractor.on( 'hauptmenu', 'q', self.__exit )
        self.userinteractor.on( 'hauptmenu', '1', self.__connect2csv )  
        self.userinteractor.on( 'hauptmenu', '2', self.__connect2db )
        self.userinteractor.on( 'hauptmenu', 'e', self.__backToStart )

        # init Menü 2 (Item menü)
        self.menu.on( 'itemmenu', 's', self.__m2_showStatistics )
        self.menu.on( 'itemmenu', 'n', self.__m2_newElement )
        self.menu.on( 'itemmenu', 'l', self.__readItemOfList )
        self.menu.on( 'itemmenu', 'a', self.__changeItemOfList )
        self.menu.on( 'itemmenu', 't', self.__showNextPage )
        self.menu.on( 'itemmenu', 'p', self.__showPrevPage )

        #init Menü 3 (changing menu)
        self.menu.on( 'changingmenu', 'c', self.__change_item )
       
        
        # check whether save
        self.menu.on('save_check', 'y', self.__save_y_interaction)
        self.menu.on('update_check', 'y', self.__updateItem_y)
        self.menu.on('update_check', 'n', self.__updateItem_n)
        
        #check if ready
        self.userinteractor.on('ready_check', 'y', self.__ready_y)
        self.userinteractor.on('ready_check', 'n', self.__ready_n)
        self.userinteractor.on('ready_check', 'e', self.__ready_e)

    
        

    def __backToStart (self):

        self.menu.startMenu()

    def __m2_newElement( self ):
        self.command = "n"
        self.userinteractor.new_element_input(self.connector, self.command)
    
    def __readItemOfList(self):
        self.command = "l"
        
        numberOfList = self.userinteractor.readListItem()
        downloadedItem = self.connector.load_by_id(numberOfList)

        self.userinteractor.getSpecifiedItem(self.connector, downloadedItem)

    def __changeItemOfList(self):
        self.command = "a"
        number = self.connector.get_last_id()

        self.userinteractor.change_item_by_number(self.connector, number, self.pageNumber)
        
    
    def __change_item(self, stringInput, dateToDo, checkDone, numberOfList):

        self.menu.wanna_save_change_question(self.connector, self.command, stringInput, dateToDo, checkDone, numberOfList, self.pageNumber)

    def __showNextPage (self, arrAllItems):

        self.pageNumber += 1
        self.menu.main_menu(arrAllItems, self.pageNumber)

    def __showPrevPage(self, arrAllItems):

        self.pageNumber -= 1
        self.menu.main_menu(arrAllItems, self.pageNumber)
    
    def __updateItem_y(self, newItemforDB, numberOfList ):
        self.connector.update_item(newItemforDB, numberOfList)
                        
        self.userinteractor.are_you_ready(self.connector, "a", 1)

    def __updateItem_n(self):
        self.userinteractor.are_you_ready(self.connector, "a", 1)

    def __save_y_interaction(self, newItem):
        self.connector.save(newItem)

    def __exit( self ):
        sys.exit()

    def __connect2csv( self ):
        self.connector = CSV_Connector.CSV_Connector()

    def __connect2db( self ):
        self.connector = DB_Connector.DB_Connector()

    def __m2_showStatistics( self ):
        arrOfAllElements = self.connector.load_all()
        all_Done_Array = self.connector.get_done_items( )
        
        self.menu.printStatistic(arrOfAllElements, all_Done_Array ) 
        
    def __saveNewItem( self, item ):
        statistic = self.connector.save( )
        print( statistic )

    def __ready_y( self, connector ):
        self.menu.main_menu(connector, 1)

    def __ready_n( self, connector, command, pageNumber):
        self.menu.main_menu_interaction(connector, command, pageNumber)

    def __ready_e( self ):
        self.menu.main_menu_interaction(self.connector, self.command, 1)


    def run( self ):
        self.__initActions()
        self.menu.startMenu()
        self.userinteractor.getItemMenuOption()
        arrAllItems = self.connector.load_all()
        self.menu.main_menu(arrAllItems, self.pageNumber)

main = Main( )
main.run( ) 

"""def test( ):
    print( 'Bye' )
    sys.exit( )

menu = Menu.Menu( )
menu.on( 'hauptmenu', 'q', test )
menu.startMenu()"""


