from clases import *
from funciones import *
#import clases
#import funciones
import numpy as np
import random

tablero_JP = Tablero(10).crear_tablero()
tablero_MP = tablero_JP.copy()
tablero_JD = tablero_JP.copy()
tablero_MD = tablero_JP.copy()
print(tablero_JP)

flota = colocar_barcos(tablero_JP)
