'''
Practice Python Problem 13
Write a program that asks the user how many Fibonnaci numbers to generate 
and then generates them. Take this opportunity to think about how you can 
use functions. Make sure to ask the user to enter the number of numbers in 
the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of 
numbers where the next number in the sequence is the sum of the previous two 
numbers in the sequence. 

Link:http://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html

'''

def fib():
	n=int(raw_input("How many numbers in Fibonnaci sequence do you want to generage: "))
	x=[1,1]
	for i in range(2,n):
		x.append(x[i-2]+x[i-1])
		i+=1
	return "Here is a beautiful fabonacci sequence for you: " + str(x)

print fib()