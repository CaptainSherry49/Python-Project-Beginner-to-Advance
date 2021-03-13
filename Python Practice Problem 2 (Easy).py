# -------------------- Divide the Apples --------------- #

"""
The task you have to perform is “Divide the Apples.” This task consists of a total of 10 points to evaluate your
performance.


Problem Statement:-
Harry Potter has got the “n” number of apples. Harry has some students among whom he wants to distribute the apples.
These “n” number of apples is provided to harry by his friends, and he can request for few more or few less apples.

You need to print whether a number is in range mn to mx, is a divisor of “n” or not.


Input:

Take input n, mn, and mx from the user.

Output:
Print whether the numbers between mn and mx are divisor of “n” or not.
If mn=mx, show that this is not a range, and mn is equal to mx. Show the result for that number.


Example:
If n is 20 and mn=2 and mx=5

2 is a divisor of 20

3 is not a divisor of 20

…

5 is a divisor of 20

"""

try:
    number_of_apples = int(input("Enter the number of apple Harry has got:  "))
    print()

except ValueError:
    print("\nYour input seems to be wrong Please check your input again.")

else:

    if number_of_apples < 2:
        print("please provide number of apples greater than or almost 2")
    elif number_of_apples > 200:
        print("Please provide number of apples less than or equal to 200")
    else:

        try:
            minimum = int(input("Enter the Minimum range of Student:    "))
            print()

            maximum = int(input("Enter the maximum range of Student:    "))
            print()

        except ValueError:
            print("\nYou input seems to be wrong please check your input again..")

        else:
            # ----------- main ----------- #
            print()
            print("Program is executing ....")
            print()
            print()

            if minimum == maximum:
                print("This is not a range.")
            elif minimum > number_of_apples or maximum > number_of_apples:
                print("You can't provide minimum or maximum range greater than number of apples.")
            elif minimum < 1:
                print("You can't provide a range less than 1 .")
            elif maximum < minimum:
                print("You can't provide maximum range less than minimum")
            else:
                for apples in range(minimum, maximum + 1):
                    if number_of_apples % apples != 0:
                        print(f"{apples} is not a divisor of {number_of_apples}")
                    else:
                        print(f"{apples} is a divisor of {number_of_apples}")
