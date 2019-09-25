from tkinter import *

mainWindow = Tk()
mainWindow.title("CheckButtons")

def showVar():
    print("männlich: %d,\nweiblich: %d" % (var1.get(),var2.get()))

Label(mainWindow,text="Geschlecht:").grid(row=0,sticky=W)

var1 = IntVar()
Checkbutton(mainWindow, text="männlich",variable=var1).grid(row=1, sticky=W)
var2= IntVar()
Checkbutton(mainWindow,text="weiblich",variable=var2).grid(row=2,sticky=W)

Button(mainWindow,text="show",command=showVar).grid(row=3,sticky=W)

mainloop()
