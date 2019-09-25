import tkinter as tk

mainWindow = tk.Tk()
tk.Label(mainWindow,
         text ="Ich bin in der obersten Zeile",
         fg = "light sky blue", #foreground
         font = "Times").pack()
tk.Label(mainWindow,
         text ="Ich bin in der mittleren Zeile",
         fg ="violet red",
         bg = "chocolate1",
         font = "Helvetica 24 bold").pack()

mainWindow.mainloop()


