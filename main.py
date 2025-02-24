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

####################
# Clase para pedir domicilio
####################


####################
# Clase para pedir órdenes físicas
####################


def admin():
    print("Ingrese su número de cédula(para salir ingrese 0)")
    cedula = entrada()
    admin = Administrativo.verificarAdmin(cedula)
    if admin != False:
        verdad = False
        intentos = 0
        print("Ingrese la contraseña")
        while(not verdad):
            contrasena = entrada()
            verdad = admin.verificarCodigo(contrasena)
            intentos += 1
            if verdad == True:
                print("Bienvenido admin. " + str(admin.nombre))
                return True
            elif intentos > 3:
                print("Demasiados intentos")
                return False
            print("Contraseña incorrecta, inténtelo nuevamente")
            intentos += 1
    elif cedula == 0:
        return -1
    else:
        print("Administrador no encontrado")
        return False

##################
# Métodos para administración de sucursales
##################
def pedirPrestamo():
    aceptado = False
    eleccion = -1
    prestamo = 0
    while aceptado == False:
        x = 0
        for i in Banco.getBancos():
            x += 1
            print(str(x) + ". " + i.__str__())
        print("Escriba el número del banco que le interesa más")
        eleccion = entrada()
        if (eleccion <= 0) or (eleccion >= len(Banco.getBancos())):
            return 0
        eleccion -= 1
        elegido = Banco.getBancos()[eleccion]
        prestamo = elegido.aceptar(Empresa.solvencia(), Empresa.getDeudas())
        if prestamo == 0:
            print("Su solicitud no ha sido aceptada")
            print("Escoja otra opción")
        else:
            prestamo += Banco.calcularPrestamo(Empresa.solvencia(), prestamo)
            print("Se le han prestado $" + str(round(prestamo/1000000, 1)) + "M")
            anos = 0
            correcto = False
            while correcto == False:
                print("Escriba la cantidad de años en los que desea pagar su préstamo")
                anos = entrada()
                if (anos <= 0) or (anos > 10):
                    print("No se va a aceptar un plazo de esa cantidad de años")
                else:
                    if anos == 1:
                        print("Tendrá que pagar en " + str(anos) + " año")
                    else:
                        print("Tendrá que pagar en " + str(anos) + " años")
                    correcto = True
            interes = prestamo * anos * 0.03
            total = round(prestamo + interes)
            Empresa.endeudar(total)
            print("Se han añadido $" + str(round(total/1000000,1)) + "M a su deuda")
            aceptado = True
    return prestamo

def comprarTerreno(presupuesto):
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
    print("Escoja en cuál barrio desea abrir la sucursal")
    for i in range(0, no, 1):
        s = noHay[i]
        print(str(i + 1) + ". " + s.__str__())
    eleccion = entrada()
    while eleccion > no:
        print("Opción no disponible")
        print("Escoja otra opción")
        eleccion = entrada()
    barrio = noHay[eleccion - 1]
    locales = barrio.getEsquinas()
    i = 0
    espacios = []
    print("Escoja la ubicación")
    for local in locales:
        if Sucursal.calcularDistancia(local.getCoordenadas()) == False:
            continue
        espacios.append(local)
        print(str(i + 1) + ". " + local.getDireccion())
        i += 1
    eleccion = entrada()
    while eleccion > i or eleccion < 1:
        print("Opción no disponible")
        print("Escoja otra opción")
        eleccion = entrada()
    esquina = espacios[eleccion - 1]
    direccion = esquina.getCoordenadas()
    esqPer = Barrio.esquinasPer(direccion)
    valor = []
    cantidad = []
    print("Escoja cuál de los locales disponibles le parece más interesante")
    for n in range(0, esqPer, 1):
        cOsto = Barrio.precio(presupuesto)
        valor.append(cOsto)
        cantidad.append(Barrio.espacio(cOsto))
        print(str(n + 1) + ". Precio: $" + str(round(valor[n] / 1000000)) + "M, Capacidad: " + str(cantidad[n]) + " mesas")
    este = 5
    while este > len(cantidad) or este < 1:
        este = entrada()
        if este > len(cantidad) or este < 1:
            print("Esa opción no está disponible")
    espacio = cantidad[este - 1]
    presupuesto -= valor[este - 1]
    presupuesto -= 10000000
    nombre = barrio.getNombre()
    barrio.setSucursal(True)
    new = Sucursal.getSucursales()[-1].getId()
    return Sucursal(new + 1, nombre, espacio, direccion, presupuesto)

def habilitarSucursal(dataManager, sucursal):
    cantidad = sucursal.getCantidad()
    bien = False
    while bien == False:
        print("Escoja cuántas mesas de 4 espacios desea comprar: $500.000")
        pequenas = entrada()
        print("Escoja cuántas mesas de 6 espacios desea comprar: $800.000")
        medianas = entrada()
        print("Escoja cuántas mesas de 8 espacios desea comprar: $1.200.000")
        grandes = entrada()
        if (pequenas < 0) or (medianas < 0) or (grandes < 0):
            print("No están permitidos los números negativos")
            continue
        if pequenas + medianas + grandes > cantidad:
            print("Esas son demasiadas mesas, no tenemos suficiente espacio para todas")
            continue
        if pequenas + medianas + grandes < cantidad:
            print("Necesitamos más mesas, esas no son suficientes para llenar el espacio")
            continue
        sucursal.comprarMesas(pequenas, medianas, grandes)
        bien = True
    sucursal.restarPresupuesto(10000000)
    print("Se ha comprado un cocina profesional de $10.000.000")
    for i in range(5):
        nombre = sucursal.autoMesero(dataManager)
        print("Se ha contaratado a " + nombre + " para trabajar como mesero")
    for i in range(3):
        nombre = sucursal.autoChef(dataManager)
        print("Se ha contaratado a " + nombre + " para trabajar como chef")
    print("Ingrese el nombre del administrador que se va a contratar")
    admin = ingresarNombre()
    cedula = Empleado.generarDocumento()
    print("Ingrese la contraseña para la nueva cuenta")
    clave = input()
    Administrativo(admin, cedula, clave)
    print("No olvide los datos")
    print("Nuevo admin: " + admin)
    print("Documento: " + str(cedula))
    print("Contraseña: " + str(clave))
        
def cerrarSucursal():
    sucursales = Sucursal.getSucursales()
    i = 1
    print("Escoja la sucursal que desea cerrar")
    for sucursal in sucursales:
        print(str(i) + ". " + sucursal.__str__())
        i += 1
    print(str(i) + ". No cerrar ninguna")
    eleccion = entrada()
    if eleccion <= 0 or eleccion > len(sucursales):
        print("No se ha cerrado ninguna sucursal")
        return
    nombre = sucursales[eleccion - 1].getUbicacion()
    sucursales[eleccion - 1].cerrar()
    print("Se ha cerrado la sucursal de " + nombre)
         
def menuFinanzas():
    salir = False
    while salir == False:
        print("===Menú finanzas===")
        print("Qué acción desea realizar")
        print("1. Ver finanzas generales")
        print("2. Ver sucursales")
        print("3. Abrir sucursal")
        print("4. Cerrar sucursal")
        print("5. Pagar deudas")
        print("6. Salir")

        eleccion = entrada()

        if eleccion == 1:
            print(Empresa.verFinanzas())
        elif eleccion == 2:
            print(Sucursal.verSucursales())
        elif eleccion == 3:
            presupuesto = pedirPrestamo()
            if presupuesto == 0:
                print("No se ha concretado ningún préstamo")
                continue
            sucursal = comprarTerreno(presupuesto)
            habilitarSucursal(sucursal)
        elif eleccion == 4:
            try:
                if len(Sucursal.getSucursales()) == 1:
                    name = Sucursal.getSucursales()[0].getUbicacion()
                    error = One_Sucursal(name)
                    raise error
            except One_Sucursal:
                print(error.mensaje())
                continue
            cerrarSucursal()
        elif eleccion == 5:
            paga = Empresa.pagarDeudas(Sucursal.getSucursales())
            if paga == 0:
                print("No tenemos fondos suficientes para realizar un abono")
            else:
                print("Se han pagado $" + str(round(paga/1000000)) + "M de la deuda")
        elif eleccion == 6:
            print("Adiós")
            return
        else:
            print("Opción no disponible")

##################
# Métodos para administración pedidos físicos
##################
def ordenFisica():
    cliente = Cliente(1, "Osito69", "CLL2_CRR3", "50774 63 m13764")
    i = 0
    eleccion= 0

    for sucursal in Sucursal.getSucursales():
        i += 1
        print(str(i) + ". " + sucursal.__str__())
    print("Indique en cuál sucursal se está realizando la orden")
    while eleccion < 1 or eleccion > len(Sucursal.getSucursales()):
        eleccion = entrada()
        if eleccion < 1 or eleccion > len(Sucursal.getSucursales()):
            print("Esa opción no está disponible")
    sucursal = Sucursal.getSucursales()[eleccion - 1]
    print("Ingrese la cantidad de personas que se presentan con usted(Incluyéndolo a usted)")
    cantidad = 0
    while cantidad < 1 or cantidad > 8:
        cantidad = entrada()
        if cantidad < 1 or cantidad > 8:
            print("No es posible registrar esa cantidad")
    mes = None
    for mesa in sucursal.getMesas():
        if mesa.getCapacidad() >= cantidad and mesa.estaReservada() == False:
            mes = mesa
            mesa.setReserva(True)
            break
    if mes == None:
        print("No hay mesas disponibles")
        return
    meso = None
    for mesero in sucursal.getMeseros():
        if mesero.isDisponible() == True:
            meso = mesero
            mesero.setDisponible(False)
            break
    if meso == None:
        print("No hay nadie que pueda atender en este momento")
        return
    orden = OrdenFisica(mes, cliente, meso, sucursal)
    args = orden.hacerPedido()
    pedido = PedidoFisico(args[0], args[1], args[2], args[3], args[4], args[5], args[6])
    pedido.facturacion()

def menuContratacion(dataManager):
        print("Qué desea hacer?")
        print("1. Ver información personal")
        print("2. contratar personal")
        print("3. despedir personal")
        print("4. salir")
        eleccion = entrada() 

        if eleccion == 1:
            print("1. ver meseros")
            print("2. salir")
            eleccion = entrada()
            if eleccion == 1:
                contratacion = Contratacion()
                contratacion.ver_meseros() 
                menuContratacion(dataManager)             
            elif eleccion == 2:
                    pass
            else:
                print("Opción no válida")
        ###############################        

        elif eleccion == 2:
            contratacion = Contratacion()
# Solicitar los datos del mesero
            print("=== Contratación de un nuevo mesero ===")

            print("Ingrese el ID del mesero: ", end = "")
            id_mesero = entrada()
            print("Ingrese el nombre del mesero: ", end = "")
            nombre = ingresarNombre()
            direccion = input("Ingrese la dirección del mesero: ")
            while True:
                try:
                    print("Ingrese la edad del mesero: ")
                    edad = entrada()
                    if edad < 18 or edad > 70:
                        error = Edad(edad)
                        raise error
                except Edad:
                    print(error.mensaje())
                    continue
                break
            while True:
                try:
                    sueldo = float(input("Ingrese el sueldo del mesero: "))
                    if sueldo < 1500000 or sueldo > 2300000:
                        error = Sueldo(sueldo)
                        raise error
                except ValueError:
                    print("Sueldo inválido. Debe ser un número.")
                    continue
                except Sueldo:
                    print(error.mensaje())
                    continue
                break

# Mostrar las sucursales disponibles
            print("Seleccione la sucursal a la que se asignará el mesero:")
            idx = 0
            string =""
            for sucursal in Sucursal.getSucursales():
                idx += 1
                string = string + str(idx) + ". "
                string = string + sucursal.__str__()
                if sucursal != Sucursal.getSucursales()[-1]:
                    string = string + "\n"
            print(string)
            while True:
                try:
                    indice = entrada()
                    if indice < 1:
                        raise IndexError
                    sucursal = Sucursal.getSucursales()[indice - 1]
                except (IndexError):
                    print("Sucursal inválida, ingrese el número que acompaña la sucursal")
                    continue
                break

# Llamada al método para contratar el mesero con los argumentos ingresados
            contratacion.contratar_mesero(id_mesero, nombre, direccion, edad, sueldo, sucursal,dataManager)
            print("Mesero contratado exitosamente.")



            menuContratacion(dataManager)

        elif eleccion == 3:
            datos = dataManager
            contratacion = Contratacion()
            print("Ingrese el ID del mesero a despedir: ")
            id_mesero = entrada()
            contratacion.despedir_mesero(id_mesero)
            menuContratacion(dataManager)
        elif eleccion == 4:
            pass



def menuPrincipal():
    dataManager = DataManager()
    salir = False
    while salir == False:
        Empresa.calcularFinanzas(Sucursal.getSucursales())
        print("===Menú principal===")
        print("1. Finanzas")
        print("2. Personal")
        print("3. Órdenes")
        print("4. Domicilios")
        print("5. Reservaciones")
        print("6. Guardar y salir")

        print("Seleccione una opción")
        eleccion = entrada()
        if eleccion == 1:
            verdad = False
            while verdad == False:
                verdad = admin()
                if verdad == True: 
                    menuFinanzas()
                elif verdad == -1:
                    break
        
        elif eleccion == 2:
            verdad = False
            while verdad == False:
                verdad = admin()
                if verdad == True:
                   menuContratacion(dataManager)
                elif verdad == -1:
                    break
                
        
        elif eleccion == 3:
            ordenFisica()
            print("Gracias por su compra")

        elif eleccion == 4:
            pedir_domicilio = PedirDomicilio(dataManager)
            pedir_domicilio.realizar_pedido()
        
        elif eleccion == 5:
            pass

        elif eleccion == 6:
            salir = True

        else:
            print("Opción no válida, intente nuevamente")

if __name__ == "__main__":
    menuPrincipal()