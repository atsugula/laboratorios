import cabezote
cabezote.mensaje()
# Variables globales
valor_hora=10000
n=0
m=0
datos=[] # Matriz que guarda empleados y semanas
totalHoras=[] # Arreglo que guarda las horas por empleado
semanaHoras=[] # Arreglo que guarda las horas por semana
# Almacenar en datos
def almacenar():
    global datos, totalHoras, datos
    for ni in range(n):
        datos[ni][0]=input(f'¡Digite el nombre del empleado {ni+1}!: ')
        for mi in range(1,m):
            datos[ni][mi]=int(input(f'¡Digite la cantidad de horas trabajadas en la semana {mi}!: '))
            totalHoras[ni]+=datos[ni][mi] # Sumamos las horas
# Metodo principal
def principal(): # Pedir los datos iniciales
    global n, m, totalHoras, semanaHoras
    n=int(input('¡Digite n, la cantidad de empleados!: '))
    m=int(input('¡Digite m, la cantidad de semanas!: '))+1
    totalHoras=[0 for x in range(n)] # Inicializamos el arreglo con la cantidad empleados
    semanaHoras=[0 for x in range(m-1)] # Inicializamos el arreglo con la cantidad de hora x semanas
    return [[0 for x in range(m)] for y in range(n)]
# Calcular salario empleado
def calcularSalario():
    salarios=[0 for x in range(n)]
    for i in range(n):
        salarios[i]=totalHoras[i]*valor_hora
    return salarios
# Calcular horas por semana para la nomina de la empresa
def calcularNomina():
    contador=0
    nomina=[0 for x in range(m-1)]
    for i in range(m):
        for empleado in datos:
            if (contador == (len(empleado)-1)):
                continue
            semanaHoras[contador] += empleado[contador+1]
        contador+=1
    for i in range(m-1):
        nomina[i]=semanaHoras[i]*valor_hora
    return nomina
# Llamado de funciones
datos=principal()
almacenar()
salarios=calcularSalario()
nomina=calcularNomina()
opcion=1
while (opcion>0):
    opcion=int(input('Ingrese la opción que desea! 1 (Salario total x empleado) 2 (Nomina por semana) 0 (Salir) :'))
    if (opcion>2 or opcion<0):
        print('No se reconoce la opción')
    elif(opcion==1):
        print('Salario por empleado:')
        for i in range(n):
            print(f'El salario del empleado {datos[i][0]} es ${salarios[i]}')
    else:
        print('Pagos por semana:')
        for i in range(n):
            print(f'En la semana {i+1} se pago de nomina {nomina[i]}')
print('------- FIN DEL PROGRAMA -------')