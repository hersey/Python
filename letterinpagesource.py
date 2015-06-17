#Level 2 for pythonchallenge.com
#Step 1: Get page source from a url: http://www.pythonchallenge.com/pc/def/ocr.html

'''
import urllib2
response = urllib2.urlopen(str(raw_input("Input the page url you want to see: ")))
page=response.read()
print page

#Step 2: find characters in the big messy chunk of source code. 
'''
import urllib2
import sys

def find_letter():
	response = urllib2.urlopen(str(raw_input("Input the page url you want to see: ")))
	page=response.read()
	for i in page: 
		if i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
			#sys.stdout.write(i)
			sys.stdout.write(i) #this allows you to print without a newline or space: http://stackoverflow.com/questions/493386/how-to-print-in-python-without-newline-or-space

find_letter()


#the messy code hides the keyword "equality"
