#This is simple code to help you see the pagesource in an url

import urllib2
response = urllib2.urlopen(str(raw_input("Input the page url you want to see: ")))
page=response.read()
print page