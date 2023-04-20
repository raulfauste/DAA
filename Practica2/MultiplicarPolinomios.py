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

def multiplicarPolis(pol1,pol2,n,m):
    if len(pol1)==1 and len(pol2)==1:
        sol = []
        sol.append(pol1[-1]*pol2[-1])
        return sol
    elif len(pol1)==1 and len(pol2)>1:
        sol = []
        for i in range(len(pol2)):
            sol.append(pol2[i]*pol1[-1])
        return sol
    elif len(pol1)>=1 and len(pol2)==1:
        sol = []
        for i in range(len(pol1)):
            sol.append(pol1[i]*pol2[-1])
        return sol
    else:
        mitad = min(n//2,m//2)
        if mitad==0:
            mitad = mitad+1
        pb = pol1[:mitad]
        pa = pol1[mitad:]
        qb = pol2[:mitad]
        qa = pol2[mitad:]
        primer = multiplicarPolis(pa,qa,n-mitad,m-mitad)
        segundo = multiplicarPolis(pb,qb,mitad-1,mitad-1)
        sol1 = []
        sol2 = []
        tercer = multiplicarPolis(SumaResta(pa,pb,n-mitad,mitad-1,0,0,sol1,1),SumaResta(qa, qb, m - mitad, mitad - 1, 0, 0, sol2, 1),n-mitad,m-mitad)
        sol3 = []
        sol4= []
        solAux1 = SumaResta(tercer,primer,len(tercer)-1,len(primer)-1,0,0,sol3,0)
        solAux2 = SumaResta(solAux1,segundo,len(solAux1)-1,len(segundo)-1,0,0,sol4,0)
        for i in range(2*mitad):
            primer.insert(0,0)
        for i in range(mitad):
            solAux2.insert(0,0)
        sol5 = []
        sol6 = []
        solAux3 = SumaResta(primer,solAux2,len(primer)-1,len(solAux2)-1,0,0,sol5,1)
        ans = SumaResta(solAux3,segundo,len(solAux3)-1,len(segundo)-1,0,0,sol6,1)
        return ans



n = int(input())
lista1 = lee_lista(n+1)
m = int(input())
lista2 = lee_lista(m+1)
solucion = multiplicarPolis(lista1,lista2,n,m)
imprime_polinomio(solucion,len(solucion)-1,0)