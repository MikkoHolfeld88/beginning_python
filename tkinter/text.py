import tkinter as tk

mainWindow = tk.Tk()
text_mikko = "Wege entstehen dadurch, dass man sie geht."
message = tk.Message(mainWindow, text = text_mikko)
message.config(bg="lightgreen", font=("Helvetica", 24,"italic"))
message.config(bd=4,padx=40,pady=6,relief="raised",width=400,anchor="w")
message.pack()
tk.mainloop()
