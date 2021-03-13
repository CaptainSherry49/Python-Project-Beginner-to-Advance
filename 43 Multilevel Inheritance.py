# ------------------------------ Multilevel Inheritance ----------------- #
'''
Multilevel Inheritance
In multilevel inheritance, features of the base class and the derived class are further inherited into the new derived class.
This is similar to a relationship representing a child and grandfather.
'''


class GrandFather:
    football_champion = 2


class Father(GrandFather):
    other_activities = 'lots'

    def activities(self):
        return f'I am Sherry, My Father activities are {self.other_activities}'


class Son(Father):

    def __init__(self, name, age):
        self.Name = name
        self.Age = age

    sports = 'Cricket'

    def activities(self):
        return f'My favourite Sports are {self.sports}'


Idrees_khan = GrandFather()
Saboor_khan = Father()
sherry = Son('Sheheryar', 16)

print(sherry.football_champion)

'''
agar koi method jo Father or GrandFather ma same ha to Son agar osa access kara ga to wo Father wala hi access kar la ga 
q k osa wo method pehla hi mil jai ga
'''


# ------------------------------ Exercise ---------------------------- #
'''
Three Classes = Electronic_device, Pocket_Gadget, Phone
MeaningFull Methods and Variables
'''


class Electronicdevice:
    sell_per_anum = 1000
    which_device = 'Mobile Phone'

    def device_and_sell(self):
        return f'The main device is {self.which_device}, and the Sell per annum is {self.sell_per_anum}'


class PocketGadget(Electronicdevice):
    first_gadget = 'Charger'
    second_gadget = 'Cable Wire'

    def gadget(self):
        return f'First Gadget to introduce is {self.first_gadget}, Second is {self.second_gadget}'


class Phone(PocketGadget):

    phone = 'Sony'

    def details(self):
        return f'Electronic Device is {self.which_device}, Main Gadget is {self.second_gadget} & Phone is {self.phone}.'


device = Electronicdevice
P_gadget = PocketGadget
mobile = Phone

