import random  # Importa el módulo random para generar números aleatorios

# Función que genera una matriz n x m con temperaturas aleatorias
def generar_matriz_temperaturas(n, m, temp_min=20, temp_max=100):
    matriz = []  # Crea una lista vacía que representará la matriz final
    for i in range(n):  # Recorre cada fila (de 0 hasta n-1)
        fila = []  # Crea una lista vacía para representar una fila de sensores
        for j in range(m):  # Recorre cada columna (de 0 hasta m-1)
            temp = random.uniform(temp_min, temp_max)  # Genera un número decimal aleatorio entre temp_min y temp_max
            fila.append(round(temp, 1))  # Redondea la temperatura a 1 decimal y la añade a la fila
        matriz.append(fila)  # Añade la fila completa a la matriz
    return matriz  # Retorna la matriz completa generada

# Función que detecta temperaturas superiores al umbral (por defecto 80 °C)
def detectar_temperaturas_criticas(matriz, umbral=80):
    print("Detectando temperaturas críticas mayores a", umbral, "°C:")  # Imprime el encabezado
    for i in range(len(matriz)):  # Recorre cada fila de la matriz (i es el índice de fila)
        for j in range(len(matriz[0])):  # Recorre cada columna de la fila actual (j es el índice de columna)
            if matriz[i][j] > umbral:  # Verifica si el valor de temperatura es mayor que el umbral
                # Si se cumple, imprime una advertencia con la posición del sensor y la temperatura
                print(f"⚠️ Temperatura crítica detectada en sensor [{i}][{j}]: {matriz[i][j]}°C")

# Definir el tamaño de la matriz: 5 filas y 4 columnas
n = 5  # Número de filas (sensores en dirección vertical)
m = 4  # Número de columnas (sensores en dirección horizontal)

# Genera la matriz de sensores con temperaturas aleatorias
matriz_sensores = generar_matriz_temperaturas(n, m)

# Imprime la matriz generada para visualizar los datos de temperatura
print("Matriz de sensores (temperaturas en °C):")
for fila in matriz_sensores:  # Recorre cada fila de la matriz
    print(fila)  # Imprime la fila completa (una lista de temperaturas)

# Llama a la función para buscar e imprimir temperaturas críticas
detectar_temperaturas_criticas(matriz_sensores)
