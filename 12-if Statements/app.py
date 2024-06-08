# if statement is a condition

x = 4
y = 2

# conditionals <, >, ==, !=, >=, <= 
if x>y:
    print(str(x) + ' is grether than ' + str(y))



a = False
b = 'Felix'

if a == True:
    print('a is true')
elif a == False:
    print('a is false')
else:
    print('None of the above')



# and checks if the two condition are both correct, using or will vary depending if one is correct or not
boy = True
short = True

if boy == True or short == True:
    print('He is a boy and he is short')
else:
    print('not a boy and not short')