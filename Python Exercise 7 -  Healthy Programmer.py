# -------------------------------- Healthy Programmer ----------------------- #
'''
A programmer works from 9am to 5pm = 8 hours.
water = water.mp3 (3.5 ltr) - code = Drank - log into file with time
eyes = eyes.mp3 (30 min) - code = Break - log into file with time
exercise = exercise.mp3 (45 min) - code = Exercise - log into file with time

Modules to Use :
Time - time and date
Pygame - to play audio

# -------------------------- Water ------------------- #
1 glass = 200ml
1 ltr = 1000ml
3.5ltr = 3500ml
total = 18 glasses
time = 26.6 min

# ----------------------- Eyes ----------------- #
Eyes_time  = every 30min
total = 16 times


# ------------------------ Phy Exercise ---------------- #
Physical_time = every 45 min
total = 10
'''


# -------------------------- Lets Starts --------------------------- #

import time
from pygame import mixer


# ---------------------- mp3 ----------------------- #
def water_music():
    mixer.init()
    mixer.music.load('C:\\Users\shehe\Downloads\Music\water.mp3.mp3')
    mixer.music.play()


def eyes_music():
    mixer.init()
    mixer.music.load('C:\\Users\shehe\Downloads\Music\eyes.mp3')
    mixer.music.play()


def phy_music():
    mixer.init()
    mixer.music.load('C:\\Users\shehe\Downloads\Music\physical.mp3')
    mixer.music.play()


# ----------------- Time ---------------- #
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)


# ------------------ Water Func ------------------- #
def water_drink():
    for i in range(18):   # 18 times
        time.sleep(1597)  # every 26.6 minute == 1597 secs
        water_music()
        user = input('If you Drank water, so please enter the Water code: ').upper()
        if user == 'DRANK':
            with open('Water.txt', 'a') as f:
                f.write(f'At {datetime.now()} Sherry Drink Water\n')
            mixer.music.stop()
        else:
            print('Invalid Input')


# ------------------------ Eyes Func ----------------------- #
def eyes_relaxation():
    for i in range(16):  # 16 times
        time.sleep(1800)  # every 30 minute == 1800 secs
        eyes_music()
        user = input('This is Eyes relaxation time, when you Done please Enter Eyes Code: ').upper()
        if user == 'EYDONE':
            with open('Eyes.txt', 'a') as f:
                f.write(f'At {datetime.now()} Sherry Done Eyes Exercise\n')
            mixer.music.stop()
        else:
            print('Invalid Input')


# ---------------------------- Ph Exercise Func ---------------------------- #
def phy_exercise():
    for i in range(10):  # 10 times
        time.sleep(2700)  # every 45 minute == 2700 secs
        phy_music()
        user = input('This is Physical Exercise time, when you Done please Enter Physical Code: ').upper()
        if user == 'PHDONE':
            with open('Exercise.txt', 'a') as f:
                f.write(f'At {datetime.now()} Sherry Done Physical Exercise\n')
            mixer.music.stop()
        else:
            print('Invalid Input')


# ----------------------------- Main Function ---------------- #


while current_time >= '09:00:00' and current_time <= '17:00:00':
    if current_time > '17:00:00':
        pass
    else:
        water_drink()
        eyes_relaxation()
        phy_exercise()
        break
