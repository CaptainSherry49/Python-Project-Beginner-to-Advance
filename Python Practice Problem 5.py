# --------------------- Palindromify the List --------------------- #

"""
The task you have to perform is “Palindromify the List.” This task consists of a total of 10 points to evaluate your
performance.

The task is very similar to the previous one . Tutorial #109 ( Python Problem 4)

Problem Statement:-
You are given a list that contains some numbers. You have to print a list of next palindromes only if the number is
greater than 10; otherwise, you will print that number.

Input:
[1, 6, 87, 43]

Output:
[1, 6, 88, 44]
"""


print("------------------  This is the Program for Next Palindrome List ('Palindromify the List') -------------")

print("\nYou have to provide a list of numbers and in return we will modify that list with the next palindrome for each"
      " number, (if the number is greater than 10).\n")


try:
    how_many_input = int(input("\n* How many numbers is in your list ? "))
except ValueError:
    print("- Enter only integer.")

else:

    print()
    print(f"* Enter that {how_many_input} numbers one by one:")

    # Taking Input From user and then store it into empty list
    numbers = []

    for i in range(1, how_many_input + 1):
        try:
            print()
            user_inp = int(input(f"{i} - Enter Number for Palindrome:    "))
        except ValueError:
            print(f"\n- Enter only integers. This will not be Taken as number.")
        else:
            numbers.append(user_inp)

    # Code for Finding Next Palindrome
    palindrome_num = []

    for i in numbers:
        z = i + i
        for x in range(i, z + 1):
            if x > 10:
                x = x+1
                my_str = str(x)
                reverse_str = my_str[::-1]
                if my_str == reverse_str:
                    palindrome_num.append(x)
                    x += 1
                    break
            else:
                palindrome_num.append(x)
                break

# ----------------- Printing the given list and modify list ---------------- #

    print(f"\n* The List you provide us is {numbers}.\n\n* After modifying the given list, the next palindrome number "
          f"for each list item is:  {palindrome_num}")

# ------------------ Done ----------- #
