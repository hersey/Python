#Find pattern: This program is written to find the follow patter:
#Three capital letters + One lower case + Three capital letters
#the source is an url input by the user. 

import urllib2
import re

response = urllib2.urlopen(str(raw_input("Input the page url you want to see: ")))
text=response.read()
#text=str(raw_input("Input the text you want to find match: "))
print re.findall(r'[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]',text)  #match the exact pattern using re commands. 


#['qIQNlQSLi', 'eOEKiVEYj', 'aZADnMCZq', 'bZUTkLYNg', 'uCNDeHSBj', 'kOIXdKBFh', 'dXJVlGZVm', 'gZAGiLQZx', 'vCJAsACFl', 'qKWGtIDCj']

'''
answer: linkedlist
'''
