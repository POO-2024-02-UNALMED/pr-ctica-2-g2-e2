import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..','excepcion')))
from Agotado import Agotado

class Espacio(Agotado):

    def __init__(self, cantidad):
        super().__init__()
        self.mensaje(cantidad)
    
    def mensaje(self, cantidad):
        print("las mesas que complen con sus necesidades: {} ubicaciones".format(cantidad))
        print("Intente de nuevo en otro momento")
Espacio(12)