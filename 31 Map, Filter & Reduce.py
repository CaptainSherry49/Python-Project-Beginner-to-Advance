# ------------------------------- Map ------------------------ #
'''
The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.
'''

num = ['1', '2', '3', '4', '5']

num = list(map(int, num))

a = num[2] + 1
print(a)

# ---------------------- using map func to apply square lambda func in the list 'num2' --------------- #

num2 = [2, 3, 4, 5, 6, 7, 8, 9]
num2 = list(map(lambda x: x*x, num2))
print(num2)


def square(n):
    return n*n


def cube(n):
    return n*n


lst = [square, cube]

for i in range(5):
    val = list(map(lambda x: x(i), lst))
    print(val)


# ----------------------------- Filter Function --------------------- #
'''
The filter() function returns an iterator were the items are filtered through a function to test if the item is accepted or not.
'''

list1 = [2, 3, 3, 6, 87, 58, 456, 312, 12]


def gr_than_50(n):
    return n > 50


gr = list(filter(gr_than_50, list1))
print(gr)


# ------------------------------ Reduce --------------------------- #

from functools import reduce

num3 = [1, 3, 4, 6]

s = reduce(lambda x,y: x + y, num3)
print(s)
