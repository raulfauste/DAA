def lee_lista(n):
    a = []
    if n > 0:
        cadenaEntrada = input()
        for i in range(0, n):
            elemento = int(cadenaEntrada.split(" ")[i])
            a.append(elemento)

    return a

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

#segun el valor de la flag sumamos(1) o restamos (0)
def SumaResta(a,b,n,m,i,j,sol,flag):
    if i==n+1 and j==m+1:
        pass
    else:
        if flag==1:
            if i<n+1 and j<m+1:
                sol.append(a[i]+b[j])
                SumaResta(a, b, n, m, i+1, j + 1, sol, flag)
            elif i == n + 1:
                sol.append(b[j])
                SumaResta(a, b, n, m, i, j + 1, sol, flag)
            elif j == m + 1:
                sol.append(a[i])
                SumaResta(a, b, n, m, i + 1, j, sol, flag)
        else:
            if i<n+1 and j<m+1:
                sol.append(a[i] - b[j])
                SumaResta(a, b, n, m, i+1, j + 1, sol, flag)
            elif i == n + 1:
                sol.append(-b[j])
                SumaResta(a, b, n, m, i, j + 1, sol, flag)
            elif j == m + 1:
                sol.append(a[i])
                SumaResta(a, b, n, m, i + 1, j, sol, flag)
    return sol

n = int(input())
lista1 = lee_lista(n+1)
m = int(input())
lista2 = lee_lista(m+1)
sol=[]
ans = SumaResta(lista1,lista2,n,m,0,0,sol,1) #1 = suma
imprime_polinomio(sol,max(n,m),0)
sol=[]
ans = SumaResta(lista1,lista2,n,m,0,0,sol,0) #0 = resta
imprime_polinomio(sol,max(n,m),0)