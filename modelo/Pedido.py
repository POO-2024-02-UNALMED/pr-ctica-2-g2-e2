import sys
from datetime import datetime
from typing import List
from modelo.Producto import Producto
from modelo.Incidencia import Incidencia
from modelo.Domicilio import Domicilio
from modelo.EstadoPedido import EstadoPedido
from modelo.Cliente import Cliente

class Pedido:
    def __init__(self, id: int, productos: List[Producto], domicilio: Domicilio, cliente: Cliente):
        self.id = id
        self.productos = productos
        self.domicilio = domicilio
        self.estado = EstadoPedido.RECIBIDO
        self.fecha_creacion = datetime.now()
        self.fecha_entrega = None
        self.subtotal = sum(p.precio for p in productos)
        self.costo_envio = domicilio.barrio.get_costo_envio() if domicilio and domicilio.barrio else 0
        self.descuento = 0
        self.total = self.subtotal + self.costo_envio - self.descuento
        self.notas = ""
        self.cliente = cliente
        self.repartidor = None
        self.incidencias = []

    def aplicar_recargo(self, recargo: float):
        self.total += recargo

    def aplicar_descuento(self, descuento: float):
        self.descuento = descuento
        self.calcular_costos()

    def calcular_costos(self):
        self.subtotal = sum(p.precio for p in self.productos)
        self.total = self.subtotal + self.costo_envio - self.descuento

    def agregar_incidencia(self, incidencia: Incidencia):
        self.incidencias.append(incidencia)

    def set_estado(self, estado: EstadoPedido):
        self.estado = estado

    def set_fecha_entrega(self, fecha: datetime):
        self.fecha_entrega = fecha
