

class HundirLaFlota:
    def __init__(self):
        self.dim_barcos = [2, 3, 3, 4, 5]
        self.tablero_usuario = [[" "] * 10 for _ in range(10)]
        self.tablero_pc = [[" "] * 10 for _ in range(10)]
        self.usuario_tablero_guess = [[" "] * 10 for _ in range(10)]
        self.pc_tablero_guess = [[" "] * 10 for _ in range(10)]
        self.letras_a_numeros = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}



    def jugar_el_juego(self):
        self.#funcion poner barco (self.tablero_pc)
        self.#funcion poner barco(self.tablero_usuario)
        self.#imprimir tablero maquina(self.tablero_pc)
        self.#imprimir tablero usuario(self.tablero_usuario)
        

        while True:
            # Turno Usuario
            while True:
                print('Donde quieres disparar?')
                self.#imprimir tablero usuario(self.usuario_tablero_guess)
                self.#funcion turno usuario(sel.usuario_tablero_guess)
                break
            if self.#funcion que cuenta los golpes a los barcos(self.usuario_tablero_guess) == 17:
                print("Has ganado!")
                break

            # Turno PC
            while True:
                self.#funcion turno(self.pc_tablero_guess)
                break
            self.#funcion imprimir tablero(self.pc_tablero_guess)
            if self.#funcion que cuenta los golpes de los barcos(self.pc_tablero_guess) == 17:
                print("Has Perdido :(")
                break

# Se crea la instancia de HundirLaFlota y comienza el juego
play = HundirLaFlota()
play.jugar_el_juego()
