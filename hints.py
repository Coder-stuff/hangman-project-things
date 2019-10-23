mystring = "arizona"
mylist = list(mystring)
print(mylist)

#how to create a list with _ where letters go
guesslist = []
for a in mylist:
	guesslist.append("_")

print(guesslist)

#how to replace a specific item in a list
#So say the user types r for guess. You would 
guesslist[2] = "r"

print(guesslist)