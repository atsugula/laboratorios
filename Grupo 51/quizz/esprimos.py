def principal():
    cont = 0
    cantidad=100
    try:
        cantidad=int(input('Ingrese el limite del numero de la lista, por defecto es 100: '))
    except ValueError:
        cantidad=100
    print(f'============ NUMEROS PRIMOS HASTA EL {cantidad} ===============\n')
    for i in range(2, cantidad+1):
        primos = True
        for j in range(2,i):
            if i == j:
                break
            elif i % j == 0:
                primos = False
            else:
                continue
        if primos == True:
            print(i,end=',')
            cont += 1
    print('\n\n===================== FIN PROGRAMA =====================')