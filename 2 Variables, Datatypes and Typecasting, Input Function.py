# ------------------- Variables ---------------#

first = 'Hello Sherry!'   # This is string value store in a variable 'first'
second = 49  # This is integer value store in a variable 'second'
third = 10.13  # This is float value store in a variable 'third'
fourth = True  # This is a boolean value store in a variable 'fourth'


# ------------------------- DataType -------------------#

print(type(first))
print(type(second))
print(type(third))
print(type(fourth))


# ------------------ TypeCasting ---------------------#

var1 = 45  # Simple integer variable
var2 = int('345')  # Change type of string value into integer
print(var1 + var2)

# Types: <int>,  <float>, <str>, <bool>


# ------------------------- Input Function ------------------- #

user = input('Enter anything: ')  # Input Function take's input as string
print('You Entered', user)


# -------------------- Remember--------------------------#

'''
We can add two integer and float with each other , we can also add integer with float
but we cannot add an integer with string & float with string , we can only concatenate
string with string.
'''


# ----------------------- Quiz ---------------------------#

print('Enter Two Numbers to add them - ')
val1 = int(input('Enter First value: '))
val2 = int(input('Enter Second Value: '))
print('Your Answer is', val1 + val2)