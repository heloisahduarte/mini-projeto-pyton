import tkinter as tk

app = tk.Tk() #cria a janela
app.geometry("400x300") #define o tamanho da janela

label = tk.Label(master=app, text="alguma coisa...", )

btn = tk.Button(master=app, text="Clique aqui", fg="white", bg="blue") #cria um botão com o texto "Clique aqui"
#master=app define a janela pai do botão, text="Clique aqui" deine o texto exibido no botão

btn.place(relx=0.5, rely=0.5, anchor="center")
#place() é um método de layout que posiciona o widget em coordenadas específicas dentro da janela.
#relx=0.5 e rely=0.5 posicionam o botão no centro da janela, anchor="center" alinha o centro do botão com as coordenadas especificadas.

app.mainloop() #inicia o loop principal da interface gráfica, permitindo que a janela seja exibida e interativa.