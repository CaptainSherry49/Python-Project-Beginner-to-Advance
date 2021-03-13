f2 = open('Sherry.txt')
try:
    with open('does.txt') as f:
        f.read()
except Exception as e:
    print(e)
else:
    print('This will run only if "except" is not running')
finally:
    print('YE to hoga')
    f2.close()


print('Important Stuff that should must be printing.')

'''
Finally ham code cleanup k liya use karta ha, chaha hamara code 'try' block ma jai ya 'except' ma jai 'Finally lazmi run
run hoga.
Else tab run hoga jab 'except' run nhi hoga yani k error nhi aye ga
'''
