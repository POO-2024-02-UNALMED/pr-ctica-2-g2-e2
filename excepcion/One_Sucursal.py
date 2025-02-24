class One_Sucursal(Exception):
    def __init__(self,  sucursal):
        self.sucursal = sucursal
    
    def mensaje(self):
        return "La sucursal de " + self.sucursal + " es la única que continúa abierta, no podemos cerrar más"