import tkinter  # Tkinter is Python's de-facto standard GUI (Graphical User Interface) package.
import cv2   # Wrapper package for OpenCV python bindings.
import PIL.Image, PIL.ImageTk   # Python Imaging Library adds image processing capabilities to your Python interpreter.
from functools import partial  # Partial functions allow us to fix a certain number of arguments of a function and
# generate a new function.
import threading
import time
import imutils


# Width and Height of our main screen

SET_WIDTH = 650
SET_HEIGHT = 368


stream = cv2.VideoCapture('images/run out.mp4')
flag = True


# Function for play
def play(speed):

    global flag

    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

    grabbed, frame = stream.read()
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image= PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    if flag:
        canvas.create_text(120, 25, fill='white', font='courier 20 italic bold', text='  Decision Pending')
    flag = not flag


# Function For Pending
def pending(decision):
    # 1. Display Decision Pending Image
    frame = cv2.cvtColor(cv2.imread("images/Decision Pending.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

    # 2. Wait for 1 Second
    time.sleep(1.5)

    # 3. Display Sponsor Image
    frame2 = cv2.cvtColor(cv2.imread("images/Sponsor.png"), cv2.COLOR_BGR2RGB)
    frame2 = imutils.resize(frame2, width=SET_WIDTH, height=SET_HEIGHT)
    frame2 = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame2))
    canvas.image = frame2
    canvas.create_image(0, 0, image=frame2, anchor=tkinter.NW)

    # 4. Wait for 1.5 Second
    time.sleep(2.5)

    # 5. Display Out/Not out Image
    if decision == 'out':
        decision_img = 'images/Out.png'
    else:
        decision_img = 'images/Not out.png'

    frame3 = cv2.cvtColor(cv2.imread(decision_img), cv2.COLOR_BGR2RGB)
    frame3 = imutils.resize(frame3, width=SET_WIDTH, height=SET_HEIGHT)
    frame3 = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame3))
    canvas.image = frame3
    canvas.create_image(0, 0, image=frame3, anchor=tkinter.NW)


# Function For Out
def out():
    thread = threading.Thread(target=pending, args=('out',))
    thread.daemon = 1
    thread.start()


# Function For Not Out
def not_out():
    thread = threading.Thread(target=pending, args=('not out',))
    thread.daemon = 1
    thread.start()


# Tkinter GUI starts here

window = tkinter.Tk()
window.title("Programming_With_Sherry Third Umpire Decision Review Kit")
cv_img = cv2.cvtColor(cv2.imread("images/Welcome.png"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0, 0, anchor=tkinter.NW, image=photo)
canvas.pack()

#  Buttons to control playback
btn = tkinter.Button(window, text="<< Previous (fast)", width=50, command=partial(play, -25))
btn.pack()

btn = tkinter.Button(window, text="<< Previous (slow)", width=50, command=partial(play, -2))
btn.pack()

btn = tkinter.Button(window, text="Next (slow) >>", width=50, command=partial(play, 2))
btn.pack()

btn = tkinter.Button(window, text="Next (fast) >>", width=50, command=partial(play, 25))
btn.pack()

btn = tkinter.Button(window, text="Give Out", width=50, command=out)
btn.pack()

btn = tkinter.Button(window, text="Give Not Out", width=50, command=not_out)
btn.pack()


window.mainloop()
