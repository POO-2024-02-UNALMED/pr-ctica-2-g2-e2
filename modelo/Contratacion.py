import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..','modelo')))
from Mesero import Mesero
from Empleado import Empleado
from Sucursal import Sucursal
from entrada import entrada, ingresarNombre

class Contratacion:
    def __init__(self):
        x = []
        for mesero in Empleado.getPersonal():
            if mesero.getRol() == "MESERO":
                x.append(mesero)
        self.sucursales = Sucursal.getSucursales()  # Lista de sucursales disponibles
        self.meseros = x  # Lista de meseros contratados
    def contratar_mesero(self, id, nombre, direccion, edad, sueldo, sucursal, datos):

        mesero = Mesero(datos, id, nombre, direccion, edad, sucursal, sueldo=sueldo)
        self.meseros.append(mesero)
        sucursal.meseros.append(mesero)
        return mesero
    
    def ver_meseros(self):
        print("Meseros contratados:")
        for mesero in self.meseros:
            print(mesero)

    def despedir_mesero(self, id):
        id_mesero = id
        mesero_encontrado = None
        
        for mesero in self.meseros:
            if mesero.ID == id_mesero:
                mesero_encontrado = mesero
                break

        if mesero_encontrado:
            self.meseros.remove(mesero_encontrado)


            if mesero_encontrado in Empleado.empleados:
                Empleado.empleados.remove(mesero_encontrado)


            if mesero_encontrado in mesero_encontrado.SUCURSAL.meseros:
                mesero_encontrado.SUCURSAL.meseros.remove(mesero_encontrado)

            print("Mesero despedido exitosamente.")
        else:
            print("Mesero con ID", id_mesero, "no encontrado.")