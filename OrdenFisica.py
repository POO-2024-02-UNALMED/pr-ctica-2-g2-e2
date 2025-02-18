from excepcion import entrada
from modelo.Chef import Chef

class OrdenFisica:
    def __init__(self, mesa, cliente, mesero, sucursal):
        self.mesa = mesa
        self.CLIENTE = cliente
        self.mesero = mesero
        self.SUCURSAL = sucursal
    
    def getMesa(self): return self.mesa

    def getCliente(self): return self.CLIENTE

    def getMesero(self): return self.mesero

    def getSucursal(self): return self.SUCURSAL

    def setMesa(self, mesa): self.mesa = mesa

    def setMesero(self, mesero): self.mesero = mesero

    def hacerPedido(self):
        print("Ingrese cuántos platos desea ordenar")
        cantPer = entrada()
        while cantPer <= 0:
            print("El número de platos debe ser mayor a 0")
            cantPer = entrada()
        platoF = []
        print(self.SUCURSAL.mostrarMenu())
        if cantPer < 6 and cantPer > 0:
            i = 0
            plato = 0
            while i < cantPer:
                print("¿Qué plato desea ordenar?")
                plato = entrada()
                if plato < 1 or plato > len(self.SUCURSAL.getMenu()):
                    print("Opción no disponible")
                    continue
                for plato2 in self.SUCURSAL.getMenu():
                    if plato2.getId() == plato:
                        print("Pedido confirmado de " + plato2.getNombre())
                        platoF.append(plato2)
                i += 1
        if cantPer >= 6:
            plato = 0
            print("La cantidad de platos es mayor a 5, por lo tanto se le dará el mismo plato a todos los invitados, escoja cuál")
            plato = entrada()
            while plato < 1 or plato > len(self.SUCURSAL.getMenu()):
                print("Opción no disponible")
                plato = entrada()
            for i in range(cantPer):
                for plato2 in self.SUCURSAL.getMenu():
                    if plato2.getId() == plato:
                        platoF.append(plato2)
        return [self.mesa, self.CLIENTE, self.mesero, self.SUCURSAL, cantPer, Chef.asignar(self.SUCURSAL), platoF]