import tkinter as tk

mainWindow = tk.Tk()
img_wolf = tk.PhotoImage(file="img/wolf.gif")

wolf_label = tk.Label(mainWindow, image=img_wolf).pack(side="right")

mainWindow.mainloop()
