import tkinter as tk
import sys
import datetime
from typing import List
from PedirDomicilio import PedirDomicilio
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
from OrdenFisica import OrdenFisica
from PedidoFisico import PedidoFisico
from entrada import entrada, ingresarNombre
from excepcion.Edad import Edad
from excepcion.One_Sucursal import One_Sucursal
from excepcion.Stock import Stock
from modelo.Contratacion import Contratacion
from excepcion.Sueldo import Sueldo
from tkinter import Tk, Label, Button

dataManager = DataManager()
Empresa.calcularFinanzas(dataManager.get_sucursales())
verificar = 0
resultado_datos = None

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
pantalla4 = tk.Frame(ventana, bg="lightblue")

def cambiar_pantalla(frame):
    frame.tkraise()

ventana.grid_rowconfigure(0, weight=1)
ventana.grid_columnconfigure(0, weight=1)
    
for frame in (pantalla1, pantalla2, pantalla3, pantalla4):
    frame.grid(row=0, column=0, sticky="nsew")

def admin(callback=None):
    limpiar_frame(pantalla3)
    cambiar_pantalla(pantalla3)
    tk.Button(pantalla3, text="Salir", command=lambda: cambiar_pantalla(pantalla1)).pack(pady=5)
    tk.Label(pantalla3, text="Ingrese su número de cédula").pack(pady=(alto_pantalla/6))
    
    cedula_entry = tk.Entry(pantalla3)
    cedula_entry.pack(pady=5)
    
    tk.Button(pantalla3, text="Confirmar", command=lambda: procesar_cedula(cedula_entry, callback)).pack(pady=5)


def procesar_cedula(cedula_entry, callback):
    tk.Button(pantalla3, text="Salir", command=lambda: cambiar_pantalla(pantalla1)).pack(pady=5)
    try:
        cedula = int(cedula_entry.get().strip())
    except ValueError:
        tk.Label(pantalla3, text="Ingrese una cédula válida").pack(pady=5)
        return

    if cedula == 0:
        cambiar_pantalla(pantalla1)
        return

    admin_obj = Administrativo.verificarAdmin(cedula)
    if admin_obj:
        admin2(admin_obj, callback)
    else:
        tk.Label(pantalla3, text="Administrador no encontrado").pack(pady=5)

def admin2(admin_obj, callback):
    global admin_attempts
    admin_attempts = 0  
    limpiar_frame(pantalla3)
    cambiar_pantalla(pantalla3)
    tk.Button(pantalla3, text="Salir", command=lambda: cambiar_pantalla(pantalla1)).pack(pady=5)
    tk.Label(pantalla3, text="Ingrese la contraseña").pack(pady=(alto_pantalla/6))
    password_entry = tk.Entry(pantalla3, show="*")
    password_entry.pack(pady=5)
    
    tk.Button(pantalla3, text="Confirmar", 
              command=lambda: procesar_contrasena(admin_obj, password_entry, callback)).pack(pady=5)
    
def procesar_contrasena(admin_obj, password_entry, callback):
    global admin_attempts
    admin = False
    try:
        password = int(password_entry.get().strip())
    except ValueError:
        tk.Label(pantalla3, text="Ingrese una contraseña válida (numérica)").pack(pady=5)
        return

    admin_attempts += 1
    if admin_obj.verificarCodigo(password):
        admin =True
        tk.Label(pantalla3, text="Bienvenido admin. " + str(admin_obj.nombre)).pack(pady=(alto_pantalla/6))
        if admin==True:
            
            callback()
    else:
        if admin_attempts > 3:
            tk.Label(pantalla3, text="Demasiados intentos, la policia se presentara en su ubicacion proximamente").pack(pady=5)
        else:
            tk.Label(pantalla3, text="Contraseña incorrecta, inténtelo nuevamente").pack(pady=5)
            password_entry.delete(0, tk.END)
            

            
def Ver_finanzas():
    limpiar_frame(pantalla3)
    cambiar_pantalla(pantalla3)
    if not pantalla3.winfo_children():

        lbl = Label(pantalla3, text=(Empresa.verFinanzas())).pack(pady=(alto_pantalla/5))
        tk.Button(pantalla3, text="Regresar", command=mostrarMenuFinanzas).pack(pady=5)
        

def Sucursales():
    limpiar_frame(pantalla3)
    cambiar_pantalla(pantalla3)
    if not pantalla3.winfo_children():
        
        lbl = Label(pantalla3, text=(Sucursal.verSucursales())).pack(pady=(alto_pantalla/5))
        tk.Button(pantalla3, text="Regresar", command=mostrarMenuFinanzas).pack(pady=5)
        
def limpiar_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()
        
def asignar(x):
    eleccion_var.set(x)
    thiseleccion = eleccion_var.get()
    print(eleccion_var.get())
    
def procesar_prestamo(prestamo, entry_anos):
    try:
        anos = int(entry_anos.get())
        if anos <= 0 or anos > 10:
            tk.Label(pantalla4, text="No se acepta un plazo fuera del rango permitido (1-10 años)").pack(pady=5)
        else:
            mensaje = f"Tendrá que pagar en {anos} año" if anos == 1 else f"Tendrá que pagar en {anos} años"
            tk.Label(pantalla4, text=mensaje).pack(pady=5)


            interes = prestamo * anos * 0.03
            total = round(prestamo + interes)
            Empresa.endeudar(total)

            tk.Label(pantalla4, text=f"Se han añadido ${round(total/1000000,1)}M a su deuda").pack(pady=5)
            tk.Button(pantalla4, text="Continuar", command=comprarTerreno(prestamo)).pack(pady=5)
            
    except ValueError:
        tk.Label(pantalla4, text="Por favor, ingrese un número válido").pack(pady=5)
    


    
def accion(x):
    cambiar_pantalla(pantalla4)
    limpiar_frame(pantalla4)
    x -= 1
    elegido = Banco.getBancos()[x]
    prestamo = elegido.aceptar(Empresa.solvencia(), Empresa.getDeudas())
    
    if prestamo == 0:
        lbl= Label(pantalla4, text=("Su solicitud no ha sido aceptada, Escoja otra opción")).pack(pady=(alto_pantalla/5))
        tk.Button(pantalla4, text="volver a elegir", command=PedirPrestamo).pack(pady=5)
    else:
        prestamo += Banco.calcularPrestamo(Empresa.solvencia(), prestamo)
        lbl= Label(pantalla4, text=("Se le han prestado $" + str(round(prestamo/1000000, 1)) + "M")).pack(pady=(alto_pantalla/5))
        anos = 0
        correcto = False
        while correcto == False:
            lbl= Label(pantalla4,text="Escriba la cantidad de años en los que desea pagar su préstamo").pack(pady=5)
            anos = tk.Entry(pantalla4)
            anos.pack(pady=5)
            tk.Button(pantalla4, text="Confirmar", command=lambda: procesar_prestamo(prestamo, anos)).pack(pady=5)
            tk.Button(pantalla3, text="Salir", command=lambda: cambiar_pantalla(pantalla2)).pack(pady=5)
            correcto = True
    return prestamo
        
    
def PedirPrestamo():
    cambiar_pantalla(pantalla3)
    limpiar_frame(pantalla3)
    aceptado= False
    prestamo = 0
    lbl= Label(pantalla3, text=("Seleccione el número del banco que le interesa más")).pack(pady=(alto_pantalla/5))
    x=0
    for i in Banco.getBancos():
        x += 1
        prestamo= tk.Button(pantalla3, text=(str(i) + ". " + i.__str__()), command=lambda x=x: accion(x)).pack(pady=5)
    tk.Button(pantalla3, text="Salir", command=lambda: cambiar_pantalla(pantalla2)).pack(pady=5)
    return prestamo

def no_tengo_idea(i,presupuesto,cOsto,valor,cantidad,direccion,barrio,este):
    espacio = cantidad[i]
    presupuesto -= valor[i]
    presupuesto -= 10000000
    nombre = barrio.getNombre()
    barrio.setSucursal(True)
    new = Sucursal.getSucursales()[-1].getId()
    cambiar_pantalla(pantalla2)
    return Sucursal(new + 1, nombre, espacio, direccion, presupuesto)

def seleccionar(x,espacios,presupuesto,barrio,este):
    limpiar_frame(pantalla4)
    esquina = espacios[x - 1]
    direccion = esquina.getCoordenadas()
    esqPer = Barrio.esquinasPer(direccion)
    valor = []
    cantidad = []
    lbl= Label(pantalla3, text=("Escoja cuál de los locales disponibles le parece más interesante")).pack(pady=(alto_pantalla/5))
    for n in range(0, esqPer, 1):
        cOsto = Barrio.precio(presupuesto)
        valor.append(cOsto)
        cantidad.append(Barrio.espacio(cOsto))
        tk.Button(pantalla4,text=(str(n + 1) + ". Precio: $" + str(round(valor[n] / 1000000)) + "M, Capacidad: " + str(cantidad[n]) + " mesas"), command=lambda i=n: no_tengo_idea(i,presupuesto,cOsto,valor,cantidad,direccion,barrio,este)).pack(pady=5)
    tk.Button(pantalla3, text="Salir", command=lambda: cambiar_pantalla(pantalla2)).pack(pady=5)


def compra(x,noHay,presupuesto):
    cambiar_pantalla(pantalla4)
    limpiar_frame(pantalla4)
    barrio = noHay[x - 1]
    locales = barrio.getEsquinas()
    i = 0
    espacios = []
    lbl= Label(pantalla3, text=("Escoja la ubicación")).pack(pady=(alto_pantalla/5))
    for local in locales:
        if Sucursal.calcularDistancia(local.getCoordenadas()) == False:
            continue
        espacios.append(local)
        i += 1
        este = 5
        tk.Button(pantalla4,text=(str(i) + ". " + local.getDireccion()), command=lambda i=i: seleccionar(i,espacios,presupuesto,barrio,este)).pack(pady=5)
    tk.Button(pantalla3, text="Salir", command=lambda: cambiar_pantalla(pantalla2)).pack(pady=5)

    
def comprarTerreno(presupuesto):
    cambiar_pantalla(pantalla3)
    limpiar_frame(pantalla3)
    candidatos = Barrio.getCiudad()
    hay = []
    noHay = []
    si = 0
    no = 0
    for barrio in candidatos:
        if barrio.tieneSucursal() == True:
            hay.append(barrio)
            si +=1
        else:
            noHay.append(barrio)
            no += 1
    lbl= Label(pantalla3, text=("Escoja en cuál barrio desea abrir la sucursal")).pack(pady=(alto_pantalla/6))
    for i in range(0, no, 1):
        s = noHay[i]
        x=0
        x+=1
        eleccion= tk.Button(pantalla3, text=(str(i + 1) + ". " + s.__str__()), command=lambda x=x: compra(x,noHay,presupuesto)).pack(pady=3)
    tk.Button(pantalla3, text="Salir", command=lambda: cambiar_pantalla(pantalla2)).pack(pady=5)

        
def Abrir_sucursal():
    limpiar_frame(pantalla3)
    cambiar_pantalla(pantalla3)
    presupuesto = 0
    presupuesto = PedirPrestamo()

def continuar_cerrar(x,sucursales):
    limpiar_frame(pantalla3)
    cambiar_pantalla(pantalla3)
    eleccion = x
    nombre = sucursales[eleccion - 1].getUbicacion()
    sucursales[eleccion - 1].cerrar()
    lbl= Label(pantalla3, text=("Se ha cerrado la sucursal de " + nombre)).pack(pady=(alto_pantalla/5))   
    tk.Button(pantalla3, text="Salir", command=lambda: cambiar_pantalla(pantalla2)).pack(pady=5)
            
def Cerrar_sucursal():
    limpiar_frame(pantalla3)
    cambiar_pantalla(pantalla3)
    try:
        if len(Sucursal.getSucursales()) == 1:
            name = Sucursal.getSucursales()[0].getUbicacion()
            error = One_Sucursal(name)
            raise error
    except One_Sucursal:
        lbl =Label(pantalla3,text=(error.mensaje())).pack(pady=5)
        tk.Button(pantalla3, text="Salir", command=lambda: cambiar_pantalla(pantalla2)).pack(pady=5)
        return 0
    sucursales = Sucursal.getSucursales()
    i = 1
    lbl= Label(pantalla3, text=("Escoja la sucursal que desea cerrar")).pack(pady=(alto_pantalla/5))
    for sucursal in sucursales:
        eleccion= tk.Button(pantalla3, text=(str(i) + ". " + sucursal.__str__()), command=lambda x=i: continuar_cerrar(x,sucursales)).pack(pady=5)
        i += 1
    tk.Button(pantalla3, text="Salir", command=lambda: cambiar_pantalla(pantalla2)).pack(pady=5)

def Pagar_Duedas():
    limpiar_frame(pantalla3)
    cambiar_pantalla(pantalla3)
    paga = Empresa.pagarDeudas(Sucursal.getSucursales())
    if paga == 0:
        lbl =Label(pantalla3,text=("No tenemos fondos suficientes para realizar un abono")).pack(pady=5)
        tk.Button(pantalla3, text="Salir", command=lambda: cambiar_pantalla(pantalla2)).pack(pady=5)
    else:
        lbl =Label(pantalla3,text=("Se han pagado $" + str(round(paga/1000000)) + "M de la deuda")).pack(pady=5)
        tk.Button(pantalla3, text="Salir", command=lambda: cambiar_pantalla(pantalla2)).pack(pady=5)

def Finanzas():
    limpiar_frame(pantalla2)
    cambiar_pantalla(pantalla2)

    admin(callback=mostrarMenuFinanzas)

def mostrarMenuFinanzas(): 
    limpiar_frame(pantalla2)
    cambiar_pantalla(pantalla2)
    if not pantalla2.winfo_children():
        lbl = Label(pantalla2, text="===Menú finanzas===").pack(pady=(alto_pantalla/5))
    
        lbl = Label(pantalla2, text="Qué acción desea realizar").pack(pady=5)
        tk.Button(pantalla2, text="1. Ver finanzas generales", command=Ver_finanzas).pack(pady=5)
        tk.Button(pantalla2, text="2. Ver sucursales", command=Sucursales).pack(pady=5)
        tk.Button(pantalla2, text="3. Abrir sucursal", command=Abrir_sucursal).pack(pady=5)
        tk.Button(pantalla2, text="4. Cerrar sucursal", command=Cerrar_sucursal).pack(pady=5)
        tk.Button(pantalla2, text="5. Pagar deudas", command=Pagar_Duedas).pack(pady=5)
        tk.Button(pantalla2, text="6. Salir", command=lambda: cambiar_pantalla(pantalla1)).pack(pady=5)
    


def menuContratacion(dataManager):
    lbl = Label(pantalla2, text="Qué desea hacer?").pack(pady=5)
    tk.Button(pantalla2, text="1. Ver información personal", command=meseros).pack(pady=5)
    tk.Button(pantalla2, text="2. contratar personal", command=mostrarMenuPersonal).pack(pady=5)
    tk.Button(pantalla2, text="3. despedir personal", command=meseros).pack(pady=5)
    tk.Button(pantalla2, text="4. salir", command=mostrarMenuPersonal).pack(pady=5)
       
def meseros():
        limpiar_frame(pantalla2)
        cambiar_pantalla(pantalla2)
        Ver_meseros()
        tk.Button(pantalla2, text="salir", command=menuContratacion).pack(pady=5)
         
def Informacion_per():
        limpiar_frame(pantalla2)
        cambiar_pantalla(pantalla2)
        tk.Button(pantalla2, text="1. ver meseros", command=meseros).pack(pady=5)
        tk.Button(pantalla2, text="2. salir", command=mostrarMenuPersonal).pack(pady=5)
    
def Ver_meseros():
        lbl = Label(pantalla2, text="Qué desea hacer?").pack(pady=5)
        for mesero in Contratacion().meseros:
            lbl = Label(pantalla2, text=(mesero)).pack(pady=1)

def Conseguir_datos(id_mesero):
    global resultado_datos
    try:
        id = int(id_mesero.get().strip())
    except ValueError:
        tk.Label(pantalla3, text="Ingrese una id válida").pack(pady=5)
    resultado_datos = id




def Contratar_personal():
    global resultado_datos
    limpiar_frame(pantalla2)
    cambiar_pantalla(pantalla2)
    tk.Button(pantalla2, text="Salir", command=lambda: menuContratacion).pack(pady=5)
    contratacion = Contratacion()
    lbl = Label(pantalla2, text="=== Contratación de un nuevo mesero ===").pack(pady=5)
    lbl = Label(pantalla2, text="Ingrese el ID del mesero: ").pack(pady=5)
    id_mesero = tk.Entry(pantalla2)
    id_mesero.pack(pady=5)
    id= 0
    tk.Button(pantalla2, text="Confirmar", command=lambda: Conseguir_datos(id_mesero) ).pack(pady=5)
    id_mesero = resultado_datos
    print(id_mesero)
    

def mostrarMenuPersonal():
    limpiar_frame(pantalla2)
    cambiar_pantalla(pantalla2)
    
    if not pantalla2.winfo_children():
        lbl = Label(pantalla2, text="Qué desea hacer?").pack(pady=(alto_pantalla/5))
    
        lbl = Label(pantalla2, text="Qué acción desea realizar").pack(pady=5)
        tk.Button(pantalla2, text="1. Ver información personal", command=Informacion_per).pack(pady=5)
        tk.Button(pantalla2, text="2. contratar personal", command=Contratar_personal).pack(pady=5)
        tk.Button(pantalla2, text="3. despedir personal", command=Abrir_sucursal).pack(pady=5)
        tk.Button(pantalla2, text="6. Salir", command=lambda: cambiar_pantalla(pantalla1)).pack(pady=5)

def Ordenes():
    print("a")
def Domicilios():
    print("b")
def Reservaciones():
    print("a")
def Guardar_y_salir():
    ventana.destroy()
    
 

def Personal():
    limpiar_frame(pantalla2)
    cambiar_pantalla(pantalla2)

    admin(callback=mostrarMenuPersonal)

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
 