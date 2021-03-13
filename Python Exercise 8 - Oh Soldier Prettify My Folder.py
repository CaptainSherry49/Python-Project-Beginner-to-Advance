# ------------------------ Exercise 8: Oh Soldier Prettify My Folder ------------ #
"""
Create a function which takes 3 inputs - 'path' - 'file' - 'format'
given path ma jitni bhi files ha on  k first letter ko capital karna ha or jo name
file ma given ha osa chor k or ya process sirf txt files k sath karna ha, & jo format given ha os format ki sari
files ko name dena ha 1,2,3... kar k.
"""

# ---------------------- Lets Starts -------------- #
import os


def prettify_folder(path, file, frmt):
    file_item = []

    # Opening file for store file item in above empty list
    with open(file) as f:
        for item in f:
            item = item.rstrip()
            file_item.append(item)

    i = 1
    list_of_directories = os.listdir(path)

    #  For renaming files
    for files in list_of_directories:
        if files not in file_item and files.endswith('.txt'):
            os.rename(os.path.join(path, files), os.path.join(path, ''.join([files.capitalize()])))
        else:
            pass

    #  for renaming 'format' files name
    for jpg in list_of_directories:
        if jpg.endswith(frmt):
            os.rename(os.path.join(path, jpg), os.path.join(path, str(i) + '.jpg'))
            i += 1
        else:
            pass


Path = input("Enter Path name : ")
File = input('Enter File name: ')
Frmt = input('Enter Format: ')


prettify_folder(Path, File, Frmt)

# Done It ! :)
