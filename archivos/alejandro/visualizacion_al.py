

import numpy as np
import pandas as pd

# Diccionario para hacer la visualización más estética
SIMBOLOS = {"agua": "🌊", "impacto": "🔥", "vacío": "⬜"}

def marcar_disparo(tablero, coordenada, impacto):
    """
    Marca un disparo en el tablero.
    
    Parámetros:
    - tablero: np.array de strings con el tablero del jugador.
    - coordenada: tupla (fila, columna) con la posición disparada.
    - impacto: booleano (True si impactó un barco, False si es agua).
    
    Retorna:
    - El tablero actualizado.
    """
    fila, columna = coordenada
    tablero[fila, columna] = SIMBOLOS["impacto"] if impacto else SIMBOLOS["agua"]
    return tablero

def mostrar_tablero(tablero):
    """
    Muestra el tablero en forma de tabla bonita usando Pandas.
    """
    df = pd.DataFrame(tablero, index=[f"{i}" for i in range(len(tablero))], 
                      columns=[f"{j}" for j in range(len(tablero[0]))])
    
    print("\nTablero actualizado:\n")
    # Muestra el tablero como tabla
    print("    " + "   ".join(f"{i:2}" for i in df.columns))

    # Imprimir DataFrame con formato corregido
    for i, row in df.iterrows():
        print(f"{i:2} " + "  ".join(str(x).ljust(2) for x in row))
    
# 📌 Ejemplo de uso
tablero = np.full((10,10), SIMBOLOS["vacío"], dtype=str)  # Crear un tablero vacío

# Simulamos algunos disparos
tablero = marcar_disparo(tablero, (4, 3), impacto=True)  # Impacto en (2,3)
tablero = marcar_disparo(tablero, (0, 1), impacto=False)  # Agua en (1,1)

# Mostramos el tablero con Pandas
mostrar_tablero(tablero)