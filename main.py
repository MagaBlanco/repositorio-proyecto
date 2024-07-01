from funciones_modulo1 import *
from funciones_modulo2 import *
from funciones_modulo3 import *
from funciones_estadisticas import *
from funciones_validaciones import *
import pickle
def main():
    equipos_lista = []
    estadios_lista = []
    partidos_lista = []
    clientes_lista = []
    #Importamos los datos de las API
    equipos_lista, estadios_lista, partidos_lista, clientes_lista = leerArchivo()
    if equipos_lista == []:   
        #Descarga los datos de los partidos
        r1 = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json")
        equipos = r1.json()

        #Descarga los datos de los estadios, restaurantes y productos
        r2 = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json")
        estadios = r2.json()

        #Descarga los datos de los partidos
        r3 = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json")
        partidos = r3.json()
        crear_equipo(equipos, equipos_lista)
        crear_estadio(estadios, estadios_lista)
        crear_partido(partidos, equipos_lista, estadios_lista, partidos_lista)
    print("**********   BIENVENIDO A LA GESTION DE LA EURO 2024   **********")
    
    
    entrada = 0
    cliente = 0
    while True:
        
        opcion = input(""" Seleccione la opcion que desee:
                       (1) Buscar partidos
                       (2) Comprar entrada
                       (3) Registro de asistencia a partidos (Verificacion de entradas)
                       (4) Ver productos de restaurantes (Solo para VIP)
                       (5) Comprar en restaurante (Solo VIP)
                       (6) Estadisticas
                       (7) Salir
                       
                       ->  """)
        
        opcion = validarOp(opcion, 8, "Introduzca una opcion valida: ")


    
        if opcion == "1":
            opc1 = input("""Como desea buscar los partidos: 
                         (1) Por pais
                         (2) Por estadio
                         (3) Por fecha
                         (4) Volver al menu principal
                         ->  """)
            opc1 = validarOp(opc1, 4, "Introduzca una opcion valida: ")
        

            if opc1 == "1":
                buscar_partidos_pais(partidos_lista)

            elif opc1 == "2":
                buscar_partido_estadio(partidos_lista)

            elif opc1 == "3":
                buscar_partido_fecha(partidos_lista)

            




        elif opcion == "2":
            comprar_entrada(clientes_lista, partidos_lista)




        elif opcion == "3": #registro de asistencia (verificacion de entradas)
            entrada, cliente = verificar_entrada(clientes_lista)






        elif opcion == "4": 

            if entrada != 0 and entrada.tipo == "VIP":
                
                num = 1
                for rest in entrada.partido.estadio.restaurante:
                    
                    print(f"{num} - {rest.nombre}")
                    num += 1

                rest = input("Ingrese el restaurante que desea ver: ")
                
                

                while True:
                    try:
                        resta = entrada.partido.estadio.restaurante[int(rest) -1]
                        break

                    except:
                        print("")
                        rest = input("Ingrese el restaurante que desea ver: ")


                opc2 = input("""Como desea buscar los productos?
                                (1) Por nombre
                                (2) Por tipo (Alimento o Bebida)
                                (3) Por rango de precio
                                (4) Volver al menu inicial
                                ->  """)
                opc2 = validarOp(opc2, num, "Introduzca una opcion valida: ")
                if opc2 == "1": 
                    resta.buscar_nombre()

                elif opc2 == "2": 
                    resta.buscar_tipo()

                elif opc2 == "3": 
                    resta.buscar_precio()

                elif opc2 == "4": 
                    break
            

            else:
                print("Asista a un partido para entrar al restaurante")
                






        elif opcion == "5":
             if entrada != 0 and entrada.tipo == "VIP":
                gestion_venta_restaurante(entrada,clientes_lista)
             else:
                print("Asista a un partido para entrar al restaurante")




        elif opcion == "6":
            while True:
                opc = input("""Cual estadistica desea ver? 
                            (1) Promedio de gasto de un cliente VIP
                            (2) Asistencia a partidos 
                            (3) Partido con mayor asistencia
                            (4) Partido con mayor boletos vendidos
                            (5) Top 3 productos mas vendidos en el restaurante
                            (6) Top 3 clientes
                            (7) Salir
                             
                            ->  """)
                
                if opc == "1":
                    est1(clientes_lista)

                elif opc == "2":
                    est2(partidos_lista)

                elif opc == "3":
                    est3(partidos_lista)

                elif opc == "4":
                    est4(partidos_lista)
                
                elif opc == "5":
                    est5(estadios_lista)
                    

                elif opc == "6":
                    est6(clientes_lista)
                    

                elif opc == "7":  

                    break




        elif opcion == "7":
            print("Saliendo del programa...")
            break
        cargarArchivo(equipos_lista, estadios_lista, partidos_lista, clientes_lista)


def leerArchivo():
    try:
        with open('equipos.txt', 'rb') as f:
            equipos_lista = pickle.load(f)
        with open('estadios.txt', 'rb') as f:
            estadios_lista = pickle.load(f)
        
        with open('partidos.txt', 'rb') as f:
            partidos_lista = pickle.load(f)
        
        with open('clientes.txt', 'rb') as f:
            clientes_lista = pickle.load(f)
    except :
        equipos_lista = []
        estadios_lista = []
        partidos_lista = []
        clientes_lista = []
    return equipos_lista, estadios_lista, partidos_lista, clientes_lista

def cargarArchivo(equipos_lista, estadios_lista, partidos_lista, clientes_lista):
    with open('equipos.txt', 'ab') as f:
        pickle.dump(equipos_lista, f)
    with open('estadios.txt', 'ab') as f:
        pickle.dump(estadios_lista, f)
    with open('partidos.txt', 'ab') as f:
        pickle.dump(partidos_lista, f)
    with open('clientes.txt', 'ab') as f:
        pickle.dump(clientes_lista, f)
main()