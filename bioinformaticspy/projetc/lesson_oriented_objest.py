class pet: 
    number_of_legs = 0
    
    def sleep (self):
        print "zzzzzzzz"

    def count_legs(self):
        print 'have %s legs' % self.number_of_legs

class dog (pet):
    def bark(self):
        print "xoof"

doug=dog()
doug.number_of_legs=0
doug.count_legs()

