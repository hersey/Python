'''
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

Problem 6: 
Url: http://www.practicepython.org/exercise/2014/03/12/06-string-lists.html

'''

word=str(raw_input("Give me a word: "))

if word==word[::-1]:
	print "The word is a palindrome."
else: 
	print "The word is not a palindrome."