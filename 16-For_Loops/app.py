# for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# list loop
mylist = ['Hyuki', 'Geo', 'Inrad']

for values in mylist:
    # with condition
    if values == 'Geo':
        break # the output will be only hyuki, because of the condition loop
    print(values)



# dictionary loop but it only prints the key not the value
my_dictionary = {
    'name': 'Ronald',
    'age': 21,
    'location': 'Philippines'
}

for values in my_dictionary:
    print(values)



# looping range
for x in range(4): # you can also put range(3,7) the print will start at 3 to 7
    print(x)
else:
    print('Finished Looping')
