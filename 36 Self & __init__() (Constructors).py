'''
The constructor is a method that is called when an object is created.
This method is defined in the class and can be used to initialize basic variables.
If you create four objects, the class constructor is called four times.
'''

class School:
    no_of_leaves = 8

    # ------------------------------- Constructor ---------------------- #
    def __init__(self, name, standard, faculty):  # __init__ is a constructor which takes arguments of class using def
        self.Name = name
        self.Standard = standard
        self.Faculty = faculty

    def printdetails(self):  # class method
        return f'Name is {self.Name}. Standard is {self.Standard} and Faculty is {self.Faculty}. '


hamza = School('Hamza Rehman', 11, 'Pre-Engineering')
zulqarnain = School('Zulfiqarnian Haider', 11, 'Pre-Medical')

# ab muja har object k liya alag sa variable banana ki zaroorat nhi ha q k ma na class k indar init ka method use kar liya ha
# __init__ takes class's arguments, object bana k jo argument ham class ko provide karta ha wo __init__ handle karta ha

print(zulqarnain.Standard)
