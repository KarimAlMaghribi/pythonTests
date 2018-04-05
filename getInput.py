introduce = "Dies ist ein kleiner Rechner\nZuersteinmal geben Sie bitte zwei zahlen ein!"
firstMessage = "Ihre erste Zahl lautet: "
secondMessage = "Ihre zweite Zahl lautet: "

print(introduce)

number_1 = int( input(firstMessage) )
number_2 = int( input(secondMessage) )

operator = input( 3 )

if operator == 3:
	print(str(number_1 + number_2))
elif operator == "-":
	print(str(number_1 - number_2))
elif operator == "*":
	print(str(number_1 * number_2))
elif operator == "/":
	print(str(number_1 / number_2))
else:
	print ("Der Operator ist nicht korrekt")
