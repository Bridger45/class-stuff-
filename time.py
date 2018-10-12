#bridger hope
#9/18
#get time

#import what is needed
import calendar
import time
from tkinter import *
from tkinter import ttk
from tkinter import font
def the_time():
    seconds = calendar.timegm(time.gmtime())
    current_seconds = seconds % 60
    minutes = seconds // 60
    current_minutes  = minutes % 60
    hours = minutes // 60
    current_hours = hours % 24
    if current_hours >=12:
        tag=" AM"
    else:
        tag=" PM"

    #set the timezone
    current_hours = current_hours - 6
    #format the output
    the_time = str(current_hours)+":"+str(current_minutes)+":"+str( current_seconds)+tag
    #return th ouput
    return the_time

def quit(*args):
    root.destroy()

def show_time():
    time = the_time()
    #show time
    txt.set(time)
    #trigger the tick after 1000ms
    root.after(1000, show_time)


#use tkinter lib for showing the clock
root = Tk()
root.attributes("-fullscreen", False)
root.configure(background='Pink')
root.bind("x", quit)
root.after(1000, show_time)

fnt = font.Font(family='Helvetica', size=60, weight='bold')
txt = StringVar()
lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground="red", background="yellow")
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)
root.mainloop()


