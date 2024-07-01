def validarStr(palabra, mensaje):
    while not palabra.isalpha():
        palabra = input(mensaje)
    return palabra

def validarInt(numero, mensaje):
    while not numero.isnumeric():
        numero = input(mensaje)
    return numero

def validarOp(numero, max, mensaje):
    while not numero.isnumeric() and  not (0 < int(numero) <= max):
        numero = input(mensaje)
    return numero
def validar_sino(palabra, mensaje):
    while not palabra.isalpha() or( mensaje != "S" and mensaje != "N"):
        palabra = input(mensaje)
    return palabra