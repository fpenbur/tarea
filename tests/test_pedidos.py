"""Pruebas de la función calcular_descuento."""

from utilidades import calcular_descuento


def test_descuento_mayor_100():
    assert calcular_descuento(150) == 15.0


def test_descuento_mayor_50():
    assert calcular_descuento(80) == 4.0


def test_sin_descuento():
    assert calcular_descuento(20) == 0
