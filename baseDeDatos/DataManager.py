import threading
from typing import List

class DataManager:
    def __init__(self):
        self.clientes = []
        self.productos = []
        self.repartidores = []
        self.pedidos = []
        self.zonas = []
        self.incidencias = []
        self.domicilios = []
        self.admins = []
        self.next_pedido_id = threading.Lock()
        self.next_incidencia_id = threading.Lock()
        self.sucursales = []
        self.ciudad = [None] * 16
        self.reservaciones = []
        self.cargar_datos_prueba()

    def borrar_datos(self):
        self.clientes.clear()
        self.productos.clear()
        self.repartidores.clear()
        self.pedidos.clear()
        self.zonas.clear()
        self.incidencias.clear()
        self.domicilios.clear()
        self.admins.clear()
        self.sucursales.clear()
        self.ciudad = [None] * 16
        print("Todos los datos han sido borrados correctamente.")

    def cargar_datos_prueba(self):
        self.zonas.extend([
            {"id": 1, "nombre": "Centro", "costo_envio": 2.99},
            {"id": 2, "nombre": "Norte", "costo_envio": 3.99},
            {"id": 3, "nombre": "Sur", "costo_envio": 3.99},
        ])
        
        self.repartidores.extend([
            {"id": 1, "nombre": "Juan Pérez", "calificacion": 4.5},
            {"id": 2, "nombre": "María García", "calificacion": 4.8},
        ])
        
        self.productos.extend([
            {"id": 1, "nombre": "Pizza Margherita", "precio": 12.99, "stock": 20},
            {"id": 2, "nombre": "Hamburguesa Clásica", "precio": 8.99, "stock": 15},
            {"id": 3, "nombre": "Ensalada César", "precio": 7.99, "stock": 10},
            {"id": 4, "nombre": "Pasta Alfredo", "precio": 10.99, "stock": 12},
            {"id": 5, "nombre": "Refresco", "precio": 2.99, "stock": 50},
        ])
        
        self.admins.extend([
            {"nombre": "Lionel Messi", "id": 12345},
            {"nombre": "Elena Nito", "id": 10453},
            {"nombre": "Alma Marcela Gozo", "id": 42012},
        ])
        
        print("Datos de prueba cargados correctamente.")
    
    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)
    
    def buscar_cliente_por_id(self, id):
        return next((cliente for cliente in self.clientes if cliente["id"] == id), None)
    
    def agregar_producto(self, producto):
        self.productos.append(producto)
    
    def buscar_producto_por_id(self, id):
        return next((producto for producto in self.productos if producto["id"] == id), None)
    
    def verificar_disponibilidad_producto(self, producto_id):
        producto = self.buscar_producto_por_id(producto_id)
        return producto is not None and producto["stock"] > 0
    
    def actualizar_stock_producto(self, producto_id, cantidad):
        producto = self.buscar_producto_por_id(producto_id)
        if producto:
            producto["stock"] += cantidad
    
    def agregar_repartidor(self, repartidor):
        self.repartidores.append(repartidor)
    
    def asignar_repartidor_disponible(self):
        return next((repartidor for repartidor in self.repartidores if repartidor["calificacion"] > 4), None)
    
    def agregar_pedido(self, pedido):
        with self.next_pedido_id:
            pedido["id"] = len(self.pedidos) + 1
        self.pedidos.append(pedido)
    
    def buscar_pedido_por_id(self, id):
        return next((pedido for pedido in self.pedidos if pedido["id"] == id), None)
    
    def get_pedidos_vigentes(self):
        return [pedido for pedido in self.pedidos if pedido.get("estado") not in ["Cancelado", "Entregado"]]
    
    def get_ciudad(self):
        return self.ciudad
    
    def add_sucursal(self, sucursal):
        self.sucursales.append(sucursal)
    
    def get_sucursales(self):
        return self.sucursales
