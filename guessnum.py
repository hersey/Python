'''
Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they 
guessed too low, too high, or exactly right.

'''

import random

guess=0

count=0

number=random.randint(1,100)

#print number

print "Let's play a game. Type 'exit' to quit."

while guess!=number and guess!='exit':
	guess=raw_input('Give me a number between 1 and 100: ')
	if guess=="exit":
		break
	guess=int(guess)
	count+=1

	if guess<number:
		print("Too low.")
	elif guess>number:
		print("Too high.")
	else:
		print("You got it!")
		print "It took you " + str(count) + " tries!"

