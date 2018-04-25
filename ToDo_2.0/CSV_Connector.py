import Connector
import csv
import ListItem
from datetime import datetime
import re

class CSV_Connector(Connector.Connector):

    def connect(self):
        pass
    
    
    def save(self, item):
        
        with open(r"C:\Users\krakia\Desktop\4.Semester\Test\ToDo\CSV_ToDo.csv", 'wa', newline= '') as csvfile:
            file_reader = csv.reader(csvfile, delimiter=',', quotechar="|")

           
                

            filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_NONE)
            
            if file_reader[0][0] != "strToDo":
                filewriter.writerow(("strToDo", "booleanToDo", "dateToDo"))

            if item[1] == True:
                boolean = "true"
            else:
                boolean = "false"
            
            date = item[2].strftime("%d.%m.%Y")

            filewriter.writerow( [ item[0], boolean, date] )
    

    def load_all(self):
        
        with open(r"C:\Users\krakia\Desktop\4.Semester\Test\ToDo\CSV_ToDo.csv", newline= '') as csvfile:
            file_reader = csv.reader(csvfile, delimiter=',', quotechar="|")

            itemArray = []
            i=0
            for line in file_reader:
                
                if not line:
                    continue

                corrected_strToDo = re.sub('"', '', line[0])
                    
                if corrected_strToDo == "strToDo":
                    continue

                i += 1
                    
                if line[1] == "true":
                    boolean = True
                else:
                    boolean = False
                    
                dateToDo = line[2]
                result = re.sub('"', '', dateToDo)
                    
                result = datetime.strptime( result, "%d.%m.%Y" )

                init_Item = ListItem.ItemOfToDoList( corrected_strToDo, result, boolean )
                item = init_Item.getItem()
                    
                l = list(item)
                l.append(i)
                item = tuple(l)
                    
                itemArray.append(item)

            return itemArray
    
    
    def load_by_id(self, id_of_item):
        
        with open(r"C:\Users\krakia\Desktop\4.Semester\Test\ToDo\CSV_ToDo.csv", newline= '') as csvfile:
            file_reader = csv.reader(csvfile, delimiter=',', quotechar="|")

            itemArray = []
            i=0
            for line in file_reader:
                if not line:
                    continue
                corrected_strToDo = re.sub('"', '', line[0])
                if corrected_strToDo == 'strToDo':
                    continue
                i += 1
                
                if line[1] == "true":
                    boolean = True
                else:
                    boolean = False
                
                dateToDo = line[2]
                result = re.sub('"', '', dateToDo)
                
                result = datetime.strptime( result, "%d.%m.%Y" )

                init_Item = ListItem.ItemOfToDoList( corrected_strToDo, result, boolean )
                item = init_Item.getItem()
                
                l = list(item)
                l.append(i)
                item = tuple(l)
                
                new_index = int(id_of_item)
                itemArray.append(item)
            
            downloadedItem = itemArray[new_index]

            return downloadedItem

    
    def update_item(self, item, id_of_item):

        start_item = ("strToDo", "booleanToDo", "dateToDo")
                        
        itemArray=[]
        itemArray.append(start_item)
                        
        all_itemArray = file.readFile()
                        
        for item in all_itemArray:
            itemArray.append(item)
                        
        itemArray[id_of_item] = item

        
        with open(r"C:\Users\krakia\Desktop\4.Semester\Test\ToDo\CSV_ToDo.csv",'w') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=',',
                                             quotechar='', quoting=csv.QUOTE_NONE)
            
            arrayListofItems = []
            for item in itemArray:
                arrayListofItems.append(item)

            for item in arrayListofItems:

                if item[0] == "strToDo":
                    csv_writer.writerow( [ item[0], item[1], item[2] ] )
                    continue
                
                if item[1] == True:
                    boolean = "true"
                else:
                    boolean = "false"
                
                date = item[2]
                
                if type(date) != str :

                   new_date = date.strftime("%d.%m.%Y")
                
                
                csv_writer.writerow( [ item[0], boolean, new_date] )


    def get_last_id(self):
        
        with open(r"C:\Users\krakia\Desktop\4.Semester\Test\ToDo\CSV_ToDo.csv", newline= '') as csvfile:
            file_reader = csv.reader(csvfile, delimiter=',', quotechar="|")

            itemArray = []

            for line in file_reader:
                if not line:
                    continue
                item = ListItem.ItemOfToDoList(line[0], line[2], line[1])
                itemArray.append(item)
            
            focusedItemArray = itemArray[1:]
            length_of_array = len(focusedItemArray)

        return length_of_array


    def get_done_items(self):
        
        with open(r"C:\Users\krakia\Desktop\4.Semester\Test\ToDo\CSV_ToDo.csv", newline= '') as csvfile:
            file_reader = csv.reader(csvfile, delimiter=',', quotechar="|")

            itemArray = []
            i=0
            for line in file_reader:
                
                if not line:
                    continue

                corrected_strToDo = re.sub('"', '', line[0])
                    
                if corrected_strToDo == "strToDo":
                    continue

                i += 1
    
                if line[1] == "true":

                    boolean = True
                    dateToDo = line[2]
                    
                    result = re.sub('"', '', dateToDo)
                    result = datetime.strptime( result, "%d.%m.%Y" )
                    
                    init_Item = ListItem.ItemOfToDoList( corrected_strToDo, result, boolean )
                    item = init_Item.getItem()
                    
                    l = list(item)
                    l.append(i)
                    item = tuple(l)
                        
                    itemArray.append(item)

            return itemArray    
    
    
   