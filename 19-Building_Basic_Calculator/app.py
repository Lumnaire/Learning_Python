num1 = int(input('Enter 1st number: '))
operator = input('Enter operator: ')
num2 = int(input('Enter 2nd number: '))

if operator == '+':
    solution = num1 + num2
    print('Answer:',solution)
elif operator == '-':
    solution = num1 - num2
    print('Answer:',solution)
elif operator == '*':
    solution = num1 * num2
    print('Answer:',solution)
elif operator == '/':
    solution = num1 / num2
    print('Answer:',solution)
else:
    print('Invalid Operator')