# import pyautogui
# from PIL import Image, ImageGrab
# import time
# # from numpy import asarray


# def hit(key):
#     pyautogui.keyDown(key)


# def draw():
#     pass


# def is_Collide(data):
#     for i in range(200, 280):
#             for j in range(400, 420):
#                 if data[i, j] < 100:
#                     return True
#     return False


# if __name__ == "__main__":
#     print("Hey.. Dino game is about to start in 3 Sec.")
#     time.sleep(3)
#     hit("up")

#     while True:
#         image = ImageGrab.grab().convert('L')
#         data = image.load()
#         if is_Collide(data):
#             hit("up")
#         # print(asarray(image))
#         # for i in range(200, 280):
#         #     for j in range(400, 420):
#         #         data[i, j] = 0
        
#         # image.show()

import pyautogui # pip install pyautogui
from PIL import Image, ImageGrab # pip install pillow
# from numpy import asarray
import time

def hit(key):
    pyautogui.keyDown(key)
    return

def isCollide(data):
    # Draw the rectangle for birds
    for i in range(160, 210):
        for j in range(350, 413):
            if data[i, j] < 100:
                hit("down")
                return

    for i in range(175, 215):
        for j in range(420, 480):
            if data[i, j] < 100:
                hit("up")
                return
    return

if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(2)
    # hit('up') 

    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        isCollide(data)
            
        # print(asarray(image))
        '''
        # Draw the rectangle for cactus
        for i in range(175, 215):
            for j in range(420, 480):
                data[i, j] = 0
        
        # Draw the rectangle for birds
        for i in range(160, 210):
            for j in range(350, 413):
                data[i, j] = 171

        image.show()
        break
        '''

