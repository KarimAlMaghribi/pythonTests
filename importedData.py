import sys

def checker(a):
	if a == 7 :
		print("Die Zahl ist " + str(a) )
	else:
		print("Die Zahl ist nicht 7, sondern " + str(a) )

		
if __name__ == "__main__" :
	
	print("Das darf eigentlich nicht ausgegegben werden.")

else:
	
	print( __file__.split("/")[len(__file__.split("/"))-1] + " kommt von einem importierten Modul " )