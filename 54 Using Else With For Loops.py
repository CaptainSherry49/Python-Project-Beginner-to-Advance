meal = ['bread', 'vegetable', 'rice']

for item in meal:
    print(item)
else:
    print('This will print when for loop is ended properly')

# --------------------------- Remember -------------------- #
'''
if there is a break statement in for loop our else statement will not br executed
'''

# ------------------- Where we can use ------------- #
user = input('What you want to eat: ').lower()
for item in meal:
    if item == user:
        print(f'Take your {user}.')
        break
else:
    print(f'Sorry sir your {user} was not found. ')
