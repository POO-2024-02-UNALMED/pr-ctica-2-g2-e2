import sys
from typing import List

class Cliente:
    def __init__(self, id: int, nombre: str, direccion: str, telefono: str):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.puntos = 0
        self.historial_pedidos = []
    
    def get_id(self):
        return self.id
    
    def set_id(self, id: int):
        self.id = id
    
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre: str):
        self.nombre = nombre
    
    def get_direccion(self):
        return self.direccion
    
    def set_direccion(self, direccion: str):
        self.direccion = direccion
    
    def get_telefono(self):
        return self.telefono
    
    def set_telefono(self, telefono: str):
        self.telefono = telefono
    
    def get_puntos(self):
        return self.puntos
    
    def set_puntos(self, puntos: int):
        self.puntos = puntos
    
    def get_historial_pedidos(self):
        return self.historial_pedidos
    
    def set_historial_pedidos(self, historial_pedidos: List):
        self.historial_pedidos = historial_pedidos
    
    def agregar_pedido(self, pedido):
        self.historial_pedidos.append(pedido)
    
    def dar_calificacion(self, mesero, chef, calificacion):
        if calificacion < 1:
            calificacion = 1
        if calificacion > 5:
            calificacion = 5
        
        mesero.setCalificacion(calificacion)
        mesero.ganarPuntos(calificacion)
        chef.setCalificacion(calificacion)
        chef.ganarPuntos(calificacion)
    
    def sumar_puntos(self, suma: int):
        if suma in [1, 2, 3]:
            self.puntos += suma
    
    def reclamar_puntos(self, precio: float):
        while True:
            try:
                respuesta = int(input("Tiene un descuento disponible. ¿Desea reclamarlo? 1) Sí 2) No: "))
                if respuesta in [1, 2]:
                    break
                print("Por favor, ingrese 1 para Sí o 2 para No.")
            except ValueError:
                print("Entrada no válida. Ingrese un número válido.")
        
        if respuesta == 1:
            print("Descuento reclamado.")
            precio -= precio * 0.2
            self.puntos -= 20
        else:
            print("Descuento guardado.")
        return precio
    
    def __str__(self):
        return self.nombre
