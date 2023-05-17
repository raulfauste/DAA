#Ejercicio 1
def esPar(n,flag):
    if n==0:
        return flag
    else:
        if flag:
            flag=False
        else:
            flag=True
        return esPar(n-1,flag)


sol = esPar(10,True)
print(sol)


#Ejercicio 2
def potencia(b,n):
    if n==1:
        return b
    elif n==2:
        return b**2
    else:
        mitad = n//2
        return potencia(b,mitad)*potencia(b,n-mitad)


print(potencia(2,7))


#Ejercicio 3
#def potenciaMatriz(A,n):
#    if n==0:
#        return np.identity()
#    else:
#        return np.dot(A,potenciaMatriz(A,n-1))

#Este esta sin probar


#Ejercicio 4
def funcion(n):
    if n==1:
        return n
    else:
        return n**3+funcion(n-1)


def g(m,n,f):
    if m==n:
        return f(m)
    else:
        return f(m)+g(m+1,n,f)

print(g(1,3,funcion))


#Ejercicio 5
def productoLento(n,m):
    if n==0:
        return 0
    else:
        return m + productoLento(n-1,m)

print(productoLento(5,4))


#Ejercicio 7
def digitos(n):
    if n<10:
        return 1
    else:
        return 1 + digitos(n//10)

print(digitos(547))


#Ejercicio 8
def cambioBi(n):
    if n<2:
        return n
    else:
        return 2*cambioBi(n//10) + n%10

print(cambioBi(10110))


#Ejercicio 9
def cambioBase(n,b):
    if n<b:
        return n
    else:
        return 10*cambioBase(n//b,b) + n%b

print(cambioBase(22,2))



#Ejercicio 10
def bit(n):
    r = n%10
    if r==1:
        return 1
    else:
        return 1+bit(n//10)

print(bit(1110100))


#Ejercicio 12
def vocales(w):
    if len(w)==1:
        if w[0]=='a' or w[0]=='e' or w[0]=='u' or w[0]=='o' or w[0]=='i':
            return 1
        else:
            return 0
    else:
        if w[0]=='a' or w[0]=='e' or w[0]=='u' or w[0]=='o' or w[0]=='i':
            return 1 + vocales(w[1:])
        else:
            return 0 + vocales(w[1:])


print(vocales("mariaisabel"))


#Ejercicio 13
def Pascal(lista,sol):
    if len(lista)==1:
        return []
    else:
        return [lista[0]+lista[1]] + Pascal(lista[1:],sol)

print(Pascal([1,3,3,1],[]))


#Ejercicio 14
def insertar(n,num):
    r = n%10
    if r==0:
        return num
    elif r<=num:
        return n*10 + num
    else:
        return 10*insertar(n//10,num)+n%10

print(insertar(24667,5))


#Ejercicio 15
def introduce(x,lista,ind):
    if ind==-1:
        lista.insert(ind+1, x)
    elif x>=lista[ind]:
        lista.insert(ind+1,x)
    else:
        introduce(x,lista,ind-1)

lista = [2,4,6,6,7]
introduce(5,lista,4)
print(lista)