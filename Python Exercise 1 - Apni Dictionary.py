# Exercise-1
'''
Create a Dictionary and take input from the user and return the meaning of
the word from the dictionary
'''


# ---------------------- Lets Starts ------------------------ #

our_Dict = {'Agree': 'متفق', 'Cattle': 'مویشی', 'Swear': 'قسم کھانا',
            'Time': 'وقت', 'Title': 'عنوان', 'Precaution': 'احتیاط',
            'Executable': 'قابل عمل', 'Abandon': 'ترک کرنا', 'Cyclone': 'طوفان',
            'Gesture': 'اشارہ'}

print(f'These are the word in our Dictionary {our_Dict.keys()}')
user = input('Enter the Word to get the meaning:  ')
print(f'{user} meaning is {our_Dict[user]}')