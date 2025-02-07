from modelo.Administrativo import Administrativo
from modelo.Banco import Banco
from modelo.Barrio import Barrio
from modelo.Sucursal import Sucursal
from modelo.Empresa import Empresa
from modelo.Plato import Plato

def entrada():
    x = False
    while (x == False):
        try:
            cedula = int(input())
        except ValueError:
            print("Error de entrada, por favor ingrese un número")
            continue
        x = True
    return cedula
    
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
                print("Escriba la cantidad de años en los que desa pagar su préstamo")
                anos = entrada()
                if (anos <= 0) or (anos > 10):
                    print("No se va a aceptar un plazo de esa cantidad de años")
                else:
                    print("Tendrá que pagar en " + str(anos) + " años")
                    correcto = True
            interes = prestamo * anos * 0.03
            Empresa.endeudar(prestamo + interes)
            print("Se han añadido " + str(prestamo + interes) + "a su deuda")
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
    while eleccion > i:
        print("Opción no disponible")
        print("Escoja otra opción")
        eleccion = entrada()
    esquina = espacios[eleccion - 1]
    direccion = esquina.getCoordenadas()
    esqPer = Barrio.esquinasPer(direccion)
    valor = []
    cantidad = []
    print("Escoja cuál de los locales disponibles le parecen más interesantes")
    for n in range(0, esqPer, 1):
        cOsto = Barrio.precio()
        valor.append(cOsto)
        cantidad.append(Barrio.espacio(cOsto))
        print(str(n + 1) + ". Precio: $" + str(round(valor[n] / 1000000)) + "M, Capacidad: " + cantidad[n] + " mesas")
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
    return Sucursal(1, nombre, espacio, direccion, presupuesto)

def menuFinanzas():
    salir = False
    while salir == False:
        Empresa.calcularFinanzas()
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
            pass
        elif eleccion == 3:
            presupuesto = pedirPrestamo()
            if presupuesto == 0:
                print("No se ha concretado ningún préstamo")
                continue
            sucursal = comprarTerreno(presupuesto)
            
        elif eleccion == 4:
            pass
        elif eleccion == 5:
            pass
        elif eleccion == 6:
            salir == True
        else:
            print("Opción no disponible")
            pass

if __name__ == "__main__":
    Administrativo("Messi", 12345, 4488123)
    Banco("Bancolombia", 7, 900000000)
    Banco("Banco de Bogotá", 9, 1300000000)
    Banco("Avevillas", 4, 400000000)
    Banco("Davivienda", 5, 700000000)
    a = [-8, -4]
    b = [-4, 0]
    c = [0, 4]
    d = [4,8]
    Barrio("La Estrella", 7.99, a, d)
    Barrio("Sabaneta", 6.99, b, d)
    Barrio("Intagüí", 5.99, c, d)
    Barrio("Envigado", 4.99, d, d)
    Barrio("Robledo", 6.99, d, c)
    Barrio("Bello", 7.99, c, c)
    Barrio("Poblado", 4.99, b, c)
    Barrio("Niquía", 7.49, a, c)
    Barrio("Alpujarra", 3.99, a, b)
    Barrio("Cisneros", 3.99, b, b)
    Barrio("San Antonio", 3.99, c, b)
    Barrio("Parque Berrío", 3.99, d, b)
    Barrio("Prado", 4.49, d, a)
    Barrio("Caribe", 5.49, c, a)
    Barrio("Acevedo", 6.49, b, a)
    Barrio("Madera", 6.99, a, a)
    Sucursal(1, "Cisneros", 35, [-3, -3], 57000000)
    Sucursal(2, "Robledo", 30, [5, 3], 48000000)
    Sucursal(3, "Sabaneta", 30, [-2, 6], 44000000)

    print(Empresa.getSucursales())
    verdad = False
    while verdad == False:
        verdad = administradir = admin()
        if administradir == -1:
            print("Adiós")
            break
    if verdad == True:
        menuFinanzas()