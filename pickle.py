# Level 5 for pythonchallenge.com: http://www.pythonchallenge.com/pc/def/peak.html

#Have error in Pickle file. Need to revisit 

'''
Pickle: 
a Python object that has undergone the native serialization by the pickle module.
Pickle allows the programmer to generate a string representation of any object, 
very useful in saving complicated data types.
'''



import pickle
import urllib

test=pickle.load(urllib.urlopen('http://www.pythonchallenge.com/pc/def/banner.p'))


def print_line(pair_list):
    print ''.join(pair[0] * pair[1] for pair in pair_list)
 
for pair_list in test:
    print_line(pair_list)
