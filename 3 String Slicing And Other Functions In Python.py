# ----------------------- String Slicing -------------- #

# In python indexes are starts from 0
mystr = 'Sherry want to become a Data Scientist'
print(mystr[5])  # This will access fifth letter of our string
print(mystr[0:7])  # Access letter from first alphabet to seventh
print(mystr[:5])  # From 0 to 4
print(mystr[8:])  # From 8 to the rest
print(mystr[:])  # 0 to the rest
print(mystr[27:-1])  # negative slicing
print(mystr[7:20:2])  # Now 1 letter will be skipped

# Remember:
#  In slicing first value is included but the second is excluded

# ------------ length ----------- #
print(len(mystr))  # This will print the length of our string


# ------------------------- String Method ------------------#

new = 'Cricket Fever'
print(new.capitalize())  # Capitalized first letter of  string
print(new.casefold())  # Converts string into lower case
print(new.count('c'))  # Returns the number of times a specified value occurs in a string
print(new.endswith('t'))  # Returns true if the string ends with the specified value
print(new.find('k'))  # Searches the string for a specified value and returns the position of where it was found
print(new.index('i'))  # Searches the string for a specified value and returns the position of where it was found
print(new.isalnum())  # Returns True if all characters in the string are alphanumeric
print(new.isalpha())  # Returns True if all characters in the string are in the alphabet
print(new.join('Hi'))  # Joins the elements of an iterable to the end of the string
print(new.lower())  # Converts a string into lower case
print(new.replace('k','-'))  # Returns a string where a specified value is replaced with a specified value
print(new.split())  # Splits the string at the specified separator, and returns a list
print(new.strip())  # Returns a trimmed version of the string
print(new.title())  # Converts the first character of each word to upper case
print(new.upper())  # Converts a string into upper case
