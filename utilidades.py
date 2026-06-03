def mostrar_titulo(titulo):
    print("\n============================")
    print(titulo)
    print("============================")


def pedir_numero(mensaje):
    valor = input(mensaje)
    try:
        return int(valor)
    except ValueError:
        print("Número no válido. Se usará 0")
        return 0


def formatear_moneda(cantidad):
    return str(round(cantidad, 2)) + " €"


def calcular_descuento(subtotal):
    if subtotal > 100:
        return subtotal * 0.10
    elif subtotal > 50:
        return subtotal * 0.05
    return 0
