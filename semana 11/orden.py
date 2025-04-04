def bubble_sort(fila):
    # Algoritmo de ordenación Bubble Sort
    n = len(fila)
    for i in range(n):
        for j in range(0, n-i-1):
            if fila[j] > fila[j+1]:
                fila[j], fila[j+1] = fila[j+1], fila[j]

def ordenar_fila(matriz, indice_fila):
    # Ordena la fila especificada de la matriz
    if 0 <= indice_fila < len(matriz):
        bubble_sort(matriz[indice_fila])
    else:
        print("Índice de fila esta fuera de rango.")

# Definición de la matriz 3x3
matriz = [
    [9, 2, 5],
    [3, 8, 1],
    [6, 7, 4]
]

# Imprimir matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenar la segunda fila indice 1
ordenar_fila(matriz, 1)

# Imprimir matriz después de ordenar
print("\nMatriz después de ordenar la fila 1:")
for fila in matriz:  #Recorremos la lista
    print(fila)