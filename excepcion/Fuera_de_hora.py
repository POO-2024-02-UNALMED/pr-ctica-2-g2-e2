class Fuera_de_hora:
    def __init__(self, hora):
        self.hora  = hora
        self.mensaje()
        
    def mensaje(self):
        print("Error, {} está fuera de horario de atención".format(self.hora))
        