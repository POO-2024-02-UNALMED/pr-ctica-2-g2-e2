import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..','excepcion')))
from Agotado import Agotado

class Stock(Agotado):

    def __init__(self):
        super().__init__()
        print("los productos para poder cocinar el producto solicitado")
        print("Por favor escoja otro")