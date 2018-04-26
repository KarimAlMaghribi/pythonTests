from ToDoTerminal import ToDoTerminal
from datetime import datetime

class ToDoItem( ToDoTerminal ):
    def __init__( self, pObjData = None ):
        self.done       = False
        self.deadline   = datetime.now( )
        self.message    = ""
        self.menu       = {
            "title" : "Eintragmenu",
            "items" : {
                "n" : {
                    "title" : "Nachricht ändern",
                    "action": self.editMessage
                },
                "d" : {
                    "title" : "Dedline ändern",
                    "action": self.editDedline
                },
                "s" : {
                    "title" : "Status ändern",
                    "action": self.changeState
                },
                "f" : {
                    "title" : "Fertig",
                    "action": False
                }
            }
        }

    def changeState( self ):
        self.done = not self.done
        print( 'Neue Status ist: ', ( 'erlädigt' if self.done else 'offen' ) )
        return True

    def editMessage( self ):
        self.message = self._waitOfUser( 'Nachricht eingeben: ' )
        return True

    def editDedline( self ):
        while True:
            dedline = self._waitOfUser( 'Dedline eingeben: ' )
            try:
                self.deadline = datetime.strptime( dedline, "%d.%m.%Y")
                break
            except ValueError:
                print( 'Ungültige Datum. Bitte im Format DD.MM.YYYY eingeben.' )
            
        return True
    
    def edit( self ):
        self._clear( )
        while self._showMenu( self.menu ):
            pass

    def show( self ):
        self._clear( )
        print( '┌────────── Eintragvorschau ──────────' )
        print( '│ Status  : ', ( 'erlädigt' if self.done else 'offen' ) )
        print( '│ Dedline : ', self.deadline.strftime( '%d.%m.%Y' ) )
        print( '│ Message : ', self.message )
        print( '└─────────────────────────────────────' )
        self._waitOfUser( 'Irgendwas eingeben um fortfahren: ' )

    def __str__( self ):
        result  = '[' + (  '*' if self.done else ' ' ) + ']'
        message = self.message
        msgLen  = len( message )
        maxLen  = 20
        if msgLen > maxLen:
            message = message[0:(maxLen-4)] + ' ...'
        result += ' ' + message.ljust( maxLen )
        result += ' ( ' + self.deadline.strftime( '%d.%m.%Y' ) + ' )'
        return result