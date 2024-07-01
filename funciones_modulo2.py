from funciones_modulo1 import *
from cliente import Cliente
from entrada import Entrada


clientes_lista = []


def comprar_entrada(clientes_lista, partidos_lista):

    """ Gestiona la compra de las entradas
    Si la cedula ingresada del comprador es un numero vampiro se le aplica un descuento del 50%
    muestra la lista de asientos a escoger dependiendo del partido y si el cliente es VIP o General"""

    while True:
        print("***Gestion de entradas***")
        print()
        cliente = ""
        
        cedula = input("Ingrese su cedula: ")
        cedula = int(validarInt(cedula,"Ingrese su cedula: " ))
        for c in clientes_lista:
           if c.cedula == cedula:
              cliente = c
        if cliente == "":
            nombre = input("Ingrese su nombre: ")
            nombre = validarStr(nombre, "Ingrese su nombre")
            edad = int(input("Ingrese su edad:  "))
        else:
           nombre = cliente.nombre
           edad = cliente.edad
        
        #Muestra los partidos para seleccionar
        for i, partido in enumerate(partidos_lista): 
            print(f"{i+1}")
            partido.mostrar_partido()

        partido_seleccionado = input("Ingrese el numero de partido a escoger: ")
        partido_seleccionado = validarOp(partido_seleccionado, 36, "Ingrese el numero de partido a escoger: ")


   
        for partido in partidos_lista:
           if partido.numero == int(partido_seleccionado):
              partido_seleccionado = partido
              break
            

        entrada = input("Ingrese el tipo de entrada que desea:\n(G) General \n(V) VIP \n-> ").upper()
        entrada = validarStr(entrada, "Ingrese el tipo de entrada que desea:\n(G) General \n(V) VIP \n-> ").upper()
        precio = 0
        if entrada == "G":
            tipo = "General"
            precio = 35
            print(f"El precio de la entrada es de {precio}$")
            limite = partido_seleccionado.estadio.capacidad[0]

        elif entrada == "V":
            tipo = "VIP"
            precio = 75
            limite = partido_seleccionado.estadio.capacidad[1]

            print(f"El precio de la entrada es de {precio}$")
        
        
        #impresion de la lista de asientos
        cont = 1
        fila = ""


        for i in range(limite):
           if i not in partido_seleccionado.asientos_ocupados:                
                fila += str(i) + " | "
           else:
              fila += "X | "
              
           if cont == 11:
              
              print(fila)
              print("____________________________________________________________________________________________")
              fila = ""
              cont = 1
           cont +=1
              
        print(fila)
        asiento = input("Seleccione su asiento: ")
        asiento = validarOp(asiento, limite, "Seleccione su asiento: ")

        while int(asiento) in partido_seleccionado.asientos_ocupados:
            asiento = input("Seleccione un asiento disponible: ")
            asiento = validarOp(asiento, limite, "Seleccione su asiento: ")

        
        if vampiro(cedula) == True:
           descuento = precio * 0.5
           print("Felicidades, ha recibido un descuento del 50% en su entrada!")

        else: 
           descuento = 0

        iva = precio * 0.16
        total = iva + precio - descuento
        

        
        print(f"El total a pagar con impuestos es: {total}$ \n")

        
        
        opcion = input("Desea proceder a pagar la entrada? \n(S) Si \n(N) No \n-> ").upper()
        
        

        if opcion == "S":

            
            print("Pago exitoso!")
            partido_seleccionado.asientos_ocupados.append(int(asiento))
            nueva_entrada = Entrada(partido_seleccionado,tipo,asiento)
            if cliente == "":
                nuevo_cliente = Cliente(nombre,cedula,edad)   
            else:
               nuevo_cliente = cliente
            nuevo_cliente.entradas.append(nueva_entrada)
            clientes_lista.append(nuevo_cliente)
            
            #los clientes VIP son los unicos que tienen gastos para el calculo de la estadistica de promedio
            if entrada == "V":
                nuevo_cliente.gastos += total

            partido_seleccionado.boletos_vendidos += 1

            
            print(f"""
            ***Resumen de su compra***
            Partido: {partido_seleccionado.equipo_local.pais} VS {partido_seleccionado.equipo_visitante.pais} 
            Asiento: {asiento}
            Costo > Subtotal: {precio}$ 
            Descuento: {descuento}$
            IVA: {iva:.2f}$
            Total: {total}$ 
            Codigo de la entrada: {nueva_entrada.codigo} \n""") 
            
        elif opcion == "N":
            print("Pago cancelado")

        seleccion = input("Desea continuar comprando? \n(S) Si \n(N) No \n-> ").upper()
        
        
        if seleccion == "S":
            continue

        elif seleccion == 'N':
            break

        while seleccion != 'S' and seleccion != "N":
            print("Opcion invalida")
            seleccion = input("Desea continuar comprando? \n(S) Si \n(N) No \n-> ").upper()
            



    
entradas_compradas = []




def vampiro(numero):
   """
   Calcula si un numero es vampiro
   Primero se buscan los factores que son divisores del numero ingresado y se almacenan en una lista
   Luego se buscan los factores posibles para realizar la multiplicacion, separando el numero ingresado en partes
   Despues se agregan a una lista aquellos factores que posean los mismos numeros del numero original
   Por ultimo se toman los numeros de la lista y se multiplican y se verifica si el numero es o no vampiro"""

   factores = []

    
   for x in range(1, numero//2 +1):
     if numero % x == 0:
       factores.append(x)
   

   factores_posibles = []

    
   for i in factores:
     if len(str(i)) == len(str(numero)) //2:
       factores_posibles.append(i)
   
       
   factores_posibles_digitos = []  #factores que poseen los numeros del numero ingresado

    
   for j in factores_posibles:
        encontrado = True
        for x in str(j):
            if str(x) not in str(numero):
              encontrado = False
        if encontrado:
          factores_posibles_digitos.append(j)
        
   

   for x in factores_posibles_digitos:
    for h in factores_posibles_digitos:
      multiplicacion = x * h
      if multiplicacion == numero:
        
        return True
   
   return False
