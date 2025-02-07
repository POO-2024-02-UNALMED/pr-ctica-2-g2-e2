from random import uniform

class Banco:
    bancos = []

    def __init__(self, nombre, exigencia, prestamoMin):
        self.nombre = nombre
        self.exigencia = exigencia
        self. prestamoMin = prestamoMin
        Banco.bancos.append(self)

    def __str__(self):
        return self.nombre + " pagará como mínimo: $" + str(round(self.prestamoMin/1000000)) + "M"
    
    def aceptar(self, solvencia, deudas):
        tolerancia = 10 - self.exigencia
        capacidad = (solvencia - 1) * 10
        if (deudas >= 10000000 * tolerancia) or (solvencia < 1.1):
            return 0
        elif capacidad < self.exigencia:
            return 0
        valorAgregado = self.prestamoMin * ((capacidad - self.exigencia) / 10)
        return self.prestamoMin + valorAgregado
    
    @staticmethod
    def calcularPrestamo(solvencia, prestamo):
        solvencia -= 1
        recargo = solvencia * 10
        i = round(recargo)
        while(recargo > solvencia):
            x = uniform(1, i)
            x /= 10
            recargo = x
        return round(prestamo * recargo)
    
    def getNombre(self): return self.nombre

    def getExigencia(self): return self.exigencia

    def getPrestamo(self): return self.prestamoMin

    def setNombre(self, nombre): self.nombre = nombre

    def setExigencia(self, exigencia): self.exigencia = exigencia

    def setPrestamo(self, valor): self.prestamoMin = valor

    @staticmethod
    def getBancos(): return Banco.bancos