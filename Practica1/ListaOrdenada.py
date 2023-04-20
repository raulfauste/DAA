def lee_lista(n):
    a = []
    if n > 0:
        cadenaEntrada = input()
        for i in range(0, n):
            elemento = int(cadenaEntrada.split(" ")[i])
            a.append(elemento)

    return a

def introduce(x,lista,ind):
    if ind==-1:
        lista.insert(ind+1, x)
    elif x>=lista[ind]:
        lista.insert(ind+1,x)
    else:
        introduce(x,lista,ind-1)

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


n = int(input())
lista = lee_lista(n)
x = int(input())
introduce(x,lista,n-1)
imprime_lista(lista)
