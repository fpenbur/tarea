def mostrar_titulo(titulo):
    """Imprime un título enmarcado por líneas decorativas.

    Args:
        titulo (str): Texto que se mostrará como título.
    """
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
    """Convierte un número en una cadena con formato de moneda en euros.

    Args:
        cantidad (float): Valor numérico a formatear.

    Returns:
        str: Cantidad redondeada a dos decimales seguida del símbolo '€'.
    """
    return str(round(cantidad, 2)) + " €"


def calcular_descuento(subtotal):
    """Calcula el importe de descuento según el subtotal del pedido.

    Aplica un 10 % si el subtotal supera 100, un 5 % si supera 50,
    y ningún descuento en caso contrario.

    Args:
        subtotal (float): Importe bruto antes de aplicar descuentos.

    Returns:
        float: Importe a descontar (no el porcentaje, sino la cantidad).
    """
    if subtotal > 100:
        return subtotal * 0.10
    elif subtotal > 50:
        return subtotal * 0.05
    return 0
