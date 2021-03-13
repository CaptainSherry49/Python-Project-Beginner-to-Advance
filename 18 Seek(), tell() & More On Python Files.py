# ------------------------ tell Function -------------------- #
f  = open("Sherry.txt")
print(f.tell())
print(f.readline())
print(f.tell())
f.seek(12)  # seek func will reset the file pointer 
print(f.readline())
print(f.tell())  # tell func return the number that where is file pointer located now
f.close()