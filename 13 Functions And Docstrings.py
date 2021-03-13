# -------------------------- Function & Docstring-------------------- #
'''
A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result.
'''


#  In Python a function is defined using the def keyword:

def function1():   # This is a Simple Function
    print('You are in Function')


# To call a function, use the function name followed by parenthesis:
function1()


def func2(a, b):   # Function with two parameters
    print(f'c = {a * b}')


func2(10, 345)


def divide(a, b):
    '''This Function will calculate the division of the given numbers'''
    m = a / b
    print(m)


print(divide.__doc__)  # This will print the doc string of the current function
divide(34, 9)
