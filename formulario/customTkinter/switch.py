from customtkinter import *

app = CTk()
app.geometry("400x300")

swtich = CTkSwitch(master=app)

swtich.place(relx=0.5, rely=0.5, anchor="center")

app.mainloop()