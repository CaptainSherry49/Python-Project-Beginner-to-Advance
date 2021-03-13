# ---------------------------- The Next Palindrome  --------------------------------- #

"""
The task you have to perform is “The Next Palindrome.” This task consists of a total of 15 points to evaluate your
performance.

Problem Statement:-

A palindrome is a string that, when reversed, is equal to itself. Example of the palindrome includes:

676, 616, mom, 100001.

You have to take a number as an input from the user. You have to find the next palindrome corresponding to that number.
Your first input should be the number of test cases and then take all the cases as input from the user.

Input:
3

451

10

2133

Output:
Next palindrome for 451 is 454

Next palindrome for 10 is 11

Next palindrome for 2311 is 2222

These tasks will improve your logic making skills and logic is the basics of programming.
"""


print("------------------  This is the Program for Palindrome ('The Next Palindrome') -------------")

try:
    how_many_input = int(input("\nFor How many number you wanna check the next Palindrome:    "))
except ValueError:
    print("Enter only integer.")

else:

    print()
    print(f"So now You can find next palindrome for {how_many_input} numbers at a time, minimum number should be 1 and "
          f"maximum number should be 999:")

    # Taking Input From user and then store it into empty list
    numbers = []

    for i in range(1, how_many_input + 1):
        try:
            print()
            user_inp = int(input(f"{i} - Enter Number for Palindrome:    "))
        except ValueError:
            print(f"\nEnter only integers. This will not be Taken as number.")
        else:
            if 1 <= user_inp <= 999:
                numbers.append(user_inp)
            else:
                print(f"\nPlease Provide Numbers due the given condition. This '{user_inp}' will not be Taken as "
                      f"number.")

    # Code for Finding Next Palindrome
    palindrome_num = []

    for i in numbers:
        for x in range(i, 1002):
            x = x+1
            my_str = str(x)
            reverse_str = my_str[::-1]
            if my_str == reverse_str:
                palindrome_num.append(x)
                x += 1
                break
            else:
                pass

    # Printing palindrome numbers from List
    print()
    print('------------------- Next Palindrome -----------')
    print()
    y = 0
    for value in palindrome_num:
        print(f"\nThe Next Palindrome number for {numbers[y]} is {value}.")
        y += 1
