import tkinter as tk

def eingabe_anzeigen():
    print("Vorname: %s \nNachname: %s" % (Textfeld1.get(), Textfeld2.get()))

mainWindow = tk.Tk()
mainWindow.title("Entry Widgets")

tk.Label(mainWindow, text="Vorname").grid(row=0)
tk.Label(mainWindow, text="Nachname").grid(row=1)

Textfeld1 = tk.Entry(mainWindow)
Textfeld2 = tk.Entry(mainWindow)
Textfeld1.insert(10,"Maximilian")
Textfeld2.insert(10,"Mustermann")

Textfeld1.grid(row=0, column=1)
Textfeld2.grid(row=1, column=1)

tk.Button(mainWindow,text="Beenden",command=mainWindow.quit).grid(row=3,column=0,sticky=tk.W,pady=4)

tk.Button(mainWindow,text="Anzeigen",
              command=eingabe_anzeigen).grid(row=3,column=1,sticky=tk.W,pady=4)

mainWindow.mainloop()
