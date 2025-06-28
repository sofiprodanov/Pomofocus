import tkinter as tk
import tkinter.font as tkFont

#----------CREAR UNA VENTANA----------
ventana = tk.Tk()
ventana.title("PomoFocus")
ventana.iconbitmap('icono_alarma.ico')
ventana.minsize(500, 600)
ventana.configure(background="lightgreen")
ventana.update()

#----------COLOR Y FUENTE----------
fuente_inter = tkFont.Font(family="Inter", size=24, weight="bold")
fuente_botones = tkFont.Font(family="Jokerman", size=20, weight="bold")

#---------- CENTRAR VENTANA EN PANTALLA---------- 
ancho_ventana = 500
alto_ventana = 600
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
pos_x = int((ancho_pantalla / 2) - (ancho_ventana / 2))
pos_y = int((alto_pantalla / 2) - (alto_ventana / 2))
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")

#----------IMAGEN POMODORO----------
imagen = tk.PhotoImage(file="pomodoro.png")

#----------TEXTO DE VENTANA PRINCIPAL----------
mensaje = tk.Label(ventana,
                   text="Un temporizador Pomodoro para aumentar tu productividad 💡.\n Alcanzaras tus metas manteniendote enfocado 🧐.",
                   font=fuente_inter, bg="lightgreen", justify="center") #se ajusta con la funcion
mensaje.pack(expand=True, fill="both", padx=50, pady=50)

#----------AJUSTA LARGO DEL TEXTO----------
def ajustar_texto(event=None):
    if mensaje.winfo_exists():
        if event:
            ancho = event.width
        else:
            ancho = ventana.winfo_width()
        mensaje.config(wraplength=ancho - 100)

ventana.bind("<Configure>", ajustar_texto)