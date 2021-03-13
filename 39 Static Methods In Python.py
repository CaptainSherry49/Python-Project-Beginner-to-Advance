class School:
    no_of_leaves = 8

    def __init__(self, name, standard, faculty):  # __init__ is a constructor which takes arguments of class using def
        self.Name = name
        self.Standard = standard
        self.Faculty = faculty

    def printdetails(self):  # class method
        return f'Name is {self.Name}. Standard is {self.Standard} and Faculty is {self.Faculty}. '

    @classmethod  # class method sirf class k instance variables ko access kar sakta ha
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves
# class method is liya use kiya taka ya class ko as a input la na k self ko

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split('-'))

    # ------------------------- Static Method --------------------- #

    @staticmethod
    def simple_func(string):
        return f'{string} This is Simple Function, for this simple func we use @staticmethod'
    # @staticmethod Simple func ko class k indar baghair kisi 'self' or 'cls' k use karna k liya use karta ha


hamza = School('Hamza Rehman', 11, 'Pre-Engineering')
zulqarnain = School('Zulfiqarnian Haider', 11, 'Pre-Medical')
sherry = School.from_dash('Sheheryar Ahmed Khan-University-Data Science')

print(School.simple_func('Sherry'))