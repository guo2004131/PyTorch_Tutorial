"""
In this tutorial, we will discuss (1) iterables, (2) generators, (3) yield, and (40 itertools

"""
###############################################################################################################
# (1) Iterables
# When you create a list, you can read its items one by one. Reading its items one by one is called iteration
mylist = [1, 2, 3]
for i in mylist:
    print(i)

# mylist is an iterable. When you use a list comprehension, you create a list, and so an iterable:
mylist = [x*x for x in range(3)]
for i in mylist:
    print (i)

# Everything you can use "for... in..." on is an iterable; lists, strings, files...
# These iterables are handy because you can read them as much as you wish,
# but you store all the values in memory and this is not always what you want when you have a lot of values.
###############################################################################################################

###############################################################################################################
# (2) Generators
# Generators are iterators, but you can only iterate over them once.
# It's because they do not store all the values in memory, they generate the values on the fly:
mygenerator = (x*x for x in range(3))
for i in mygenerator:
    print (i)
# It is just the same except you used () instead of [].
# BUT, you cannot perform for i in mygenerator a second time since generators can only be used once:
# they calculate 0, then forget about it and calculate 1, and end calculating 4, one by one.
###############################################################################################################

###############################################################################################################
# (3) Yield
# Yield is a keyword that is used like return, except the function will return a generator.
def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i*i
# The mygenerator is now a "generator" type of variable.
mygenerator = createGenerator()
print (mygenerator)
# We can still reference the items in the generator.
# It comes handy when using a huge set of values that you will only need to read once.
# To master yield, you must understand that when you call the function, the code you have written in the function
# body does not run. The function only returns the generator object, this is a bit tricky.
for i in mygenerator:
    print (i)
# The hard part is that:
# The first time the "for" calls the generator object created from your function,
# it will run the code in your function from the beginning until it hits yield,
# then it'll return the first value of the loop.
# Then, each other call will run the loop you have written in the function one more time,
# and return the next value, until there is no value to return.
# The generator is considered empty once the function runs but does not hit yield anymore.
# It can be because the loop had come to an end, or because you do not satisfy an "if/else" anymore.
###############################################################################################################

###############################################################################################################
# (4) Itertools
# The itertools module contains special functions to manipulate iterables.
# Ever wish to duplicate a generator? Chain two generators?
# Group values in a nested list with a one liner? Map / Zip without creating another list?
import itertools
horses = [1, 2, 3, 4]
races = itertools.permutations(horses)
print(races)
# to use "list" to retrieve the values
print(list(itertools.permutations(horses)))
print(list(itertools.combinations(horses, 2)))
# detailed usage of itertools can be found at https://docs.python.org/2/library/itertools.html
###############################################################################################################