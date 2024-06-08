# return statement is a response from the task being executed

# basic structure of return
def my_function():
    return 5 + 4

print(my_function())



# return statement with parameter
def add_numbers(num1, num2):
    return num1+num2

print(add_numbers(5,5))



# return statement with parameter and users input
def simple_calcu(num1,num2):
    return num1 * num2

num1 = int(input('Enter num1: '))
num2 = int(input('Enter num2: '))

print('Total answer: ', simple_calcu(num1,num2))
