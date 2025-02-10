class Mesa:
    
    def __init__(self, id, capacidad, sucursal):
        self.ID = id
        self.CAPACIDAD = capacidad
        self.SUCURSAL = sucursal
        self.unida = False
        self.reservada = False

    def getId(self): return self.ID

    def getCapacidad(self): return self.CAPACIDAD

    def getSucursal(self): return self.SUCURSAL

    def estaUnidad(self): return self.unida

    def estaReservada(self): return self.reservada

    def setReserva(self, boolean): self.reservada = boolean

    def setUnion(self, boolean): self.unida = boolean