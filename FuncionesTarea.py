import tkinter as tk
import json
import os
from tkinter import simpledialog, messagebox, ttk
from Personalizacion import *

# Lista de tareas
tareas = []

# Ruta del archivo donde se guardan las tareas
ARCHIVO_TAREAS = "tareas.json"

def guardar_tareas():
    with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as f:
        json.dump(tareas, f, indent=4, ensure_ascii=False)

def cargar_tareas():
    global tareas
    if os.path.exists(ARCHIVO_TAREAS):
        with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as f:
            tareas = json.load(f)

# Función: Mostrar tareas en nueva ventana
def mostrar_tareas():
    if not tareas:
        messagebox.showinfo("Sin tareas", "No hay tareas para mostrar.")
        return

    ventana_tareas = tk.Toplevel(ventana)
    ventana_tareas.title("Lista de tareas")
    ventana_tareas.geometry("700x400")
    

    # Frame contenedor para tabla y scrollbar
    frame_tabla = tk.Frame(ventana_tareas)
    frame_tabla.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Scrollbar vertical
    scrollbar_y = tk.Scrollbar(frame_tabla, orient=tk.VERTICAL)
    scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

    # Scrollbar horizontal
    scrollbar_x = tk.Scrollbar(frame_tabla, orient=tk.HORIZONTAL)
    scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

    # Tabla
    tabla = ttk.Treeview(
        frame_tabla,
        columns=("Nombre", "Estimado", "Estado"),
        show="headings",
        yscrollcommand=scrollbar_y.set,
        xscrollcommand=scrollbar_x.set
    )
    tabla.heading("Nombre", text="Nombre de la tarea")
    tabla.heading("Estimado", text="Pomodoros estimados")
    tabla.heading("Estado", text="Estado")
    tabla.pack(fill=tk.BOTH, expand=True)

    scrollbar_y.config(command=tabla.yview)
    scrollbar_x.config(command=tabla.xview)

    def actualizar_tabla():
        tabla.delete(*tabla.get_children())
        for tarea in tareas:
            estado = "✅ Realizada" if tarea.get("Realizada") else "❌ Pendiente"
            tabla.insert("", "end", values=(tarea["Nombre"], tarea["Estimado"], estado))

    def obtener_indice_seleccionado():
        seleccion = tabla.selection()
        if seleccion:
            item = seleccion[0]
            return tabla.index(item)
        else:
            return None

    def marcar():
        indice = obtener_indice_seleccionado()
        if indice is not None:
            tareas[indice]["Realizada"] = True
            guardar_tareas()
            actualizar_tabla()
        else:
            messagebox.showwarning("Advertencia", "Seleccioná una tarea para marcar.")

    def desmarcar():
        indice = obtener_indice_seleccionado()
        if indice is not None:
            tareas[indice]["Realizada"] = False
            guardar_tareas()
            actualizar_tabla()
        else:
            messagebox.showwarning("Advertencia", "Seleccioná una tarea para desmarcar.")

    def eliminar_todas():
        if messagebox.askyesno("Confirmar", "¿Estás seguro de que querés eliminar todas las tareas?"):
            tareas.clear()
            guardar_tareas()
            actualizar_tabla()
            messagebox.showinfo("Eliminadas", "Todas las tareas fueron eliminadas.")

    # Botones
    frame_botones = tk.Frame(ventana_tareas)
    frame_botones.pack(pady=10)

    btn_marcar = tk.Button(frame_botones, text="Realizada ✅", command=marcar)
    btn_marcar.pack(side=tk.LEFT, padx=5)

    btn_desmarcar = tk.Button(frame_botones, text="Desmarcar ❌", command=desmarcar)
    btn_desmarcar.pack(side=tk.LEFT, padx=5)

    btn_eliminar_todas = tk.Button(frame_botones, text="Eliminar todas 🗑️", command=eliminar_todas)
    btn_eliminar_todas.pack(side=tk.LEFT, padx=5)

    actualizar_tabla()

# Función: Agregar tarea
def agregar_tarea():
    nombre = simpledialog.askstring("Agregar tarea", "Nombre de la tarea:")
    if nombre:
        estimado = simpledialog.askinteger("Agregar tarea", "Pomodoros estimados:")
        if estimado is not None:
            tarea = {"Nombre": nombre, "Estimado": estimado, "Realizada": False}
            tareas.append(tarea)
            guardar_tareas()

# Función: Editar tarea
def editar_tarea():
    if not tareas:
        messagebox.showinfo("Sin tareas", "No hay tareas para editar.")
        return
    # Si no hay tareas, se avisa y se corta

    opciones = "\n".join([f"{i+1}. {t['Nombre']} ({t['Estimado']} 🍅)" for i, t in enumerate(tareas)])
    seleccion = simpledialog.askinteger("Editar tarea", f"Seleccioná el número de la tarea:\n{opciones}")
    # Muestra una lista numerada de tareas y pide que selecciones una para editar

    if seleccion and 1 <= seleccion <= len(tareas):
        tarea = tareas[seleccion - 1]
        # Verifica si el número es válido y selecciona la tarea correspondiente
        nuevo_nombre = simpledialog.askstring("Editar nombre", "Nuevo nombre:", initialvalue=tarea["Nombre"])
        nuevo_estimado = simpledialog.askinteger("Editar estimado", "Nuevo estimado:", initialvalue=tarea["Estimado"])
        # Pide el nuevo nombre y estimado, mostrando los valores actuales
        if nuevo_nombre:
            tarea["Nombre"] = nuevo_nombre
        if nuevo_estimado is not None:
            tarea["Estimado"] = nuevo_estimado
        guardar_tareas()
        # Actualiza los datos si se ingresaron
    else:
        messagebox.showerror("Error", "Número de tarea inválido.")
    # ventana con mensaje de error

# Función: Eliminar tarea
def eliminar_tarea():
    if not tareas:
        messagebox.showinfo("Sin tareas", "No hay tareas para eliminar.")
        return
    # Mismo principio: si no hay tareas, se muestra aviso

    opciones = "\n".join([f"{i+1}. {t['Nombre']} ({t['Estimado']} 🍅)" for i, t in enumerate(tareas)])
    seleccion = simpledialog.askinteger("Eliminar tarea", f"Seleccioná el número de la tarea:\n{opciones}")
    # Muestra todas las tareas con números y pide que elijas cuál eliminar

    if seleccion and 1 <= seleccion <= len(tareas):
        eliminada = tareas.pop(seleccion - 1)
        guardar_tareas()
        messagebox.showinfo("Eliminada", f"Tarea eliminada: {eliminada['Nombre']}")
    # Si el número es válido, elimina la tarea de la lista y muestra un mensaje

    else:
        messagebox.showerror("Error", "Número de tarea inválido.")

# Función: marcar tarea como realizada
def marcar_como_realizada():
    if not tareas:
        messagebox.showinfo("Sin tareas", "No hay tareas para marcar.")
        return

    opciones = "\n".join([
        f"{i+1}. {t['Nombre']} ({t['Estimado']} 🍅) - {'✅' if t['Realizada'] else '❌'}"
        for i, t in enumerate(tareas)
    ])
    seleccion = simpledialog.askinteger("Marcar como realizada", f"Seleccioná el número de la tarea:\n{opciones}")

    if seleccion and 1 <= seleccion <= len(tareas):
        tareas[seleccion - 1]["Realizada"] = True
        guardar_tareas()
        messagebox.showinfo("Tarea marcada", f"Tarea marcada como realizada: {tareas[seleccion - 1]['Nombre']}")
    else:
        messagebox.showerror("Error", "Número de tarea inválido.")

