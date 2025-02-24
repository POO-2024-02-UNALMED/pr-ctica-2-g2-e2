class Repartidor:
    def __init__(self, id: int, nombre: str, is_disponible: bool):
        self.id = id
        self.costo_envio = 0.0
        self.nombre = nombre
        self.disponible = is_disponible
        self.calificacion_promedio = 0.0
        self.zonas_asignadas = []
        self.barrios_asignados = []

    # Getters y Setters
    def get_costo_envio(self):
        return self.costo_envio
    
    def get_zonas_asignadas(self):
        return self.zonas_asignadas

    def set_zonas_asignadas(self, zonas: list):
        self.zonas_asignadas = zonas

    def get_id(self):
        return self.id

    def set_id(self, id: int):
        self.id = id

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre: str):
        self.nombre = nombre
        
    def is_disponible(self):
        return self.disponible 

    def set_disponible(self, disponible: bool):
        self.disponible = disponible 

    def asignar_zona(self, zona):
        self.zonas_asignadas.append(zona)

    def get_calificacion_promedio(self):
        return self.calificacion_promedio

    def set_calificacion_promedio(self, calificacion: float):
        self.calificacion_promedio = calificacion

    def get_barrios_asignados(self):
        return self.barrios_asignados

    def set_barrios_asignados(self, barrios: list):
        self.barrios_asignados = barrios

    def __str__(self):
     return f"{self.nombre}" 