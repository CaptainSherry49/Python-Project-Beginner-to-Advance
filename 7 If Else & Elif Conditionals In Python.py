# ----------------- If Else & Elif -------------------- #

'''
Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
These conditions can be used in several ways, most commonly in "if statements" and loops.

An "if statement" is written by using the if keyword.
'''


var1 = 43
var2 = 465
var3 = int(input('Number: '))

if var3 > var2:
    print('Greater')
elif var3 == var2:
    print('Equal')
else:
    print('Lesser')

list1 = [4, 7, 89, 2]

if 7 in list1:
    print('Yes')
else:
    print('No')


# ------------------ Quiz ------------------------- #

Age = int(input('Enter Your Age:  '))

if Age > 18 and Age < 100:
    print('Yes you are eligible to Drive :)')
elif Age == 18:
    print('You have to come here so that we can Physically check you -')
elif Age < 18 and Age > 12:
    print('You are Not eligible to Drive :(')
else:
    print('Enter Valid Age')