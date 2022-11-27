import random

departamentos = []
Contenedor = []


def solicitarDepartamento(n):
    global departamentos
    departamento = input('Ingrese el departamento: ')
    departamentos.append(departamento)
    for i in range(n - 1):
        x = round((random.random() * 100), 1)
        departamentos.append(x)
    Contenedor.append(departamentos)
    departamentos = []


def imprimirInfo():
    for i in range(len(Contenedor)):
        print(Contenedor[i])


def promedioLluvia(mes):
    temporal = 0
    if mes.lower() == "enero":
        temporal = 0
    elif mes.lower() == "febrero":
        temporal = 1
    elif mes.lower() == "marzo":
        temporal = 2
    elif mes.lower() == "abril":
        temporal = 3
    elif mes.lower() == "mayo":
        temporal = 4
    elif mes.lower() == "junio":
        temporal = 5
    elif mes.lower() == "julio":
        temporal = 6
    elif mes.lower() == "agosto":
        temporal = 7
    elif mes.lower() == "septiembre":
        temporal = 8
    elif mes.lower() == "octubre":
        temporal = 9
    elif mes.lower() == "noviembre":
        temporal = 10
    elif mes.lower() == "diciembre":
        temporal = 11

    columnas = len(Contenedor[0])
    suma = 0
    contador = 0
    for j in range(columnas):
        suma = sum([fila[temporal] for fila in Contenedor])
        contador += 1
    print(f'El promedio de lluvia del mes {mes} es: {suma / contador}')


def promedioSemestr(departamento):
    temporal = 0
    contador = 0
    for i in range(len(Contenedor)):
        if departamento == Contenedor[i][0]:
            for j in range(len(Contenedor[i])):
                temporal += Contenedor[i][j]
                contador += 1
    print(f'El promedio de lluvia en el departamento {departamento} en los meses registrados es: {temporal / contador}')


on = True
while on:
    on_of = True
    option = int(input('''
Elija una opcion:
1. Registrar departamento
2. Imprimir informacion
3. Promedio dentro de un mes
4. Promedio dentro de un departamento
5. Salir \n
Opción: '''
))

    if option == 1:
        nMeses = int(input('Ingrese el numero de meses a evaluar: '))
        while on_of:
            oDepartamento = int(input('''
Elija una opcion:
1. Registrar un nuevo departamento
2. Finalizar \n'''))

            if oDepartamento == 1:
                solicitarDepartamento(nMeses)
            elif oDepartamento == 2:
                on_of = False
    elif option == 2:
        imprimirInfo()
    elif option == 3:
        m = input('Ingrese el mes a evaluar: ')
        promedioLluvia(m)
    elif option == 4:
        d = input('Ingrese el departamento a evaluar en los meses registrados: ')
        promedioSemestr(d)
    elif option == 5:
        on = False
    print(Contenedor)