import tkinter as tk

mainWindow = tk.Tk()
mainWindow.title("RadioButtons")

var = tk.IntVar()

tk.Label(mainWindow,text="Wähle eine Programmiersprache",
         font=("Hellevtiva",18),justify = tk.LEFT,
         padx = 20).pack(fill="none",ipady=10)

tk.Radiobutton(mainWindow,text=("Python"),font=("Hellevtiva",12),
               padx=20,variable=var,value=1).pack(anchor=tk.W)
tk.Radiobutton(mainWindow,text=("C++"),font=("Hellevtiva",12),
               padx=20,variable=var,value=2).pack(anchor=tk.W)

tk.mainloop()
