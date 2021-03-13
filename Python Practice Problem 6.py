import random
# -------------------- Guess the Number --------------------- #

"""
The task you have to perform is “Guess The number”. This task consists of a total of 10 points to evaluate your
performance.

 Problem Statement:-

Generate a random integer from a to b. You and your friend have to guess a number between two numbers a and b. a and b
are inputs taken from the user. Your friend is player 1 and plays first. He will have to keep choosing the number and
your program must tell whether the number is greater than the actual number or less than the actual number. Log the
number of trials it took your friend to arrive at the number. You play the same game and then the person with minimum
number of trials wins! Randomly generate a number after taking a and b as input and don’t show that to the user.

Input:
Enter the value of a

4

Enter the value of b

13

Output:
Player1 :

Please guess the number between 4 and 13

5

Wrong guess a greater number again

8

Wrong guess a smaller number again

6

Correct you took 3 trials to guess the number

Player 2:

Correct you took 7 trials to guess the number

Player 1 wins!
"""


# -------------------------- Let's Starts ------------------- #

print('------------------- Guess The Number ------------------')
print()
print("You have to input two numbers 'a' and 'b' and we will generate a random number between them (including both of "
      "them), you and your friend have to guess that number, the player with minimum numbers\nof attempts will be the "
      "winner .")
print()
print("-------------- Starting the Game .......\n")


# Creating empty list for storing both player's number of attempts
player1_attempts = []
player2_attempts = []


# ---------------------- Defining Function for guess --------------- #

# Function for Player 1 Guess :

def player1_guess():
    """This function will guess the number for player 1"""
    no_of_attempts = 1
    print('-------------------------------------------------')
    print(f"It's Player 1 turn's {player1} will guess first.")
    print('-------------------------------------------------')

    while True:
        print()
        try:
            guess_num = int(input("Guess the Number:    "))
        except ValueError:
            print("Enter only integer.")
            break
        else:
            if a <= guess_num <= b:
                if guess_num == random_number1:
                    print(f"You guess the right number {random_number1}, now wait until Player 2 guess the number.")
                    print(f"You took {no_of_attempts} attempts to guess the right number.")
                    player1_attempts.append(no_of_attempts)
                    break
                elif guess_num > random_number1:
                    print(f"Please guess less number than this...")
                else:
                    print(f"Please guess greater number than this..")
            else:
                print(f"Please Guess the number between {a} and {b}.")
            no_of_attempts += 1


# Function For Player 2 Guess:

def player2_guess():
    """This function will guess the number for player 2"""
    no_of_attempts = 1
    print('-------------------------------------------------------')
    print(f"It's Player 2 turn's {player2} will guess this time.")
    print('-------------------------------------------------------')

    while True:
        print()
        try:
            guess_num = int(input("Guess the Number:    "))
        except ValueError:
            print("Enter only integer.")
            break
        else:
            if a <= guess_num <= b:
                if guess_num == random_number2:
                    print(f"You guess the right number {random_number2}.")
                    print(f"You took {no_of_attempts} attempts to guess the right number.")
                    player2_attempts.append(no_of_attempts)
                    break
                elif guess_num > random_number2:
                    print(f"Please guess less number than this...")
                else:
                    print(f"Please guess greater number than this..")
            else:
                print(f"Please Guess the number between {a} and {b}.")
            no_of_attempts += 1

# ----------------------- Functions Ended ------------------- #


# ---------------- Taking inputs from user ------------ #
try:
    a = int(input("Enter number a:  "))
    b = int(input("Enter number b:  "))
except ValueError:
    print("Enter only integers.")
else:

    # Creating variables for storing random number for both players
    random_number1 = random.randint(a, b)
    random_number2 = random.randint(a, b)

    print()

    player1 = input("Enter the name for Player 1:   ").title()
    player2 = input("Enter the name for Player 2:   ").title()

    # Calling both Functions
    player1_guess()
    player2_guess()

    # Code for deciding the winner basis of minimum attempts
    if player1_attempts[0] < player2_attempts[0]:
        print()
        print('***************')
        print(f"{player1} wins ! {player1} took {player1_attempts} attempts. ")
        print('***************')

    elif player1_attempts[0] > player2_attempts[0]:
        print()
        print('***************')
        print(f"{player2} wins ! {player2} took {player2_attempts} attempts. ")
        print('***************')

    elif player1_attempts[0] == player2_attempts[0]:
        print()
        print(f"Game Tied ! because both of you guess the number in {player1_attempts} attempts.")
        print('***************')
