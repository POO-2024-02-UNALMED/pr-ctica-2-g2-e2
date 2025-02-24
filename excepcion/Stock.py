import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..','excepcion')))
from Agotado import Agotado

class Stock(Agotado):

    def __init__(self, producto):
        super().__init__()
        self.producto = producto
        self.mensaje()
    
    def mensaje(self):
        print("los ingredientes necesarios para poder cocinar el producto: {}".format(self.producto))
        print("Por favor escoja otro")