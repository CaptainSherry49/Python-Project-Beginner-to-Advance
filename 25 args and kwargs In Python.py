# ------------------------------------ *args ---------------------------- #
'''
If you do not know how many arguments that will be passed into your function,add a * before the parameter name in the
function definition.
This way the function will receive a tuple of arguments, and can access the items accordingly:
'''


def name_print(n, *args):   # n is a normal argument
    print(n)
    print(*args)


names = ['A','B','C','D','E']
name_print('Hi i am normal', *names)

# Remember = func_arguments(normal, *args , **kwargs)
# args ka andar chizain tuple ki type ma  jati hain chaha list hi q na ho


# --------------------------------------- **kwargs -------------------------- #
'''
If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before 
the parameter name in the function definition.
This way the function will receive a dictionary of arguments, and can access the items accordingly:
'''


kw = {'A':' First', 'B': 'Second', 'C':'Third'}


def ar_kw(n, *args, **kwargs):
    print(f'Normal argument is {n}\n')
    for i in args:
        print(f'*args are {i}\n')
    for key, value in kwargs.items():
        print(f'kwargs keys is  {key} and values is {value}')


ar_kw(618, *names, **kw)


# agar hama func ma bohat sara arguments dena ho to ham waha args or kwargs istemal karta ha
