import tkinter as tk
from tkinter import simpledialog, messagebox, ttk
from Personalizacion import *

# Lista de tareas
tareas = []

# Función: Mostrar tareas en nueva ventana
def mostrar_tareas():
    if not tareas:
        messagebox.showinfo("Sin tareas", "No hay tareas para mostrar.")
        return

    ventana_tareas = tk.Toplevel(ventana)
    ventana_tareas.title("Lista de tareas")
    ventana_tareas.geometry("700x400")

    # Tabla
    tabla = ttk.Treeview(ventana_tareas, columns=("Nombre", "Estimado", "Estado"), show="headings")
    tabla.heading("Nombre", text="Nombre de la tarea")
    tabla.heading("Estimado", text="Pomodoros estimados")
    tabla.heading("Estado", text="Estado")
    tabla.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

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
            actualizar_tabla()
        else:
            messagebox.showwarning("Advertencia", "Seleccioná una tarea para marcar.")

    def desmarcar():
        indice = obtener_indice_seleccionado()
        if indice is not None:
            tareas[indice]["Realizada"] = False
            actualizar_tabla()
        else:
            messagebox.showwarning("Advertencia", "Seleccioná una tarea para desmarcar.")

    # Botones
    frame_botones = tk.Frame(ventana_tareas)
    frame_botones.pack(pady=10)

    btn_marcar = tk.Button(frame_botones, text="Realizada ✅", command=marcar)
    btn_marcar.pack(side=tk.LEFT, padx=5)

    btn_desmarcar = tk.Button(frame_botones, text="Desmarcar ❌", command=desmarcar)
    btn_desmarcar.pack(side=tk.LEFT, padx=5)

    actualizar_tabla()



# Función: Agregar tarea
def agregar_tarea():
    nombre = simpledialog.askstring("Agregar tarea", "Nombre de la tarea:")
    if nombre:
        estimado = simpledialog.askinteger("Agregar tarea", "Pomodoros estimados:")
        if estimado is not None:
            tarea = {"Nombre": nombre, "Estimado": estimado, "Realizada": False}
            tareas.append(tarea)

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
        messagebox.showinfo("Tarea marcada", f"Tarea marcada como realizada: {tareas[seleccion - 1]['Nombre']}")
    else:
        messagebox.showerror("Error", "Número de tarea inválido.")