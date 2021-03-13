# ------------------- Writing in File ----------------- #
f = open('Sherry.txt', 'w')
a = f.write('This Content will replace the previous one')  # .write func will replace the previous text
f.close()

# -------------------- Appending in File ------------ #
f = open('Sherry.txt', 'a')
b = f.write('\nThis text will append in the end of previous text')
print(b)  # This code will print the number of character of the content in our file
f.close()


# --------------------------- Read & write both -------------- #
'''
f = open('Sherry.txt', 'r+')
print(f.read())
f.write("Thank you")
'''