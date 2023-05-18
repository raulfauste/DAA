#Ejercicio 1
def impar(n,flag):
    r = n%10
    if r%2==1 :
        flag = True
        return flag
    elif n<10:
        return flag
    else:
        return impar(n//10,flag)

print(impar(223,False))


#Ejercicio 3
def apariciones(a,b):
    if len(a)==0:
        return b
    else:
        b[a[0]]=b[a[0]]+1
        return apariciones(a[1:],b)

sol = apariciones([2,2,3,2,0,1,3,2,0,0,4],[0,0,0,0,0])
print(sol)

def ordenar(b,ind):
    if len(b)==0:
        return []
    else:
        ans = []
        for i in range(0, b[0]):
            ans.append(ind)
        return ans + ordenar(b[1:],ind+1)

print(ordenar(sol,0))

def counting_sort(a,b):
    return ordenar(apariciones(a,b),0)

print(counting_sort([2,2,3,2,0,1,3,2,0,0,4],[0,0,0,0,0]))

#Ejercicio 4
def claveMinima(tupla,mini):
    mini=min(mini,tupla[0])
    if tupla[2]!=[]:
        claveMinima(tupla[2],mini)
    if tupla[3]!=[]:
        claveMinima(tupla[3],mini)


#Ejercicio 5
def busqueda_binaria(a, x, inf):
    if inf > len(a)-1: # lista vacia
        return -1
    else:
        mitad = (inf + len(a)-1) // 2

    if x == a[mitad]:
        return mitad
    elif x < a[mitad]:
        return busqueda_binaria(a[:mitad-1], x, inf)
    else:
        return busqueda_binaria(a[:mitad+1], x, mitad + 1)

print(busqueda_binaria([1,2,3,4,5],3,0))


#Ejercicio 6
def BooleanBB(a,x):
    if len(a)==1 and a[0]!=x:
        return False
    else:
        mitad = len(a)//2
        if a[mitad]==x:
            return True
        elif x<a[mitad]:
            return BooleanBB(a[:mitad],x)
        else:
            aux = a[mitad:]
            return BooleanBB(aux,x)

print(BooleanBB([1,2,3,4,5],0))


#Ejercicio 7
def funcionInd(lista,sup,inf):
    if inf>sup:
        return -1
    else:
        mitad = (sup+inf)//2
        if lista[mitad]==mitad:
            return mitad
        elif lista[mitad]>mitad:
            return funcionInd(lista,mitad-1,inf)
        else:
            return funcionInd(lista,sup,mitad+1)

print(funcionInd([-3,-1,2,5,6,7,9],6,0))


#Ejercicio 8
def funcionParImpar(lista,sup,inf,ind):
    if inf>sup:
        return ind
    else:
        mitad = (inf +sup)//2
        if lista[mitad]%2==0:
            ind = max(ind,mitad)
            return funcionParImpar(lista,sup,mitad+1,ind)
        else:
            return funcionParImpar(lista,mitad-1,inf,ind)

print(funcionParImpar([2,-4,10,8,0,12,9,3,-15,3,1],10,0,-1))
print(funcionParImpar([-1,-1,1,3,5,1,9,3,-15,3,1],10,0,-1))
print(funcionParImpar([2,-4,10,8,0,12,2,0,0,0,0],10,0,-1))