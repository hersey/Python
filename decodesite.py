'''
Practice Problem 17 
The How To Decode A Website exercise was a challenging one, involving many complex pieces of code and two new Python modules. 
When appropaching problems like this one, it helps to develop a plan for the program before executing it.

Our plan should be as follows:

Use the requests library to load the HTML of the page into Python
Set up BeautifulSoup to process the HTML
Find out which HTML tags contain all the titles
Use BeautifulSoup to extract all the titles from the HTML
Format them nicely

The following program strip the news titles on techcrunch.com homepage.

Link: http://www.practicepython.org/solution/2014/07/10/17-decode-a-web-page-solutions.html
'''

import requests
from bs4 import BeautifulSoup

base_url='http://www.techcrunch.com'  #Make a request to NYT
r=requests.get(base_url)  # Make a get request
soup=BeautifulSoup(r.text) # Return all the HTML from the returned request

#Return all tags with story-telling as a class. 

# find and loop through all elements on the page with the 
# class name "post-title"
for story_heading in soup.find_all(class_="post-title"):
	# for the story headings that are links, print out the text
    # and format it nicely
    # for the others, take the contents out and format it nicely
	if story_heading.a:
		print(story_heading.a.text.replace('\n',' ').strip())
	else: 
		print(story_heading.contents[0].strip())