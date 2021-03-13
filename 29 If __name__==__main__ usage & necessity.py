# -------------------------- If __name__==__main__ Concept ------------------------------ #
import File1

File1.print_string('A, P, I')

'''
if we import any external file and use it's functions it will run our function but it will also run all the other 
execution which is done in that file , so to avoid this problem we are using ( __name__ == __main__)
'''

# jis file ko import kar raha hain os ma main use karna ha, yaha pa nhi karna ha
