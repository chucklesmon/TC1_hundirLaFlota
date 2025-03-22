import random

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

                if tablero_jugador.tablero_disparos[fila, columna] != "O":
                    break  # Coordenada válida
                else:
                    print("Ya has disparado ahí. Elige otra coordenada.")
            except ValueError:
                print("Entrada inválida. Introduce números entre 0 y 9.")
                continue

        # Comprobar impacto en el tablero de la máquina
        if tablero_maquina.tablero_barcos[fila, columna] == 1:
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
        lista_posiciones_maquina.remove((fila, columna))  # Eliminar posición usada
        print(f"La máquina dispara a ({fila}, {columna})")

        if tablero_jugador.tablero_barcos[fila, columna] == 1:
            print("La máquina te ha dado!")
            tablero_jugador.tablero_barcos[fila, columna] = "X"
            actualizar_tablero(tablero_jugador, tablero_maquina)  # Llamada a la función de Alejandro
            return turno_jugador  # La máquina sigue si acierta
        else:
            print("La máquina falló.")
            tablero_jugador.tablero_barcos[fila, columna] = "O"
            actualizar_tablero(tablero_jugador, tablero_maquina)  # Llamada a la función de Alejandro
            return not turno_jugador  # Cambia el turno si falla