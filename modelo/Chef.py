from Empleado import Empleado
import datetime

class Chef(Empleado):
    def __init__(self, datos, id, nombre, direccion, edad, sucursal, antiguedad = 1, sueldo= 1800000):
        super().__init__(datos, id, nombre, direccion, edad, sueldo, "CHEF")
        self.antiguedad = antiguedad
        self.fechaDeContratacion = datetime.date.today()
        self.SUCURSAL = sucursal
        self.ultimaCalificacion = 0
        self.pedidosActuales = 0
        self.puntaje = 0
        self.disponible = True
        self.proximoObjetivo = 20
    
    @staticmethod
    def asignar(sucursal):
        for chef in sucursal.getChef():
            a = chef.getRol()
            if a == "CHEF" and chef.disponible == True:
                chef.pedidosActuales += 1
                if chef.pedidosActuales > 3:
                    chef.disponible = False
                return chef

    def ganarPuntos(self, calificacion):
        if calificacion == 1:
            if self.puntaje >= 2:
                self.puntaje -= 2
            else:
                self.puntaje = 0
        elif calificacion == 2:
            if self.puntaje >= 1:
                self.puntaje -= 1
            else: 
                self.puntaje = 0
        elif calificacion == 3:
            pass
        elif calificacion == 4:
            self.puntaje += 1
        elif calificacion == 5:
            self.puntaje += 2
        else:
            pass

        if self.getSueldo() > 3500000:
            self.puntaje = 0
            self.setSueldo(3500000)
        
        if self.puntaje >= self.proximoObjetivo:
            aumento = round(self.sueldo * 0.1)
            self.sueldo += aumento
            self.puntaje = 0
            self.proximoObjetivo = 50    
    
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