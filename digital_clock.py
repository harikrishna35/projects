from tkinter import *
from time import strftime

root=Tk()  #creating window
root.title("digit cloak")

def time():        #fun to display time on the label
    string = strftime("%H:%M:%S %p")
    lb1.config(text=string)
    lb1.after(1000,time)

lb1 = Label(root, font = ("arial", 160, "bold"),bg="black",fg="white")    #stylying the displaytime

lb1.pack(anchor ="center",fill="both",expand=1)


time()
mainloop()
