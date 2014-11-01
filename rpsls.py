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


The key idea of this program is to equate the strings
"rock", "paper", "scissors", "lizard", "Spock" to numbers
as follows:
0 - rock
1 - Spock
2 - paper
3 - lizard
4 - scissors


The following code is my second version of RPSLS:
-Fixed the problem if user input is out of the five words
-Added a loop so the game can continue
-Added counter to keep track of number of tries, users win/tie against the computer. 
'''

#Ask User for input and store in variable "Name" and translate word to number.


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
	elif name=="exit":
		return 200 
	else:
		return 100


#Computer randomly generate a number between 0 and 4.
import random
def num_to_name(num):    #Translate the number into word
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


#Use function rpsls() to compare the input of user vs machine

def rpsls(p, m):
	if p==100: 
		return "You entered an invalid word. Try again."   # Check on invalid input from users.
	elif p==200:
		print "Thanks for playing."    #Give user an exit to quit the game everytime the game restarts. 
		exit()
	elif(p-m)%5 in (1,2):
		return "Congrats, you win. Go human!"
	elif (p-m)%5 in (3,4):
		return "Sorry, computer wins. Go AI!"
	elif p==m:
		return "It's a tie!"
	else:
		return none

# "User_win/tie" variables keeps a count on how many times user win/tie. "Count" lets user choose how many times
#they want to play against the computer. "Tries" keeps a count of how many times user has played. 
 
def main():
	print "Welcome to Sheldon Cooper's famous Rock-Paper-Scissors-Lizard-Spock game."
	print "Here're the rules:\nScissors cut Paper\nPaper covers Rock\nRock crushes Lizard \nLizard poisons Spock \n\
Spock smashes Scissors \nScissors decapitate Lizard \nLizard eats Paper \nPaper disproves Spock \nSpock vaporizes Rock \nRock crushes Scissors." 
	count=int(raw_input("How many times do you want to play against the computer? Choose 1 to 10: "))  
	print "Type 'exit' to quit the game."
	user_win=0
	tie=0
	tries=1
	while tries<=count: 
		player=name_to_num(str(raw_input("Choose one out of 'rock, paper, scissors, lizard or spock': ")))
		if player==200:
			print "Thanks for playing. We'll miss you. You won "+str(user_win)+" times and tied "+ str(tie)+" times."
			exit()
		machine=random.randint(0,4)
		print "Your computer chose " + str(num_to_name(machine)) + "."   #Show user what machine chose.
		print rpsls(player,machine)
		if rpsls(player,machine)=="Congrats, you win. Go human!":
			user_win+=1
		elif rpsls(player,machine)=="It's a tie!":
			tie+=1
		print "You have "+ str(count-tries) + " more chances."
		tries+=1
	print "Game Over. You won the computer "+str(user_win)+" times and tied "+ str(tie)+" times."

main()


