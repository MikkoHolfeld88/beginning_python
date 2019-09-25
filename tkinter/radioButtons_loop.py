import tkinter as tk

mainWindow = tk.Tk()
mainWindow.title("RadioButtons_loop")

var = tk.IntVar()
var.set(0) #initializing the choice

programmingLanguages = [
    ("Python",1),
    ("Perl",2),
    ("C++",3),
    ("C#",4),
    ("Java",5),
    ("JavaScript",6)
]

def showChoice():print(var.get())

tk.Label(mainWindow,text="Wähle eine Programmiersprache",
         font=("Hellevtiva",14),justify = tk.LEFT,
         padx = 20).pack(fill="none",ipady=10)

for val, language in enumerate (programmingLanguages):
    tk.Radiobutton(mainWindow,
                   text=language,
                   padx=20,
                   variable=var,
                   command=showChoice,
                   value=val).pack(anchor=tk.W)

mainWindow.mainloop()
