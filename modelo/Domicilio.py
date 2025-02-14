from datetime import datetime, timedelta
from modelo.Barrio import Barrio
from modelo.Repartidor import Repartidor
from modelo.EstadoPedido import EstadoPedido

class Domicilio:
    def __init__(self, cliente, barrio: Barrio, repartidor: Repartidor):
        self.cliente = cliente
        self.barrio = barrio
        self.repartidor = repartidor
        self.estado = EstadoPedido.RECIBIDO
        self.tiempo_estimado_entrega = datetime.now() + timedelta(minutes=30)
        self.comentarios_entrega = ""
        self.distancia_km = 0.0
        
    def calcular_costo_envio(self):
        return self.barrio.get_costo_envio()
    
    def set_repartidor(self, repartidor: Repartidor):
        self.repartidor = repartidor
    
    def set_estado(self, estado: EstadoPedido):
        self.estado = estado
    
    def get_distancia_km(self):
        return self.distancia_km
    
    def set_tiempo_estimado_entrega(self, tiempo: datetime):
        self.tiempo_estimado_entrega = tiempo
    
    def set_comentarios_entrega(self, comentarios: str):
        self.comentarios_entrega = comentarios
    
    def set_barrio(self, barrio: Barrio):
        self.barrio = barrio
    