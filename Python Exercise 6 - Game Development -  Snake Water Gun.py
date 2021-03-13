# ----------------------------------- Snake, Water, Gun Game ---------------------------- #
'''
The snake drinks the water, the gun shoots the snake, and gun has no effect on water.
'''


# ----------------------------- Lets Starts ------------------------- #
import random

print('This is Snake, Water, Gun game . The snake drinks the water, the gun shoots the snake, and gun has no effect on water.\n')
print('You have only 10 Chances to Play this game, when ever you win you will gain 10 point in the end which player have most point he will be the winner of the game.\n')
s = 'Snake'
w = 'Water'
g = 'Gun'

players = [s, w, g]


i = 1
pc_score = 0
user_score = 0
chances_left = 10

while i <= 10:
    user = input('Enter : "S" of Snake, "W" for Water, & "G" for Gun \n').upper()
    print()
    pc = random.choice(players)
    if user == 'S' and pc == w:
        print(f'10 Points for you :) because you choose "{user}" & pc choose {pc}')
        print()
        user_score += 10
        print(f'Chances left {chances_left - i}')
        print()
    elif user == 'S' and pc == g:
        print(f'10 Points for Pc :( because you choose "{user}" & pc choose {pc}')
        print()
        pc_score += 10
        print(f'Chances left {chances_left - i}')
        print()
    elif user == 'S' and pc == s:
        print('Tie')
        print(f'You choose "{user}" & pc choose {pc}')
        print()
        print(f'Chances left {chances_left - i}')
        print()
    elif user == 'W' and pc == s:
        print(f'10 Points for Pc :( because you choose "{user}" & pc choose {pc}')
        print()
        pc_score += 10
        print(f'Chances left {chances_left - i}')
        print()
    elif user == 'W' and pc == g:
        print(f'10 Points for you :) because you choose "{user}" & pc choose {pc}')
        print()
        user_score += 10
        print(f'Chances left {chances_left - i}')
        print()
    elif user == 'W' and pc == w:
        print('Tie')
        print(f'You choose "{user}" & pc choose {pc}')
        print()
        print(f'Chances left {chances_left - i}')
        print()
    elif user == 'G' and pc == s:
        print(f'10 Points for you :) because you choose "{user}" & pc choose {pc}')
        print()
        user_score += 10
        print(f'Chances left {chances_left - i}')
        print()
    elif user == 'G' and pc == w:
        print(f'10 Points for Pc :( because you choose "{user}" & pc choose {pc}')
        print()
        pc_score += 10
        print(f'Chances left {chances_left - i}')
        print()
    elif user == 'G' and pc == g:
        print('Tie')
        print(f'You choose "{user}" & pc choose {pc}')
        print()
        print(f'Chances left {chances_left - i}')
        print()
    else:
        print('Invalid Input')
        break
    i += 1

# ----------------------------- Scores Program ---------------------- #
print()
print('#---------------------------- Result Time -------------------------- #')
print()
if user_score > pc_score:
    print(f'You Won! Your Score is {user_score} & Pc Score is {pc_score}')
elif user_score == pc_score:
    print(f'Game Tie! Your Score is {user_score} & Pc Score is {pc_score}')
else:
    print(f'Pc Won! Pc Score is {pc_score} & Your Score is {user_score}')