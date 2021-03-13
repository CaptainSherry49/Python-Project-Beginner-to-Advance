# ---------------------- Try Except ------------------------- #
'''
The try block lets you test a block of code for errors.
The except block lets you handle the error.
The finally block lets you execute code, regardless of the result of the try- and except blocks
'''


try:
    num1 = int(input('Enter num1: '))
    num2 = int(input('Enter num2: '))
    print(f'sum of both number is {num1 + num2}')
except Exception as e:
    print(e)


print('The above code may give an error if we enter a string value into it , but if we use'
      ' "try , except " the error will not br generated and this line will be print.')