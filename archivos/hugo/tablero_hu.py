import numpy as np

class Tablero:
       
    def __init__(self, lado = 10):
        self.ancho = lado
        self.alto = lado

    def crear_tablero(self):
        nuevo_tablero = np.full((self.ancho, self.alto), "\u007E")
        return nuevo_tablero
        

    