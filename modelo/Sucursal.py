from Plato import Plato
from Empresa import Empresa
from Esquina import Esquina
from math import sqrt

class Sucursal:
    sucursales = []
    
    def __init__(self, id, nombre, cantidad, direccion = [], presupuesto = 0):
        self.ID = id
        self.UBICACION = nombre
        self.mesas = []
        self.meseros = []
        self.direccion = direccion
        self.presupuesto = presupuesto
        self.MENU = [Plato("Hamburguesa", 15000, 1),
                     Plato("Perro", 14000, 2),
                     Plato("Pizza Margarita", 21000, 3),
                     Plato("Pasta Alfredo", 16000, 4),
                     Plato("Salchipapas", 13000, 5),
                     Plato("Hamburguesa vegana", 17000, 6),
                     Plato("Picada", 30000, 7)]
        self.reservaciones = []
        self.Chef = []
        Sucursal.sucursales.append(self)
        print(self)

    @staticmethod
    def nuevaSucursal(sucursal): Empresa.sucursales.append(sucursal)

    @staticmethod
    def calcularDistancia(coordenadas):
        x = coordenadas[0]
        y = coordenadas[1]
        for sucursal in Sucursal.sucursales:
            x1 = sucursal.direccion[0]
            y1 = sucursal.direccion[1]
            distancia = sqrt((x * x1) + (y * y1))
            if distancia < 4:
                return False
        return True
    
    def __str__(self):
        return ("-Sucursal de " + str(self.UBICACION) + "(" + str(Esquina.fromCOO(self.direccion).getDireccion()) + "): \n" +
                "Cantidad de mesas: " + str(len(self.mesas)) + "\n" + 
                "Presupuesto: $" + str(round(self.presupuesto/1000000)) + "M")