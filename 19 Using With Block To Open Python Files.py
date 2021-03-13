# ---------------------------- With Bock to OPen Files ------------------- #
with open('Sherry.txt') as f:  # after using ' with ' we don't have to close the file
    print(f.read())


# ------------------ Question of the Day -------------------- #
'''
After read the whole file using with block, if we open file again and trying to read that file,
is we are able to read that file (yes or no & why)
'''

# Answer
'''
Yes we can read it again because with block will close the file by itself .
'''