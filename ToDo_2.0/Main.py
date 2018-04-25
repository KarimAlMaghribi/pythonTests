
import Menu
import sys
import CSV_Connector
import DB_Connector

class Main:
    def __init__( self ):
        self.menu       = Menu.Menu( )
        self.connector  = None

    def __initActions( self ):
        # init Menü 1 (Hauptmenü)
        self.menu.on( 'hauptmenu', 'q', self.__exit )
        self.menu.on( 'hauptmenu', '1', self.__connect2csv )  
        self.menu.on( 'hauptmenu', '2', self.__connect2db )
        # init Menü 2 (Item menü)
        self.menu.on( 'itemmenu', 's', self.__showStatistics )
        self.menu.on( 'itemmenu', 'n', self.__showStatistics )
        self.menu.on( 'itemmenu', 'l', self.__showStatistics )
        self.menu.on( 'itemmenu', 'a', self.__showStatistics )
        self.menu.on( 'itemmenu', 't', self.__showStatistics )
        self.menu.on( 'itemmenu', 'p', self.__showStatistics )


    def __exit( self ):
        sys.exit()

    def __connect2csv( self ):
        self.connector = CSV_Connector.CSV_Connector()

    def __connect2db( self ):
        self.connector = DB_Connector.DB_Connector()

    def __showStatistics( self ):
        
        statistic = self.menu.printStatistics( ) 
        
    
    def __saveNewItem( self, item ):
        statistic = self.connector.save( )
        print( statistic )

    def run( self ):
        ## TODO Running
        pass

main = Main( )
main.run( )

"""def test( ):
    print( 'Bye' )
    sys.exit( )

menu = Menu.Menu( )
menu.on( 'hauptmenu', 'q', test )
menu.startMenu()"""


