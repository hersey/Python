'''
My if-else game
'''

print '''
You are standing in front of a time machine. There are two doors you can open.
'''

door = raw_input('Do you want to open door 1 or door 2? ')


if door == 'door 1' or door == 'Door 1' or door == '1': 
	print "Now you are going to travel to the past. There're two options: "
	print "1. Visit early 20th century Paris"
	print "2. Visit the Renaissance era."

	past = raw_input ('Do you want to choose 1 or 2? ')
	if past == '1': 
		print "Oh, look! Ernst Hemingway is sitting at a cafe in Saint German des pres. Approach?"
		EH = raw_input ('Yes/No: ')
		if EH == 'Yes':
			print "He smiled at you and invited you for a cup of coffee. Enjoy!"
		else:
			print "Oh come on! Hemingway thought you're ignoring him. How sad."
	elif past == '2':
		print "Oops, you have landed at Leonardo Da Vinci\'s studio. Say Hi?"
		LDV = raw_input ('Yes/No: ')
		if LDV == 'Yes':
			print "Oh, he just invited you to be his model. Have fun :)"
		else: 
			print "Hmm...Ok, now you are just transpassing. Get out before the police comes."
	else: 
		print "Not following rules? I like that. I will send you to ancient egypt. Good luck!"

elif door == 'door 2' or door == 'Door 2' or door == '2':
	print "Woohoo. You are currently traveling to the future. Hold tight. You have two choices: "
	print "1. Fly to 50 years from now and see what\'s it like."
	print "2. Meet a superintelligence AI and see what happens."

	future = raw_input ('Do you want to choose 1 or 2? ')
	if future == '1':
		print "So...you are inside a self-driving vehicle. Do you want to go somewhere cool?"
		SD = raw_input ('Yes/No: ')
		if SD == 'Yes':
			print "Wow..you are traveling on the super-highway to the Mars colony Elon Musk built. Buckle up!"
		else: 
			print "Seriously? You are in the future dude. Ok, car, let\'s drive to In-and-out."
	elif future == '2':
		print "A superintelligence is approaching you..Want to start a chat?"
		AI = raw_input('Yes/No: ')
		if AI == 'Yes':
			print "AI is going to take you to his 4-dimensional house built in mid air. Have fun!"
		else:
			print "Oh, not good. AI thinks you are a threat. He is going to fight you. Run!"
else: 
	print "Sorry, you have missed your time-traveling opportunity. Go back to work!"












