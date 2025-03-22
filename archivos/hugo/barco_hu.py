class Barco:
    def __init__(self, longitud):
        self.longitud = longitud
        self.barco = '*' * longitud


    def mostrar_barco(self):
        print(self.barco)


