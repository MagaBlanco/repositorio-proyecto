

class Producto:
    def __init__(self,nombre,cantidad,precio,stock,adicional):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.stock = stock
        self.adicional = adicional
        self.veces_vendido = 0

    def mostrar(self):
        return print(f"Producto: {self.nombre} - Precio: {self.precio} - Presentacion: {self.adicional}\n")


class Alimento(Producto):
    def __init__(self, nombre, cantidad, precio, stock, adicional,tipo):
        super().__init__(nombre, cantidad, precio, stock, adicional)
        self.tipo = "Alimento"

    def mostrar(self):
        return print(f"Producto: {self.nombre} - Precio: {self.precio} - Presentacion: {self.adicional}\n")


class Bebida(Producto):
    def __init__(self, nombre, cantidad, precio, stock, adicional,tipo):
        super().__init__(nombre, cantidad, precio, stock, adicional)
        self.tipo = "Bebida"

    def mostrar(self):
        return print(f"Producto: {self.nombre} - Precio: {self.precio} - Presentacion: {self.adicional}\n")
    