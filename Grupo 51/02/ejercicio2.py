#*********************************************
#       PARTE PRINCIPAL DEL CODIGO
#*********************************************
def valor_hora(horasT):
    if(horasT<=160):
        costoH=10000
    else:
        costoH=15000
    return costoH
#*********************************************
#       PARTE PRINCIPAL DEL CODIGO
#*********************************************
def deter_subsidio(salario):
    if(salario<=500000):
        subsidio=6000000
    elif(salario>500000) and (salario<=1500000):
        subsidio=3000000
    else:
        subsidio=1000000
    return subsidio
#*********************************************
#       PARTE PRINCIPAL DEL CODIGO
#*********************************************
horasT=int(input('Ingrese la cantidad de horas trabajadas: '))
#Hacemos las validaciones de las horas
costoH=valor_hora(horasT)
#Al saber cuanto vale la hora, simplemente multiplicamos
salario=costoH*horasT
#Determinamos cuanto es el salario
subsidio=deter_subsidio(salario)
#*********************************************
#          IMPRIMIMOS LOS DATOS
#*********************************************
print('El salario del trabajador es: ',str(salario))
print('El subsidio del trabajador es: ',str(subsidio))