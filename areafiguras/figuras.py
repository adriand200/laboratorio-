# Calcular el área de figuras geométricas
import math

# 1. Cuadrado
def area_cuadrado(lado):
    """
    Calcula el área de un cuadrado
    area = lado * lado
    :param lado: float
    :return: float
    """
    area = lado ** 2
    return area

# 2. Círculo
def area_circulo(radio):
    """
    Calcula el área de un círculo
    area = pi * radio^2
    :param radio: float
    :return: float
    """
    area = math.pi * (radio ** 2)
    return area

# 3. Triángulo
def area_triangulo(base, altura):
    """
    Calcula el área de un triángulo
    area = (base * altura) / 2
    :param base: float
    :param altura: float
    :return: float
    """
    area = (base * altura) / 2
    return area

# 4. Rectángulo
def area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo
    area = base * altura
    :param base: float
    :param altura: float
    :return: float
    """
    area = base * altura
    return area

# 5. Rombo
def area_rombo(diagonal_mayor, diagonal_menor):
    """
    Calcula el área de un rombo
    area = (D * d) / 2
    :param diagonal_mayor: float
    :param diagonal_menor: float
    :return: float
    """
    area = (diagonal_mayor * diagonal_menor) / 2
    return area

# 6. Trapecio
def area_trapecio(base_mayor, base_menor, altura):
    """
    Calcula el área de un trapecio
    area = ((B + b) * h) / 2
    :param base_mayor: float
    :param base_menor: float
    :param altura: float
    :return: float
    """
    area = ((base_mayor + base_menor) * altura) / 2
    return area

# 7. Romboide
def area_romboide(base, altura):
    """
    Calcula el área de un romboide
    area = base * altura
    :param base: float
    :param altura: float
    :return: float
    """
    area = base * altura
    return area

# 8. Pentágono regular
def area_pentagono(perimetro, apotema):
    """
    Calcula el área de un pentágono regular
    area = (P * a) / 2
    :param perimetro: float
    :param apotema: float
    :return: float
    """
    area = (perimetro * apotema) / 2
    return area
