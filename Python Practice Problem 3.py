# ----------------- Foods and Calories ------------- #

"""
The task you have to perform is “Foods and Calories.” This task consists of a total of 15 points to evaluate your
performance.


Problem Statement:-

You visited a restaurant called CodeWithHarry, and the food items in that restaurant are sorted, based on their amount
of calories. You have to reserve this list of food items containing calories.


You have to use the following three methods to reserve a list:

* Inbuilt method of python
* List name [::-1] slicing trick
* Swap the first element with the last one and second element with second last one and so on like,
    [6 7 8 34 5] -> [5 34 8 7 6]


Input:
Take a list as an input from the user

[5, 4, 1]

Output:
[1, 4, 5]

[1, 4, 5]

[1, 4, 5]

All three methods give the same results!
"""

# ---------------- Let's Starts ------------------- #
restaurant_name = "Code With Sherry"

food_items = ['Papad', 'Phulka', 'Soup', 'Salad', 'Paratha']

food_items_calories = [45, 60, 75, 100, 150]

print(f"Welcome Sir this is our Restaurant '{restaurant_name}', we designed a calories chart for every food item:\n\t"
      f"Food items : {food_items} , Calories Chart : {food_items_calories}")


#  ---------------------  For reversing the list ------------- :

# ---------------  Method 1 ----------------- #:


def inbuilt_method():
    """This function take's list as an input and then reversed that list with .reverse method"""
    print()
    user_list1 = input("Sir provide your list here we will reverse your list with Method 1 (Inbuilt method):     ")\
        .title()
    print()
    if user_list1 == 'Calories Chart':
        user_list1 = food_items_calories
        print()
        print(f"The list you provide us is {user_list1}.")
        print()
        print('Reversing the List....')
        print()
        user_list1.reverse()
        print(f"Here is your reversed list with Method 1: {user_list1}")
    else:
        print("Please provide Correct list name.")


# --------------- Method 2 ------------------- #


def slicing_method():
    """This function take's list as an input and then reversed that list with slicing method"""

    print()
    user_list2 = input("Sir provide your list here we will reverse your list with Method 2 (Slicing Trick):     ")\
        .title()
    if user_list2 == 'Calories Chart':
        user_list2 = food_items_calories
        print()
        print(f"The list you provide us is {user_list2}.")
        print()
        print('Reversing the List....')
        print()
        reversed_list = user_list2[::-1]
        print(f"Here is your reversed list with Method 2: {reversed_list}")
    else:
        print("Please provide Correct list name.")


# --------------  Method 3 --------------- #


def swap_method():
    """This function take's list as an input and then reversed that list with swap method"""

    print()
    user_list3 = input("Sir provide your list here we will reverse your list with Method 3 (Swap Method):     ").title()
    if user_list3 == 'Calories Chart':
        user_list3 = food_items_calories
        print()
        print(f"The list you provide us is {user_list3}.")
        print()
        print('Reversing the List....')
        print()
        x = 0
        y = -1
        demo_list = user_list3[:]
        for i in user_list3:
            user_list3[y] = demo_list[x]
            demo_list.pop(x)
            y -= 1

        print(f"Here is your reversed list with Method 3: {user_list3}")
    else:
        print("Please provide Correct list name.")


# ---------------- ALL Method -------------- #

def all_method():
    """This method will reverse the given list with all method"""

    user_list4 = food_items_calories[:]
    print()
    user_list5 = input("Sir provide your list here we will reverse your list with Method 4 (All Method):     ").title()

    if user_list5 == 'Calories Chart':
        user_list5 = food_items_calories
        user_list5.reverse()
        print()
        print(f"Method 1 Output is : {user_list5}")
        print()

        reversed_list4 = user_list4[::-1]
        print(f"Method 2 Output is : {reversed_list4}")
        print()

        x = 0
        y = -1
        demo_list4 = user_list4[:]
        for i in user_list4:
            user_list4[y] = demo_list4[x]
            demo_list4.pop(x)
            y -= 1
        print(f"Method 3 Output is : {user_list4}")
    else:
        print("Enter Valid Input.")


# --------------- main ------------ #
print()
print('------------------- List Reversing Program ---------- ')
print()
print("Welcome to List reversing program: Give us your list as input and we will reverse that list with different "
      "method -")
print()
try:
    num_inp = int(input("For Inbuilt Method press 1 --- For Slicing Method press 2 ----- For Swap Method press 3 ---- "
                        "For all method press 4 ---- :  "))
except ValueError:
    print("Enter only Integer")
else:
    if num_inp == 1:
        inbuilt_method()
    elif num_inp == 2:
        slicing_method()
    elif num_inp == 3:
        swap_method()
    elif num_inp == 4:
        all_method()
    else:
        print("Invalid input.")


# Finally Done !
