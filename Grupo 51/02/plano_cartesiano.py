x=float(input('Ingrese la cordenada de x: '))
y=float(input('Ingrese la cordenada de y: '))

if (x>0) and (y>0):
    print('CUADRANTRE I')
elif (x<0) and (y>0):
    print('CUADRANTRE II')
elif (x<0) and (y<0):
    print('CUADRANTRE III')
elif (x>0) and (x<0):
    print('CUADRANTE IV')
else:
    print('SE ENCUENTRA EN EL ORIGEN')