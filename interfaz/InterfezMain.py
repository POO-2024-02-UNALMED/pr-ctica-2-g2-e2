import tkinter as tk
from typing import List
from tkinter import Tk, Label, Button



ventana = Tk()
ventana.title("Menu Principal")
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
ventana.geometry(f"{ancho_pantalla}x{alto_pantalla}")

pantalla1 = tk.Frame(ventana, bg="lightblue")
pantalla2 = tk.Frame(ventana, bg="lightgreen")

def cambiar_pantalla(frame):
    frame.tkraise()

ventana.grid_rowconfigure(0, weight=1)
ventana.grid_columnconfigure(0, weight=1)
    
for frame in (pantalla1, pantalla2):
    frame.grid(row=0, column=0, sticky="nsew")

def Finanzas():
    cambiar_pantalla(pantalla2)
    
    if not pantalla2.winfo_children():
        lbl = Label(pantalla2, text="===Menú finanzas===").pack(pady=(alto_pantalla/5))
    
        lbl = Label(pantalla2, text="Qué acción desea realizar").pack(pady=5)
        tk.Button(pantalla2, text="1. Ver finanzas generales", command=Finanzas).pack(pady=5)
        tk.Button(pantalla2, text="2. Ver sucursales", command=Personal).pack(pady=5)
        tk.Button(pantalla2, text="3. Abrir sucursal", command=Ordenes).pack(pady=5)
        tk.Button(pantalla2, text="4. Cerrar sucursal", command=Domicilios).pack(pady=5)
        tk.Button(pantalla2, text="5. Pagar deudas", command=Reservaciones).pack(pady=5)
        tk.Button(pantalla2, text="6. Salir", command=lambda: cambiar_pantalla(pantalla1)).pack(pady=5)
def Personal():
    pantalla1.config(bg="red")
def Ordenes():
    pantalla1.config(bg="green")
def Domicilios():
    pantalla1.config(bg="white")
def Reservaciones():
    pantalla1.config(bg = "yellow")
def Guardar_y_salir():
    pantalla1.config(bg="blue")

lbl = Label(pantalla1, text="===Menú principal===").pack(pady=(alto_pantalla/5))

tk.Button(pantalla1, text="Finanzas", command=Finanzas).pack(pady=5)
tk.Button(pantalla1, text="Personal", command=Personal).pack(pady=5)
tk.Button(pantalla1, text="Órdenes", command=Ordenes).pack(pady=5)
tk.Button(pantalla1, text="Domicilios", command=Domicilios).pack(pady=5)
tk.Button(pantalla1, text="Reservaciones", command=Reservaciones).pack(pady=5)
tk.Button(pantalla1, text="Guardar y salir", command=Guardar_y_salir).pack(pady=5)



print("===Menú principal===")
print("1. Finanzas")
print("2. Personal")
print("3. Órdenes")
print("4. Domicilios")
print("5. Reservaciones")
print("6. Guardar y salir")

cambiar_pantalla(pantalla1)

ventana.mainloop()
