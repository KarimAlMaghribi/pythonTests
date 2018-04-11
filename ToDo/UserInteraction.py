# -*- coding: utf-8 -*-

import List
import SqlConnector
def getStrToDo () :
  
    return input("Was haben Sie vor?   " )

def getDateToDo():

    
    return input("Und an welchem Datum? || dd.mm.yyyy   ")

def getNumberOfList():
    return int(input("Welchen Nummer der Liste wollen Sie näher betrachten?   "))

def getCharOfMenu():
    return input("Welche Option wählen Sie?   ")

def checkIfReady():

    command = input ( "DRÜCKEN SIE ( q ) ZUM VERLASSEN   ")

    if command == "q":

        List.initToDoList()
    
    else :
        print("Dies war keine korrekte Eingabe\nDRÜCKEN SIE ( q ) ZUM VERLASSEN   ")

def getCommand():
    
    command = input("Meine Wahl ist:   ")

    if command == "n" :
        
        newToDoData = getStrToDo()
        newToDoDate = getDateToDo()
        
        List.addListItem (newToDoData, newToDoDate)

    elif command == "l" :
        
        print("Mit dieser Option, können Sie eines Ihrer Einträge auslesen.")
        numberOfList = input("Welche Nummer wollen Sie einlesen?   ")

        List.putOutSpecifiedItemOfList(numberOfList)

    elif command == "s":
        
        print("Mit dieser Option, können Sie eines Ihrer Einträge ändern.")
        numberOfList = input("Welche Nummer in Ihrer Liste wollen Sie ändern?   ")
        
        List.changeSpecifiedItemOfList(numberOfList)
    
    elif command == "t" :
       
        List.pageChanger("t")    

    
    elif command == "p" :
        
        List.pageChanger("p") 
    
    return command

def setWelcomeText():
    
    print("\n\nDie Organisation des Arbeitsablaufes durch Tätigkeitslisten in die noch unerledigte Aufgaben festgehalten werden," +
          "ist eine erfolgreiche Arbeitstechnik zur Strukturierung und Verwaltung anfallender Aufgaben. Dieses schriftliche Planen" +
          " hilft nicht nur seine Vergeßlichkeit in den Griff zu bekommen, sondern ist oftmals bereits der erste Schritt zur Bewältigung der Dinge. Los gehts!\n\n")

    print("Hier finden Sie Ihre To-Do-Liste:")

def initMenu ():
    
    print("Menu:\nWählen Sie zwischen den folgenden Optionen: ")
    print("n -> Neuer Listen - Eintrag")
    print("l -> Einen Eintrag lesen")
    print("s -> Status eines Eintrags ändern")
    print("t -> Nächste Seite der To - Do - Liste")
    print("p -> Vorrige Seite der To - Do - Liste")


def changingInteraction():

    print("Sie haben folgende Option zur Änderung Ihrer Eingaben:\n\n")
    
    print("( t )  ||  Tätigkeit ändern ")
    print("( d )  ||  Datum ändern ")
    print("( s )  ||  Status ändern ")
    print("( q )  ||  Verlassen \n\n")

    command = input ("Was ist Ihr Wunsch?   ")
    
    return command
