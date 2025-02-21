import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..','excepcion')))
from Fuera_de_hora import Fuera_de_hora

class Hora_Pedido(Fuera_de_hora):
    def __init__(self, hora):
        super().__init__(hora)
    
    def mensaje(self):
        print("El horario de reservas estáentre 8:00-20:00")