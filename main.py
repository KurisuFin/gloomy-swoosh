import numpy as np
import cv2
from tkinter import *
from PIL import Image, ImageTk, ImageDraw
from datetime import datetime
from math import floor
from time import time


class Camera(object):
    @staticmethod
    def _set_time(img, fill=(0, 0, 0)):
        t = datetime.today().strftime('%d.%m.%Y  %H:%M:%S.%f')
        d = ImageDraw.Draw(img)
        d.text((10, 10), t, fill=fill)

    def take(self):
        raise NotImplementedError

    def release(self):
        raise NotImplementedError


class WebCamera(Camera):
    def __init__(self, cam_index):
        self.cap = cv2.VideoCapture(cam_index)

    def take(self):
        self.cap.grab()
        _, cv2_img = self.cap.retrieve()
        # print(dir(self.cap))

        cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(cv2_img)
        self._set_time(img, fill=(255, 255, 0))
        return ImageTk.PhotoImage(img)

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()
        print('WebCamera released')


class ImageCamera(Camera):
    def take(self):
        img = Image.new('RGB', (640, 480), color=(255, 255, 255))
        self._set_time(img)
        return ImageTk.PhotoImage(image=img)

    def release(self):
        pass


if __name__ == "__main__":
    def refresher():
        img = camera.take()
        label.configure(image=img)
        label.image = img
        root.after(100, refresher)

    root = Tk()

    camera = WebCamera(0)
    # camera = ImageCamera()
    label = Label(root, relief=RAISED)
    label.pack(side='top')

    refresher()
    root.mainloop()
    camera.release()

