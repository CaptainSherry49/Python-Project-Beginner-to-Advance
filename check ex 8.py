import  os
path = 'J:\Code With Harry\Python using Pycharm\Python Projects\This'

# lst = ['hamza.txt', 'zulqarnain.txt', 'furkan.txt']
list_of_directories = os.listdir(path)

file_item = []
with open("This/don't touch.txt") as f:
    for item in f:
        item = item.rstrip()
        file_item.append(item)

# print(file_item)
for files in list_of_directories:
    if files not in file_item and files.endswith('.txt'):
        print(files.capitalize())
    else:
        pass
