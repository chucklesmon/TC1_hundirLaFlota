import numpy as np
import variables as v

class Tablero:
       
    def __init__(self, lado = 10):
        self.ancho = lado
        self.alto = lado

    def crear_tablero(self):
        nuevo_tablero = np.full((self.ancho, self.alto), v.SIMBOLOS["vacío"])
        return nuevo_tablero
        

    