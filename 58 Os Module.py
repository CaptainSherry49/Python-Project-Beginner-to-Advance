import os

print(os.getcwd())  # get current working directory
os.chdir('C://')  # Change directory
print(os.listdir())   # list of all directory by default it take current path
os.mkdir('Folder 1')  # Make Directory this will make a new directory
os.makedirs('This/that')  # Make Directory with Sub-directory
os.rename('Sherry.txt', 'CSherry.txt')  # To rename file
print(os.environ.get('path'))  # To access environment variable
print(os.path.join('C://', 'CSherry.txt'))  # join both path and remove extra '/'
print(os.path.exists('C://'))  # return Boolean if file exist or not
print(os.path.isdir('C://'))
print(os.path.isfile('C://'))
