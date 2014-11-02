'''
Practice Python Problem 11
Ask the user for a number and determine whether the number is prime or not. 
(For those who have forgotten, a prime number is a number that has no divisors.). 
Link: http://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html
'''


def prime():
	num=float(raw_input("Give me a positive integer to test if it's a prime number: "))
	if num!=int(num) or num<=0:  #return alert if the number is a float, string or not a positive number. 
		return "A prime number has to be a positive integer."
	else:
		x=range(1,int(num)+1)  #x is from 1 to this number (note: the range excludes the upper end, therefore num+1)
		divisors=[]    #create an empty list that will be filled by the number's divisors.
		for i in x:
			if num%i==0:
				divisors.append(i) #append the divisors list as i rotate in the range of 1 to the number
		if divisors==[1,int(num)]:
			return "This number is a prime number."  #Return "prime number" if the divisors are 1 and itself.
		else: 
			return "This number is not a prime number. Here are its divisors:" + str(divisors) #Return all its divisors if not a prime number.


print prime()