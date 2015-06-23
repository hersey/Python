# A maze game to practice loops

''' Logic for this game

start(): Choose a room 
1. Blue room: Open a door:
	-Yes: Press a red button:
			-Yes: Enter puzzle()
				-Give a random number from 1 to 5
				-Have three time to guess
				-If guess right, exit game. If guess wrong, exit with Self-destruction.
			-No: Going to green_room()
	-No: Explosion. 
2. Green room: How many wishes
	-Typed in a number: 
		-Number <=5: Take you to wish room
			-Wish_room (): Ask you three questions --> Grant you wish.
		-Number > 5: Too greedy. Quit. 
	-Typed in a non-number: Alert. Reenter green room. 

'''

from sys import exit
import random 

def blue_room (): 
	print 'Welcome to the blue room. You are trapped in a cell in Alcatraz. You have 5 min to escape.'
	print 'There is a tiny door on the ceiling. Open it?'
	door_open = False

	while True: 
		answer = raw_input('Yes/No: ')
		if answer.lower() == 'yes' and not door_open:
			print 'Wow..You have entered a strange light tunnel. A red button is in front of you. Press it?'
			door_open = True
		
		elif answer.lower() == 'yes' and door_open:
			puzzle()

		elif answer.lower() == 'no' and door_open:
			print 'The tunnel is leading you to a strange place....'
			green_room()
		else: 
			print dead('You are running out of time. The room will explode in 5,4,3,2,1...')
	
def green_room ():
	print 'Welcome to the green room. You can be granted for wishes. How many do you want?'
	wish = raw_input('> ')   #raw_input data type is default to be string.
	if wish.isdigit() == True:  #To detect whether a raw_input is integer, then convert if it is. (data type is always a string.)
		int_wish = int(wish)
	else:
		print 'Your input is not a number! But wait...it is taking you to a random room...'
		blue_room()

	if int_wish <= 5:
		print 'Your wishes are granted. Follow me to the wish room.'
		wish_room()
	else:
		print dead('So greedy. You receive no wishes.')

	
def puzzle():
	print 'Welcome! You have just arrived into a puzzle world.'
	counter = 0
	r = random.randint(1,5)
	while counter < 3: 
		num = int(raw_input('You have three chances to play this game. Give me a random number from 1 to 5: ')) #Make sure datatype is integer
		if num == r: 
			print "Congratulation! You win the game. You are the number %r survivor! " % (r*5)
			exit(0)			
		else:
			print 'Wrong guess. Try again.'
			counter +=1
		
		if counter>=3: 
			print dead('Sorry, you are out of luck! Self-destruction initiated.')
			break
		


def wish_room():
	print 'Welcome to the wish room. But I can only give you One wish---I will assemble it for you.'
	place = raw_input('Where do you want to visit the most? ' )
	thing = raw_input('What\'s your most favorite thing to do? ')
	star = raw_input('Which movie star do you like the most? ')
	age = raw_input('What is your age? ')
	print 'Your wish is granted...Ready? You will be traveling in %s for %r days, %s everyday with %s.' % (place, (70-int(age))/2, thing, star)
	exit(0)

def dead(text): 
	print text,'Bye! See you in another life.'
	exit(0)



def start(): 
	print 'You are in a dark room. There are two doors in front of you.'
	print 'Which door do you take? Blue or Green?'
	door = raw_input ('> ')
	if door.lower() == 'blue': 
		blue_room ()
	elif door.lower() == 'green':
		green_room ()
	else: 
		dead('Looks like you are not interested in the game.')



start()

