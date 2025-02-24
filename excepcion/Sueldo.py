class Sueldo(Exception):
    def __init__(self, sueldo):
        self.sueldo = sueldo
    
    def mensaje(self):
        if self.sueldo < 1500000:
            return "$" + str(self.sueldo) + " es menos del salario mínimo($1500000)"
        if self.sueldo > 2300000:
            return "$" + str(self.sueldo) + " es demasiado, no podemos permitirnos pagarle más de 2300000"