# -------------------------- Abstract Base Class --------------------- #
from abc import ABC, abstractmethod
# @abstractmethod ko import karna ka liya ABC module ko import karna lazmi ha


class Shape(ABC):
    @abstractmethod
    def print_area(self):
        return 0
# ya abstract method ha ab jo class is class sa inherit hogi osa lazman aik print_area name ka method banana hoga


class Rectangle(Shape):
    sides = 4

    def __init__(self):
        self.length = 6
        self.breadth = 7

    def print_area(self):
        return self.length * self.breadth
# agar ham ya print_area method nhi banata to hama error show hoga


shape1 = Rectangle()
print(shape1.breadth)
print(shape1.print_area())

# ------------------- Remember --------------------- #
'''
Ham abstract base class k object nhi bana sakta, is file ma hamara pas shape aik abs class ha to ham os ka object nhi
bana sakta
'''