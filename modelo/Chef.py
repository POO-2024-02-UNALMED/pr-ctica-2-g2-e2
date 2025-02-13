from Empleado import Empleado
import datetime

class Chef(Empleado):
    def __init__(self, datos, id, nombre, direccion, edad, sucursal, antiguedad = 1, sueldo= 1500000):
        super().__init__(datos, id, nombre, direccion, edad, sueldo, "CHEF")
        self.antiguedad = antiguedad
        self.fechaDeContratacion = datetime.date.today()
        self.SUCURSAL = sucursal
        self.ultimaCalificacion = 0
        self.pedidosActuales = 0
        self.puntaje = 0
        self.disponible = True
        self.proximoObjetivo = 0
    
    def getPuntaje(self): return self.puntaje

    def getAntiguedad(self): return self.antiguedad

    def getSucursal(self): return self.SUCURSAL

    def getCalificacion(self): return self.ultimaCalificacion

    def getPedidosActuales(self): return self.pedidosActuales

    def isDisponible(self): return self.disponible

    def getProximoObjetivo(self): return self.proximoObjetivo

    def setPuntaje(self, puntaje): self.puntaje = puntaje

    def setAntiguedad(self, x): self.antiguedad = x

    def setCalificacion(self, x): self.ultimaCalificacion = x

    def setDisponible(self, x): self.disponible = x

    def setProximoObjetivo(self, x): self.proximoObjetivo = x