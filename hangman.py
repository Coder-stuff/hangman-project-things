print("Welocme to Hangman")
print("Try to guess the random word")
print("You have 6 lives")
import time
import os
frameList = [
'''
 _________________________
|                         |
|              +======+   |
|                   \\ |   |
|                     |   |
|                     |   |
|                     |   |
|                     |   |
|                     |   |
|                   ===== |
|_________________________|''',
'''
 _________________________
|                         |
|              +======+   |
|             ( )    \\|   |
|                     |   |
|                     |   |
|                     |   |
|                     |   |
|                     |   |
|                   ===== |
|_________________________|''',
'''
 _________________________
|                         |
|              +======+   |
|             ( )    \\|   |
|              |      |   |
|              |      |   |
|              |      |   |
|                     |   |
|                     |   |
|                   ===== |
|_________________________|''',
'''
 _________________________
|                         |
|              +======+   |
|             ( )    \\|   |
|              |      |   |
|              |      |   |
|              |      |   |
|             /       |   |
|                     |   |
|                   ===== |
|_________________________|''',
'''
 _________________________
|                         |
|              +======+   |
|             ( )    \\|   |
|              |      |   |
|              |      |   |
|              |      |   |
|             /\\      |   |
|                     |   |
|                   ===== |
|_________________________|''',
'''
 _________________________
|                         |
|              +======+   |
|             ( )    \\|   |
|              |      |   |
|             /|      |   |
|              |      |   |
|             /\\      |   |
|                     |   |
|                   ===== |
|_________________________|''',
'''
 _________________________
|                         |
|              +======+   |
|             ( )    \\|   |
|              |      |   |
|             /|\\     |   |
|              |      |   |
|             /\\      |   |
|                     |   |
|                   ===== |
|_________________________|'''
]
EndgameList = [
'''
 _________________________
|                         |
|      Y                  |
|                         |
|                         |
|                         |
|                         |
|                         |
|                         |
|                         |
|_________________________|''',
'''
 _________________________
|                         |
|      Y O                |
|                         |
|                         |
|                         |
|                         |
|                         |
|                         |
|                         |
|_________________________|''',
'''
 _________________________
|                         |
|      Y O U              |
|                         |
|                         |
|                         |
|                         |
|                         |
|                         |
|                         |
|_________________________|''',
'''
 _________________________
|                         |
|      Y O U              |
|                         |
|           L             |
|                         |
|                         |
|                         |
|                         |
|                         |
|_________________________|''',
'''
 _________________________
|                         |
|      Y O U              |
|                         |
|           L             |
|            O            |
|                         |
|                         |
|                         |
|                         |
|_________________________|''',
'''
 _________________________
|                         |
|      Y O                |
|          U              |
|                         |
|            L            |
|             O           |
|               S         |
|                         |
|                         |
|_________________________|''',
'''
 _________________________
|                         |
|                         |
|     Y                   |
|        O                |
|           U             |
|         L               |
|            O            |
|               S         |
|                   E     |
|_________________________|'''

]

a = "a"
b = "b"
c = "c"
d = "d"
e = "e"
f = "f"
g = "g"
h = "h"
i = "i"
j = "j"
k = "k"
l = "l"
m = "m"
n = "n"
o = "o"
p = "p"
q = "q"
r = "r"
s = "s"
t = "t"
u = "u"
v = "v"
w = "w"
x = "x"
y = "y"
z = "z"
letterBank = []

fourLwrds = ["help","hide","face","home","eyes","arms","tree","pond","lake","free","joke","nail"]
fiveLwrds = ["ocean","hands","roots","beast","yeast","plant","socks","ankle","zebra"]
sixLwrds = ["copter","screen","papers","hoodie","bottle","beetle","rapper","finger"]
sevenLwrds = ["walmart","sticker","jukebox","windows","bicycle"]
eightLwrds = ["computer","national","keyboard"]
import random
letters = input("How many letters do you want the word to be? (minimum of 4 letters, max of 8): ")
if letters == "4":
	wordList = fourLwrds
	
elif letters == "5":
	wordList = fiveLwrds
	
elif letters == "6":
	wordList = sixLwrds
	
elif letters == "7":
	wordList = sevenLwrds
	
elif letters == "8":
	wordList = eightLwrds
	
else:
	print("You need to type a number 4-8")



lives = 6
word = random.choice(wordList)
listword = list(word)
print(listword)	
guessList = []
for a in listword:
	guessList.append("_")


while True:
	print(str(guessList) + " here are the letters you need to guess")
	print("Here are the lettters that you have guessed so far: " + str(letterBank))
	print("type (quit) to quit")
	choice = input("Guess a letter: ")
	index = 0
	if choice == "quit":
		break
	for letter in listword:
		if letter == choice:
			guessList[index] = choice
		index += 1
	if letter != choice:
		lives -= 1
		print("you have " +str(lives) +" guesses left")
	letterBank.append(choice)
	if lives == 6:
		print(frameList[0])
	if lives == 5:
		print(frameList[1])
	if lives == 4:
		print(frameList[2])
	if lives == 3:
		print(frameList[3])
	if lives == 2:
		print(frameList[4])
	if lives == 1:
		print(frameList[5])
	if lives == 0:
		print(frameList[6] +"   Last life!")
	if lives < 0:
		print(frameList +"you lose, out of lives")
		break
	if guessList == listword:
		print("You guessed the word! (you win)")
		break
		



