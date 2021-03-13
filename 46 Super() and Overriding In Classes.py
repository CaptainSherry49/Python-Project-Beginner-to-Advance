# ------------------------------ Super() --------------------------- #
'''
The super() function is used to give access to methods and properties of a parent or sibling class.
The super() function returns an object that represents the parent class.
'''


class A:

    classvar1 = 'I am in Class A'

    def __init__(self):
        self.var1 = "I am in Class A's Constructor"
        self.classvar1 = 'Instance variable of Class A'   # This is instance variable
        self.special = 'special'

class B(A):
    classvar2 = 'I am in Class B'

    def __init__(self):
        super().__init__()  # Now this constructor can access all method and variable of parent class
        self.var1 = "I am in Class B's Constructor"
        self.classvar1 = 'Instance variable of Class B'   # This is instance variable


a = A()
b = B()

# print(b.classvar1)  # this will find instance var first in class B, if didn't found then in A Class otherwise it print class var
print(b.special, b.classvar1, b.var1)

'''
main thing is that if i want to use parent class attributes and methods with using child class constructor i have to 
write super().__init__() in child class constructor
'''