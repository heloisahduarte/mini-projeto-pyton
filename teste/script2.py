import tkinter as tk
import time
import math 

WIDTH, HEIGHT = 400, 150 #
FONT = ("Helvetica", 48, "bold")

def lerp_color(c1, c2, t): 
    # Interpola entre duas cores RGB
    return tuple(int(a + (b - a) * t) for a, b in zip(c1, c2))

def rgb_to_hex(rgb):
    return "#%02x%02x%02x" % rgb

def draw_gradient_text(canvas, text, x, y, font, phase):
    canvas.delete("hora")
    n = len(text)
    # Cores do degradê (pode customizar)
    color1 = (151, 143, 102)  # marrom claro
    color2 = (98, 43, 20)     # marrom escuro
    for i, char in enumerate(text):
        # Onda animada no degradê
        t = (i + math.sin(phase + i * 0.7)) / (n + 1)
        color = lerp_color(color1, color2, t)
        canvas.create_text(
            x + i * 32, y + math.sin(phase + i * 0.7) * 8, # efeito de onda vertical
            text=char, font=font, fill=rgb_to_hex(color), tags="hora"
        )

def update_clock():
    global phase
    hora = time.strftime("%H:%M:%S")
    draw_gradient_text(canvas, hora, 60, HEIGHT//2, FONT, phase)
    phase += 0.15
    app.after(60, update_clock)

app = tk.Tk()
app.title("Relógio Degradê em Ondas")
app.configure(bg="#622B14")

canvas = tk.Canvas(app, width=WIDTH, height=HEIGHT, bg="#622B14", highlightthickness=0)
canvas.pack()

phase = 0
update_clock()
app.mainloop()