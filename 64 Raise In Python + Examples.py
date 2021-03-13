# ------------------------------- Raise --------------- #
"""
The raise keyword is used to raise an exception.

You can define what kind of error to raise, and the text to print to the user.
"""
#
a = input("Enter Your Name: ")

if a.isnumeric():
    raise Exception('Numbers are not allowed !')

print(f'Hello {a} ')

# The code which is taking lot of time
# -------------------------------------------------------------------------------- #
b = int(input("How much do you earn: "))

if b == 0:
    raise ZeroDivisionError


# ---------------------             ------------------------------#
A = 2  # Remove this a when you are checking below code

c = input("Enter your name: ")
try:
    A
except Exception as e:
    if c == "Sherry":
        raise ValueError("Sherry is banned")

    print("Exception Handled")
