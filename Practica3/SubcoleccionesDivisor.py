def lee_lista(n):
    a = []
    if n > 0:
        cadenaEntrada = input()
        for i in range(0, n):
            elemento = int(cadenaEntrada.split(" ")[i])
            a.append(elemento)

    return a

def genera_subconjuntos_wrapper(elementos,m):
    sol = [None] * (len(elementos))
    solu = genera_subconjuntos(0,-1,sol,elementos,m)
    return solu

def genera_subconjuntos(i,j,sol,elementos,m):
    if i == m:
        return 1
    elif i>m:
        return 0
    else:
        ans = 0
        for k in range(j+1,len(elementos)):
            if (i>=1 and elementos[k]%elementos[sol[0]]==0) or i==0:
                sol[i]=k
                ans = ans + genera_subconjuntos(i+1,k,sol,elementos,m)
        return ans



n = int(input())
a = lee_lista(n)
a.sort()
m = int(input())
print(genera_subconjuntos_wrapper(a,m))