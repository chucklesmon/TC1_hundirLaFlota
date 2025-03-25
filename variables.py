# Booleano que controla si se está jugando o no
jugando = True

# Boolano que comprueba en que turno estamos, necesario para la funcion Disparo
turno_jugador = True

# Variables para iniciar los tableros de ambos jugadores
tablero_jugador = []
tablero_maquina = []

# Variables para iniciar los tableros donde se reflejaran los disparos 
tablero_disparos_jugador = []
tablero_disparos_maquina = []

# Lista de posiciones donde puede disparar la máquina
lista_posiciones_maquina = [(i, j) for i in range(10) for j in range(10)]

# Simbolos para hacer la visualizacion mas clara
SIMBOLOS = {"agua": "🌊", "impacto": "🔥", "vacío": "⬜", "barco": "🚢"}


