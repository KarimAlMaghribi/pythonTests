class newClass:
	
	k = 10
	word = "word"
	
	list = []

	def __init__ (self, newNumber = 0) :
		self.i = 3
		self.aNumber = newNumber

	def changeItTillYouMakeIt(self, numberOfChangement, wordOfChangement) :
		self.k = numberOfChangement
		self.word = wordOfChangement
		
		self.list.append( 'Test' );
		
		newClass.list = [self.k, self.word]
		self.list = [self.k, self.word]
		
		self.list.append( 'Test2' );
		
		
		
		
instance_1 = newClass(4)
print(instance_1.k, instance_1.word, instance_1.list )

instance_2 = newClass(5)
print(instance_2.k, instance_2.word, instance_2.list )

instance_1.changeItTillYouMakeIt(0, "changedWord")
print(instance_1.k, instance_2.k, instance_1.word, instance_2.word,instance_1.list, instance_2.list  )
'''
class A:
	name = "Klassenvariable"
	
	def __init__( self ):
		self.printVars( );
	
	def change( self, pStrKlassenName, pStrInstancname ):
		A.name = pStrKlassenName;
		self.printVars( );
		
		self.name = pStrInstancname;
		self.printVars( );
	
	def printVars( self ):
		print( "KV:", A.name );
		print( "IV:", self.name );
		print( "________" )
	

i1 = A()
i2 = A()
i3 = A()
print( "###################" )
i1.change( 'Klassenname 1', 'Instanzname1' )

print( "_______________" )
i1.printVars()
i2.printVars()
i3.printVars()
'''