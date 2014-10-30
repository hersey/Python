'''
Take two lists, say for example these two:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python

Link: http://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html

'''


import random

a=random.sample(range(100),10)
b=random.sample(range(100),10)

print "List a is: " + str(a)
print "List a is: " + str(b)

common=[]

for i in a:
	if i in b:
			common.append(i)

print "The overlap of a and b is: " + str(common)

#Alternative

result=[i for i in a if i in b]

print result
