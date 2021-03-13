# --------------------------- Open File ------------------------------------- #
f = open("Sherry.txt")  # f is use as a pointer for this file to handle this file
content = f.read()  # This variable is for accessing the content
print(content)  # Now print the content

f.close()


f = open("Sherry.txt")
content2 = f.read(25)  # Jitna words read karna ha otna numbers likh sakta ha
print(content2)

f.close()   # Remember after opening file you should have to close the file also

# -------------------------- Iterating on File ------------------ #
# We can also iterate content of File
s = open("Sherry.txt")
for line in s:
    print(line, end='')
s.close()

# ------------------ Readline ------------------ #
# we can also use readline function to read line by line content of a file
print()
b = open('Sherry.txt')
print(b.readline())  # jitni bar readline func chalai ga otni lines print hogi
b.close()


# ---------------------- Readlines ------------------- #
c = open('Sherry.txt')
print(c.readlines())  # readlines func will read lines & return list
c.close()