# Level 4 in Python Challenge. http://www.pythonchallenge.com/pc/def/linkedlist.php
# Base url has a pageid=some_num. when you input that number into the new page id, it jumps to a new page. 



import urllib, re

baseurl="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

#pageid="12345"
pageid="46059"

counter=0
while counter < 410: #arbitrary big number
	#fetch page by combining baseurl and pageid. 
	pagedata = urllib.urlopen(baseurl+pageid).read()
	#get next page id by obtaining the current number on the screet
	pageid = "".join(re.findall("and the next nothing is ([0-9]+)", pagedata))
	#if problem grepping a number then break out loop  
	if  pageid == "":
		break
	else:
		print counter,"(next ",pageid, "):", pagedata
 	counter+=1

print pagedata