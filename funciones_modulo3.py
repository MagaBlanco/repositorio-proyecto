from funciones_modulo1 import *
from funciones_modulo2 import *
from entrada import *
from partidos import *

entradas_verificadas = 0  #para las estadisticas 


def verificar_entrada(clientes_lista): 
    """Verificacion de entradas"""


    codigo = (input("Ingrese el codigo unico de la entrada:  "))
    codigo = int(validarInt(codigo, ("Ingrese el codigo unico de la entrada:  ")))
    encontrado = False
    entrada = 0
    cliente = 0

    #busca en la lista de clientes su entrada, si el codigo coincide con el ingresado se verifica
   
    for c in clientes_lista:
        for e in c.entradas:
            if codigo == e.codigo:
                if c not in e.partido.asistencia:
                    encontrado = True
                    entrada = e
                    cliente = c
                    entrada.partido.asistencia.append(cliente)
                
                    break


    if encontrado:
        
        print("Entrada verificada")

    else:
        print("Entrada invalida")
    return entrada, cliente




def numero_perfecto(numero):
    """Verifica que un numero sea perfecto"""

    factores = []
    for n in range(1, numero //2 +1):
        if numero % n == 0:
            factores.append(n)

    total = sum(factores)

    if total == numero:
        return True
    
    else:
        return False





def gestion_venta_restaurante(entrada, clientes_lista):

    """Gestiona la compra de productos en los restaurantes si el cliente es VIP"""
    cliente_vip = ""
    if entrada.tipo == "VIP":

        cedula = (input("Ingrese su cedula: "))
        cedula = int(validarInt(cedula, "Ingrese su cedula: "))
        for cliente in clientes_lista:
            if cliente.cedula == cedula:
                cliente_vip = cliente

        if cliente_vip != "":
            
            r = True
            carrito = {}
            while True:
                num = 1
                if r:
                    for rest in entrada.partido.estadio.restaurante:
                        print(f"{num} - {rest.nombre}")
                        num +=1
                    opcion = input("Ingrese el numero del restaurante en el que desea comprar: ")
                    try:
                        restaurante = entrada.partido.estadio.restaurante[int(opcion)-1]

                    except: 
                        print("Opcion invalida")
                        opcion = input("Ingrese el numero del restaurante en el que desea comprar: ")

                    r = False

                num = 1
                productos = []
                for produc in restaurante.productos:
                    if produc.adicional == "alcoholic" and cliente_vip.edad < 18:
                        continue
                    productos.append(produc)
                    print(f"Producto #{num}")
                    produc.mostrar()
                    num += 1

                op = input("Ingrese el numero del producto que desea comprar: ")
                while True:
                    try:
                        producto = productos[int(op)-1]
                        break

                    except:
                        print("Opcion valida")
                        op = input("Ingrese el numero del producto que desea comprar: ")

                #producto = productos[int(op)-1]
                cantidad = input("Ingrese la cantidad que desea comprar: ")
                while True:
                    if cantidad.isnumeric():
                        break

                    else: 
                        cantidad = input("Ingrese la cantidad que desea comprar: ")

                carrito[producto] = cantidad
                seguir = (input("Ingrese 1 para seguir comprando, 2 para cambiar de restaurante o 3 para pagar: "))
                seguir = int(validarOp(seguir, 3, "Ingrese 1 para seguir comprando, 2 para cambiar de restaurante o 3 para pagar: "))
                if seguir == 2:
                    r = True
                elif seguir == 3:
                    break
            num = 1
            for p, c in carrito.items():
                precio = int(p.precio)*int(c) 
                print(f"-{num} {p.nombre} x{c}  -> {precio}$")
                num +=1
            while True:
                el = input("Desea eliminar algun producto del carrito? 1 Si 2 No ")
                el = validarOp(el, 3, "Desea eliminar algun producto del carrito? 1 Si 2 No " )
                if int(el) == 2:
                    break
                el = input("Ingrese el indice del producto que desea eliminar: ")
                el = validarOp(el, len(carrito.keys()), "Desea eliminar algun producto del carrito? 1 Si 2 No " )
                num = 1
                for p, c in carrito.items():
                    if num == int(el):
                        carrito.pop(p)
                        print("Producto eliminado")
                        break
                    num +=1
            pagar = input("Desea proceder con la compra? 1 Si 2 No: ")
            el = validarOp(el, 2, "Desea proceder con la compra? 1 Si 2 No: " )
            if pagar == 2:
                print("Compra cancelada")
                return
            print(f"""---------FACTURA---------""")
            num = 1
            subtotal = 0
            d = 0
            for p, c in carrito.items():
                precio = int(p.precio)*int(c) 
                print(f"-{num} {p.nombre} x{c}  -> {precio}$")
                p.stock -= int(c)
                subtotal += p.precio * int(cantidad)
                num +=1
                p.veces_vendido += int(c)


            if numero_perfecto(cliente.cedula):
                descuento = 0.85
                d = subtotal*0.15
            else:
                descuento = 1
            
            
            
            total = subtotal * descuento

            print(f"""
                  Subtotal: {subtotal}
                  Descuento = {d}
                  Total: {total}
 """)
            cliente_vip.gastos += total
        else:
            print("No se encontro al cliente")
    else:
        print("No es un cliente VIP")