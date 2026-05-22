import tkinter as tk

app = tk.Tk() 
app.geometry("400x300") 

label = tk.Label(master=app, text="alguma coisa...", )

btn = tk.Button(master=app, text="Clique aqui", fg="white", bg="blue") 

btn.place(relx=0.5, rely=0.5, anchor="center")

app.mainloop() 