def lee_lista(n):
    a = []
    if n > 0:
        cadenaEntrada = input()
        for i in range(0, n):
            elemento = int(cadenaEntrada.split(" ")[i])
            a.append(elemento)

    return a

def separar(a,pares,impares):
    if len(a)==0:
        tupla = (impares, pares)
        print(tupla)
    else:
        if a[0]%2==0:
            pares.append(a[0])
        else:
            impares.append(a[0])
        separar(a[1:],pares,impares)


n = int(input())
a = lee_lista(n)
pares = []
impares = []
separar(a,pares,impares)