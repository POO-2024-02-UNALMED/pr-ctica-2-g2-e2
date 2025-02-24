class Edad(Exception):
    def __init__(self, edad):
        self.edad = edad
    
    def mensaje(self):
        if self.edad < 18:
            return "Esta es una empresa seria, aquí no se acepta el trabajo infantil"
        if self.edad > 70:
            return "NO podemos contratar al alguien de tan avanzada edad"