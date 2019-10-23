secretw = "chris"
secretw = list(secretw)
frameList = [
'''
a''','''as''','''ass''','''hi''','''awaw''','''wha''','''waw'''

]

misses = 0

while misses < 7:
	guess = input("Guess a letter: ")
	if guess in secretw:
		#loop through secretw and change my guessList at the correct indexes
		print("letter is in word")
	else:
		misses +=1
		print(frameList[misses]) #misses is the index, so whatever number misses is equal to, that is what index frame will show in the list




print("game ova")