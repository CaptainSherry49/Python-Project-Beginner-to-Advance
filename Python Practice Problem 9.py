import random
# ----------------------------- "Jumbled Funny Names" ---------------------- #

"""
The task you have to perform is “Jumbled Funny Names”. This task consists of a total of 20 points to evaluate your
performance.

Problem Statement:-

It's result day at school and not everyone is happy. You decided to make your friends laugh by jumbling their names to
come up with some funny names.

Your program should take the number of names and the names separated by space as input. Output should be funny names in
the same order.

Input:
Enter number of friends:

3

Enter the name of your 3 friends:

Rohan Das

Shubham Agarwal

Ritesh Arora

Output:

Ritesh Das

Shubham Arora

Rohan Agarwal
"""


# ---------------------- Let's Starts --------------------- #


# Function for jumbled first and last names
def jumbling_names(name_list):
    """This function will take names list as input and then jumbled the name first and last name and return them"""
    f_name = []
    l_name = []

    for name in name_list:
        separate = name.split(" ")
        f_name.append(separate[0])
        l_name.append(separate[1:])

    string = []
    for last in l_name:
        for j in last:
            string.append(j)

    print("\n\nAnd the Names are: \n")
    for funny_name in f_name:
        print(f"{funny_name} {random.choice(string)}")


# --------------------- Main Scenario ------------------------------ #
if __name__ == '__main__':
    print("------------------------- Jumbled Funny Names ----------------------")
    print()
    print('-----------------------------------------------------------------------------------------------------------')
    print("I know you all are in tension because of the result of your exams, here i come to entertain all of you by "
          "jumbling all of your name with each others, lets starts: ")
    print('-----------------------------------------------------------------------------------------------------------')

    try:
        num = int(input("\nEnter how many name you are jumbling:  "))
    except ValueError:
        print("Enter integers Only")
    else:
        names = []

        print(f"\nEnter the name of your {num} friends: \n")
        for i in range(1, num + 1):
            user_name = input(f"Enter name {i}:  ").title()
            names.append(user_name)

        jumbling_names(names)

# Finally Done !
