import sys
from datetime import datetime
from enum import Enum

class TipoIncidencia(Enum):
    RETRASO = "Retraso"
    PRODUCTO_DANADO = "Producto Dañado"
    PRODUCTO_INCORRECTO = "Producto Incorrecto"
    CLIENTE_AUSENTE = "Cliente Ausente"
    OTRO = "Otro"

class Incidencia:
    def __init__(self, id: int, descripcion: str, tipo: TipoIncidencia):
        self.id = id
        self.descripcion = descripcion
        self.tipo = tipo
        self.fecha = datetime.now()
        self.resolucion = None
    
    def get_id(self):
        return self.id
    
    def set_id(self, id: int):
        self.id = id
    
    def get_descripcion(self):
        return self.descripcion
    
    def set_descripcion(self, descripcion: str):
        self.descripcion = descripcion
    
    def get_tipo(self):
        return self.tipo
    
    def set_tipo(self, tipo: TipoIncidencia):
        self.tipo = tipo
    
    def get_fecha(self):
        return self.fecha
    
    def set_fecha(self, fecha: datetime):
        self.fecha = fecha
    
    def get_resolucion(self):
        return self.resolucion
    
    def set_resolucion(self, resolucion: str):
        self.resolucion = resolucion
