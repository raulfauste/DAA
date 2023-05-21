#Ejercicio 1
def wrapper(elementos):
    sol = [None]*len(elementos)
    sub_ind(0,-1,sol,elementos)

def sub_ind(i,j,sol,elementos):
    imprimir(sol,elementos,i)
    for k in range(j+1,len(elementos)):
        sol[i]=k
        sub_ind(i+1,k,sol,elementos)

def imprimir(sol,elementos,n):
        print('{',end='')
        for i in range(0,n-1):
            print(elementos[sol[i]],',',sep='',end='')
        if n>0:
            print(elementos[sol[n-1]],sep='',end='')
        print('}')

print(wrapper(['a','b','c']))


#Ejercicio 3
#Identico al problema de imprimir las permutaciones de N elementos
#Imprimios una lista donde en cada indice indicamos la posicion de la torre en esa columna:
#(0,1,3,2) -> En la columna 2, la torre esta en la fila 3
def wrapper_torres(n):
    filas = [True]*n
    sol = [None]*n
    n_torres(n,0,filas,sol)

def n_torres(n,i,filas,sol):
    if n==i:
        imprimir_torres(sol,n)
    else:
        for k in range(0,n):
            if filas[k]:
                sol[i]=k
                filas[k]=False
                n_torres(n,i+1,filas,sol)
                filas[k]=True


def imprimir_torres(sol,n):
    print(sol)

wrapper_torres(4)


#Ejercicio 4
#Otra vez se reduje al problema de generar permutaciones (de 3*3) que cumplan alguna condicion
#Aqui numeramos las casillas de la siguiente forma: casilla [i][j] = 3*i+j
#Codigo no eficiente, ya que se podrian ir haciendo las comprobaciones antes y no al final.
#Pero como solo pide para n=3, sobra.
def wrapper_s():
    matriz = [0]*9
    libres = [True]*10
    sudoku(0,matriz,libres)

def checksudoku(matriz):
    cont = 0
    if matriz[0]+matriz[1]+matriz[2]==15:
        cont = cont+1
    if matriz[3]+matriz[4]+matriz[5]==15:
        cont = cont+1
    if matriz[6]+matriz[7]+matriz[8]==15:
        cont = cont+1
    if matriz[0]+matriz[3]+matriz[6]==15:
        cont = cont+1
    if matriz[1]+matriz[4]+matriz[7]==15:
        cont = cont+1
    if matriz[2]+matriz[5]+matriz[8]==15:
        cont = cont+1
    if matriz[0]+matriz[4]+matriz[8]==15:
        cont = cont+1
    if matriz[2]+matriz[4]+matriz[6]==15:
        cont = cont+1
    return cont==8

def sudoku(i,matriz,libres):
    if i==9 and checksudoku(matriz):
        print(matriz)
    else:
        for k in range(1,10):
            if libres[k]:
                matriz[i]=k
                libres[k]=False
                sudoku(i+1,matriz,libres)
                libres[k]=True

wrapper_s()


#Ejercicio 5
#Consiste en ir probando literalmente todas las posibilidades
#Muy sencillo
#Muy util hacerse la matriz de incrementos.
def wrapper_c(n,iniX,iniY):
    sol = [None]*n
    for i in range(0,n):
        sol[i]=[0]*n
    inc = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
    sol[iniX][iniY]=1
    if caballos(2,n,iniX,iniY,sol,inc):
        imprimirMov(sol)

def imprimirMov(B):
    n = len(B)
    for i in range(0,n):
        for j in range(0,n):
            print(" %5d" % (B[i][j]),end='')
        print()

def caballos(i,n,posX,posY,sol,inc):
    if i>n**2:
        return True
    else:
        stop = False
        k=0
        while not stop and k<8:
            fila = posX + inc[k][0]
            col = posY + inc[k][1]
            if fila>=0 and fila<n and col>=0 and col<n and sol[fila][col]==0:
                sol[fila][col]=i
                stop = caballos(i+1,n,fila,col,sol,inc)
                if not stop:
                    sol[fila][col]=0
            k = k+1
        return stop

wrapper_c(5,2,2)


#Ejercicio 7
def wrapper_tug(elementos):
    sol = [None]*len(elementos)
    res = [None]*len(elementos)
    return minima_dif(sol,elementos,0,0,0,1000000000,res)

def minima_dif(sol,elementos,i,izq,der,min,res):
    if i==len(elementos):
        return sol,abs(izq-der)
    else:
        for k in range(0,2):
            sol[i]=k
            if k==0:
                izq = izq + elementos[i]
            else:
                der = der + elementos[i]
            aux = minima_dif(sol,elementos,i+1,izq,der,min,res)
            if k==0:
                izq = izq - elementos[i]
            else:
                der = der - elementos[i]
            if aux[1]<min:
                min=aux[1]
                res=aux[0].copy()
        return res,min

lista,num = wrapper_tug([3,5,9,14,20,24])
print(lista)
print(num)

#Ejercicio 8
def wrapper_suma(elementos,n):
    sol = [None] * (len(elementos))
    suma=0
    suma_sub(sol,elementos,n,suma,0)

def suma_sub(sol, elementos,n,suma,i):
    if  suma==n:
        imprimir_suma(sol,elementos)
    elif suma<n and i<len(elementos):
        for k in range(0,2):
            if suma + k*elementos[i] <=n:
                sol[i]=k
                suma = suma + k*elementos[i]
                suma_sub(sol,elementos,n,suma,i+1)

def imprimir_suma(sol,elementos):
    for i in range(len(sol)):
        if sol[i]==1:
            print(elementos[i],end=' ',sep=' ')
    print()


wrapper_suma([1,2,3,5,6,7,9],13)


#EXTRA: Mochila que devuelve el mayor valor posible
#Se puede implementar otra poda por valor
def wrapper_bag(peso,valor,c):
    sol = [None]*(len(peso))
    acu=0
    return mochila(peso,valor,c,sol,acu,0,-1)

def mochila(peso,valor,c,sol,acu,i,best):
    if len(peso)==i:
        cont = 0
        for j in range(0,len(peso)):
            if sol[j]==1:
                cont = cont + valor[j]
        return cont
    else:
        for k in range(0,2):
            if acu + k*peso[i] <= c:
                sol[i]=k
                acu = acu + k*peso[i]
                best = max(best,mochila(peso,valor,c,sol,acu,i+1,best))
        return best

print("hola")
print(wrapper_bag([3,6,9,5],[7,2,10,4],15))











