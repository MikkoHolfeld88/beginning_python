import tkinter as tk

counter = 0

def counterLabel(label):
    counter = 0
    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(1000,count)
    count()

mainWindow = tk.Tk()
mainWindow.title("Sekunden zählen")
label = tk.Label(mainWindow, fg="dark green")
label.pack()
counterLabel(label)
button = tk.Button(mainWindow,text="STOP",width = 25, command=mainWindow.destroy)
button.pack()


mainWindow.mainloop()

