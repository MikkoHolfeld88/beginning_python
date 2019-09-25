import tkinter as tk

def writeSlogan(): print ("tkinter is so easy to use!") #Function Delcaration

mainWindow = tk.Tk()
frame = tk.Frame(mainWindow)
frame.pack()

button = tk.Button(frame, text="BEENDEN",fg="red",command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,text="AKTION",command=writeSlogan)
slogan.pack(side=tk.LEFT)

mainWindow.mainloop()

