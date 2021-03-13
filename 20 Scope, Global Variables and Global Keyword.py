# --------------------------- Global & Local Variable --------------- #

l = 10  # Global variable -  every function can use this variable


def func1(n):
    l = 7
    m = 8  # both are local variable only this function can use this both variables
    print(l, m)
    print(n, 'I have printed')


func1('Sherry')
print(l)  # this print function will print the global variable not the function's local variable


# ------------------------ Global Keyword ---------------------- #
def func1(n):
    m = 8  # local variable
    global l  # now we can change variable l because of global keyword
    l += 45
    print(l, m)
    print(n, 'I have printed')


# -------------------------- Global keyword miss concept -------------------- #
def harry():
    x = 20

    def rohan():
        global x  # is func ka harry k 'x' pa kuch asar nhi para ga q k ya global ma 'x' ko check kara ga local ma nhi
        x = 88
    print('before calling rohan:', x)
    rohan()
    print('after calling rohan:', x)


harry()
