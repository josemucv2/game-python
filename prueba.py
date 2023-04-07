from tkinter import simpledialog, messagebox
import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.withdraw()

user_name = simpledialog.askstring(title="Nombre de usuario",
                                   prompt="Por favor ingrese su nombre:")
# Mostrar la ventana de alerta
messagebox.showinfo('Informacion', user_name)
# Cerrar la ventana principal


root.destroy()
root.mainloop()
