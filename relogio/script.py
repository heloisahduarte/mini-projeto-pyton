import tkinter as tk
import time

def update_clock(): #função para atualizar o relógio a cada segundo
    hora_certa = time.strftime("%H:%M:%S")  #obtém a hora atual formatada como horas:minutos:segundos
    ceas.config(text=hora_certa)  #atualiza o texto do label ceas com a hora atual
    ceas.after(1000, update_clock)  #chama a função update_clock novamente após 1000 milissegundos (1 segundo) para atualizar o relógio continuamente


app = tk.Tk() #cria a janela
app.title("Time") #titulo da janela

ceas = tk.Label(app, text="", font=("Helvetica", 48), fg='#978F66', bg="#622B14") #cria um label para exibir a hora
ceas.pack() #organiza o label na janela usando o método pack()

update_clock() #chama a função update_clock para iniciar a atualização do relógio
app.mainloop()  #inicia o loop principal da interface gráfica, permitindo que a janela seja exibida e interativa. O relógio será atualizado a cada segundo graças à função update_clock.