from time import sleep
from tkinter import *
from PIL import Image, ImageTk
import numpy as np
import cv2

import threading
from threading import Thread
from time import sleep


# def asdf():
#     cap = cv2.VideoCapture(0)
#
#     while True:
#         ret, frame = cap.read()
#         cv2.imwrite('path/to/image.png', frame)
#         if cv2.waitKey(30) & 0xFF == ord('q'):
#             break
#
#     cap.release()
#     cv2.destroyAllWindows()


#


class Capturer(object):
    def __init__(self, cam_index):
        self.cap = cv2.VideoCapture(cam_index)

    def take(self):
        if self.cap.isOpened():
            _, cv2_img = self.cap.read()
            print(type(cv2_img))
            # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 100)
            # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 100)
            cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
            pil_img = Image.fromarray(cv2_img)
            return pil_img
        else:
            print('Problem with video capturer')

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()


capturer = Capturer(1)
root = Tk()

img = ImageTk.PhotoImage(image=capturer.take())

label = Label(root, relief=RAISED, image=img)


def callback(e):
    change_image()
    # img2 = ImageTk.PhotoImage(capturer.take())
    # label.configure(image=img2)
    # label.image = img2


def change_image():
        capturer.cap.grab()
        _, cv2_img = capturer.cap.retrieve()

        cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(cv2_img)

        img2 = ImageTk.PhotoImage(pil_img)
        label.configure(image=img2)
        label.image = img2


def threaded_function(i, x):
    for i in range(i):
        capturer.cap.grab()
        w = cv2.waitKey(10)
        print(w)
        if w:
            _, cv_img = capturer.cap.retrieve()
            img2 = ImageTk.PhotoImage()
            label.configure(image=img2)
            label.image = img2

        print("running %s" % x)
        sleep(1)


# thread = Thread(target=threaded_function, kwargs={'i': 10, 'x': 'yksi'})
# thread.start()


label.pack(side='top')
root.bind("<Return>", callback)

root.mainloop()

exit(0)
