def func1():
    print('Becoming a Python Hero')


func2 = func1
del func1
func2()  # func2 will be still execute because we assign func1 into func2, func2 makes copy of func1

# ---------------------------- Function return function ----------------- #


def func_returner(num):
    if num == 0:
        return print
    else:
        return sum


print(func_returner(5))


# -------------------------- #
def executor(func):
    func('this')


executor(print)


# -------------------------------- Decorators -------------------------- #
def dec1(fun):
    def exe_now():
        print('Executing now')
        fun()
        print('Executed')
    return exe_now


# A decorator takes in a function, adds some functionality and returns it.
@dec1     # @dec1 == w_i_s = dec1(w_i_s)
def w_i_s():
    print('Sherry is a Programmer')


w_i_s()
