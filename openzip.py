# Problem 6: 
# Open zip files and read through them. 

'''

filename = './channel.zip'
 
def download_zipfile(): 
    import urllib2 #library to open URL
    zf = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/channel.zip')
    output = open(filename,'wb')   #File mode, write and binary
    output.write(zf.read())  
    output.close()



def process():
    from zipfile import ZipFile
    file_list = ZipFile(filename)
 
    import re
    regex = re.compile(r'(\d+)$')
 
    comments = []
    nothing = '90052'
 
    try:
        for info in file_list.infolist():
            fn = '%s.txt' % nothing
            comments.append(file_list.getinfo(fn).comment)
            nothing = regex.search(file_list.read(fn,'r')).group()
    except:
        print ''.join(comments)
 
if __name__ == '__main__':
    process()

'''

import urllib,zipfile,re,collections
o=[]
n='90052'
f='%s.txt'
nnr="Next nothing is (\d+0)"

file= zipfile.ZipFile('channel.zip')

while True:
	try:
		n=re.search(nnr,file.read(f%n)).group(1)
	except: 
		print file.read(f%n)

	o.append(file.getinfo(f%n).comment)

print "".join(o)

