class School:
    no_of_leaves = 8

    def __init__(self, name, standard, faculty):  # __init__ is a constructor which takes arguments of class using def
        self.Name = name
        self.Standard = standard
        self.Faculty = faculty

    def printdetails(self):  # class method
        return f'Name is {self.Name}. Standard is {self.Standard} and Faculty is {self.Faculty}. '

    # -------------------------- Class Method ---------------------- #

    @classmethod  # class method sirf class k instance variables ko access kar sakta ha
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves
# class method is liya use kiya taka ya class ko as a input la na k self ko


hamza = School('Hamza Rehman', 11, 'Pre-Engineering')
zulqarnain = School('Zulfiqarnian Haider', 11, 'Pre-Medical')


School.change_leaves(14)
print(hamza.no_of_leaves)
