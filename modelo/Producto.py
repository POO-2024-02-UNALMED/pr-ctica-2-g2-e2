class Producto:
    def __init__(self, id: int, nombre: str, precio: float, stock: int):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def get_id(self):
        return self.id
    
    def get_nombre(self):
        return self.nombre
    
    def get_precio(self):
        return self.precio
    
    def get_stock(self):
        return self.stock
    
    def actualizar_stock(self, cantidad: int):
        nuevo_stock = self.stock - cantidad
        if nuevo_stock < 0:
            raise ValueError("No hay suficiente stock para el producto.")
        self.stock = nuevo_stock
    
    def __str__(self):
        return f"Producto(id={self.id}, nombre='{self.nombre}', precio={self.precio}, stock={self.stock})"
