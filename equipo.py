

class Equipo:

    def __init__(self,id,codigo_fifa,pais,grupo):
        self.pais = pais
        self.codigo_fifa = codigo_fifa
        self.grupo = grupo
        self.id = id

    def mostrar_equipo(self):
        return print(f""" Datos del equipo 
                    Pais: {self.pais}
                    Codigo FIFA: {self.codigo_fifa}
                    Grupo: {self.grupo}\n""")
        