import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..','modelo')))
from Mesero import Mesero
from Empleado import Empleado
from excepcion import entrada, ingresarNombre

class Contratacion:
    def __init__(self, datos):
        self.datos = datos
        self.sucursales = datos.sucursales  # Lista de sucursales disponibles
        self.meseros = datos.meseros  # Lista de meseros contratados
    def contratar_mesero(self, id, nombre, direccion, edad, sueldo, sucursal):

        mesero = Mesero(self.datos, id, nombre, direccion, edad, sucursal, sueldo=sueldo)
        self.meseros.append(mesero)
        sucursal.meseros.append(mesero)
        print("Mesero contratado exitosamente.")
        return mesero
    
    def ver_meseros(self):
        print("Meseros contratados:")
        for mesero in self.meseros:
            print(mesero)

    def despedir_mesero(self):
        id_mesero = input("Ingrese el ID del mesero a despedir: ")
        mesero_encontrado = None
        
        for mesero in self.meseros:
            if mesero.ID == id_mesero:
                mesero_encontrado = mesero
                break

        if mesero_encontrado:
        
            self.meseros.remove(mesero_encontrado)


            if mesero_encontrado in self.datos.empleados:
                self.datos.empleados.remove(mesero_encontrado)

            if mesero_encontrado in Empleado.empleados:
                Empleado.empleados.remove(mesero_encontrado)


            if mesero_encontrado in mesero_encontrado.SUCURSAL.meseros:
                mesero_encontrado.SUCURSAL.meseros.remove(mesero_encontrado)

            print("Mesero despedido exitosamente.")
        else:
            print("Mesero con ID", id_mesero, "no encontrado.")