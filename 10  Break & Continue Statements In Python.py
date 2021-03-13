# ------------------------ Break And Continue ----------------------- #

'''
Break = STop the Loop and Exit the Program
Continue = The continue keyword is used to end the current iteration in a for loop
(or a while loop), and continues to the next iteration.
'''


i = 1

while (True):
    print(i,  end=' ')
    if i == 49:
        break
    i += 1


# ------------------------ Quiz --------------------- #


while True:
    user = int(input('Enter number: '))
    if user <= 100:
        print('Try Again')
        continue
    else:
        print(f'Finally you Entered {user}')
        break