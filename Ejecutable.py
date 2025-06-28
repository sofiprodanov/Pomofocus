import tkinter as tk
from tkinter import simpledialog, messagebox
from FuncionesPomodoro import *
from FuncionesTarea import *
from FuncionesInformacion import *

# ---------- FRAMES POMODORO ----------
crear_frame_Pomodoro("Paso de bebé", 10)
crear_frame_Pomodoro("Popular", 25)
crear_frame_Pomodoro("Medio", 40)
crear_frame_Pomodoro("Extendido", 60)

# ---------- FRAME PERSONALIZADO ----------
def personalizado():
    tiempo = simpledialog.askstring("Personalizado", "¿Cuánto tiempo querés? Ingresa en minutos: ")
    try:
        duracion = int(tiempo)
    except (TypeError, ValueError):
        messagebox.showinfo("Error...", "Se trabaja solo en minutos. Ingrese numeros enteros")
        return
    
    if duracion > 0:
        nombre = f"Personalizado {duracion}"
        if nombre not in frames:
            crear_frame_Pomodoro(nombre, duracion)
        mostrar_frame(nombre)

# ---------- MENÚ ----------
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

menu_pomodoro = tk.Menu(barra_menu, tearoff=0, background="white", foreground="black")
barra_menu.add_cascade(label="Pomodoro", menu=menu_pomodoro)

menu_concentracion = tk.Menu(menu_pomodoro, tearoff=0, background="white", foreground="black")
menu_pomodoro.add_cascade(label="Nivel de concentración", menu=menu_concentracion)

menu_concentracion.add_command(label="Paso de bebé", command=lambda: mostrar_frame("Paso de bebé"))
menu_concentracion.add_command(label="Popular", command=lambda: mostrar_frame("Popular"))
menu_concentracion.add_command(label="Medio", command=lambda: mostrar_frame("Medio"))
menu_concentracion.add_command(label="Extendido", command=lambda: mostrar_frame("Extendido"))
menu_concentracion.add_command(label="Personalizado", command=personalizado)

menu_tarea = tk.Menu(barra_menu, tearoff=0, background="white", foreground="black")  # Crea una opción en la barra llamada “Tarea”
barra_menu.add_cascade(label="Tarea", menu=menu_tarea)

menu_tarea.add_command(label="Agregar", command=agregar_tarea)
menu_tarea.add_command(label="Editar", command=editar_tarea)    # Agrega las 4 opciones: Agregar, Editar, Eliminar, Mostrar tareas
menu_tarea.add_command(label="Eliminar", command=eliminar_tarea)
menu_tarea.add_separator()
menu_tarea.add_command(label="Mostrar tareas", command=mostrar_tareas)

def cerrar_ventana():
    ventana.quit()
submenu = tk.Menu(menu_pomodoro)
menu_pomodoro.add_command(label="Salir", command=cerrar_ventana)

barra_menu.add_command(label="¿Que es Pomofocus?", command=abrir_ventana_informacion)

ventana.after(100, ajustar_texto) # Ajusta el mensaje de la ventana principal

ventana.mainloop()