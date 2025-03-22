import numpy as np
import random


def colocar_barcos(tablero_base):
    #Llama a la función que crea los barcos para colocar
    tablero_marcas = tablero_base
    flota_creada = crear_barcos()

    #Convoca uno por uno a todos los barcos de la flota
    for elem in flota_creada:
        #Determina la eslora del barco
        eslora = len(elem)
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

