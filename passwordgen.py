'''
Practice Python Problem 16: 
Write a password generator in Python. Be creative with how you generate passwords 
- strong passwords have a mix of lowercase letters, uppercase letters, numbers, 
and symbols. The passwords should be random, generating a new password every time 
the user asks for a new password. Include your run-time code in a main method.


The password generator includes two user inputs: 
1. How many digits of password users want to generate: ask for a number
2. The strength of password: user choose 'weak', 'medium' or 'strong': convert rawinput into lower() for consistency. 

For weak password: generate random N digit numbers. 
For medium password: generate random N digit numbers+letters(lower and upper cases)
For strong password: generate random N digit numbers, letters(lower and upper) and symbols "!@#$%^&*._'".

Note: All random sampling are without replacement. Using random.sample(population, k) to generate. 

'''

import string, random
digit=int(raw_input("How many digits of password do you want to generate: "))
strength=raw_input("How strong do you want your password to be? \nType \"Weak\", \"Medium\" or \"Strong\": ").lower()

def password(d,s):
	if s=="weak":
		return ''.join(random.sample(string.digits,d))
	elif s=="medium":
		return ''.join(random.sample(string.letters+string.digits,d))
	elif s=='strong':
		return ''.join(random.sample(string.letters+string.digits+"!@#$%^&*._'",d))
	else:
		return "Your input is not valid."

print password(digit,strength)



