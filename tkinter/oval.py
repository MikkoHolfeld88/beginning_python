import tkinter as tk
from tkinter import *
from random import randint

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Creating MainWindow App runs on
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

mainWindow = Tk()

screen_width = mainWindow.winfo_screenwidth()
screen_height = mainWindow.winfo_screenheight()

mainWindow.minsize(int(screen_width/2),int(screen_height/2))
mainWindow.title("Circle")

canvas = Canvas(mainWindow,width=screen_width,height=screen_height)

canvas.pack()

class Circle():

    def __init__(x,y,size,color):
        canvas.create_oval(x,y,size,size,color)

Kreis = Circle(45,45,56)

mainloop()

