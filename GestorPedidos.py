from typing import List
import datetime
from modelo.Cliente import Cliente
from modelo.Pedido import Pedido
from modelo.Producto import Producto
from modelo.Barrio import Barrio
from modelo.Domicilio import Domicilio
from modelo.EstadoPedido import EstadoPedido
from baseDeDatos import DataManager

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

        domicilio = Domicilio(cliente, barrio_seleccionado, repartidor)
        pedido_id = self.data_manager.get_next_pedido_id()
        pedido = Pedido(pedido_id, productos, domicilio, cliente)

        self.aplicar_descuentos(pedido, cliente)
        if self.es_hora_pico():
            self.aplicar_recargo_pico(pedido)

        self.data_manager.agregar_pedido(pedido)
        return pedido


    def asignar_repartidor_disponible(self):
        return next((r for r in self.data_manager.repartidores if r.is_disponible()), None)

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