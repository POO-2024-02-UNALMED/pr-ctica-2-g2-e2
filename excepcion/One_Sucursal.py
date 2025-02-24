class One_Sucursal(Exception):
    def __init__(self,  sucursal):
        self.sucursal = sucursal
        print("Error, no hay más sucursales")
    
    def mensaje(self):
        print("La sucursal de " + self.sucursal + " es la única que continúa abierta, no podemos cerrar más")