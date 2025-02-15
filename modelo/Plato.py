class Plato:
    
    def __init__(self, nombre, precio, id):
        self.ID = id
        self.nombre = nombre
        self.precio = precio
    
    def getId(self): return self.ID

    def getNombre(self): return self.nombre

    def getPrecio(self): return self.precio

    def __str__(self):
        return self.nombre + ": $" + str(self.precio)