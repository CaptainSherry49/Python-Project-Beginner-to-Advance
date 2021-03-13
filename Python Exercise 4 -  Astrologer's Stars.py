# -------------------------- Star's Pattern ---------------------- #
'''
input = integer
boolean = True or False
True: n = 4 - no of rows
*
* *
* * *
* * * *
False: n = 4  - no of rows
* * * *
* * *
* *
*
'''

# --------------------- Lets Starts ----------------------- #
print('This is Star Printer Program - You have to enter no. of row only & program will,'
      'Print the series of the Star')
print()
print('For ascending order pattern type "True" , For descending order pattern type "False"')
print()
user = int(input('Enter no of rows: '))
ad = bool((input('Enter Pattern Type: ').upper()))


if ad == True:
    for i in range(user):
        print('* ' * (i + 1))
elif ad == False:
    for i in range(user, 0, -1):
        print('* ' * i)
