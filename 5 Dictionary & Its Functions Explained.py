# ----------------------------------- Dictionary ---------------------- #

# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is unordered, changeable and does not allow duplicates.
# Dictionaries are written with curly brackets, and have keys and values:


d1 = {'Things': 'Chezain', 'Above': 'Opar', 'Pair': 'Jora', 'Think': 'Sochna', 'Covid':'Coronavirus', 'Disease':'bemari'}

print(d1)
print(d1['Above'])  # Access Element

d1['Abuse'] = 'Galiyan'  # Adding new item in Dictionary
print(d1)


# ----------------------------- Dictionary Methods -------------------------- #

copyd1 = d1.copy()  # Returns a copy of the dictionary
print(copyd1)

print(d1.get('Covid'))  # Returns the value of the specified key

print(d1.items())  # Returns a list containing a tuple for each key value pair

print(d1.keys())  # Returns a list containing the dictionary's keys

print(d1.values())  # Returns a list containing the dictionary's Values

print(d1.pop('Disease'))  # Removes the element with the specified key
print(d1)

d1.update({'Stare':'Ghoorna'})  # Updates the dictionary with the specified key-value pairs
print(d1)

d1.popitem()  # Removes the last inserted key-value pair
print(d1)

print(d1.setdefault('Things','saman'))  # Returns the value of the specified key. If the key does not exist: insert the key, with the specified value

d1.clear()  # Removes all the elements from the dictionary
print(d1)
