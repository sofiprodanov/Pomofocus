import tkinter as tk
from Personalizacion import *
import winsound

# Variables globales
frames = {}
temporizador_id = None
modo_actual = None
segundos_restantes = 0
huboafter = False
descanso = False
etiqueta_estado = tk.Label(bg="lightgreen", font=("Jokerman", 30), fg="white", pady=15)

# ---------- FUNCIONES ALARMA ----------
def sonar_alarma():
     winsound.PlaySound("chime_time.wav", winsound.SND_FILENAME)

# ---------- FUNCIONES BOTON ----------
def mostrar_frame(nombre):
    global segundos_restantes, temporizador_id, modo_actual, huboafter, etiqueta_estado
    
    mensaje.pack_forget()

    for f in frames.values():
        f.pack_forget()
    frames[nombre].pack(fill="both", expand=True)
    
    modo_actual = nombre
    segundos_restantes= frames[nombre].duracion * 60

    if huboafter :
        ventana.after_cancel(temporizador_id)
        temporizador_id = None

    reiniciar_temporizador()
    etiqueta_estado.configure(text="¿EMPEZAMOS?")

def iniciar_temporizador(duracion, nombre_modo):
    global segundos_restantes, modo_actual
    modo_actual = nombre_modo
    if segundos_restantes <= 0:
        segundos_restantes = int(duracion * 60)
    actualizar_tiempo()
    cuenta_regresiva()
    actualizar_botones(nombre_modo, "Stop", detener_temporizador)
    etiqueta_estado.configure(text="ESTUDIANDO...")

def cuenta_regresiva():
    global segundos_restantes, temporizador_id, descanso, huboafter

    minutos = segundos_restantes // 60
    segundos = segundos_restantes % 60
    frames[modo_actual].etiqueta.config(text=f"{minutos:02d}:{segundos:02d}")

    if segundos_restantes > 0:
        segundos_restantes = segundos_restantes - 1
        temporizador_id = ventana.after(1000, cuenta_regresiva)
        huboafter=True
    else:
        sonar_alarma()
        if descanso:
            etiqueta_estado.configure(text="ESTUDIANDO...")
            iniciar_temporizador(frames[modo_actual].duracion , modo_actual)
            descanso = False
        else:
            etiqueta_estado.configure(text="DESCANSANDO...")
            iniciar_descanso()
            descanso = True

def detener_temporizador():
    global temporizador_id, huboafter
    if temporizador_id:
        ventana.after_cancel(temporizador_id)
        temporizador_id = None
        huboafter = False
    actualizar_botones(modo_actual, None, None, mostrar_extra=True)
    etiqueta_estado.configure(text="¿SEGUIMOS?")

def continuar_temporizador():
    cuenta_regresiva()
    actualizar_botones(modo_actual, "Stop", detener_temporizador)
    etiqueta_estado.configure(text="ESTUDIANDO...")

def reiniciar_temporizador():
    global segundos_restantes
    if modo_actual:
        segundos_restantes = int(frames[modo_actual].duracion * 60)
        actualizar_tiempo()
        actualizar_botones(modo_actual, "Iniciar", lambda: iniciar_temporizador(frames[modo_actual].duracion, modo_actual))
        etiqueta_estado.configure(text="¿EMPEZAMOS?")

def iniciar_descanso():
    global segundos_restantes
    segundos_restantes = 5 * 60 # 5 minutos 
    actualizar_tiempo()
    cuenta_regresiva()
    actualizar_botones(modo_actual, "Stop", detener_temporizador)

def actualizar_tiempo():
    minutos = segundos_restantes // 60
    segundos = segundos_restantes % 60
    frames[modo_actual].etiqueta.config(text=f"{minutos:02d}:{segundos:02d}")

def actualizar_botones(nombre, texto_principal, comando_principal, mostrar_extra=False):
    f = frames[nombre]
    if texto_principal and comando_principal:
        f.boton.config(text=texto_principal, command=comando_principal)
        f.boton.pack()
    else:
        f.boton.pack_forget()
    if mostrar_extra:
        f.frame_botones_extra.pack(pady=10)
    else:
        f.frame_botones_extra.pack_forget()

# ---------- CREACIÓN DE FRAMES ----------
def crear_frame_Pomodoro(nombre, duracion):
    global etiqueta_estado, fuente_botones
    frame = tk.Frame(ventana, bg="lightgreen")
    frame.duracion = duracion

    #Contenedor central
    contenedor_central = tk.Frame(frame, bg="lightgreen")
    contenedor_central.place(relx=0.5, rely=0.5, anchor="center")

    #Funcion descanso y estudiando
    etiqueta_estado.pack(pady=(0, 10))
    
    # Etiqueta del temporizador (centrada)
    tk.Label(contenedor_central, image=imagen, bg="lightgreen").pack()
    etiqueta = tk.Label(contenedor_central, bg="lightgreen", text=f"{duracion:02d}:00", font=("Jokerman", 40), fg="white")
    etiqueta.pack(pady=20)

    # Botón de inicio (centrado)
    boton = tk.Button(contenedor_central,text="Inicio", font=fuente_botones, bg="salmon", fg="white", padx=10, pady=5)
    boton.pack()

    # Botones extra (también dentro del contenedor central, pero ocultos inicialmente)
    frame_botones_extra = tk.Frame(contenedor_central, bg="lightgreen")
    boton_continuar = tk.Button(frame_botones_extra, text="Continuar", font=fuente_botones, bg="salmon", fg="white", padx=10, pady=10, command=continuar_temporizador)
    boton_reiniciar = tk.Button(frame_botones_extra, text="Reiniciar", font=fuente_botones, bg="salmon", fg="white", padx=10, pady=10, command=reiniciar_temporizador)
    boton_continuar.pack(side="left", padx=10)
    boton_reiniciar.pack(side="left", padx=10)

    frame.etiqueta = etiqueta
    frame.boton = boton
    frame.frame_botones_extra = frame_botones_extra

    boton.config(command=lambda: iniciar_temporizador(duracion, nombre))

    frames[nombre] = frame