def escalarXmatriz(num, matriz):
    filas = len(matriz)
    col = len(matriz[0])
    sol = [[0 for _ in range(col)] for _ in range(filas)]
    for i in range(filas):
        for j in range(col):
            sol[i][j] = num * float(matriz[i][j])
    return sol

def modulo(vector):
    acu = 0
    for i in vector:
        acu += i[0] ** 2
    sol = acu ** 0.5
    return sol

def traspuesta(matriz):
    filas = len(matriz)
    col = len(matriz[0])
    sol = [[0 for _ in range(filas)] for _ in range(col)]
    for i in range(filas):
        for j in range(col):
            sol[j][i] = float(matriz[i][j])
    return sol

def resta(matriz1, matriz2):
    filas = len(matriz1)
    col = len(matriz1[0])
    sol = [[0 for _ in range(col)] for _ in range(filas)]
    for i in range(filas):
        for j in range(col):
            sol[i][j] = float(matriz1[i][j]) - float(matriz2[i][j])
    return sol


def producto(matriz1, matriz2):
    filas1 = len(matriz1)
    col1 = len(matriz1[0])
    filas2 = len(matriz2)
    col2 = len(matriz2[0])
    sol = [[0 for _ in range(col2)] for _ in range(filas1)]
    for i in range(filas1):
        for j in range(col2):
            for k in range(col1):
                sol[i][j] += float(matriz1[i][k]) * float(matriz2[k][j])
    return sol

def descensoGradiente(A,b,xo,alfa,epsi):
    x = xo
    g = resta(producto(producto(escalarXmatriz(2,traspuesta(A)),A),x),producto(escalarXmatriz(2,traspuesta(A)),b))
    while modulo(g)>epsi:
        x = resta(x,escalarXmatriz(alfa,g))
        g = resta(producto(producto(escalarXmatriz(2,traspuesta(A)),A),x),producto(escalarXmatriz(2,traspuesta(A)),b))
    return x

#leemos N y M
entrada = input()
n = int(entrada.split(" ")[0])
m = int(entrada.split(" ")[1])

#Inicializamos matriz A
matriz = []
for i in range(n):
    matriz.append([])
    for j in range(m):
        matriz[i].append(None)

#Leemos A
for i in range(n):
    entrada = input().split(" ")
    for j in range(len(entrada)):
        matriz[i][j] = float(entrada[j])

#Leemos b
b = []
entrada = input().split(" ")
for i in range(len(entrada)):
    b.append([])
    b[i].append(float(entrada[i]))

#Leemos Xo
xo=[]
entrada = input().split(" ")
for i in range(len(entrada)):
    xo.append(([]))
    xo[i].append(float(entrada[i]))

#Leemos alfa y beta
alfa = float(input())
epsi = float(input())

ans = descensoGradiente(matriz,b,xo,alfa,epsi)

for i in range(len(ans)):
    n = round(ans[i][0],12)
    print("{:.4f}".format(n),end=' ')
print()
