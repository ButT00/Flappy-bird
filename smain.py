import tkinter       #  because we make a gui 
import cv2           # it used to capture vidio using Opencv to use it pip install opencv-python
import threading   # we import this because we not need any blockage in program
from functools import partial
import imutils
import time

import PIL.Image, PIL.ImageTk  # PIL mean python image library  # to install pip install pillow
# imagetk is used to show the image in the kinterwindow 

# This is the width and height of our main screen

SET_WIDTH = 650
SET_HEIGHT = 500

stream = cv2.VideoCapture("p.mp4")
def play(speed):
    print(f"The speed is {speed}")
    # play the video in reverse
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)
        
        
    grabbed, frame = stream.read()
    frame = imutils.resize(frame, width = SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image = frame, anchor= tkinter.NW)


def pending(decision):
    # 1. Display decision pending image
    frame = cv2.cvtColor(cv2.imread("decisionpend.jpg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    canvas.create_text(150,30, fill ="black" , font= "times 26 bold", text= "Abdullah's 3rd empire software " )
    # 2. then wait for 1 second
    time.sleep(3)
   
    
    # 3. then display sponser image
    frame = cv2.cvtColor(cv2.imread("sponcer.jpg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame,width = SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image = frame, anchor= tkinter.NW)
    # 4. wait for 1.5 second 
    
    time.sleep(3)
    
    # 5. display out/notout image
    if decision== 'out':
        decisionI = "out.jpg"
    else:
        decisionI = "notout.jpg"
    frame = cv2.cvtColor(cv2.imread(decisionI), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame,width = SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image = frame, anchor= tkinter.NW)
    
    
def out():
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1
    thread.start()
    print("Player is out")


def not_out():
    thread = threading.Thread(target=pending, args=("not out",))
    thread.daemon = 1
    thread.start()
    print("Player is not out")


#tkinter gui start here

window = tkinter.Tk()      # we make a windows for it 
window.title("Abdullah Faisal third umpire Rewiew kit")  # now we make a title for that
cv_img = cv2.cvtColor(cv2.imread("welcome.jpg"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window,width=SET_WIDTH, height=SET_HEIGHT) # now we set a width height and wnidow

# to insert image in gui we code
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0,0, anchor = tkinter.NW, image = photo)
canvas.pack()


# button to control our software


btn = tkinter.Button(window, text= "<<Previous (Fast)", width=50, command=partial(play, -25))
btn.pack()

btn = tkinter.Button(window, text="<<Previous slow", width=50, command=partial(play,-2))
btn.pack()

btn = tkinter.Button(window,text="Next (slow) >>", width = 50, command=partial(play,2))
btn.pack()

btn = tkinter.Button(window, text="Next (fast) >>" , width = 50, command=partial(play,25))
btn.pack()

btn = tkinter.Button(window , text = "Give out" , width=50, command= partial(out,))
btn.pack()

btn = tkinter.Button(window, text  ="Give not out" , width =50, command=partial(not_out,))
btn.pack()

btn = tkinter.Button(window, text=">> Rate Abdullah's coding `<<", width = 50)
btn.pack()


window.mainloop()  # the main loop of tkinter can run beacuse it is very necessary otherwise our gui hang