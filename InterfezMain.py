import tkinter as tk
import sys
import datetime
from typing import List
from modelo.Administrativo import Administrativo
from modelo.Banco import Banco
from modelo.Cliente import Cliente
from modelo.Barrio import Barrio
from modelo.Sucursal import Sucursal
from modelo.Empresa import Empresa
from modelo.Empleado import Empleado
from modelo.Domicilio import Domicilio
from modelo.Pedido import Pedido
from modelo.EstadoPedido import EstadoPedido
from modelo.Producto import Producto
from baseDeDatos.DataManager import DataManager
from modelo.Chef import Chef
from OrdenFisica import OrdenFisica
from PedidoFisico import PedidoFisico
from entrada import entrada, ingresarNombre
from typing import List
from tkinter import Tk, Label, Button

dataManager = DataManager()
Empresa.calcularFinanzas(dataManager.get_sucursales())


ventana = Tk()
ventana.title("Menu Principal")
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
ventana.geometry(f"{ancho_pantalla}x{alto_pantalla}")
eleccion_var=tk.IntVar(value=-1)
eleccion = 0

pantalla1 = tk.Frame(ventana, bg="lightblue")
pantalla2 = tk.Frame(ventana, bg="lightgreen")
pantalla3 = tk.Frame(ventana, bg="lightgreen")

def cambiar_pantalla(frame):
    frame.tkraise()

ventana.grid_rowconfigure(0, weight=1)
ventana.grid_columnconfigure(0, weight=1)
    
for frame in (pantalla1, pantalla2, pantalla3):
    frame.grid(row=0, column=0, sticky="nsew")
    
def Ver_finanzas():
    cambiar_pantalla(pantalla3)
    if not pantalla3.winfo_children():

        lbl = Label(pantalla3, text=(Empresa.verFinanzas())).pack(pady=(alto_pantalla/5))
        tk.Button(pantalla3, text="Regresar", command=Finanzas).pack(pady=5)

def Sucursales():
    cambiar_pantalla(pantalla3)
    if not pantalla3.winfo_children():
        
        lbl = Label(pantalla3, text=(Sucursal.verSucursales())).pack(pady=(alto_pantalla/5))
        tk.Button(pantalla3, text="Regresar", command=Finanzas).pack(pady=5)
        
def limpiar_frame():
    for widget in pantalla3.winfo_children():
        widget.destroy()


def asignar(x):
    eleccion_var.set(x)
    thiseleccion = eleccion_var.get()
    print(eleccion_var.get())
        

        
def Abrir_sucursal():
    limpiar_frame()
    cambiar_pantalla(pantalla3)


def Finanzas():
    limpiar_frame()
    cambiar_pantalla(pantalla2)

    
    if not pantalla2.winfo_children():
        lbl = Label(pantalla2, text="===Menú finanzas===").pack(pady=(alto_pantalla/5))
    
        lbl = Label(pantalla2, text="Qué acción desea realizar").pack(pady=5)
        tk.Button(pantalla2, text="1. Ver finanzas generales", command=Ver_finanzas).pack(pady=5)
        tk.Button(pantalla2, text="2. Ver sucursales", command=Sucursales).pack(pady=5)
        tk.Button(pantalla2, text="3. Abrir sucursal", command=Abrir_sucursal).pack(pady=5)
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
    ventana.destroy()

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
