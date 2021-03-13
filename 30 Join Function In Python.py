# ------------------------------ Join Function --------------------------- #
name_list = ['Warner', 'Finch', 'Smith', 'Maxwell', 'Pain', 'Starc', 'Cummins']


# situation is that we have to add 'and' in the end of every list item, we can done this by using for loop but this is not the ideal way
# --------------------------- apni example ---------------- #

# for item in name_list:
#     print(f'{item} and ', end=' ')

# -------------- Join -------------- #

a = ' and '.join(name_list)
print(a)


# --------------------- Example to understand the join method little bit more ------------------- #

a = 'hi'
b = 'how'
c = 'are'
d = 'you'
abcd = [a, b, c, d]
x = ', '.join(abcd)
print(x)