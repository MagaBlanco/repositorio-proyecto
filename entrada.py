import random

class Entrada:
    def __init__(self,partido,tipo,asiento):
        self.partido = partido
        self.tipo = tipo
        self.asiento = asiento
        self.codigo =  random.randint(000000000,999999999)
