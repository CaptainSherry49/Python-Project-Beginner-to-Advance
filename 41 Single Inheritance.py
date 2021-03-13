# -------------------------- Inheritance ------------------- #
'''
Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class.
'''

# ----------------------- Inheritance Concept --------------- #
class School:
    no_of_leaves = 8

    def __init__(self, name, standard, faculty):
        self.Name = name
        self.Standard = standard
        self.Faculty = faculty

    def printdetails(self):
        return f'Name is {self.Name}. Standard is {self.Standard} and Faculty is {self.Faculty}. '

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split('-'))

    @staticmethod
    def simple_func(string):
        return f'{string} This is Simple Function, for this simple func we use @staticmethod'


# ------------------------ Single Inheritance --------------- #
class Student(School):

    def __init__(self, height, faculty, ide, *languages):
        self.Height = height
        self.Faculty = faculty
        self.Languages = languages
        self.IDE = ide

    def printprog(self):
        return f'The Programmer Name is {self.Name}. Standard is {self.Standard} and Faculty is {self.Faculty}. '


SHerry = School('Sheheryar', 14, 'AI')
Hamza = School('Hamza Rehman', 11, 'Learner')

zulqarnain = Student(5.4, 'Web-developer', 'Vs Code', 'Html', 'Css', 'Js')

print(zulqarnain.Languages)   # q k ya class inherite kar rahi ha School class sa to ya os k method bhi use karsakti ha
