# Problem 6: 
# Open zip files and read through them. 

'''
import zipfile
 
def read_zip_file(filepath):
    zfile = zipfile.ZipFile(filepath)
    for finfo in zfile.infolist():
        ifile = zfile.open(finfo)
        line_list = ifile.readlines()
        print line_list


print read_zip_file('/Users/heliu/Documents/Github/Python/channel.zip') 
'''

import zipfile

zip = zipfile.ZipFile(open('/Users/heliu/Documents/Github/Python/channel.zip','r'))

nothing = '90052'
comments = [] #The answer is *in* the zip..
while True:
    raw_data = zip.read(file % nothing)
    print raw_data
    nothing = int(raw_data.split()[-1])
    comments.append(zip.getinfo(file % nothing).comment)

print "".join(comments)