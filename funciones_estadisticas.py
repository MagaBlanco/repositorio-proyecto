from funciones_modulo1 import *
from funciones_modulo2 import *
from funciones_modulo3 import *


def est1(clientes):
    """Promedio de gasto de un cliente VIP"""
    
    total = 0
    cTotal = 0

    #se busca en la lista de clientes VIP que son los que poseen gastos, los generales no tienen
    for c in clientes:
        total += c.gastos
        if c.gastos != 0:
            cTotal +=1
    if cTotal != 0:
        print(f"El promedio de gasto de un cliente VIP en un partido es de {total/cTotal} ")


def est2(partidos):
    """Asistencia a partidos"""
    lista_asistencia = []

    #se busca en la lista de partidos la mayor asistencia
    #se va comparando la longitud de la lista de asistencia y 
    #va agregando a la lista de lista_asistencia de mayor a menor
    for partido in partidos:
        mayor_asistencia = partido
        for p in partidos:
            if len(p.asistencia) > len(mayor_asistencia.asistencia) and p not in lista_asistencia:
                mayor_asistencia = p
        lista_asistencia.append(mayor_asistencia)
    num = 1

    #recorre la lista de asistencia y los imprime 
    for partido in lista_asistencia:

        print(f"""--------------------------------------------------------------
                    {num} {partido.equipo_local.pais} vs {partido.equipo_visitante.pais}
                            Boletos vendidos: {partido.boletos_vendidos}
                            Asistencia: {len(partido.asistencia)}
                            Personas que asistieron: 
              """)
        for cliente in partido.asistencia:
            print(f"                 {cliente.nombre}")



def est3(partidos):
    """Partido con mas asistencias"""
    
    mayor_asistencia = partidos[0]

    #se busca en la lista de partidos y se compara la longitud de asistencia que es una lista
    for p in partidos:
        if len(p.asistencia) > len(mayor_asistencia.asistencia):
            mayor_asistencia = p

    print(f"El partido con mayor asistencia es: {mayor_asistencia.equipo_local.pais} vs {mayor_asistencia.equipo_visitante.pais} con {len(mayor_asistencia.asistencia)}")



def est4(partidos):
    """Partido con mayor boletos vendidos"""

    mayor_boletos = partidos[0]

    #busca en la lista de partidos el que tenga mayoria de boletos vendidos
    #va comparando hasta hallar el mayor

    for p in partidos:
        if p.boletos_vendidos > mayor_boletos.boletos_vendidos:
            mayor_boletos = p

    #al terminar de recorrer la lista, halla al mayor con ventas y se llama al atributo de equipos para saber cual es
    print(f"El partido con mayor boletos vendidos es: {mayor_boletos.equipo_local.pais} vs {mayor_boletos.equipo_visitante.pais} con {mayor_boletos.boletos_vendidos}")


def est5(estadios_lista):
    """Top 3 productos más vendidos en el restaurante"""
    
    productos_lista = []
    top_productos = []
    
    #busca en la lista de estadios los restaurantes y los productos en ellos y los agrega a la lista
    for i in estadios_lista:
        for rest in i.restaurante:
            for produ in rest.productos:             
                productos_lista.append(produ)

    #busca en la lista de productos aquellos que tengan la mayoria de veces vendidos segun el contador de cada uno
    #si el producto ya esta en la lista no lo vuelve a agregar a ella para eso es la primera parte del if
    # la segunda parte del if es la que compara el conteo de veces comprados
    for j in range(3):
        for product in productos_lista:
            producto_mayor_vendido = productos_lista[0]

            if producto_mayor_vendido in top_productos or (product.veces_vendido > producto_mayor_vendido.veces_vendido and product not in top_productos):
                producto_mayor_vendido = product
        top_productos.append(producto_mayor_vendido) 

    print(f"""Top 3 de productos mas vendidos:
          1.- {top_productos[0].nombre} {top_productos[0].veces_vendido} veces
          2.- {top_productos[1].nombre} {top_productos[1].veces_vendido} veces
          3.- {top_productos[2].nombre} {top_productos[2].veces_vendido} veces

""")              





def est6(clientes_lista):
    """Top 3 de clientes (clientes que más compraron boletos)"""


    top_clientes = []
    #busca en la lista de clientes, como asistencia es una lista verifica a cauntos partidos asistio (verifico la entrada)
    #si lo consigue lo agrega a la lista, repite la busqueda 3 veces
    #si el cliente ya esta en la lista no lo vuelve a agregar
    for i in range(3):
        cliente_mayor_boleto = clientes_lista[0]
        for cliente in clientes_lista:

            if cliente_mayor_boleto in top_clientes or (len(cliente.entradas) >len( cliente_mayor_boleto.entradas) and cliente not in top_clientes):
                cliente_mayor_boleto = cliente
        top_clientes.append(cliente_mayor_boleto)

    print(f"""Top 3 de clientes que compraron mas boletos:
          1.- {top_clientes[0].nombre} con {len(top_clientes[0].entradas)}
          2.- {top_clientes[1].nombre} con {len(top_clientes[0].entradas)}
          3.- {top_clientes[2].nombre} con {len(top_clientes[0].entradas)}
            """)
    

