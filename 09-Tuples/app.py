# tuples are used to store multiple items in a single variable
# closely related to list but it has a basic difference like tuples are immutable (cannot change value)

three_numbers = (1, 2, 3)
strings = ('About', 'Home', 'Contacts')
#three_numbers[1] = 10 #this will be an error because tuples is immutable it cannot be changed
print(three_numbers[1])
print(len(three_numbers))
print(type(three_numbers))
print(strings)

# tuple cosntructor works the same
exampleString = tuple(('Hi', 'Hello', 'Good'))
print(exampleString)
