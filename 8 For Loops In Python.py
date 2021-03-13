# ------------------- For Loops --------------------------- #

'''
A for loop is used for iterating over a sequence (that is either a list,
a tuple, a dictionary, a set, or a string).
'''


list1 = ['Sherry', 'Carry', 'Harry', 'Marie']

for item in list1:
    print(item)


# ------------------------ Quiz --------------------------#
mix = [12,'Hi', 5, 'Here', 47, 9, 'Join']

for i in mix:
    if type(i) == int and i > 6:
        print(i)
    else:
        pass