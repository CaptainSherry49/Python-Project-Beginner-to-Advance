# ----------------------- Your Age in 2090 --------------------- #
"""
The task you have to perform is “Your Age In 2090”. This task consists of a total of 10 points to evaluate your
performance.

Problem Statement:-
Take age or year of birth as an input from the user. Store the input in one variable. Your program should detect whether
the entered input is age or year of birth and tell the user when they will turn 100 years old. (5 points).


Here are a few instructions that you must have to follow:

Do not use any type of modules like DateTime or date utils. (-5 points)
Users can optionally provide a year, and your program must tell their age in that particular year. (3points)


Your code should handle all sort of errors like:                       (2 points)

You are not yet born
You seem to be the oldest person alive
You can also handle any other errors, if possible!

"""

# --------------- let's Starts -------------- #
print("This is a Program ('Your age in 2090'). This program will detect whenever you will be turn to 100 age, and if"
      " you want to check your age in any particular year you can also check that (Optionally).\n")


class AgeDetector:
    def __init__(self, user_inp, length_of_user_inp):
        self.user_inp = user_inp
        self.user_inp_length = length_of_user_inp

    def detect_age_or_year(self):
        """This function will detect the user input is that input is user's Age or Year of Birth"""

        if self.user_inp_length == 2:
            print("The input which user provide is his/her 'Age'. ")
        elif self.user_inp_length == 4 and self.user_inp > 1920 and self.user_inp <= 2021:
            print("The input which user provide is his/her 'Year of Birth'. ")
        else:
            print(f"you age {user_input} seems to be wrong...")

    def calculate_100_for_age(self):
        """This program will calculate the year for Age that when will user become 100"""

        user_age = self.user_inp
        print(f"You will be turn to age 100 in the year {2021 + (100 - user_age)}")

    def calculate_100_for_birth_year(self):
        """This program will calculate the year for Birth year that when will user become 100"""

        user_year_of_birth = self.user_inp
        finding_user_age = 2021 - user_year_of_birth
        print(f"You will be turn to age 100 in the year {2021 + (100 - finding_user_age)}")

    def age_in_specific_year(self):
        """This program will check user age in given specific year"""
        future_age = int(input("In which year you want to check your age will be ?  "))
        if self.user_inp_length == 2:
            print(f"You will be {(future_age - 2021) + self.user_inp} year old in {future_age}")
        elif self.user_inp_length == 4:
            finding_user_age = 2021 - self.user_inp
            print(f"You will be {(future_age - 2021) + finding_user_age} year old in {future_age}")

#


user_input = int(input("Enter your Age or Year of Birth:  "))
length = len(str(user_input))

sherry = AgeDetector(user_input, length)


# This program will detect that user input is 'Age' or 'Year'

print("\nDetecting user Input....")
sherry.detect_age_or_year()


# if your age in 'Age' use this program:

print("\nCalculating 100th Age for User Age...\n")
sherry.calculate_100_for_age()
print()


# if your age in 'year' use this program:

print("\nCalculating 100th Age for User Birth year...\n")
sherry.calculate_100_for_birth_year()
print()


# if you want to check your age in specific year
#
print()
sherry.age_in_specific_year()
