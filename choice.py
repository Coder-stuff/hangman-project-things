import random
lives =5
leele = ["asdf","bmni","coye","dwuk"]
guesslist = []
wordlist = []
word = random.choice(leele)
while True:
	wordlist.append(word)
	for a in word:
		guesslist.append("_")
	print(guesslist)
	print(wordlist)
	print(word)

	choice = input("yo whats yo guess ")
	print(choice)
	if choice in wordlist:
		wordlist.remove(choice)
		guesslist.insert(choice)
		print(guesslist)

	else:
		print("no")
		lives = lives-1
	if lives <1:
		break