import tkinter as ks
from time import strftime
 
root = ks.Tk() # create a window
root.title("Digital Clock") # title of the window

def time():
    string = strftime('%H:%M:%S %p') # format of the time
    label.config(text = string) # set the text of the label to the current time
    label.after(1000, time) # call the time function after 1000ms (1 second)

label = ks.Label(root, font = ('calibri', 40, 'bold'), background = 'black', foreground = 'purple') # create a label to display the time
label.pack(anchor = 'center') # pack the label in the center of the window

time() # call the time function to update the time
root.mainloop() # run the main loop of the window