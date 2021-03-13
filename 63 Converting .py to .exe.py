"""
Step 1:

Install the library pyinstaller.
Type below command in the command prompt.

pip install pyinstaller

Step 2:

Go into the directory where your ‘.py’ file is located.

Step 3:

Press shift⇧ button and simultaneously right click at the same location. You will get below box.

Step 4:

Click on ‘Open PowerShell window here’.

Step 5:

type :  pyinstaller --onefile  'filename.py'

Step 6:

After typing the command ‘Hit the Enter’.
It will take some time to finish the process depending on the size of the file and how big is your project.

Step 7:

See the directory it should look like this:

Convert-.py-to.exe

‘build’ folder and ‘filename.spec’ is of no use. You can delete these if you want, it will not affect your ‘.exe’ file.

Step 8:

Open ‘dist’ folder above. Here you will get your ‘.exe’ file.

"""

num = int(input('Enter a number: '))
for i in range(1, num + 1):
    print(i)
