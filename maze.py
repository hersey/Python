# A maze game to practice loops

''' Logic for this game

start() 
1. Blue room: Open a door:
	-Yes: Press a red button:
			-Yes: Enter dimension()
			-No: Explosion.
	-No: 
2. Green room

'''

from sys import exit

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
			green_room()

		elif answer.lower() == 'No' and door_open:
			print dead('Oops, did I forget to tell you, the room will explode in 5,4,3,2,1...')
		elif answer.lower() == 'No' and not door_open: 
			print dead('You are running out of time. The room will explode in 5,4,3,2,1...')
		else: 
			print dead('You are running out of time. The room will explode in 5,4,3,2,1...')
	
def green_room ():
	print 'Welcome to the green room. You can be granted for wishes. How many do you want?'
	wish = raw_input('> ')   #raw_input data type is default to be string.

	if wish.isdigit() == True: 
		int_wish = int(wish)
		if int_wish <= 5:
			print 'Your wishes are granted. Follow me to the wish room.'
			wish()
		else:
			print dead('So greedy. You receive no wishes.')
	else:
		print 'please type a number.'
		green_room()
	
#Problem: how to detect whether a raw_input is a number

def wish():
	print 'Welcome to the wish room. I will assemble your wish.'
	place = raw_input('What is your favorite place in the world?' )
	thing = raw_input('What do you love to do?' )
	age = raw_input('What is your age?')
	print 'Your wish is granted. You will be %s in %s for %r years.' % (place,thing,70-int(age))

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

'''
def dimension():
	print 'Welcome! You have just arrived into a 4 dimension world.'

	i = 0

'''

start()

