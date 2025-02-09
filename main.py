import sys
import datetime
from typing import List
from modelo.Administrativo import Administrativo
from modelo.Banco import Banco
from modelo.Banco import Cliente
from modelo.Banco import Barrio
from modelo.Banco import Sucursal
from modelo.Banco import Empresa
from modelo.Cliente import Cliente
from modelo.Plato import Plato
from modelo.Domicilio import Domicilio
from modelo.Pedido import Pedido
from modelo.EstadoPedido import EstadoPedido
from modelo.Producto import Producto
from baseDeDatos.DataManager import DataManager

####################
# Clase para pedir domicilio
####################
class GestorPedidos:
    HORA_INICIO = datetime.time(8, 0)
    HORA_CIERRE = datetime.time(22, 0)
    RECARGO_HORA_PICO = 1.2

    def __init__(self, data_manager: DataManager):
        self.data_manager = data_manager

    def crear_pedido(self, cliente: Cliente, productos: List[Producto], barrio_seleccionado: Barrio) -> Pedido:
        hora_actual = datetime.datetime.now().time()
        if hora_actual < self.HORA_INICIO or hora_actual > self.HORA_CIERRE:
            raise Exception("Fuera del horario de servicio (8:00 - 22:00)")

        for producto in productos:
            if not self.data_manager.verificar_disponibilidad_producto(producto.id):
                raise Exception(f"Producto no disponible: {producto.nombre}")

        if not barrio_seleccionado:
            raise Exception("El barrio seleccionado no es válido.")

        repartidor = self.asignar_repartidor_disponible()
        if not repartidor:
            raise Exception("No hay repartidores disponibles para el barrio seleccionado.")

        domicilio = Domicilio(barrio_seleccionado, repartidor, None)
        pedido_id = self.data_manager.get_next_pedido_id()
        pedido = Pedido(pedido_id, productos, domicilio, cliente)

        self.aplicar_descuentos(pedido, cliente)
        if self.es_hora_pico():
            self.aplicar_recargo_pico(pedido)

        self.data_manager.agregar_pedido(cliente, pedido)
        return pedido

    def asignar_repartidor_disponible(self):
        return next((r for r in self.data_manager.repartidores if r.disponible), None)

    def es_hora_pico(self) -> bool:
        hora = datetime.datetime.now().time()
        return (datetime.time(12, 0) <= hora <= datetime.time(14, 0)) or \
               (datetime.time(19, 0) <= hora <= datetime.time(21, 0))

    def aplicar_recargo_pico(self, pedido: Pedido):
        recargo_total = pedido.total * (self.RECARGO_HORA_PICO - 1)
        pedido.aplicar_recargo(recargo_total)

    def aplicar_descuentos(self, pedido: Pedido, cliente: Cliente):
        if self.es_cliente_frecuente(cliente):
            pedido.aplicar_descuento(pedido.subtotal * 0.1)

    def es_cliente_frecuente(self, cliente: Cliente) -> bool:
        un_mes_atras = datetime.datetime.now() - datetime.timedelta(days=30)
        return sum(1 for p in cliente.historial_pedidos if p.fecha_creacion > un_mes_atras) > 10

    def actualizar_estado_pedido(self, pedido: Pedido, nuevo_estado: EstadoPedido):
        estado_anterior = pedido.estado
        pedido.estado = nuevo_estado
        self.notificar_cambio_estado(pedido, estado_anterior, nuevo_estado)
        if nuevo_estado == EstadoPedido.ENTREGADO:
            pedido.domicilio.repartidor.disponible = True
            pedido.fecha_entrega = datetime.datetime.now()

    def notificar_cambio_estado(self, pedido: Pedido, estado_anterior: EstadoPedido, nuevo_estado: EstadoPedido):
        print(f"Pedido {pedido.id} cambió de estado: {estado_anterior} -> {nuevo_estado}")

class PedirDomicilio:
    def __init__(self, data_manager: DataManager):
        self.data_manager = data_manager
        self.gestor_pedidos = GestorPedidos(data_manager)

    def inicializar_datos(self):
        respuesta = input("¿Desea reiniciar los datos antes de iniciar el programa? (S/N): ").strip().upper()
        if respuesta == "S":
            self.data_manager.borrar_datos()
            self.data_manager.cargar_datos_prueba()
            print("Los datos han sido reiniciados correctamente.")
        else:
            print("Iniciando sin reiniciar los datos...")

    def realizar_pedido(self):
        print("\n¿Desea realizar un nuevo pedido o ir al menú de gestión?")
        print("1. Realizar nuevo pedido")
        print("2. Ir al menú de gestión")
        opcion = self.entrada()

        if opcion == 1:
            try:
                cliente = self.seleccionar_o_crear_cliente()
                if not cliente:
                    print("No se pudo registrar el cliente.")
                    return
                
                productos_seleccionados = self.seleccionar_productos()
                if not productos_seleccionados:
                    print("No se seleccionaron productos.")
                    return

                barrio_seleccionado = self.seleccionar_barrio()
                if not barrio_seleccionado:
                    print("No se seleccionó un barrio válido.")
                    return
                
                pedido = self.gestor_pedidos.crear_pedido(cliente, productos_seleccionados, barrio_seleccionado)
                self.mostrar_resumen_pedido(pedido)
            except Exception as e:
                print(f"Error inesperado: {e}")
        
        self.gestionar_pedidos()

    def seleccionar_barrio(self):
        ciudad = self.data_manager.get_ciudad()
        if not ciudad:
            print("No hay barrios configurados.")
            return None

        print("Seleccione el barrio para la entrega:")
        for idx, barrio in enumerate(ciudad, 1):
            print(f"{idx}. {barrio} - Costo de envío: ${barrio.get_costo_envio()}")
        
        seleccion = self.entrada()
        if 1 <= seleccion <= len(ciudad):
            return ciudad[seleccion - 1]
        else:
            print("El número ingresado no corresponde a ningún barrio listado.")
            return None

    def seleccionar_o_crear_cliente(self):
        cliente_id = self.entrada("Ingrese el ID del cliente: ")
        cliente = self.data_manager.buscar_cliente_por_id(cliente_id)
        
        if not cliente:
            print("Cliente no encontrado. Ingrese los datos para registrarlo.")
            nombre = input("Nombre: ")
            direccion = input("Dirección: ")
            telefono = input("Teléfono: ")
            cliente = Cliente(cliente_id, nombre, direccion, telefono)
            self.data_manager.agregar_cliente(cliente)
            print("Cliente registrado exitosamente.")
        else:
            print(f"Cliente encontrado: {cliente}")
        return cliente

    def seleccionar_productos(self):
        productos_disponibles = self.data_manager.get_productos()
        if not productos_disponibles:
            print("No hay productos disponibles.")
            return []

        print("\nProductos disponibles:")
        for producto in productos_disponibles:
            print(f"{producto.id}. {producto.nombre} - ${producto.precio}")

        productos_seleccionados = []
        while True:
            producto_id = self.entrada("ID del producto (0 para finalizar): ")
            if producto_id == 0:
                break
            producto = self.data_manager.buscar_producto_por_id(producto_id)
            if producto:
                productos_seleccionados.append(producto)
                print(f"{producto.nombre} añadido al pedido.")
            else:
                print("Producto no encontrado. Intente nuevamente.")
        return productos_seleccionados
    
    def mostrar_resumen_pedido(self, pedido):
        print("\n=== Resumen del Pedido ===")
        print(f"ID Pedido: {pedido.id}")
        print("Productos:")
        for producto in pedido.productos:
            print(f"- {producto.nombre}: ${producto.precio:.2f}")
        print(f"\nBarrio: {pedido.domicilio.barrio}")
        print(f"Repartidor: {pedido.domicilio.repartidor.nombre}")
        print(f"Tiempo estimado: {pedido.domicilio.tiempo_estimado_entrega}")
        print(f"\nSubtotal: ${pedido.subtotal:.2f}")
        print(f"Costo de envío: ${pedido.costo_envio:.2f}")
        if pedido.descuento > 0:
            print(f"Descuento aplicado: ${pedido.descuento:.2f}")
        print(f"Total a pagar: ${pedido.total:.2f}")
        print(f"\nEstado del pedido: {pedido.estado.descripcion}")

    def entrada(self, mensaje="Ingrese una opción: "):
        while True:
            try:
                return int(input(mensaje))
            except ValueError:
                print("Error: Entrada no válida. Por favor, ingrese un número.")


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