# Importar funciones desde los scripts
from interfaz import (
    menu,
    solicitar_datos_cuadrado,
    solicitar_datos_circulo,
    solicitar_datos_triangulo,
    solicitar_datos_rectangulo,
    solicitar_datos_rombo,
    solicitar_datos_trapecio,
    solicitar_datos_romboide,
    solicitar_datos_pentagono,
    mostrar_area
)

from figuras import (
    area_cuadrado,
    area_circulo,
    area_triangulo,
    area_rectangulo,
    area_rombo,
    area_trapecio,
    area_romboide,
    area_pentagono
)

# Constantes para las opciones del menú
CUADRADO = 1
CIRCULO = 2
TRIANGULO = 3
RECTANGULO = 4
ROMBO = 5
TRAPECIO = 6
ROMBOIDE = 7
PENTAGONO = 8
SALIR = 9

# Inicializar opción
op = 0

# Bucle principal
while op != SALIR:
    op = menu()

    if op == CUADRADO:
        lado = solicitar_datos_cuadrado()
        area = area_cuadrado(lado)
        mostrar_area("cuadrado", area)

    elif op == CIRCULO:
        radio = solicitar_datos_circulo()
        area = area_circulo(radio)
        mostrar_area("círculo", area)

    elif op == TRIANGULO:
        base, altura = solicitar_datos_triangulo()
        area = area_triangulo(base, altura)
        mostrar_area("triángulo", area)

    elif op == RECTANGULO:
        base, altura = solicitar_datos_rectangulo()
        area = area_rectangulo(base, altura)
        mostrar_area("rectángulo", area)

    elif op == ROMBO:
        D, d = solicitar_datos_rombo()
        area = area_rombo(D, d)
        mostrar_area("rombo", area)

    elif op == TRAPECIO:
        B, b, h = solicitar_datos_trapecio()
        area = area_trapecio(B, b, h)
        mostrar_area("trapecio", area)

    elif op == ROMBOIDE:
        base, altura = solicitar_datos_romboide()
        area = area_romboide(base, altura)
        mostrar_area("romboide", area)

    elif op == PENTAGONO:
        P, a = solicitar_datos_pentagono()
        area = area_pentagono(P, a)
        mostrar_area("pentágono", area)

    elif op == SALIR:
        print("¡Gracias por utilizar la calculadora de figuras geométricas!")

    else:
        print("¡Opción no válida! Por favor, intenta de nuevo.")
