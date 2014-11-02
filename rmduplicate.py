'''
Practice Problem 14: 
Write a program (function!) that takes a 
list and returns a new list that contains all the elements of 
the first list minus all the duplicates.
Link: http://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html
'''

s=[1,2,3,3,5,6,2,2,2,2,2,3,4,5,"jack",'james','joe','jack']

def rmdp(x):
	return list(set(x))   #set is a collection of elements where no element is repeated. 

print s
print rmdp(s)


