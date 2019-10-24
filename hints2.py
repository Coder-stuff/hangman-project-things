# how to loop through a string and replace letters
mystery = list("halloween")
guessList = list("_________")
while True:
	guess = input("guess a letter: ")
	index = 0

	for letter in mystery:
		if letter == guess:
			guessList[index] = guess
		index += 1


	print(guessList)