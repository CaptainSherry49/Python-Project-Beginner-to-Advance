# --------------------------------- Access Specifiers --------------------- #
'''
                                    Public Access Modifier:

The members of a class that are declared public are easily accessible from any part of the program.
All data members and member functions of a class are public by default.

 # public data members
           self.geekName = name
           self.geekAge = age


                                    Protected Access Modifier:

The members of a class that are declared protected are only accessible to a class derived from it.
Data members of a class are declared protected by adding a single underscore ‘_’ symbol before the data member of that class.

# protected data members
     _name = None
     _roll = None
     _branch = None


                                    Private Access Modifier:

The members of a class that are declared private are accessible within the class only, private access modifier is
the most secure access modifier. Data members of a class are declared private by adding a double
underscore ‘__’ symbol before the data member of that class.

# private members
     __name = None
     __roll = None
     __branch = None
'''