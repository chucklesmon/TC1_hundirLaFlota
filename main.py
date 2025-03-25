import funciones as f
import variables as v

# Inicia los tableros y los barcos
f.setup_partida() 

# Bucle que inicializa la partida
while v.jugando:
    f.disparo(v.tablero_jugador, v.tablero_maquina, v.lista_posiciones_maquina)





