# list structure is an array

countries = ['Philippines', 'Vietnam', 'Japan', 'India', 'Belgium']
name = 'Ronald'
age = 21

print(countries[0]) # gets the value in the array
print(countries[0][0]) # gets the index value inside your array value
print(countries[1:4]) # 1 gets the starting index and 4 limits the printing
print(type(countries)) # checks variable type
print(type(name))
print(type(age))

countries[1] = 'Russia' # changes value in the list
countries[3] = 'Canada'
print(countries)

print(countries[-2]) # gets the last or bottom part of the list
print(len(countries))

# can insert any variable type like int or boolean 
fruits = ['Banana', 17, True, 'Peach']
print(type(fruits[1])) # finds the variable type inside the list

# This is called list constructor, although it is the same above
data = list(('Rio', 'Berlin', 54, False))
print(data)