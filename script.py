import tkinter as tk
import time

def update_clock():
    hora_certa = time.strftime("%H:%M:%S")
    ceas.config(text=hora_certa)
    ceas.after(1000, update_clock)

app = tk.Tk()
app.title("Ceas Python")

ceas = tk.Label(app, text="", font=("Helvetica", 48))
ceas.pack()

update_clock()
app.mainloop()