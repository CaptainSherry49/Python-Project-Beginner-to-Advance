class Employee:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def who_is_employee(self):
        return f'Employee name is {self.fname} {self.lname}'

    def email(self):
        return f'Email = {self.fname}.{self.lname}@gmail.com'


sherry = Employee('Sheheryar', 'Ahmed Khan')
shayan = Employee('Shayan', 'Ahmed Khan')

# print(sherry.email())

# --------------------- Object Introspection -------------- #
'''
In programming, introspection is the ability to determine the type of an object at runtime. It is one of Python's 
strengths. Everything in Python is an object and we can examine those objects. Python ships with a few built-in
functions and modules to help us.
'''
print(type(shayan))  # this will return type
print(id(shayan))  # this will return id
print(dir(shayan))  # this will return all methods

