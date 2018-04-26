import os

class ToDoTerminal():
    def _clear( self ):
        os.system('cls' if os.name=='nt' else 'clear')

    def _waitOfUser( self, pStrMessage = "_: " ):
        return input( pStrMessage )
    
    def _showMenu( self, pObjMenu ):
        ttlLen  = len( pObjMenu[ "title" ] )
        items   = pObjMenu[ "items" ]
        result  = False

        # Menü ausgeben
        head = "┌────────── " + pObjMenu[ "title" ] + " ──────────┐"
        print( head )
        if len( items ) > 0:
            hLen = len( head ) - 1
            for key, item in items.items():
                item = "│ " + key.ljust( 3 ) + ": " + item[ "title" ]
                if len( item ) > (hLen - 4):
                    item = item[0:hLen - 4] + '...'
                print( item.ljust( hLen ) + '│' )
        print( "└───────────{0}───────────┘".format( "─" * ttlLen ) )

        # Auf Eingabe warten
        while True:
            cmd = self._waitOfUser( )
            if cmd in items:
                action = items[ cmd ][ "action" ]
                if ( callable( action ) ):
                    result = action( )
                else:
                    result = action
                break
            else:
                print( "Ungueltige Eingabe. Bitte nur: " + str( list( items.keys() ) ) + " eingeben." )

        return result