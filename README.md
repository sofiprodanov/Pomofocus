# 🍅 Pomofocus

Pomofocus es una aplicacion de escritorio desarrollada en **Python** con **Tkinter**, que implementa la tecnica **Pomodoro** para mejorar la productividad y la gestion del tiempo de estudio o trabajo.

## 📌 Descripcion

Pomofocus permite a los usuarios:
- Elegir entre niveles de concentracion predefinidos (**Paso de bebe**, **Popular**, **Medio**, **Extendido**) o definir uno **Personalizado**.
- Gestionar tareas con funciones para **agregar**, **editar**, **eliminar**, **marcar como realizadas** y **visualizar** la lista de tareas.
- Configurar descansos automaticos entre ciclos de estudio.
- Visualizar informacion sobre la tecnica Pomodoro dentro de la propia app.

Todo se ejecuta en una interfaz grafica amigable y personalizable.

## 🚀 Como ejecutar

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/tu-repo.git
   cd tu-repo
   ```
   
2. Asegurate de tener **Python 3** instalado.

3. Coloca los siguientes archivos en la misma carpeta:
   - `Ejecutable.py`
   - `FuncionesPomodoro.py`
   - `FuncionesTarea.py`
   - `FuncionesInformacion.py`
   - `Personalizacion.py`
   - Ademas, asegurate de tener:
     - `pomodoro.png` (imagen del Pomodoro)
     - `icono_alarma.ico` (ícono de la app)
     - `chime_time.wav` (sonido de la alarma)

4. Ejecuta:
   ```bash
   python Ejecutable.py
   ```

## 🗂️ Estructura del proyecto

- **Ejecutable.py**: Archivo principal. Inicia la ventana principal, crea el menu y gestiona la navegacion.
- **FuncionesPomodoro.py**: Controla la logica del temporizador Pomodoro, sus estados y transiciones.
- **FuncionesTarea.py**: Maneja la lista de tareas: crear, leer, actualizar, eliminar y marcar tareas como realizadas.
- **FuncionesInformacion.py**: Despliega informacion educativa sobre la tecnica Pomodoro y los niveles de concentracion.
- **Personalizacion.py**: Configuracion de estilo, ventana principal, fuentes, colores e imagen principal.

## 👥 Colaboradores

- **Prodanov, Sofia**
- **Pozzi, Santiago**
- **Suarez, Fernando**
- **Gnus, Matias**

## ⚙️ Tecnologias utilizadas

- Python 3
- Tkinter

## 📄 Licencia
Este proyecto está licenciado bajo la Licencia MIT.
Consulta el archivo [LICENSE](LICENSE)  para más información.
