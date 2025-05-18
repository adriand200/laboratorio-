# Solicita y muestra información

# Menú
def menu():
    """
    Muestra el menú de opciones
    """
    print("\nBienvenido a la calculadora de figuras geométricas")
    print("Seleccione una figura para calcular su área:")
    print("1. Cuadrado")
    print("2. Círculo")
    print("3. Triángulo")
    print("4. Rectángulo")
    print("5. Rombo")
    print("6. Trapecio")
    print("7. Romboide")
    print("8. Pentágono regular")
    print("9. Salir")
    opcion = int(input("Seleccione una opción: "))
    return opcion

# Solicitudes de datos
def solicitar_datos_cuadrado():
    lado = float(input("Ingrese el lado del cuadrado: "))
    return lado

def solicitar_datos_circulo():
    radio = float(input("Ingrese el radio del círculo: "))
    return radio

def solicitar_datos_triangulo():
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    return base, altura

def solicitar_datos_rectangulo():
    base = float(input("Ingrese la base del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))
    return base, altura

def solicitar_datos_rombo():
    D = float(input("Ingrese la diagonal mayor del rombo: "))
    d = float(input("Ingrese la diagonal menor del rombo: "))
    return D, d

def solicitar_datos_trapecio():
    B = float(input("Ingrese la base mayor del trapecio: "))
    b = float(input("Ingrese la base menor del trapecio: "))
    h = float(input("Ingrese la altura del trapecio: "))
    return B, b, h

def solicitar_datos_romboide():
    base = float(input("Ingrese la base del romboide: "))
    altura = float(input("Ingrese la altura del romboide: "))
    return base, altura

def solicitar_datos_pentagono():
    P = float(input("Ingrese el perímetro del pentágono: "))
    a = float(input("Ingrese el apotema del pentágono: "))
    return P, a

# Mostrar resultados
def mostrar_area(figura, area):
    """
    Muestra el área de una figura
    :param figura: str
    :param area: float
    """
    print(f"El área del {figura} es: {area}")
