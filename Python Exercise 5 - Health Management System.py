# ----------------- Health Management System -------------------- #
'''
3 Clients = Shayan, Ariyan & Umair.
Files = Total 6 Files.
Writes a func that when executed ask input that want to log or retrieve & then what
to lock & retrieve food or exercise & take another input  client's name & store them into
files.
Time func = (def getdate():
                 import datetime
                 return datetime.datetime.now() )
'''

# ------------------------------- Lets Starts ------------------------ #

# -------------------------- time function ------------------------- #


def getdate():
    import datetime
    return datetime.datetime.now()

# ------------------------------- Lock FUnction ----------------------- #


def log_shayan_food():
    with open('ShayanFood.txt', 'a') as f:
        log = input('Enter Food: ')
        f.write(f'At {getdate()} Shayan Eat  = {log}\n')
        print('Successfully write')


def log_shayan_exercise():
    with open('ShayanExercise.txt', 'a') as f:
        log = input('Enter Exercise: ')
        f.write(f'At {getdate()} Shayan Done  = {log}\n')
        print('Successfully write')


def log_ariyan_food():
    with open('AriyanFood.txt', 'a') as f:
        log = input('Enter Food: ')
        f.write(f'At {getdate()} Ariyan Eat = {log}\n')
        print('Successfully write')


def log_ariyan_exercise():
    with open('AriyanExercise.txt', 'a') as f:
        log = input('Enter Exercise: ')
        f.write(f'At {getdate()}  Ariyan Done = {log}\n')
        print('Successfully write')


def log_umair_food():
    with open('UmairFood.txt', 'a') as f:
        log = input('Enter Food: ')
        f.write(f'At {getdate()} Umair Eat  = {log}\n')
        print('Successfully write')


def log_umair_exercise():
    with open('UmairExercise.txt', 'a') as f:
        log = input('Enter Exercise: ')
        f.write(f'At {getdate()} Umair Done = {log}\n')
        print('Successfully write')


# -------------------------------- Retrieve Functions --------------------- #
def retrieve_shayan_food():
    with open('ShayanFood.txt') as f:
        print(f.read())


def retrieve_shayan_exercise():
    with open('ShayanExercise.txt') as f:
        print(f.read())


def retrieve_ariyan_food():
    with open('AriyanFood.txt') as f:
        print(f.read())


def retrieve_ariyan_exercise():
    with open('AriyanExercise.txt') as f:
        print(f.read())


def retrieve_umair_food():
    with open('UmairFood.txt') as f:
        print(f.read())


def retrieve_umair_exercise():
    with open('UmairExercise.txt') as f:
        print(f.read())


# --------------------------------------- Again Function ------------------------ #
def yes_no():
    again = input("Do you wanna try again - Y or N  ?  ").upper()
    print()
    if again == "Y":
        health_management_system()
    else:
        pass


# ------------------- Main Function ---------------------------#
print('Clients = Shayan, Ariyan, Umair')
print()


def health_management_system():
    print('This is Health Management System, You can log or retrieve any of clients file')
    print()
    log_retrieve = input('What do you want to do Log or Retrieve, For log enter "L" and For retrieve enter "R" : ').upper()
    print()
    clients_name = int(input('For which client you are doing this, press 1 for Shayan, 2 for Ariyan, 3 for Umair:  '))
    print()
    food_exercise = input('For Food press "a", For Exercise "b" :  ').upper()
    print()
    if log_retrieve == "L" and clients_name == 1 and food_exercise == "A":
        log_shayan_food()
        print()
        yes_no()

    elif log_retrieve == "L" and clients_name == 1 and food_exercise == "B":
        log_shayan_exercise()
        print()
        yes_no()

    elif log_retrieve == "R" and clients_name == 1 and food_exercise == "A":
        retrieve_shayan_food()
        print()
        yes_no()

    elif log_retrieve == "R" and clients_name == 1 and food_exercise == "B":
        retrieve_shayan_exercise()
        print()
        yes_no()

    elif log_retrieve == "L" and clients_name == 2 and food_exercise == "A":
        log_ariyan_food()
        print()
        yes_no()

    elif log_retrieve == "L" and clients_name == 2 and food_exercise == "B":
        log_ariyan_exercise()
        print()
        yes_no()

    elif log_retrieve == "R" and clients_name == 2 and food_exercise == "A":
        retrieve_ariyan_food()
        print()
        yes_no()

    elif log_retrieve == "R" and clients_name == 2 and food_exercise == "B":
        retrieve_ariyan_exercise()
        print()
        yes_no()

    elif log_retrieve == "L" and clients_name == 3 and food_exercise == "A":
        log_umair_food()
        print()
        yes_no()

    elif log_retrieve == "L" and clients_name == 3 and food_exercise == "B":
        log_umair_exercise()
        print()
        yes_no()

    elif log_retrieve == "R" and clients_name == 3 and food_exercise == "A":
        retrieve_umair_food()
        print()
        yes_no()

    elif log_retrieve == "R" and clients_name == 3 and food_exercise == "B":
        retrieve_umair_exercise()
        print()
        yes_no()
    else:
        print('Enter valid value')


health_management_system()
