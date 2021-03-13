# ------------------------  Guess The Number ---------------- #
import random


print('Welcome to the Guess Game - You have to Guess the Hidden number')
print('You have only 10 Chances to Guess the Number, SO lets Start (Good Luck)')

hidden_num = random.randint(1, 100)

no_of_chances = 1
left_chance = 10

while no_of_chances <= 10:
    print()
    user = int(input('Enter to Guess: '))
    print()
    if user == hidden_num:
        print('Congratulation You won! You Guess the Right number :)')
        print()
        print(f'You Guess the Hidden Number in {10-(left_chance-no_of_chances)} Attempts')
        break
    elif user < hidden_num:
        print('NO Please Guess the Higher Number than that - ')
        print(f'Chances Left = {left_chance-no_of_chances}')
    elif user > hidden_num:
        print('NO Please Guess the lower Number than that - ')
        print(f'Chances left = {left_chance-no_of_chances}')
    no_of_chances += 1
else:
    print()
    print('Sorry ! But You are Fail to Guess the Number :( ')
