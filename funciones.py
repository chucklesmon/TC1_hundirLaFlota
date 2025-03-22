import barco as b
import numpy as np
import random
import tablero as t

"""
funciones hugo
"""
# H: Inicia lo necesario para la partida, genera tableros y coloca los barcos, la generacion de barcos habría que cambiarla por una funcion generar_flota
# para poder generar los barcos que quieras
def setup_partida():
    tablero_jugador = t.Tablero().crear_tablero()
    tablero_maquina = t.Tablero().crear_tablero()
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

    flota = colocar_barcos(tablero_jugador)
    flota_maquina = colocar_barcos(tablero_maquina)

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

"""
funcion para generar barcos e ir probando, teniendo la clase barco no es necesaria, lo dejo comentado hasta que este funcionando el juego


def crear_barcos():
    #Función temporal para pruebas.
    #Habrá que ensamblar con los objetos de la clase barco
    barco1 = [0,0,0,0]
    barco2 = [0,0,0]
    barco3 = [0,0,0]
    barco4 = [0,0]
    barco5 = [0,0]
    barco6 = [0,0]
    barco7 = [0]
    barco8 = [0]
    barco9 = [0]
    barco10 = [0]
    nueva_flota = [barco1, barco2, barco3, barco4, barco5, barco6, barco7, barco8, barco9, barco10]
    return nueva_flota
"""

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
                if tablero_juego[coord_f + indice, coord_c] == "\u1403":
                    posible_form = False
        elif curso == 2:
            if coord_c + longitud <= 9:
                if tablero_juego[coord_f, coord_c + indice] == "\u1403":
                    posible_form = False
    
    #Devuelve el booleano de la posibilidad
    return posible_form


def comprobar_dist_barcos(longitud, coord_f, coord_c, curso, tablero_juego):
    #Inicializa la variable booleana que se va a devolver
    posible_esp = True

    #Comprueba las casillas adyacentes al extremo del barco
    if curso == 1:                
        if coord_f + longitud <= 9:
            if tablero_juego[coord_f - 1, coord_c] == "\u1403" or tablero_juego[coord_f + longitud, coord_c] == "\u1403":
                posible_esp = False
    elif curso == 2:
        if coord_c + longitud <= 9:
            if tablero_juego[coord_f, coord_c - 1] == "\u1403" or tablero_juego[coord_f, coord_c + longitud] == "\u1403":
                posible_esp = False
    
    #Comprueba las casillas adyacentes a la longitud del barco
    for indice in range(longitud):
        if curso == 1:
            if tablero_juego[coord_f, coord_c + 1] == "\u1403" or tablero_juego[coord_f, coord_c - 1] == "\u1403":
                posible_esp = False
        elif curso == 2:
            if tablero_juego[coord_f + 1, coord_c] == "\u1403" or tablero_juego[coord_f - 1, coord_c] == "\u1403":
                posible_esp = False 

    #Devuelve el booleano de la posibilidad
    return posible_esp


def situar_en_tablero(longitud, coord_f, coord_c, curso, tablero_juego):
    #Marca cada casilla de la eslora según el rumbo
    for indice in range(longitud):
        if curso == 1:
            tablero_juego[coord_f + indice, coord_c] = "\u1403"
        elif curso == 2:
            tablero_juego[coord_f, coord_c + indice] = "\u1403"
    
    #Devuelve el tablero con el barco
    return tablero_juego


"""
funciones cecilia
"""

def disparo(turno_jugador, tablero_jugador, tablero_maquina, lista_posiciones_maquina, actualizar_tablero):
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

    if turno_jugador:
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

                if tablero_jugador.tablero_disparos[fila, columna] != "0":  # H: tablero_disparos entiendo que es el tablero donde se van reflejando los disparos,
                    break  # Coordenada válida                                   pero creo que eso seria un .copy() del tablero, no tengo claro donde inicializarlo    
                else:                                                       #    (ni si estoy entiendiendo bien a qué quieres referenciar, no se que quieres representar con el 0)
                    print("Ya has disparado ahí. Elige otra coordenada.")
            except ValueError:
                print("Entrada inválida. Introduce números entre 0 y 9.")
                continue

        # Comprobar impacto en el tablero de la máquina
        if tablero_maquina.tablero_barcos[fila, columna] == 1: # H: misma duda que con tablero_disparos
            print("¡Impacto!")
            tablero_maquina.tablero_barcos[fila, columna] = "X" 
            tablero_jugador.tablero_disparos[fila, columna] = "X"
            actualizar_tablero(tablero_jugador, tablero_maquina)  # Llamada a la función de Alejandro
            return turno_jugador  # Sigue el turno si acierta
        else:
            print("Agua...")
            tablero_jugador.tablero_disparos[fila, columna] = "O"
            actualizar_tablero(tablero_jugador, tablero_maquina)  # Llamada a la función de Alejandro
            return not turno_jugador  # Cambia el turno si falla

    else:
        # Turno de la máquina
        fila, columna = random.choice(lista_posiciones_maquina) 

        # H: entiendo que lista_posiciones_maquina es la lista de la que hablamos donde estarían todas las posibilidades de disparo de la maquina
        #    esa lista no se si no esta hecha o si no la estoy viendo (o si te refieres a otra lista)

        lista_posiciones_maquina.remove((fila, columna))  # Eliminar posición usada
        print(f"La máquina dispara a ({fila}, {columna})")

        if tablero_jugador.tablero_barcos[fila, columna] == 1:
            print("La máquina te ha dado!")
            tablero_jugador.tablero_barcos[fila, columna] = "X"
            actualizar_tablero(tablero_jugador, tablero_maquina)  # Llamada a la función de Alejandro # H: no tengo funciones de Alejandro
            return turno_jugador  # La máquina sigue si acierta
        else:
            print("La máquina falló.")
            tablero_jugador.tablero_barcos[fila, columna] = "O"
            actualizar_tablero(tablero_jugador, tablero_maquina)  # Llamada a la función de Alejandro
            return not turno_jugador  # Cambia el turno si falla