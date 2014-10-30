'''
Make the Big Bang Theory's famous Rock-Paper-Scissors-Lizard-Spock game:

Rules: 
Scissors cut Paper
Paper covers Rock
Rock crushes Lizard
Lizard poisons Spock
Spock smashes Scissors
Scissors decapitate Lizard
Lizard eats Paper
Paper disproves Spock
Spock vaporizes Rock
Rock crushes Scissors

See coursera instruction for more detail: 
https://class.coursera.org/interactivepython-005/human_grading/view/courses/972530/assessments/28/submissions

'''

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

'''
The following code is my first version of RPSLS:
-Haven't fixed the problem if user input is out of the five words
-Need to add a loop so the game can continue
-Need to make the code shorter and simpler
'''

def name_to_num(name):
	if name=="rock":
		return 0
	elif name=="spock":
		return 1
	elif name=="paper":
		return 2
	elif name=="lizard":
		return 3
	elif name=="scissors":
		return 4
	else:
		return "You entered an invalid word. Try again."   # need to figure out how to stop the following functions if input something wrong) 


def num_to_name(num):
	if num==0:
		return "rock"
	elif num == 1:
		return "Spock"
	elif num == 2:
		return "paper"
	elif num == 3:
		return "lizard"
	elif num == 4:
		return "scissors"


#Ask User for input and store in variable "Name" and translate word to 
name=str(raw_input("Choose one out of 'rock, paper, scissors, lizard or spock': "))
player=int(name_to_num(name))
#Generate random number from 0 to 4 and assign number to a word using num_to_name function

import random
machine=random.randint(0,4)
print "Your computer chose " + str(num_to_name(machine)) + "."  #Show user what machine chose.

#Use function rpsls() to compare the input of user vs machine
def rpsls(p, m):
	if(p-m)%5 in (1,2):
		return "Congrats, you win! Go human!"
	elif (p-m)%5 in (3,4):
		return "Sorry, computer wins. Go AI!"
	elif p==m:
		return "It's a tie!"
	else: 
		return "I don't know what you just did."

print rpsls(player,machine)