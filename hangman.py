print("Welocme to Hangman")
print("Try to guess the random word")
print("You have 5 lives")
import time
import os
frameList = [
'''
 _________________________
|                         |
|              +======+   |
|                   \\|   |
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
|             ( )   \\|   |
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
|             ( )   \\|   |
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
|             ( )   \\|   |
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
|             ( )   \\|   |
|              |      |   |
|              |      |   |
|              |      |   |
|             /\\     |   |
|                     |   |
|                   ===== |
|_________________________|''',
'''
 _________________________
|                         |
|              +======+   |
|             ( )   \\|   |
|              |      |   |
|             /|      |   |
|              |      |   |
|             /\\     |   |
|                     |   |
|                   ===== |
|_________________________|''',
'''
 _________________________
|                         |
|              +======+   |
|             ( )   \\|   |
|              |      |   |
|             /|\\    |   |
|              |      |   |
|             /\\     |   |
|                     |   |
|                   ===== |
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


x=0

lives = 6
word = random.choice(wordList)
print(word)	
guessList = []
for a in word:
	guessList.append("_")


while True:
	print(str(guessList) + " here are the letters you need to guess")
	print("Here are the lettters that you have guessed so far: " + str(letterBank))
	print("type (quit) to quit")
	choice = input("Guess a letter: ")
	if choice == "quit":
		break
	if choice == a:
		letterBank.append(a)
	if choice == b:
		letterBank.append(b)
	if choice == c:
		letterBank.append(c)
	if choice == d:
		letterBank.append(d)
	if choice == e:
		letterBank.append(e)
	if choice == f:
		letterBank.append(f)
	if choice == g:
		letterBank.append(g)
	if choice == h:
		letterBank.append(h)
	if choice == i:
		letterBank.append(i)
	if choice == j:
		letterBank.append(j)
	if choice == k:
		letterBank.append(k)
	if choice == l:
		letterBank.append(l)
	if choice == m:
		letterBank.append(m)
	if choice == n:
		letterBank.append(n)
	if choice == o:
		letterBank.append(o)
	if choice == p:
		letterBank.append(p)
	if choice == q:
		letterBank.append(q)
	if choice == r:
		letterBank.append(r)
	if choice == s:
		letterBank.append(s)
	if choice == t:
		letterBank.append(t)
	if choice == u:
		letterBank.append(u)
	if choice == v:
		letterBank.append(v)
	if choice == w:
		letterBank.append(w)
	if choice == x:
		letterBank.append(x)
	if choice == y:
		letterBank.append(y)
	if choice == z:
		letterBank.append(z)
	lives=lives-1
	if lives<=1:
		print("you lose, out of lives")
		break



