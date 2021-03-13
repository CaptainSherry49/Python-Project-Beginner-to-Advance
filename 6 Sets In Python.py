# -------------------- Sets ----------------------- #

# A set is a collection which is both unordered and unindexed.
# Sets are written with curly brackets.
# Sets has unique collection of value


my_set = {12, 43, 13, 123, 42}  # Create's a set

print(type(my_set))
print(my_set)


# ------------------ Set Methods ---------------- #

my_set.add(999)  # Adds an element to the set
print(my_set)

set_2 = my_set.copy()  # Returns a copy of the set
print(set_2)

set_2.pop()  # Removes an element from the set
print(set_2)

set_2.remove(43)  # Removes the specified element
print(set_2)

set_2.clear()  # Removes all the elements from the set
print(set_2)


#  There are many more method of set which is related to math like 'Union', 'Intersection' , etc....
