# def is defining a function
# function with parameters // also str converts the int to string
def greetings_function(name, age):
    print('Welcome '+name+ ' You are ' +str(age)+ ' years old.')

greetings_function('Ronald! To the world of Python', 21)



# asterisk is used to define various values in the parameter argument
def location_function(*places):
    print('You are from '+places[0])

location_function('Philippines', 'Japan', 'Korea')



# function with parameter argument and user input
def introduction_function(name,age,location):
    print('Hello ' +name+ '! You are ' +age+ ' years old, From ' +location)

name = input('Enter your name: ')
age = input('Enter your age: ')
location = input('Enter your location: ')

introduction_function(name,age,location)
