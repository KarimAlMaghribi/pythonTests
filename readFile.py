

f = open("textDocument.txt", "w" )
f.write("hahaheeea")
f.close()
f = open("textDocument.txt", "r" )
print(f.read())
f.close()