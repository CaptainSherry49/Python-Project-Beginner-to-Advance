# ------------------------ Pickle Module ------------------- #
"""
The Python pickle module is another way to serialize and deserialize objects in Python. It differs from the json module
in that it serializes objects in a binary format, which means the result is not human readable.
"""
import pickle

# Pickling
# cars = ['audi', 'tesla', 'roll-royce', 'bmw', 'jaguar']
# file = 'mycar.pkl'
#
# with open(file, 'wb') as f:  # wb == write binary
#     pickle.dump(cars, f)  # 1 = obj for packaging, 2 = file obj


# Reading pickle binary file
with open('mycar.pkl', 'rb') as f:  # rb == read binary
    content = pickle.load(f)
print(content)


"""
pickle.loads() = This function takes a byte string as argument.
pickle.load() = This function takes a  file-like object as argument.

This was the same analogy you can take from json.load() and json.loads()

"""
