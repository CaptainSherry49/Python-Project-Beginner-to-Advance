# ------------------- Operators Overloading ------------------ #
'''
Dunder or magic methods in Python are the methods having two prefix and suffix underscores in the method name.
Dunder here means “Double Under (Underscores)”. These are commonly used for operator overloading. ...
These methods are the reason we can add two strings with '+' operator without any explicit typecasting
'''


class Employee:
    leaves_allow_per_month = 4

    def __init__(self, name, age, role):
        self.Name = name
        self.Age = age
        self.Role = role

    def print_details(self):
        return f'Name is {self.Name}, Age is {self.Age} & Role is {self.Role}'

    def __add__(self, other):   # This is called Dunder Method
        return self.Age + other.Age


emp1 = Employee('Sheheryar Ahmed khan', 16, 'Learner')
emp2 = Employee('Mosh', 44, 'Programmer')

print(f'Age of Both Employee is {emp1 + emp2}')
