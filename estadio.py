
class Estadio:
    def __init__(self,id,nombre,ubicacion,capacidad,restaurante):
        self.id = id
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.capacidad = capacidad
        self.restaurante = restaurante

    def mostrar_estadio(self):
        return print(f"""Datos estadio
                     Nombre: {self.nombre}
                    Ubicacion: {self.ubicacion}
                    Capacidad: {self.capacidad}
""")


        