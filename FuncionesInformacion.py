import tkinter as tk
from Personalizacion import *

def abrir_ventana_informacion():
    ventana_info = tk.Toplevel(ventana)
    ventana_info.title("¿Que es Pomofocus?")
    ventana_info.configure(bg="lightgreen")
    ventana_info.geometry("500x500")
    ventana_info.iconbitmap('icono_alarma.ico')

    #---------- Frame de texto ----------
    frame_texto = tk.Frame(ventana_info, bg="salmon")
    frame_texto.pack(fill="both", expand=True, padx=20, pady=20)

    scroll = tk.Scrollbar(frame_texto)
    scroll.pack(side="right", fill="y")

    texto_widget = tk.Text(
        frame_texto,
        wrap="word",
        yscrollcommand=scroll.set,
        bg= "salmon",
        font=("Helvetica", 11),
        padx=10,
        pady=10,
        relief="flat",
        borderwidth=0
    )
    scroll.config(command=texto_widget.yview)
    texto_widget.pack(fill="both", expand=True)

    # ---------- Contenido ----------
    texto_widget.insert("end", "¿Que es Pomofocus? 🍅\n", "titulo")
    texto_widget.insert("end",
        "Pomofocus es un temporizador pomodoro personalizable."
        "Su objetivo es ayudarte a concentrarte en cualquier tarea, como estudiar, escribir o programar."
        "Está inspirada en la Técnica Pomodoro, un método de gestión del tiempo desarrollado por Francesco Cirillo.\n\n",
        "cuerpo")

    texto_widget.insert("end", "¿Que es la Tecnica Pomodoro? 🤔\n", "titulo")
    texto_widget.insert("end",
        "La Tecnica Pomodoro fue creada por Francesco Cirillo como una forma mas productiva de trabajar y estudiar. "
        "La tecnica utiliza un temporizador para dividir el trabajo en intervalos, tradicionalmente de 25 minutos de duracien, separados por pausas cortas. "
        "Cada intervalo se conoce como un pomodoro, que en italiano significa 'tomate', en referencia al temporizador de cocina con forma de tomate que Cirillo usaba cuando era estudiante universitario.\n\n",
        "cuerpo")

    texto_widget.insert("end", "¿Como usar el Temporizador Pomodoro? ⏱\n", "titulo")
    pasos = [
        "Agrega las tareas en las que vas a trabajar hoy.",
        "Estima la cantidad de pomodoros (1 = 20 min de estudio) que necesitas para cada tarea.",
        "Selecciona una tarea para comenzar.",
        "Inicia el temporizador y concentrate en la tarea durante 20 minutos.",
        "Toma un descanso de 5 minutos cuando suene la alarma.",
        "Repite el ciclo de 3 a 5 veces hasta completar las tareas."
    ]

    for paso in pasos:
        texto_widget.insert("end", f"• {paso}\n", "lista")
    
    texto_widget.insert("end", "\n\n")# Agregar salto de línea para separar bien los bloques

    texto_widget.insert("end", "Niveles de concentracion 💡\n", "titulo")
    niveles_concentracion = {
    "PASO DE BEBE": [
        "10 min de estudio",
        "5 min de descanso corto",
        "10 min de descanso largo\n"
    ],
    "POPULAR": [
        "20 min de estudio",
        "5 min de descanso corto",
        "15 min de descanso largo\n"
    ],
    "MEDIO": [
        "40 min de estudio",
        "8 min de descanso corto",
        "20 min de descanso largo\n"
    ],
    "EXTENDIDO": [
        "60 min de estudio",
        "10 min de descanso corto",
        "25 min de descanso largo\n" 
    ],
    "PERSONALIZADO": [
        "El tiempo de estudio y descansos lo elegis vos!"
    ]
}
    # Insertar niveles formateados
    for nombre, tiempos in niveles_concentracion.items():
        texto_widget.insert("end", f"• {nombre}\n", "nivel")
        for tiempo in tiempos:
            texto_widget.insert("end", f"- {tiempo}\n", "tiempo")
    
     # ---------- Estilos ----------
    # ---------- Estilos ----------
    texto_widget.tag_config("titulo", font=("Helvetica", 14, "bold"), foreground="#FFFFFF", spacing3=10)
    texto_widget.tag_config("cuerpo", foreground="#FFFFFF", spacing3=10)
    texto_widget.tag_config("lista", foreground="#FFFFFF", spacing3=4)
    texto_widget.tag_config("nivel", font=("Helvetica", 11, "bold"), foreground="#FFFFFF", spacing3=2)
    texto_widget.tag_config("tiempo", foreground="#FFFFFF", lmargin1=25, lmargin2=40, spacing1=2, spacing3=2)


    texto_widget.config(state="disabled")