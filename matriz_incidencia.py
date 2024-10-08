import random

def generar_matriz_incidencia(filas, columnas):
    matriz = [[0 for _ in range(columnas)] for _ in range(filas)]
    
    for i in range(columnas):
        vertices_disponibles = [j for j in range(filas) if matriz[j][i] == 0]
        if len(vertices_disponibles) >= 2:
            arista1, arista2 = random.sample(vertices_disponibles, 2)
            matriz[arista1][i] = 1
            matriz[arista2][i] = 1

    return matriz

def contar_aristas(matriz):
    return sum(sum(fila) for fila in matriz) // 2

def contar_lazos(matriz):
    return sum(matriz[i][i] for i in range(min(len(matriz), len(matriz[0]))))

def calcular_grado(matriz):
    grados = [sum(fila) for fila in matriz]
    return grados

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

def main():
    filas = 7
    columnas = 6

    matriz_incidencia = generar_matriz_incidencia(filas, columnas)

    print("Matriz de incidencia:")
    imprimir_matriz(matriz_incidencia)

    num_aristas = contar_aristas(matriz_incidencia)
    print("Número de aristas:", num_aristas)

    num_lazos = contar_lazos(matriz_incidencia)
    print("Número de lazos:", num_lazos)

    grados_vertices = calcular_grado(matriz_incidencia)
    print("Grado de cada vértice:", grados_vertices)

if __name__ == "__main__":
    main()
