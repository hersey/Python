'''
Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 

'''

num=int(raw_input('Give me a number: '))

x=range(1,num+1)

divider=[]

for i in x: 
	if num%i==0:
		divider.append(i)

print divider

