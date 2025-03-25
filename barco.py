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


    def mostrar_barco(self):
        """
        enseña un barco, esta principalmente para probar que generaba bien los barcos, creo que falta no hace
        """
        print(self.barco)


    @classmethod
    def devolver_flota(cls):
        """
        devuelve la lista de todos los barcos, el print comentado era para hacer pruebas y si estaba almacenandolos bien

        print(f"Barcos creados: {len(cls.flota)}")
        for i, barco in enumerate(cls.flota):
            print(f"Barco {i+1}: {barco.barco}")
        """
        return cls.flota
    

    """
    esto deberia crear los barcos y no deberia ser muy dificil adaptarlo para generar los barcos que quieras, quitando las funciones a mayores para 
    comprobar que los barcos que se intenten reflejar puedan reflejarse, pero no lo probe mucho aun

    def crear_barcos():
        longitudes = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        
        for longitud in longitudes:
            Barco(longitud) 
        
        return Barco.devolver_flota() # una vez los crea devuelve la lista de barcos
    """
