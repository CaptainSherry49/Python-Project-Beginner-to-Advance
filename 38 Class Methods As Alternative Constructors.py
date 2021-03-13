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

    # ---------------------- Class method as Alternative ------------------- #
    @classmethod
    def from_dash(cls, string):
        # params = string.split('-')
        # return cls(params[0], params[1], params[2])
        # opar wali do lines ko 1 line ma kasa likha
        return cls(*string.split('-'))


hamza = School('Hamza Rehman', 11, 'Pre-Engineering')
zulqarnain = School('Zulfiqarnian Haider', 11, 'Pre-Medical')
sherry = School.from_dash('Sheheryar Ahmed Khan-University-Data Science')
'''
Ab ham na 'sherry' instance ko aik Alternative constructor ki tarha istimal kar diya ab ham is ma sirf aik string pass
karain ga baki k process ya given method k zariya kara ga
'''



print(sherry.Faculty)