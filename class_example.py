#classexample.py
'''
class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print "I AM CLASSY APPLES!"

thing = MyStuff()
thing.apple()
print thing.tangerine
'''
#### My own class code for practice ####

class startup(object):
	def __init__(self,lyrics):
		self.lyrics=lyrics

	def fund(self):   #Inside the functions in a class, self is a variable for the instance/object being accessed.
		amount = 0
		for a in self.lyrics:
			amount = amount + len(a)

		print 'Next round will be ', amount*10, ' Million'

uber = startup(['uber is your private driver'])

square = startup(['square is a card reader'])

uber.fund()
square.fund()