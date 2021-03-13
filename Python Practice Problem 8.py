import random
# ------------------------------------- "Rohan Das is a Fraud" ------------------- #

"""
The task you have to perform is “Fake Multiplication Tables”. This task consists of a total of 15 points to evaluate
your performance.

Problem Statement:-
 Rohan das is a fraud by nature. Rohan Das wrote a python function to print a multiplication table of a given number and
put one of the values (randomly generated) as wrong.

Rohan Das did this to fool his classmates and make them commit a mistake in a test. You cannot tolerate this!

So you decided to use your python skills to counter Rohan’s actions by writing a python program that validates Rohan’s
multiplication table.

Your function should be able to find out the wrong values in Rohan’s table and expose Rohan Das as a fraud.

Note: Rohan’s function returns a list of numbers like this

Rohan Das’s Function Input:
rohanMultiplication(6)

Rohan’s function returns this output:
[6, 12, 18, 26, …., 60]

You have to write a function isCorrect(table, number) and return the index where rohan’s function is wrong and print it
to the screen! If the table is correct, your function returns None
"""


# -------------------------- Let's Start ---------------------------- #


# --------------- Function of Rohan Das Fake Multiplication Table .

def rohan_fake_multiplication(number):
    """This function will take number as argument and return the list of table of that number, but 1 value in it will be
     wrong"""

    table = []
    wrong = random.randint(0, 9)
    for i in range(1, 11):
        value = number * i
        table.append(value)

    table[wrong] = table[wrong] + random.randint(0, 9)

    return table


# Calling Rohan Das Function
# print(rohan_fake_multiplication(6))


# ------------------ Function to counter Rohan Das Fraud .

def isCorrect(table, number):
    """This function will check that rohan function output is right or wrong"""
    for i in range(1, 11):
        if table[i-1] != number * i:
            return f"The Wrong Value in Rohan Das output is at the index of {i - 1}.\n\nDeclared Rohan Das is Fraud !"

    return None

# -------------------- Main Scenario ------------- #


if __name__ == '__main__':
    print('--------------------------- "Rohan Das is A Fraud" -----------------------')

    print("As i heard that Rohan Das wrote a Multiplication Table function which is returning a list of the table of "
          "that number but one of its value is wrong so i also write\n a function which will check Rohan Das function's"
          " if he is caught we will declared Rohan Das as Fraud.")

    print('\n------------------------------------------------------------')
    print("Rohan Das Function takes number as an Argument to print table of that number, my Function take Rohan's "
          "function as an first argument and then the number of the table.")
    print('--------------------------------------------------------------\n')

    try:
        num = int(input("Enter a number for Table:  "))
    except  ValueError:
        print("Enter Only Integers.")
    else:
        tab = rohan_fake_multiplication(num)

        print(f"Rohan's Output is: {tab}.\n\nAfter Sheheryar's Inspection"
              f" : {isCorrect(tab, num)}")

#  Finally Done !
