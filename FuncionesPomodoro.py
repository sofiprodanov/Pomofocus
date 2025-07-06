import tkinter as tk
from tkinter import simpledialog, messagebox
from Personalizacion import *
import winsound

# Variables globales
frames = {}
temporizador_id = None
modo_actual = None
segundos_restantes = 0
huboafter = False
descanso = False
duracion_descanso = 0 #ahora variable dinamica

# ---------- FUNCIONES ALARMA ----------
def sonar_alarma():
     winsound.PlaySound("chime_time.wav", winsound.SND_FILENAME)

# ---------- FUNCIONES BOTON ----------
def mostrar_frame(nombre):
    global segundos_restantes, temporizador_id, modo_actual, huboafter
    
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
    frames[nombre].etiqueta_estado.configure(text="¿EMPEZAMOS?")

def iniciar_temporizador(duracion, nombre_modo):
    global segundos_restantes, modo_actual, descanso, temporizador_id, duracion_descanso
    modo_actual = nombre_modo
    descanso = False

    # Cancelar after previo si existe
    if temporizador_id:
        ventana.after_cancel(temporizador_id)
        temporizador_id = None

    # Preguntar qué tipo de descanso se usará
    opcion = messagebox.askquestion(
        "Tipo de descanso",
        "¿Querés usar descanso largo?\n(Si elegís No, se usará descanso corto)",
        icon="question"
    )

    if "Personalizado" in nombre_modo:
        if opcion == "yes":
            largo = simpledialog.askinteger(
                "Descanso largo",
                "¿Cuántos minutos querés para el descanso largo? (10-40)",
                minvalue=10, maxvalue=40
            )
            if largo is None:
                messagebox.showinfo("Cancelado", "No se inició el temporizador.")
                return
            duracion_descanso = largo
        else:
            corto = simpledialog.askinteger(
                "Descanso corto",
                "¿Cuántos minutos querés para el descanso corto? (1-20)",
                minvalue=1, maxvalue=20
            )
            if corto is None:
                messagebox.showinfo("Cancelado", "No se inició el temporizador.")
                return
            duracion_descanso = corto
    else:
        if opcion == "yes":
            duracion_descanso = frames[nombre_modo].descanso_largo
        else:
            duracion_descanso = frames[nombre_modo].descanso_corto

    # Iniciar el estudio
    if segundos_restantes <= 0:
        segundos_restantes = int(duracion * 60)
    actualizar_tiempo()
    cuenta_regresiva()
    actualizar_botones(nombre_modo, "Stop", detener_temporizador)
    frames[nombre_modo].etiqueta_estado.configure(text="ESTUDIANDO...")

def cuenta_regresiva():
    global segundos_restantes, temporizador_id, descanso, huboafter

    minutos = segundos_restantes // 60
    segundos = segundos_restantes % 60
    frames[modo_actual].etiqueta.config(text=f"{minutos:02d}:{segundos:02d}")

    if segundos_restantes > 0:
        segundos_restantes -= 1
        temporizador_id = ventana.after(1000, cuenta_regresiva)
        huboafter = True
    else:
        sonar_alarma()
        if descanso:
            # Descanso terminó, volvemos al estudio
            descanso = False
            frames[modo_actual].etiqueta_estado.configure(text="ESTUDIANDO...")
            segundos_restantes = int(frames[modo_actual].duracion * 60)
            actualizar_tiempo()
            cuenta_regresiva()
            actualizar_botones(modo_actual, "Stop", detener_temporizador)
        else:
            # Trabajo terminó, comenzamos descanso
            descanso = True
            frames[modo_actual].etiqueta_estado.configure(text="DESCANSANDO...")
            iniciar_descanso()

def detener_temporizador():
    global temporizador_id, huboafter
    if temporizador_id:
        ventana.after_cancel(temporizador_id)
        temporizador_id = None
        huboafter = False
    actualizar_botones(modo_actual, None, None, mostrar_extra=True)
    frames[modo_actual].etiqueta_estado.configure(text="¿SEGUIMOS?")

def continuar_temporizador():
    cuenta_regresiva()
    actualizar_botones(modo_actual, "Stop", detener_temporizador)
    frames[modo_actual].etiqueta_estado.configure(text="ESTUDIANDO...")

def reiniciar_temporizador():
    global segundos_restantes, descanso
    descanso = False
    if modo_actual:
        segundos_restantes = int(frames[modo_actual].duracion * 60)
        actualizar_tiempo()
        actualizar_botones(modo_actual, "Iniciar", lambda: iniciar_temporizador(frames[modo_actual].duracion, modo_actual))
        frames[modo_actual].etiqueta_estado.configure(text="¿EMPEZAMOS?")

def iniciar_descanso():
    global segundos_restantes, temporizador_id

    # Cancelar after previo si existe
    if temporizador_id:
        ventana.after_cancel(temporizador_id)
        temporizador_id = None

    segundos_restantes = int(duracion_descanso * 60)
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
def crear_frame_Pomodoro(nombre, duracion, descanso_corto=None, descanso_largo=None):
    global fuente_botones
    frame = tk.Frame(ventana, bg="lightgreen")
    frame.duracion = duracion

    # Duraciones predeterminadas según el tipo
    if descanso_corto is None or descanso_largo is None:
        if nombre == "Paso de bebé":
            descanso_corto = 5
            descanso_largo = 10
        elif nombre == "Popular":
            descanso_corto = 5
            descanso_largo = 15
        elif nombre == "Medio":
            descanso_corto = 8
            descanso_largo = 20
        elif nombre == "Extendido":
            descanso_corto = 10
            descanso_largo = 25
        else:  # Personalizado
            descanso_corto = 5
            descanso_largo = 10

    frame.descanso_corto = descanso_corto
    frame.descanso_largo = descanso_largo

    #Contenedor central
    contenedor_central = tk.Frame(frame, bg="lightgreen")
    contenedor_central.place(relx=0.5, rely=0.5, anchor="center")
    
    # Etiqueta de estado
    frame.etiqueta_estado = tk.Label(frame, bg="lightgreen", font=("Jokerman", 30), fg="white", pady=15)
    frame.etiqueta_estado.pack(pady=(0, 10))

    # Imagen y temporizador
    tk.Label(contenedor_central, image=imagen, bg="lightgreen").pack()
    etiqueta = tk.Label(contenedor_central, bg="lightgreen", text=f"{duracion:02d}:00", font=("Jokerman", 40), fg="white")
    etiqueta.pack(pady=20)

    # Botón principal
    boton = tk.Button(contenedor_central,text="Inicio", font=fuente_botones, bg="salmon", fg="white", padx=10, pady=5)
    boton.pack()

    # Botones extra
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