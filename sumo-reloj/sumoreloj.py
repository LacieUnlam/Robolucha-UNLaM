#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 18:37:30 2016

@author: diego brengi
"""

# use Tkinter to show a digital clock
# tested with Python24    vegaseat    10sep2006
from tkinter import *
import time
import tkinter.messagebox
root = Tk()
time1 = ''
clock = Label(root, font=('arial', 200, 'bold'), bg='green')
clock.pack(fill=BOTH, expand=1)



def tick():
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text="HOLA\n" + time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock.after(200, tick)

def helloCallBack():
   tkinter.messagebox.showinfo( "Hello Python", "Hello World")  

B = tkinter.Button(root, text ="START", command = helloCallBack)
C = tkinter.Button(root, text ="STOP", command = helloCallBack)
D = tkinter.Button(root, text ="2NDT", command = helloCallBack)
E = tkinter.Button(root, text ="ROBOT1", command = helloCallBack)
F = tkinter.Button(root, text ="ROBOT2", command = helloCallBack)
   
B.pack(side=LEFT)  
C.pack(side=LEFT)  
D.pack(side=LEFT)  
E.pack(side=LEFT)  
F.pack(side=LEFT)  

tick()
root.mainloop(  )