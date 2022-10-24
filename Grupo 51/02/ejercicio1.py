#Determinar que lugar, segun la tabla, tomaremos como referencia
def deter_consumo(consumo):
    if (consumo>0) and (consumo<40):
        puesto=1
    else:
        puesto=2
    return puesto
#Determinamos cual es el precio por metro, segun el estrato
def deter_estrato(estrato, consumo):
    puesto=deter_consumo(consumo)
    if(estrato==1):
        if (puesto==1):
            valorEstrato=2500
        else:
            valorEstrato=3000
    elif (estrato==2):
        if (puesto==1):
            valorEstrato=3500
        else:
            valorEstrato=4500
    elif (estrato==3):
        if (puesto==1):
            valorEstrato=4500
        else:
            valorEstrato=6000
    else:
        print('No tenemos servicio para este estrato.')
        valorEstrato=0
    return valorEstrato
#Parte principal del codigo
nPredio=float(input('Ingrese el número del predio: '))
estrato=float(input('Ingrese el estrato del predio: '))
consumo=float(input('Ingrese el consumo en metros cubicos: '))
valor_m=deter_estrato(estrato, consumo)
valorFactura=valor_m*consumo
print('FACTURA CONSUMO DE AGUA')
print('Predio No. : ',str(nPredio))
print('Estrato del predio: ',str(estrato))
print('Valor factura: ',str(valorFactura))