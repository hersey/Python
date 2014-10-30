'''
Write one line of Python that takes this list a and makes a new list that has only the even 
elements of this list in it.

http://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html

'''
import random

a=random.sample(range(1000),10)

print a

b=[]

for i in a: 
	if i%2==0:
		b.append(i)

print b
