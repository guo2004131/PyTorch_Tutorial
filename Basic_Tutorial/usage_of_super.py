# to declare a class
class Foo(object):
    def __init__(self, a, b):
        self.first = a
        self.second = b


# the class "Bar" class is inherited from the class "Foo", which also consists of
# parameters: self.first and self.second.
class Bar(Foo):
    def __init__(self, c, d):
        super(Bar, self).__init__(12, d)
        self.third = c

foo = Foo(1, 2)
print ("The first in foo is %d" % foo.first)
print ("The second in food is %d" % foo.second)
bar = Bar(11, 23)
print ("\nThe first in bar is %d" % bar.first)
print ("The second in bar is %d" % bar.second)
print ("The third in bar is %d" % bar.third)
# the class "Bar" only inherit the class "Foo", but not change the parameter value.
print ("\nNow let's check what's in class Foo")
print ("The first in foo is %d" % foo.first)
print ("The second in food is %d" % foo.second)

