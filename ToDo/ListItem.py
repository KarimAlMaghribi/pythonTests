class ItemOfToDoList:
    


    def __init__ (self, strToDo, dateToDo, boolChecker = False):
        
        self.strToDo = strToDo
        self.boolChecker = boolChecker
        self.dateToDo = dateToDo
    
    def getItem(self) :
         arrItem = (self.strToDo, self.boolChecker , self.dateToDo)

         return arrItem

    def setToDo(self, strToDo):
        self.strToDo = strToDo



    def setDate(self, dateToDo):
        self.dateToDo = dateToDo

    
    def setState(self, boolChecker):
        self.boolChecker = boolChecker


