# ---------------------------------- File IO Basics ---------------------------- #
'''
"r" - read mode - open file for reading - (default mode)
"w" - write mode - open file for writing
"a" - append mode - add more content in the end of file
"x" - Creates file if not exists
"t" - text mode - (default mode)
"b" - binary mode
"+" - read and write mode
'''


# --------------------- Question of the Day ----------------------- #
# How to Access doc string of any function:
# Solution:
def addition(a, b):
    """This function will add to numbers"""
    c = a + b
    return c


print(addition.__doc__)  # This code will print the doc-string of this function
