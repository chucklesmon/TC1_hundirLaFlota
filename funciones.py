import barco as b
import numpy as np
import random
import tablero as t
import pandas as pd
import variables as v

"""
funciones hugo
"""
# H: Inicia lo necesario para la partida, genera tableros y coloca los barcos, la generacion de barcos habría que cambiarla por una funcion generar_flota
# para poder generar los barcos que quieras
def setup_partida():
    v.tablero_jugador = t.Tablero().crear_tablero()
    v.tablero_maquina = t.Tablero().crear_tablero()
    v.tablero_disparos_jugador = t.Tablero().crear_tablero()
    v.tablero_disparos_maquina = t.Tablero().crear_tablero()
    barco_1 = b.Barco(4)
    barco_2 = b.Barco(3)
    barco_3 = b.Barco(3)
    barco_4 = b.Barco(2)
    barco_5 = b.Barco(2)
    barco_6 = b.Barco(2)
    barco_7 = b.Barco(1)
    barco_8 = b.Barco(1)
    barco_9 = b.Barco(1)
    barco_10 = b.Barco(1)

    flota = colocar_barcos(v.tablero_jugador)
    flota_maquina = colocar_barcos(v.tablero_maquina)

    print(flota) # H: comprobacion para ver si monta el tablero bien
    print(flota_maquina) # H: comprobacion para ver si monta el tablero bien

    return flota, flota_maquina

"""
funciones antonio
"""
def colocar_barcos(tablero_base):
    #Llama a la función que crea los barcos para colocar
    tablero_marcas = tablero_base
    flota_creada = b.Barco.devolver_flota() # H: modificacion para coger la lista de barcos

    #Convoca uno por uno a todos los barcos de la flota
    for elem in flota_creada:
        #Determina la eslora del barco
        eslora = len(elem.barco) # H: modificacion por usar objetos
        en_tablero = False
        sin_colision = False
        con_distancia = False

        while en_tablero == False or sin_colision == False or con_distancia == False:
            #Random de coordenadas
            coordenada_fila = np.random.randint(0,9)
            coordenada_columna = np.random.randint(0,9)
            
            #Random de orientación
            rumbo = np.random.randint(1,100) #Vertical:1, Horizontal:2
            if rumbo <= 50:
                rumbo = 1
            else:
                rumbo = 2
                
            #Llama a la función de comprobar dimensiones
            en_tablero = comprobar_bordes(eslora, coordenada_fila, coordenada_columna, rumbo, tablero_marcas)

            #Llama a la función de comprobar colisión
            sin_colision = comprobar_colision(eslora, coordenada_fila, coordenada_columna, rumbo, tablero_marcas)
            
            #Llama a la función para no pegar unos barcos con otros
            con_distancia = comprobar_dist_barcos(eslora, coordenada_fila, coordenada_columna, rumbo, tablero_marcas)

        #Llama a la función de ubicar en tablero
        tablero_base = situar_en_tablero(eslora, coordenada_fila, coordenada_columna, rumbo, tablero_marcas) #if en_tablero == True and sin_colision == True:  
        
    #Devuelve tablero_flota
    return tablero_base

def comprobar_bordes(longitud, coord_f, coord_c, curso, tablero_juego):
    #Calcula la longitud que hay que sumar a la coordenada para ver si entra en tablero
    longitud_comp = longitud - 1

    #Suma la longitud a la coordenada, según el eje de rumbo
    if curso == 1:
        coord_ff = coord_f + longitud_comp
        coord_cc = coord_c
    elif curso == 2:
        coord_cc = coord_c + longitud_comp
        coord_ff = coord_f
    
    #Comprueba si está dentro de los límites del tablero
    if coord_ff > (tablero_juego[0].size - 1) or coord_ff < 0: 
        posible_tab = False
    elif coord_cc > (tablero_juego[0].size - 1) or coord_cc < 0:
        posible_tab = False
    else:
        posible_tab = True
    
    #Devuelve el booleano de la posibilidad
    return posible_tab


def comprobar_colision(longitud, coord_f, coord_c, curso, tablero_juego): 
    #Inicializa la variable booleana que se va a devolver
    posible_form = True

    #Comprueba en cada casilla de la eslora según el rumbo
    for indice in range(longitud):
        if curso == 1:
            if coord_f + longitud <= 9:
                if tablero_juego[coord_f + indice, coord_c] == v.SIMBOLOS["barco"]:
                    posible_form = False
        elif curso == 2:
            if coord_c + longitud <= 9:
                if tablero_juego[coord_f, coord_c + indice] == v.SIMBOLOS["barco"]:
                    posible_form = False
    
    #Devuelve el booleano de la posibilidad
    return posible_form


def comprobar_dist_barcos(longitud, coord_f, coord_c, curso, tablero_juego):
    #Inicializa la variable booleana que se va a devolver
    posible_esp = True

    #Comprueba las casillas adyacentes al barco, salvo los extremos
    indice = -1
    while indice < longitud + 1:
        if curso == 1 and coord_f + indice <= 9:
            if tablero_juego[coord_f + indice, coord_c - 1] == v.SIMBOLOS["barco"] or tablero_juego[coord_f + indice, coord_c + 1] == v.SIMBOLOS["barco"]:
                posible_esp = False
        elif curso == 2 and coord_c + indice <= 9:
            if tablero_juego[coord_f - 1, coord_c + indice] == v.SIMBOLOS["barco"] or tablero_juego[coord_f + 1, coord_c + indice] == v.SIMBOLOS["barco"]:
                posible_esp = False 
        indice += 1

    #Comprueba las casillas adyacentes al extremo del barco
    if curso == 1:
        if coord_f != 0 and coord_f + longitud <= 9:
            if tablero_juego[coord_f - 1, coord_c] == v.SIMBOLOS["barco"] or tablero_juego[coord_f + longitud, coord_c] == v.SIMBOLOS["barco"]:
                posible_esp = False
        elif coord_f == 0:
            if tablero_juego[coord_f + longitud, coord_c] == v.SIMBOLOS["barco"]:
                posible_esp = False
        elif coord_f + longitud > 9:
            posible_esp = False
    elif curso ==2:
        if coord_c != 0 and coord_c + longitud <= 9:
            if tablero_juego[coord_f, coord_c - 1] == v.SIMBOLOS["barco"] or tablero_juego[coord_f, coord_c + longitud] == v.SIMBOLOS["barco"]:
                posible_esp = False
        elif coord_c == 0:
            if tablero_juego[coord_f, coord_c + longitud] == v.SIMBOLOS["barco"]:
                posible_esp = False
        elif coord_c + longitud > 9:
            posible_esp = False

    #Devuelve el booleano de la posibilidad
    return posible_esp


def situar_en_tablero(longitud, coord_f, coord_c, curso, tablero_juego):
    #Marca cada casilla de la eslora según el rumbo
    for indice in range(longitud):
        if curso == 1:
            tablero_juego[coord_f + indice, coord_c] = v.SIMBOLOS["barco"]
        elif curso == 2:
            tablero_juego[coord_f, coord_c + indice] = v.SIMBOLOS["barco"] #"\u220E" Pata tachar
    
    #Devuelve el tablero con el barco
    return tablero_juego


"""
funciones cecilia
"""

def disparo(tablero_jugador, tablero_maquina, lista_posiciones_maquina):
    """
    Maneja la lógica de los disparos de los jugadores y la máquina, incluyendo el control de turnos.
    - Si es turno del jugador, pide coordenadas manualmente.
    - Si es turno de la máquina, elige una coordenada aleatoria de la lista de posiciones.
    - Evita disparos repetidos.
    - Actualiza los tableros después de cada disparo.
    - Permite al jugador salir del juego.
    - Llama a la función `actualizar_tablero` al final del disparo para reflejar los cambios visualmente.
    """

    # En general no la probe mucho porque faltan cosa de las que depende la funcion y porque hay un par de variables que no tengo claro del todo lo que 
    # se espera y no se bien como probarlo


    if v.turno_jugador:
        # Turno del jugador
        while True:
            entrada = input("Introduce la fila (0-9) o escribe 'salir' para terminar: ").strip().lower()
            if entrada == "salir":
                confirmacion = input("¿Seguro que quieres salir? (s/n): ").strip().lower()
                if confirmacion == "s":
                    print("¡Gracias por jugar!")
                    exit()
                else:
                    continue  # Volver a pedir coordenadas

            try:
                fila = int(entrada)
                columna = int(input("Introduce la columna (0-9): ").strip())
                if not (0 <= fila < 10 and 0 <= columna < 10):
                    print("Coordenadas fuera de rango. Inténtalo de nuevo.")
                    continue

                if v.tablero_disparos_jugador[fila, columna] != v.SIMBOLOS["agua"]:  # H: cuadrado blanco
                    break  # Coordenada válida                                   
                else:                                                       
                    print("Ya has disparado ahí. Elige otra coordenada.")
            except ValueError:
                print("Entrada inválida. Introduce números entre 0 y 9.")
                continue

        # Comprobar impacto en el tablero de la máquina
        if v.tablero_maquina[fila, columna] == v.SIMBOLOS["barco"]: # H: misma duda que con tablero_disparos
            print("¡Impacto!")
            v.tablero_maquina[fila, columna] = v.SIMBOLOS["impacto"] # fuego
            v.tablero_disparos_jugador[fila, columna] = v.SIMBOLOS["impacto"] # fuego
            mostrar_tablero(v.tablero_jugador)  # Llamada a la función de Alejandro
            mostrar_tablero(v.tablero_disparos_jugador)
            mostrar_tablero(v.tablero_maquina)  # Llamada a la función de Alejandro
            mostrar_tablero(v.tablero_disparos_maquina)

            comprobar_victoria(v.tablero_maquina)

            v.turno_jugador = True
            return v.turno_jugador  # Sigue el turno si acierta
        else:
            print("Agua...")
            v.tablero_disparos_jugador[fila, columna] = v.SIMBOLOS["agua"] # agua
            v.tablero_maquina[fila, columna] = v.SIMBOLOS["agua"]
            mostrar_tablero(v.tablero_jugador)  # Llamada a la función de Alejandro
            mostrar_tablero(v.tablero_disparos_jugador)
            mostrar_tablero(v.tablero_maquina)  # Llamada a la función de Alejandro
            mostrar_tablero(v.tablero_disparos_maquina) 
            v.turno_jugador = False
            return v.turno_jugador  # Cambia el turno si falla

    else:
        # Turno de la máquina
        fila, columna = random.choice(lista_posiciones_maquina) 

        # H: entiendo que lista_posiciones_maquina es la lista de la que hablamos donde estarían todas las posibilidades de disparo de la maquina
        #    esa lista no se si no esta hecha o si no la estoy viendo (o si te refieres a otra lista)

        lista_posiciones_maquina.remove((fila, columna))  # Eliminar posición usada
        print(f"La máquina dispara a ({fila}, {columna})")

        if v.tablero_jugador[fila, columna] == v.SIMBOLOS["barco"]: # barco
            print("La máquina te ha dado!")
            v.tablero_jugador[fila, columna] = v.SIMBOLOS["impacto"]
            mostrar_tablero(v.tablero_jugador)  # Llamada a la función de Alejandro
            mostrar_tablero(v.tablero_disparos_jugador)
            mostrar_tablero(v.tablero_maquina)  # Llamada a la función de Alejandro
            mostrar_tablero(v.tablero_disparos_maquina)  # Llamada a la función de Alejandro

            comprobar_victoria(v.tablero_jugador)



            v.turno_jugador = False 
            return v.turno_jugador  # La máquina sigue si acierta
        else:
            print("La máquina falló.")
            tablero_jugador[fila, columna] = v.SIMBOLOS["agua"]
            mostrar_tablero(v.tablero_jugador)  # Llamada a la función de Alejandro
            mostrar_tablero(v.tablero_disparos_jugador)
            mostrar_tablero(v.tablero_maquina)  # Llamada a la función de Alejandro
            mostrar_tablero(v.tablero_disparos_maquina) 
            v.turno_jugador = True
            return v.turno_jugador  # Cambia el turno si falla
        

"""
funciones alejandro
"""

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
    tablero[fila, columna] = v.SIMBOLOS["impacto"] if impacto else v.SIMBOLOS["agua"]
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


def comprobar_victoria(tablero):
    """
    Comprueba si algun jugador ganó la partida, de hacerlo pasa a False el booleano del bucle del principal
    """

    if not np.any(tablero == v.SIMBOLOS["barco"]): # comprueba que no haya barcos en el tablero
        if v.turno_jugador == True:
            print("Enhorabuena has ganao campeon")
        else:
            print("te gano la maquina ")

        v.jugando = False
    

    

