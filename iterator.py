'''iterator
An iterator is an object that contains a countable number of values.
An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.'''

mytuple=("computer","keyboard","mouse")
for x in mytuple:
    print(x)


mytuple=("cs","msc","mca")
myiter=iter(mytuple)
print(next(myiter))
print(next(myiter))
print(next(myiter))

mystr="banana"
myit=iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


