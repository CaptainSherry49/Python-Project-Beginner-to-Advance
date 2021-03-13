"""
Comprehensions in Python provide us with a short and concise way to construct new sequences
(such as lists, set, dictionary etc.) using sequences which have been already defined.
Python supports the following 4 types of comprehensions:

List Comprehensions
Dictionary Comprehensions
Set Comprehensions
Generator Comprehensions
"""
# ls = []
# for i in range(100):
#     if i % 3 == 0:
#         ls.append(i)
ls = [i for i in range(100) if i % 3 == 0]  # list comprehension
print(ls)


dict1 = {i: f'item {i}' for i in range(1, 100) if i % 10 == 0}  # Dictionary Comprehension
dict2 = {value: key for key, value in dict1.items()}  # reverse dict using Dict Comp
print(dict2)

