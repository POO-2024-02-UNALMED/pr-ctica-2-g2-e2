from Nombre import Nombre
from Apellido import Apellido
from random import randint

class Empleado():
    empleados = []

    def __init__(self, datos, id, nombre, direccion, edad, sueldo, rol):
        self.ID = id
        self.NOMBRE = nombre
        self.DIRECCION  = direccion
        self.EDAD = edad
        self.sueldo = sueldo
        self.ROL = rol
        datos.empleados.append(self)
        Empleado.empleados.append(self)

    def __str__(self):
        return "Nombre: " + self.NOMBRE + "/id: " + str(self.ID)
    
    @staticmethod
    def generarNombre():
        x = randint(1, 70)
        y = randint(1, 70)
        nombre = Nombre.getNombre(x)
        apellido = Apellido.getNombre(y)
        return nombre + " " + apellido

    @staticmethod
    def generarDocumento():
        bien = False
        while bien == False:
            x = randint(10000, 99999)
            bien = Empleado.verificar(x)
        return x
    
    @staticmethod
    def verificar(num):
        for i in Empleado.empleados:
            if i.ID == num: return False
        return True
    
    @staticmethod
    def despedir(empleado):
        Empleado.empleados.remove(empleado)

    @staticmethod
    def getPersonal(): return Empleado.empleados

    @staticmethod
    def setPersonal(personal): Empleado.empleados = personal

    def getId(self): return self.ID

    def getNombre(self): return self.NOMBRE

    def getDIreccion(self): return self.DIRECCION

    def getEdad(self): return self.EDAD

    def getSueldo(self): return self.sueldo

    def getRol(self): return self.ROL

    def setSueldo(self, nuevo): self.sueldo = nuevo