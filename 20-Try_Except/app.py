# try except prevent from errors // in other words error handlers
# can be also used for testing 


try:
    x = int(input('Enter an integer: '))
    print(x)

except ValueError: # there are many types of error like NameError etc. this is used for specifying an error
    print('Value not an integer')

#finally:  will execute wether it is an error or not

else: # its best practice to use else at the end for clarifying for successful execution
    print('Nothing went wrong')
