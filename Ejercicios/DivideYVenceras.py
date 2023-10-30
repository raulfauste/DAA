import math

#Ejercicio 1
def BS_noSort(lista,x,sup,inf):
    if inf>sup:
        return False
    else:
        mitad = (inf+sup)//2
        if lista[mitad]==x:
            return True
        else:
            return BS_noSort(lista,x,sup,mitad+1) or BS_noSort(lista,x,mitad-1,inf)

print(BS_noSort([1,-3,0,5,-4,2],7,5,0))


#Ejercicio 2:
def digitos(n):
    d = [False] * 10
    while n>10:
        d[n%10]=True
        n=n//10
    d[n]=True
    return d
print(digitos(2345))

def conjunto(lista,inf,sup,d):
    if inf>sup:
        return d
    else:
        mitad = (inf+sup)//2
        aux = digitos(lista[mitad])
        aux1 = conjunto(lista,mitad+1,sup,aux)
        aux2 = conjunto(lista,inf,mitad-1,aux)
        for i in range(0,10):
            d[i]=aux[i] and aux1[i] and aux2[i]
        return d

valores = [False]*10
print(conjunto([2348,1394,7523,3215],0,3,valores))


#Ejercicio 3
def max_sublist(lista):
    n = len(lista)
    if n==1:
        return lista[0]
    else:
        mitad = n//2
        max_i = max_sublist(lista[:mitad])
        max_d = max_sublist(lista[mitad:])
        izq = -math.inf
        der = -math.inf
        aux = 0
        for i in range(mitad-1,-1,-1):
            aux = aux + lista[i]
            izq = max(izq,aux)
        aux=0
        for i in range(mitad,n):
            aux = aux+lista[i]
            der = max(der,aux)
        return max(max_i,max(max_d,izq+der))

print(max_sublist([-1,-4,5,2,-3,4,2,-5]))