#basic for loop

elements = []

for i in range(0,6):
	elements.append(i)
	print '%d is added. The list now has %d elements.' % (i,len(elements))



#basic while loop 
i=0
elements = [] 

while i <= 10: 
	print 'the current i is %d' % (i)
	elements.append(i)
	i += 1
	print 'now the list is: ', elements


