from customtkinter import *

app = CTk()
app.geometry("400x300")

label = CTkLabel(master=app, text="alguma coisa...", font=("Arial", 20), text_color="#FFCC70")

label.place(relx=0.5, rely=0.5, anchor="center")

app.mainloop()