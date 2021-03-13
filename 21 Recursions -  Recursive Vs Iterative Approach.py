# ------------------------- Iterative -------------------------- #
def factorial_iterative(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    print(fac)


user = int(input('Enter number: '))
print('Factorial using iterative method :', end=' ')
factorial_iterative(user)


# ----------------------- Recursive Method --------------------- #
# Recursion is the process of defining something in terms of itself.

'''
Python also accepts function recursion, which means a defined function can call itself.
Recursion is a common mathematical and programming concept. It means that a function calls itself.
This has the benefit of meaning that you can loop through data to reach a result.
'''


def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)


a = int(input('Enter number: '))
print(factorial_recursive(a))


# --------------------------------- Quiz -------------------------- #


def fibonacci_sequence(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_sequence(n-1) + fibonacci_sequence(n - 2)


user = int(input('Enter number: '))
print(fibonacci_sequence(user))

