"""
Iterable -   __iter__() or __getitem__()
Iterator -   __next__()
Iteration -


Simply speaking, a generator is a function that returns an object (iterator) which we can iterate over
(one value at a time).
"""


def gen(n):
    for i in range(n):
        yield i


g = gen(7)
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
# print(g.__next__())   # This will give us a error of StopIteration

# String Object is iterable but innteger is not
name = 'Sherry'
itr = iter(name)
print(itr.__next__())
print(itr.__next__())