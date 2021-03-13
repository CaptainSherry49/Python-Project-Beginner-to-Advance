class Employee:
    team = 'Team Alpha'  # this is class variable, any object of this class can access this variable
    pass


sherry = Employee()
alie = Employee()

sherry.name = 'Sheheryar Ahmed khan'   # That's all are the objects own instance variables
sherry.id = 126719
sherry.std = 'Captain'

alie.name = 'Alie'
alie.id = 337274
alie.std = 'V.Captain'

print(f'Sherry id is {sherry.id}\nAlie standard is {alie.std}\nAnd both have team = {sherry.team}')
print()
print(sherry.__dict__)  # This will return the dictionary in which object sherry's all instance in it