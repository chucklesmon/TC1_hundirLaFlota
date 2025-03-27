class Barco:
    # Lista donde se guardan los barcos
    flota = [] 

    def __init__(self, longitud):
        """
        Monta el barco, cada vez que monta un barco lo añade a una lista
        """
        self.longitud = longitud
        self.barco = [0] * longitud # genera una lista con posiciones iguales a la longitud donde cada una es 0

        Barco.flota.append(self) # cada vez que se genera un barco lo añade a la lista flota


    @classmethod
    def devolver_flota(cls):
        """
        devuelve la flota de barcos
        """
        return cls.flota
    


    def crear_barcos():
        """
        crea los barcos, almacena en longitudes el tamaño de los barcos y crea un barco con cada elemento. Devuelve la flota
        """
        longitudes = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        
        for longitud in longitudes:
            Barco(longitud) 
        
        return Barco.devolver_flota() # una vez los crea devuelve la lista de barcos
