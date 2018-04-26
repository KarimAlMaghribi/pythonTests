from ToDoList import ToDoList

list = ToDoList( )


if list.connect( ):
    list.run( )
else:
    print( "Ups. ToDoList konnte keine Verbindung aufbauen" )

