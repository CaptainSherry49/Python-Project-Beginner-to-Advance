# ------------------------------ Lambda Function ------------------------------ #
'''
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.
lambda arguments : expression
'''

minus = lambda x, y: x - y
print(minus(731,598))  # This is it, this is called lambda function


# -------------------------- lambda function with list's sort function ----------------------- #
a_first = lambda a: a[1]  # lambda function which is accessing list "a" index 1 element

a = [[1, 14], [3, 5], [6, 7], [2, 0]]  # list of list
a.sort(key=a_first)  # key is a method which is taking a function
print(a)