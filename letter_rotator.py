'''
This exercise is to decode an encrypted paragraph. All letters have been moved N letters forward/backward (user input), in order
to decode a message.


source: http://www.pythonchallenge.com/pc/def/map.html
example: K -> M; O->Q 
Now I need to translate this paragraph into plain english using a simple function to convert:

g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.

Step 1: Acquire current string position from inputs.
Step 2: Minus 2 to current position.
Step 3: Transform string positions back to English. 

'''

'''
Method 1 below has some problems: for example, letter "a" is converted to "{" instead of "c" because of indexing order difference. 
The recommended solution is to use string.maketrans(from, to). See method 2. 
'''

#### Method 1 #####
import string

def letter_rotator():
	para=str(raw_input("Input the paragraph you want to decode: "))  
	num=int(raw_input("Input the number of letters you want to count FORWARD/BACKWARD: "))
	for i in para:
		position=ord(i)
		if position==32:
			new_pos=position
			print chr(new_pos),
		else: 
			new_pos=position+num
			print chr(new_pos),

letter_rotator()


#### Method 2 #####
import string

def letter_rotator():
	para=str(raw_input("Input the paragraph you want to decode: "))  
	num=int(raw_input("Input the number of letters you want to count FORWARD/BACKWARD: "))

	for i in para:
		position=ord(i)
		if position==32:
			new_pos=maketrans
			print chr(new_pos),
		else: 
			new_pos=position+num
			print chr(new_pos),

letter_rotator()

