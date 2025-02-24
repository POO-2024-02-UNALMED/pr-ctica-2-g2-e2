import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..','modelo')))
from modelo.Administrativo import Administrativo
from modelo.Banco import Banco
from modelo.Barrio import Barrio
from modelo.Sucursal import Sucursal
from modelo.Empleado import Empleado
from modelo.Empresa import Empresa
from modelo.Producto import Producto
from modelo.Repartidor import Repartidor
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
        self.next_pedido_id = 1
        self.pedido_lock = threading.Lock()
        self.next_incidencia_id = threading.Lock()
        self.sucursales = []
        self.ciudad = []
        self.bancos = []
        self.empleados = []
        self.reservaciones = []
        self.deudas = 12000000
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
        print("Todos los datos han sido borrados correctamente.")

    def cargar_datos_prueba(self):
        self.zonas.extend([
            {"id": 1, "nombre": "Centro", "costo_envio": 2.99},
            {"id": 2, "nombre": "Norte", "costo_envio": 3.99},
            {"id": 3, "nombre": "Sur", "costo_envio": 3.99},
        ])
        
        self.repartidores.extend([
            Repartidor(id=1, nombre="Juan Pérez", is_disponible=True),
            Repartidor(id=2, nombre="María García", is_disponible=True)
        ])
        
        self.repartidores[0].set_calificacion_promedio(4.5)
        self.repartidores[1].set_calificacion_promedio(4.8)
        
        self.productos.extend([
            Producto(1, "Pizza Margherita", 12.99, 20),
            Producto(2, "Hamburguesa Clásica", 8.99, 15),
            Producto(3, "Ensalada César", 7.99, 10),
            Producto(4, "Pasta Alfredo", 10.99, 12),
            Producto(5, "Refresco", 2.99, 50),
        ])
        
        self.admins.extend([
            Administrativo("Messi", 12345, 4488123),
            Administrativo("Rosa Naranjo", 10101,98201),
            Administrativo("Gustavo Cerati", 421234,54329)
        ])
        Administrativo.admins = self.admins

        self.bancos.extend([
            Banco("Bancolombia", 7, 900000000),
            Banco("Banco de Bogotá", 9, 1300000000),
            Banco("Avevillas", 4, 400000000),
            Banco("Davivienda", 5, 700000000)
        ])
        Banco.bancos = self.bancos
        a = [-8, -4]
        b = [-4, 0]
        c = [0, 4]
        d = [4,8]

        self.ciudad.extend([
            Barrio("La Estrella", 7.99, a, d),
            Barrio("Sabaneta", 6.99, b, d, True),
            Barrio("Intagüí", 5.99, c, d),
            Barrio("Envigado", 4.99, d, d),
            Barrio("Robledo", 6.99, d, c, True),
            Barrio("Bello", 7.99, c, c),
            Barrio("Poblado", 4.99, b, c),
            Barrio("Niquía", 7.49, a, c),
            Barrio("Alpujarra", 3.99, a, b),
            Barrio("Cisneros", 3.99, b, b, True),
            Barrio("San Antonio", 3.99, c, b),
            Barrio("Parque Berrío", 3.99, d, b),
            Barrio("Prado", 4.49, d, a),
            Barrio("Caribe", 5.49, c, a),
            Barrio("Acevedo", 6.49, b, a),
            Barrio("Madera", 6.99, a, a)
            ])

        Barrio.CIUDAD = self.ciudad
        
        e =Sucursal(1, "Cisneros", 35, [-3, -3], 57000000)
        f = Sucursal(2, "Robledo", 30, [5, 3], 48000000)
        g = Sucursal(3, "Sabaneta", 30, [-2, 6], 44000000)
        e.comprarMesas(20, 10, 5, 24000000)
        f.comprarMesas(15, 10, 5, 21500000)
        g.comprarMesas(15, 10, 5, 21500000)
        for i in range(5):
            e.autoMesero(self, 18000000)
            f.autoMesero(self, 18000000)
            g.autoMesero(self, 18000000)
        for i in range(3):
            e.autoChef(self, 18000000)
            f.autoChef(self, 18000000)
            g.autoChef(self, 18000000)
        self.sucursales.extend([e, f, g])
        Sucursal.sucursales = self.sucursales
        
        Empleado.setPersonal(self.empleados)
        
        Empresa.deudas = self.deudas

        print("Datos de prueba cargados correctamente.")
    
    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)
    
    def buscar_cliente_por_id(self, id):
        return next((cliente for cliente in self.clientes if cliente.id == id), None)
    
    def agregar_producto(self, producto):
        self.productos.append(producto)
    
    def buscar_producto_por_id(self, id):
        return next((producto for producto in self.productos if producto.id == id), None)
    
    def buscar_repartidor_por_id(self, id: int) -> Repartidor:
        return next((r for r in self.repartidores if r.id == id), None)
    
    def verificar_disponibilidad_producto(self, producto_id):
        producto = self.buscar_producto_por_id(producto_id)
        return producto is not None and producto.stock > 0
    
    def actualizar_stock_producto(self, producto_id, cantidad):
        producto = self.buscar_producto_por_id(producto_id)
        if producto:
            producto.stock += cantidad 
    
    def agregar_repartidor(self, repartidor: Repartidor):
        self.repartidores.append(repartidor)
    
    def asignar_repartidor_disponible(self):
        return next((
            repartidor for repartidor in self.repartidores 
            if repartidor.is_disponible() and repartidor.get_calificacion_promedio() > 4
        ), None)
    
    def agregar_pedido(self, pedido):
        pedido.id = self.get_next_pedido_id() 
        self.pedidos.append(pedido)
        
    def buscar_pedido_por_id(self, id):
        return next((pedido for pedido in self.pedidos if pedido.id == id), None)
    
    def get_pedidos_vigentes(self):
        return [
            pedido for pedido in self.pedidos 
            if pedido.estado.descripcion not in ["Cancelado", "Entregado"]
        ]
    def get_ciudad(self):
        return self.ciudad
    
    def add_sucursal(self, sucursal):
        self.sucursales.append(sucursal)
    
    def get_sucursales(self):
        return self.sucursales
    
    def get_admins(self):
        return self.admins

    def get_productos(self):
        return self.productos
    
    def get_next_pedido_id(self) -> int:
        with self.pedido_lock:  # Bloquea para evitar race conditions
            current_id = self.next_pedido_id
            self.next_pedido_id += 1
        return current_id