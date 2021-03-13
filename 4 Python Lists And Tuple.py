# ------------------------ Lists ----------------------- #

# Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data.
# Lists are created using square brackets:


grocery = ['Potatoes', 'Surf', 'Apples', 'Carrot', 'Salt', 'coriander']  # String List
numbers = [12, 34, 56, 879, 90]  # Integers List
decimal = [3.4, 1.2, 7.8, 5.6, 9.0]  # Float List
mixture = ['Apples', 'Salt', 49, 10, 4.5, 7.0, True]  # Mix List

print(len(grocery))
print(grocery[5])  # Sixth Element
print(mixture[1:5])  # Second to 4th


# ------------------------------- List Methods ------------------------- #

print(grocery.index('Carrot'))  # Returns the index of the first element with the specified value

numbers.append(12)  # Adds an element at the end of the list
print(numbers)

print(numbers.count(12))  # Returns the number of elements with the specified value

decimal.sort()  # Sorts the list
print(decimal)

mixture.remove(True)  # Removes the item with the specified value
print(mixture)

mixture.insert(4, 'Sherry')  # Adds an element at the specified position
print(mixture)

numbers.reverse()  # Reverses the order of the list
print(numbers)

print(grocery.pop(2))  # Removes the element at the specified position
print(grocery)

decimal.clear()  # Removes all the elements from the list
print(decimal)

mixture.extend([':)',':('])  # Add the elements of a list (or any iterable), to the end of the current list
print(mixture)

num2 = numbers.copy()  # Returns a copy of the list
print(num2)



# ------------------------------------ Tuple ------------------------ #

# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.
#  Tuple is immutable - cannot change


tp = (2, 4, 5, 44, 328, 4)  # This is Tuple

print(type(tp))
print(tp)


# ---------------------------- Tuple Methods ------------------------ #

print(tp.count(4))  # Returns the number of elements with the specified value

print(tp.index(328))  # Returns the index of the first element with the specified value
