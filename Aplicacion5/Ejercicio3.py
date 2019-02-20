
# Esquema CSR de la matriz
AA = [8, 4, 1, 3, 2, 1, 7, 9, 3, 1, 5]
JA = [1, 2, 3, 4, 1, 3, 5, 2, 3, 6, 6]
IA = [1, 3, 5, 8, 11, 12]

# Imprimimos el esquema CSR
print("\n\nEsquema CSR de la matriz: ")
print("AA = " + str(AA))
print("JA = " + str(JA))
print("IA = " + str(IA) + "\n")

# Tamaño de la matriz
sizei = 5
sizej = 6

# Inicializo la matriz como una lista de listas
M = [[]]

# Añadimos ceros a la matriz
for i in range(sizei):
    Row = []
    for j in range(sizej):
        Row.append(0)
    M.append(Row)

# La primera fila es errónea y se elimina
del M[0]

# Indices para recorrer los distintos arrays
indexi = 0
indexj = 0

# Recorremos el array IA
for x in range(len(IA)-1):
    # Restamos el elemento actual y el siguiente para calcular cuantos elementos hay en la fila
    for y in range(IA[x+1]-IA[x]):
        # Para el número de elementos en la fila ponemos cada uno en la columna que indica JA
        M[indexi][JA[indexj]-1] = AA[indexj]
        indexj+=1
    indexi += 1

# Imprimimos la matriz
print("\n\nMatriz asociada calculada a partir del esquema:")
for x in range(len(M)):
    print(M[x])


# Declaración del vector a multiplicar
V = [1,2,3,4,5,6]
# Declaración del vector resultado
S = [0,0,0,0,0]

# Imprimimos el vector
print("\n--------------------------------------------\n")
print("Vector a multiplicar por la matriz:")
print("V = " + str(V))

# CALCULO DE LA MATRIZ POR V
# Indices para recorrer los distintos arrays
indexi = 0
indexj = 0

# Recorremos el array IA
for x in range(len(IA)-1):
    # Restamos el elemento actual y el siguiente para calcular cuantos elementos hay en la fila
    for y in range(IA[x+1]-IA[x]):
        # Para el número de elementos en la fila actualizamos el indice del vector actual con la suma del
        # elemento correspondiente en AA por el elemento de V indicado por JA
        S[indexi] += AA[indexj] * V[JA[indexj]-1]
        indexj += 1
    indexi += 1

print("La matriz por el vector V es igual a:")
print("S = " + str(S) + "\n\n")
