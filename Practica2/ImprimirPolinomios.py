def lee_lista(n):
    a = []
    if n > 0:
        cadenaEntrada = input()
        for i in range(0, n):
            elemento = int(cadenaEntrada.split(" ")[i])
            a.append(elemento)

    return a

#flag para saber si estamos en la primera iteracion y asi considerar el caso del 0

def imprime_polinomio(a,n,flag):
    if n==-1:
        pass
    elif a[n]==0:
        if flag==0:
            print("+ ", a[n], sep='')
        else:
            imprime_polinomio(a,n-1,1)
    else:
        if a[n]>=0:
            if n==0:
                print("+ ", a[n],sep='')
            else:
                print("+ ",a[n],"x^",n,end=' ',sep='')
        else:
            if n==0:
                print("- ", -a[n],sep='')
            else:
                print("- ",-a[n],"x^",n,end=' ',sep='')
        imprime_polinomio(a,n-1,1)

n = int(input())
lista = lee_lista(n+1)
imprime_polinomio(lista,n,0)