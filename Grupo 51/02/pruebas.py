#Para la secuencia 3, 5, 7, 9, ...impar
n=int(input('Ingrese la cantidad de numeros a crear: '))
dato=3
for i in range(1,n+1):
    print("(",i,",",dato,")",end=",")
    dato+=2
#Para la secuencia 7, 15, 31 ...
m=int(input('Ingrese la cantidad de numeros a crear: '))
cont=7
for i in range(1,m+1):
    print("(",i,",",cont,")",end=",")
    cont=(cont*2)+1
#Secuencia con el primer for, utilizando funciones