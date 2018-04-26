from ToDoTerminal import ToDoTerminal
from ToDoItem import ToDoItem

class ToDoList( ToDoTerminal ):
    def __init__( self ):
        self.__items    = [ ]

    def connect( self ):
        # TODO: hier wird Verbindung zu DB aufgebaut
        return True

    def run( self ):
        menu = {
            "title" : "Hauptmenü",
            "items" : {
                "n" : {
                    "title" : "Neuer Eintrag",
                    "action": self.createNewItem
                },
                "l" : {
                    "title" : "Lesen",
                    "action": self.readItem
                },
                "e" : {
                    "title" : "Ändern",
                    "action": self.editItem
                },
                "tst" : {
                    "title" : "Uebermesig lange Menü Eintrag der abgeschnitten wird. Nur zum testen",
                    "action": True
                },
                "q" : {
                    "title" : "Beenden",
                    "action": False
                }
            }
        }

        while True:
            self.__printItems( )
            if not self._showMenu( menu ):
                break

    def createNewItem( self ):
        self._clear( )
        print( "++++++ Neuer Eintrag ++++++++" )
        ni = ToDoItem( )
        ni.edit( )

        print( ni )
        self.__items.append( ni )

        return True

    def readItem( self ):
        id = self._waitOfUser( 'Bitte Eintragid eingeben oder "q" zum abbrechen: ' )
        if id != 'q':
            try:
                self.__items[ int( id ) ].show( )
                self._clear( )
            except ValueError:
                print( 'Ups: Sie müssen eiene ganze Zahl eingeben' )
                self.readItem( )
            except IndexError:
                print( 'Ups: Für gewünschte Id exisitert kein Eintrag' )
                self.readItem( )

        return True

    def editItem( self ):
        id = self._waitOfUser( 'Bitte Eintragid eingeben oder "q" zum abbrechen: ' )
        if id != 'q':
            try:
                self.__items[ int( id ) ].edit( )
            except ValueError:
                print( 'Ups: Sie müssen eiene ganze Zahl eingeben' )
                self.editItem( )
            except IndexError:
                print( 'Ups: Für gewünschte Id exisitert kein Eintrag' )
                self.editItem( )

        return True

    def __printItems( self ):
        self._clear( )
        print( "╔═══════════════════ Items ════════════════════╗" )
        for lfdNr, item in enumerate( self.__items ):
            print( '║', ( str( lfdNr ) + ':' ).rjust( 4 ), item, '║' )
        print( "╚══════════════════════════════════════════════╝" )