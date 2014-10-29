# An exercise to build division check
#Link: http://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

#Odd or Even number

num=int(raw_input('Give me a number: '))

if num%2==0:
	print str(num) + " is an even number."
else: 
	print str(num) + " is an odd number."

#Check and divide by

a=int(raw_input('Give me a number to check: '))
b=int(raw_input('Give me a number to divide by: '))

mod=a%b

if a%b==0:
	print str(a) + " can be divided by " + str(b)
else:
	print str(a) + " can not be divided by " + str(b) + ". The remainder is "+ str(mod)


