import math

def imprime_lista(a):
    n = len(a)
    if n==0:
        pass
    elif n==1:
        print(a[0])
    else:
        print(a[0],end='')
        print(' ',end='')
        imprime_lista(a[1:])

def genera_permutaciones_wrapper(elementos,best,current,cities,grafo):
    sol = [None] * (len(elementos))
    sol[0]=0
    libres = [True] * (len(elementos))
    libres[0]=False
    return genera_permutaciones(1,libres,sol,elementos,best,current,cities,grafo,0)


def genera_permutaciones(i,libres,sol,elementos,best,current,cities,grafo,ant):
    n = len(elementos)
    if i==n:
        current = current + grafo[ant][0]
        if current<best:
            cities = sol
            best=current
        return best,cities
    else:
        for k in range(0,n):
            if libres[k] and current + grafo[ant][k] <= best:
                sol[i]=elementos[k]
                libres[k]=False
                tupla = genera_permutaciones(i+1,libres,sol,elementos,best,current + grafo[ant][k],cities,grafo,k)
                best=tupla[0]
                cities=tupla[1].copy()  #sino pierdo el valor que consigo en otra iteracion
                libres[k]=True
        return best,cities


n = int(input())
nodosX = []
nodosY = []
for i in range(n):
    entrada = input()
    x = float(entrada.split(" ")[0])
    y = float(entrada.split(" ")[1])
    nodosX.append(x)
    nodosY.append(y)

matriz = []
for i in range(n):
    matriz.append([])
    for j in range(n):
        matriz[i].append(None)

for i in range(n):
    for j in range(i,n):
        a = nodosX[i] - nodosX[j]
        a = a**2
        b = nodosY[i] - nodosY[j]
        b = b**2
        if i==j:
            matriz[i][j]=matriz[j][i]=0
        else:
            matriz[i][j]=matriz[j][i]=math.sqrt(a+b)


lista = []
for i in range(0,n):
    lista.append(i)
c = []
d,ans = genera_permutaciones_wrapper(lista,1000000000.5,0,c,matriz)
print("{:.4f}".format(d))
imprime_lista(ans)