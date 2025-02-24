from baseDeDatos import DataManager
from modelo.Cliente import Cliente
from modelo.Pedido import Pedido
from modelo.Producto import Producto
from modelo.Barrio import Barrio
from modelo.Domicilio import Domicilio
from modelo.EstadoPedido import EstadoPedido
from GestorPedidos import GestorPedidos

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
                
                pedido = self.gestor_pedidos.crear_pedido(cliente, [p for p in productos_seleccionados if isinstance(p, Producto)], barrio_seleccionado)
                self.mostrar_resumen_pedido(pedido)
            except Exception as e:
                print(f"Error inesperado: {e}")
        
        pass

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
        print(f"\nBarrio: {pedido.domicilio.barrio.nombre}")  # Access barrio name directly
        if pedido.domicilio.repartidor:
            print(f"Repartidor: {pedido.domicilio.repartidor.get_nombre()}")  # Use getter method
        else:
            print("Repartidor: No asignado")
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
