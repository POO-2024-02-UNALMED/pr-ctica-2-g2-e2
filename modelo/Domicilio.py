from datetime import datetime, timedelta
from modelo import Barrio, Repartidor, EstadoPedido, Zona

class Domicilio:
    def __init__(self, barrio: Barrio, repartidor: Repartidor, zona: Zona):
        self.barrio = barrio
        self.repartidor = repartidor
        self.zona = zona
        self.estado = EstadoPedido.RECIBIDO
        self.tiempo_estimado_entrega = datetime.now() + timedelta(minutes=30)
        self.comentarios_entrega = ""
        self.distancia_km = 0.0

    def set_repartidor(self, repartidor: Repartidor):
        self.repartidor = repartidor
    
    def set_estado(self, estado: EstadoPedido):
        self.estado = estado
    
    def set_zona(self, zona: Zona):
        self.zona = zona
    
    def get_distancia_km(self):
        return self.distancia_km
    
    def set_tiempo_estimado_entrega(self, tiempo: datetime):
        self.tiempo_estimado_entrega = tiempo
    
    def set_comentarios_entrega(self, comentarios: str):
        self.comentarios_entrega = comentarios
    
    def set_barrio(self, barrio: Barrio):
        self.barrio = barrio
    
    def get_costo_envio(self):
        return self.barrio.get_costo_envio() if self.barrio else 0.0
