from producto import *

class Restaurante:
    def __init__(self,nombre,productos):
        self.nombre = nombre
        self.productos = productos

    def mostrar_restaurante(self): #agregar el atributo id del estadio para mostrarlo 
        return print(f"""
                     Datos del restaurante: 
                     Nombre: {self.nombre}
                     """)
        
    def buscar_precio(self):
        while True:

            min = float(input("Ingrese el precio minimo: "))
            while not float(min):
                min = float(input("Ingrese el precio minimo: "))

            max = float(input("Ingrese el precio maximo: "))
            while not float(max):
                max = float(input("Ingrese el precio minimo: "))



            for producto in self.productos:
                if min <= producto.precio <= max:
                    producto.mostrar()

            opcion = input("Desea buscar otro producto? (S) Si \n (N) No \n-> ").upper()

            if opcion == "S":
                continue

            elif opcion == "N":
                break

            while opcion != "S" and opcion != "N":
                print("Opcion invalida")
                opcion = input("Desea buscar otro producto? (S) Si \n (N) No \n-> ").upper()



    def buscar_tipo(self):
        while True:

            opcion = input("Que tipo de producto desea buscar: \n(B) Bebida \n(A) Alimento \n-> ").upper()

            if opcion == "B":
                for producto in self.productos:
                    if producto.tipo == "Bebida":
                        producto.mostrar()

            elif opcion == "A":
                for producto in self.productos:
                    if producto.tipo == "Alimento":
                        producto.mostrar()


            opcion2 = input("Desea buscar otro producto? (S) Si \n (N) No \n-> ").upper()

            if opcion2 == "S":
                continue

            elif opcion2 == "N":
                break

            while opcion2 != "S" and opcion2 != "N":
                print("Opcion invalida")
                opcion2 = input("Desea buscar otro producto? (S) Si \n (N) No \n-> ").upper()
                


    def buscar_nombre(self):
        while True:

            nombre = input("Ingrese el nombre del producto a buscar: ")

            encontrado = False

            for producto in self.productos:
                if producto.nombre == nombre:
                    encontrado = True
                    producto.mostrar()

            if not encontrado:
                print("nombre invalido ")

            opcion3 = input("Desea buscar otro producto? (S) Si \n (N) No \n-> ").upper()

            if opcion3 == "S":
                continue

            elif opcion3 == "N":
                break

            while opcion3 != "S" and opcion2 != "N":
                print("Opcion invalida")
                opcion2 = input("Desea buscar otro producto? (S) Si \n (N) No \n-> ").upper()

