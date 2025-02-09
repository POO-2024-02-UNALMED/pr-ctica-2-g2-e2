from enum import Enum

class EstadoPedido(Enum):
    RECIBIDO = (1, "Recibido")
    EN_PREPARACION = (2, "En preparación")
    EN_CAMINO = (3, "En camino")
    ENTREGADO = (4, "Entregado")
    CANCELADO = (5, "Cancelado")

    def __init__(self, codigo, descripcion):
        self.codigo = codigo
        self.descripcion = descripcion

    @staticmethod
    def from_codigo(codigo):
        for estado in EstadoPedido:
            if estado.codigo == codigo:
                return estado
        raise ValueError(f"Código de estado no válido: {codigo}")

    @staticmethod
    def from_string(estado):
        estados = {
            "RECIBIDO": EstadoPedido.RECIBIDO,
            "PREPARANDO": EstadoPedido.EN_PREPARACION,
            "EN_CAMINO": EstadoPedido.EN_CAMINO,
            "ENTREGADO": EstadoPedido.ENTREGADO,
            "CANCELADO": EstadoPedido.CANCELADO
        }
        if estado in estados:
            return estados[estado]
        raise ValueError(f"Estado desconocido: {estado}")

    def get_codigo(self):
        return self.codigo

    def get_descripcion(self):
        return self.descripcion
