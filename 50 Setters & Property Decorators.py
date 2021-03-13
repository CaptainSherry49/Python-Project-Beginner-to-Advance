# ------------------------- Setters & Property Decorators -------------------- #
class Employee:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def who_is_employee(self):
        return f'Employee name is {self.fname} {self.lname}'

    @property
    def email(self):
        return f'Email = {self.fname}.{self.lname}@gmail.com'
# ab hama is method to () ka sath run karna zaroori nhi ha

    @email.setter
    def email(self, string):
        names = string.split('@')[0]
        self.fnames = names.split('.')[0]
        self.lnames = names.split('.')[1]


sherry = Employee('Sheheryar', 'Ahmed Khan')
shayan = Employee('Shayan', 'Ahmed Khan')

sherry.fname = 'Tiger'
print(sherry.email)
sherry.email = 'alpha.Sherry10@gmail.com'
print(sherry.fname)


# ya half reh gaya kuch khas nhi laga or samaj nhi araha tha
