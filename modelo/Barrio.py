from random import randint
from .Esquina import Esquina

class Barrio:
    CIUDAD = []

    def __init__(self, nombre, costoEnvio, x, y):
        self.nombre = nombre
        self.costoEnvio = costoEnvio
        self.sucursal = False
        self.esquinas = Esquina.determinarZona(x, y)
        Barrio.CIUDAD.append(self)
    
    def __str__(self):
        return self.nombre
    
    @staticmethod
    def getCiudad(): return Barrio.CIUDAD

    @staticmethod
    def esquinasPer(direccion):
        x = direccion[0]
        y = direccion[1]
        if x == 0 and (y == 1 or y == -1): return 1
        if (x == 8 or x == -8) and (y == 8 or y == -8): return 1
        if x == 0 and (y == 7 or y == -7): return 1
        if y == 0 and (x == 8 or x == -8): return 1
        if (x == 4 or x == -4) and (y == 4 or y == -4): return 1
        if (x == 4 or x == -4) and (y == 0 or y == 8 or y == -8): return 1
        if (y == 4 or y == -4) and (x == 0 or x == 8 or x == -8): return 1
        if x == 0 or y == 0: return 2
        if x == -4 or y == -4: return 2
        if x == -8 or y == -8: return 2
        if x == 4 or y == 4: return 2
        if x == 8 or y == 8: return 2
        return 4
    
    @staticmethod
    def precio(presupuesto):
        presupuesto = round(presupuesto/2)
        valor = randint(100000000, presupuesto)
        return valor

    @staticmethod
    def espacio(valor):
        n = round(valor/(10000000 * 1.5))
        r = randint(15, n)
        if r > 50:
            return 50
        else:
            return r
        
    def getNombre(self): return self.nombre

    def getCostoEnvio(self): return self.costoEnvio

    def tieneSucursal(self): return self.sucursal

    def getEsquinas(self): return self.esquinas

    def setNombre(self, nombre): self.nombre = nombre

    def setCostoEnvio(self, costo): self.costoEnvio = costo

    def setSucursal(self, x): self.sucursal = x