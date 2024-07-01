

class Partido:
    def __init__(self,equipo_local,equipo_visitante,fecha,grupo, estadio,numero):
        self.equipo_local = equipo_local  #referencia al objeto
        self.equipo_visitante = equipo_visitante
        self.fecha = fecha
        self.grupo = grupo
        self.estadio = estadio   #referencia al objeto
        self.numero = numero
        self.asistencia = []
        self.boletos_vendidos = 0
        self.asientos_ocupados = []


    def mostrar_partido(self): 
        return print(f"""DATOS DEL PARTIDO
                    Equipo local: {self.equipo_local.pais}  
                    Equipo visitante: {self.equipo_visitante.pais}
                    Fecha: {self.fecha}
                    Grupo: {self.grupo}
                    Estadio: {self.estadio.nombre}

""")