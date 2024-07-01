import requests
from producto import *
from equipo import Equipo
from estadio import Estadio
from partidos import Partido
from restaurante import Restaurante
from funciones_validaciones import *







def crear_equipo(equipos, equipos_lista):    #el nombre lo defino como pais en el objeto

    #Recorre el diccionario de equipos y crea el objeto Equipo

    for equipo in equipos:
        nuevo_equipo = Equipo(equipo['id'],equipo['code'],equipo['name'],equipo['group'])

        equipos_lista.append(nuevo_equipo)

    



def crear_estadio(estadios, estadios_lista):
  
  #Crea el objeto Estadio, Restaurante y Producto
  #primero se crea el producto, luego el restaurante y por ultimo el estadio
  

    for estadio in estadios:
        restaurantes_lista = []

        for tipo, dato in estadio.items():
            
            if tipo == "restaurants":
                for restaurante in dato:
                    productos_lista = []

                    for t, d in restaurante.items():
                        if t == "products":
                            
                            for producto in d:
                                if producto["adicional"] == "alcoholic" or producto["adicional"] == "non-alcoholic":
                                  nuevo_producto = Bebida(producto['name'], producto['quantity'],float(producto['price']) + float(producto['price']) *0.16,int(producto['stock']),producto['adicional'],"Bebida")
                                  productos_lista.append(nuevo_producto)

                                else: 
                                    nuevo_producto = Alimento(producto['name'], producto['quantity'],float(producto['price']) + float(producto['price']) *0.16,int(producto['stock']),producto['adicional'],"Alimento")
                                    productos_lista.append(nuevo_producto)
                        
                    nuevo_restaurante = Restaurante(restaurante['name'],productos_lista)
                    restaurantes_lista.append(nuevo_restaurante)

        nuevo_estadio = Estadio(estadio['id'],estadio['name'],estadio['city'],estadio['capacity'],restaurantes_lista)
        estadios_lista.append(nuevo_estadio)









def crear_partido(partidos, equipos_lista, estadios_lista, partidos_lista):   
  home = ""
  away = ""
  stadium = ""
  nuevo_partido = None

  for partido in partidos:
      
    for llave, dato in partido.items():
        if llave == "home":
            for equipo in equipos_lista:
                if equipo.pais == dato["name"]:   #probando buscar por name para que imprima el nombre y no el id
                    home = equipo
                   
        if llave == "away":
            for equipo in equipos_lista:
                if equipo.id == dato["id"]:    
                    away = equipo


        if llave == "stadium_id":    #no me agarra el estadio
            for estadio in estadios_lista:
                if estadio.id == dato:
                      stadium = estadio 

    nuevo_partido = Partido(home,away,partido['date'],partido['group'],stadium,partido['number'])
    partidos_lista.append(nuevo_partido)







def buscar_partidos_pais(partidos_lista):
  

  #no hace nada 
  #pero tampoco hay nada en partidos_lista puede ser por eso
  while True:
    partidos_pais = []
    codigo = input("Ingrese el codigo FIFA del partido o S para salir:  ").upper()
    codigo =   validarStr(codigo, "Ingrese el codigo FIFA del partido o S para salir:  ").upper()

    if codigo == "S":
        break
    for partido in partidos_lista:
        if partido.equipo_local.codigo_fifa == codigo or partido.equipo_visitante.codigo_fifa == codigo:
            partidos_pais.append(partido)

    for partido in partidos_pais:
        partido.mostrar_partido()
    if len(partidos_pais) == 0:
            print("NO SE ENCONTRARON PARTIDOS")
#buscar_partidos_pais(partidos_lista)

def buscar_partido_estadio(partidos_lista):
    """Busca los partidos segun el estadio
     Se buscan todos los partidos en el estadio ingresado y se incluyen a la lista y se muestra esa lista """
    

    while True:
        name = input("Ingrese el nombre del estadio a consultar o ingrese S para salir: ")
        
        partidos_estadio = []
        if name == "S":
            break

        for partido in partidos_lista:
            if partido.estadio.nombre == name:
                partidos_estadio.append(partido)

        for partido in partidos_estadio:
            partido.mostrar_partido()
    if len(partidos_estadio) == 0:
            print("NO SE ENCONTRARON PARTIDOS")

def buscar_partido_fecha(partidos_lista):
    

    while True:
        fecha = input("Ingrese la fecha del partido a consultar o ingrese S para salir (Formato YYYY-MM-DD):  ")
        partidos_fecha= []
        if fecha == "S":
            break
        
        for partido in partidos_lista:
            if partido.fecha == fecha:
                partidos_fecha.append(partido)

        for partido in partidos_fecha:
            partido.mostrar_partido()
        if len(partidos_fecha) == 0:
            print("NO SE ENCONTRARON PARTIDOS")
