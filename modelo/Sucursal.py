import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..','modelo')))
from Plato import Plato
from Esquina import Esquina
from Empresa import Empresa
from Mesa import Mesa
from Empleado import Empleado
from Mesero import Mesero
from Chef import Chef
from Barrio import Barrio

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
        self.chef = []
        self.espacio = cantidad
        self.gastoRecursos = 850000 * cantidad
        Sucursal.sucursales.append(self)

    @staticmethod
    def nuevaSucursal(sucursal): Empresa.sucursales.append(sucursal)

    @staticmethod
    def calcularDistancia(coordenadas):
        x = coordenadas[0]
        y = coordenadas[1]
        for sucursal in Sucursal.sucursales:
            x1 = sucursal.direccion[0]
            y1 = sucursal.direccion[1]
            distancia = ((x - x1)**2 + (y - y1)**2)**(1/2)
            if distancia < 4:
                return False
        return True
    
    def __str__(self):
        return ("-Sucursal de " + str(self.UBICACION) + "(" + str(Esquina.fromCOO(self.direccion).getDireccion()) + "): \n" +
                "Cantidad de mesas: " + str(len(self.mesas)) + "\n" + 
                "Presupuesto: $" + str(round(self.presupuesto/1000000)) + "M")
    
    @staticmethod
    def verSucursales():
        string = ""
        i = 0
        for sucursal in Sucursal.sucursales:
            if i != 0: string = string + "\n"
            string = string + sucursal.__str__()
            i += 1
        return string
    
    def autoMesero(self, dataManager, auto = 0):
        self.presupuesto += auto
        nombre = Empleado.generarNombre()
        x = Mesero(dataManager, Empleado.generarDocumento(), nombre, "CLL12_CR23", 20, self)
        self.anadirMesero(x)
        return nombre
    
    def autoChef(self, dataManager, auto = 0):
        self.presupuesto += auto
        nombre = Empleado.generarNombre()
        y = Chef(dataManager, Empleado.generarDocumento(), nombre, "CLL12_CR23", 25, self)
        self.anadirChef(y)
        return nombre
    
    def mostrarMenu(self):
        string = ""
        for i in self.MENU:
            if i.ID == len(self.MENU):
                string = string + str(i.ID) + ". " + i.__str__()
            else:
                string = string + str(i.ID) + ". " + i.__str__() + "\n"
        return string

    def comprarMesas(self, pequenas, medianas, grandes, auto = 0):
        self.presupuesto += auto
        compradas = 0
        valor1 = 0
        for i in range(0, pequenas, 1):
            compradas += 1
            valor1 += 500000
            self.mesas.append(Mesa(compradas, 4, self))
        self.presupuesto -= valor1
        valor2 = 0
        for i in range(0, medianas, 1):
            compradas += 1
            valor2 += 800000
            self.mesas.append(Mesa(compradas, 6, self))
        self.presupuesto -= valor2
        valor3 = 0
        for i in range(0, grandes, 1):
            compradas += 1
            valor3 += 1200000
            self.mesas.append(Mesa(compradas, 8, self))
        self.presupuesto -= valor3

    def anadirMesero(self, mesero):
        self.meseros.append(mesero)
        self.presupuesto -= (mesero.getSueldo() * 12)
    
    def anadirChef(self, chef):
        self.chef.append(chef)
        self.presupuesto -= (chef.getSueldo() * 12)

    def restarPresupuesto(self, valor):
        self.presupuesto -= valor
    
    def cerrar(self):
        liquidacion = len(self.mesas) * 1000000
        Barrio.quitar(self.UBICACION)
        for mesero in self.meseros:
            liquidacion += mesero.getSueldo() * 6
            Empleado.despedir(mesero)
        for chef in self.chef:
            liquidacion += chef.getSueldo() * 6
            Empleado.despedir(chef)
        Sucursal.sucursales.remove(self)
        parte = liquidacion / len(Sucursal.sucursales)
        for sucursal in Sucursal.sucursales:
            sucursal.presupuesto += parte

    def aumentarPresupuesto(self, valor): self.presupuesto += valor
    
    def getCantidad(self): return self.espacio

    def getId(self): return self.ID

    def getUbicacion(self): return self.UBICACION

    def getId(self): return self.ID

    def getEspacio(self): return len(self.mesas)

    def getMeseros(self): return self.meseros

    def getGasto(self): return self.gastoRecursos

    def getMesas(self): return self.mesas

    def getDireccion(self): return self.direccion

    def getPresupuesto(self): return self.presupuesto

    def getMenu(self): return self.MENU

    def getReservas(self): return self.reservaciones

    def getChef(self): return self.chef

    @staticmethod
    def getSucursales(): return Sucursal.sucursales