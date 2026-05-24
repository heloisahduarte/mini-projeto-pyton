from customtkinter import *
from PIL import Image

app= CTk()
app.geometry("400x300")

set_appearance_mode("dark")

img = Image.open("formulario/comCustom/message.png")

btn = CTkButton(master=app, text="Clique aqui", corner_radius=32, 
                hover_color="#4158D0", border_color="#FFCC70", 
                border_width=2, image=CTkImage(light_image=img, dark_image=img))

btn.place(relx=0.5, rely=0.5, anchor="center") #.place() é um método de posicionamento que permite colocar o widget em uma posição específica dentro do contêiner pai.

app.mainloop()