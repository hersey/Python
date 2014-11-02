'''
Practice Python Problem 4:
Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
If you do not know what a divisor is, it is a number that divides evenly into another number. For example, 13 
is a divisor of 26 because 26 divided by 13 has no remainder.
url: http://www.practicepython.org/exercise/2014/02/26/04-divisors.html
'''

num=int(raw_input('Give me a number: '))

x=range(1,num+1)

divisor=[]

for i in x: 
	if num%i==0:
		divisor.append(i)

print divisor

