class thisIsClass:
	a = 3
	b = 4
	c = 5
	
	def muliplication(self, number1, number2, number3) : 
			
		a = number1
		b = number2
		c = number3
		
		d = a + b + c
		print( str( d ) ) 
		

instanz = thisIsClass()
instanz.muliplication(instanz.a, instanz.b, instanz.c)