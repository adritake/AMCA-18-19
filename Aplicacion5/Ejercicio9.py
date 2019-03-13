# Script para calcular el método de las potencias o el método de las potencias normalizado de una matriz determinada

import numpy as np

# Si NORMALIZADO == True se usa el método de las potencias normalizado
NORMALIZADO = False

# Número de iteraciones que se van a hacer en el método de las potencias
ITERACIONES = 20

# Matriz a calcular el método de las potencias

'''
# Matriz ejercicio 6
M = np.array([[4, -1, 1],
              [-1, 3, -2],
              [1, -2, 3],
              ])

# Matriz ejercicio 7 a)
M = np.array([[2, 1, 1],
              [1, 2, 1],
              [1, 1, 2],
              ])

# Matriz ejercicio 7 b)
M = np.array([[1, 1, 1],
              [1, 1, 0],
              [1, 0, 1],
              ])

# Matriz ejercicio 8
M = np.array([[1/3, 2/3,    2,    3],
              [  1,   0,   -1,    2],
              [  0,   0, -5/3, -2/3],
              [  0,   0,    1,    0],
              ])
'''

# Matriz ejercicio page rank
A = 0.8575
B = 0.4325
C = 0.29083
D = 0.22
E = 0.0075

M = np.array([[E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E],
              [B,E,E,E,E,E,C,E,E,E,E,E,E,E,E,E,E,E,E,E],
              [E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E],
              [E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E],
              [E,E,E,A,E,E,E,E,E,B,E,E,E,E,E,E,E,E,E,E],
              [B,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E],
              [E,E,E,E,E,E,E,E,E,E,B,E,E,E,E,E,E,E,E,E],
              [E,A,E,E,E,E,C,E,E,E,E,E,E,E,E,E,E,E,E,E],
              [E,E,B,E,A,E,E,E,E,E,E,E,E,E,B,E,E,E,E,E],
              [E,E,E,E,E,E,E,E,D,E,E,E,E,E,E,E,E,E,E,E],
              [E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E],
              [E,E,E,E,E,A,C,A,E,E,E,E,E,E,E,A,E,E,E,E],
              [E,E,E,E,E,E,E,E,D,E,E,E,E,E,E,E,A,A,E,E],
              [E,E,B,E,E,E,E,E,D,E,E,E,E,E,E,E,E,E,B,B],
              [E,E,E,E,E,E,E,E,E,B,E,E,E,A,E,E,E,E,E,E],
              [E,E,E,E,E,E,E,E,E,E,B,E,E,E,E,E,E,E,E,E],
              [E,E,E,E,E,E,E,E,E,E,E,A,E,E,E,E,E,E,E,E],
              [E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,E,B,E],
              [E,E,E,E,E,E,E,E,E,E,E,E,A,E,E,E,E,E,E,B],
              [E,E,E,E,E,E,E,E,D,E,E,E,E,E,B,E,E,E,E,E],
              ])



# Tamaño de la matriz
size = len(M)
# Imprimimos la matriz
print("Matriz: ")
for r in M:
    print(r)

print("-----------------------------\n")

# Inicializamos el vector X como un vector de ceros salvo la primera componente que vale 1
X = np.zeros(size)
X[0] = 1

# Vector donde guardamos los resultados para calcular finalmente el valor propio dominante
componentes = np.array([])

# Método de las potencias estándar
if not NORMALIZADO:
    # Se va multiplicando la matriz M por el vector X y guardando los resultados en el vector componentes
    for i in range(ITERACIONES):
        componentes = np.append(componentes,X[0])
        print(X)
        X = M.dot(X)

    # Calculamos la norma infinito del vector
    norma = np.amax(X)
    # Imprimimos el vector obtenido
    print("Vector propio: " + str(X))
    # Imprimimos el vector normalizado (vector/norma)
    print("Vector propio normalizado: " + str(X/norma))
    # Calculamos el valor propio como el último elemento del vector componentes dividido entre el penúltimo elemento
    sizecom = len(componentes)
    propio = componentes[sizecom-1]/componentes[sizecom-2]
    propio_redondeado = np.round(propio,1)
    print("Valor propio: " + str(propio) + " ~~ " + str(propio_redondeado) )

# Método de las potencias normalizado
# En este caso solo se puede obtener el vector propio por lo que no necesitamos guardar los resultados
else:
    for i in range(ITERACIONES):
        X = M.dot(X)
        X = X/np.amax(X)
    print("Vector propio: " + str(X))
