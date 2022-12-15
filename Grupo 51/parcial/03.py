salida = True
n = int(input('Ingrese el número de personas a ingresar: '))
while salida:
    if n < 3:
        print('Error son minimo 3 pacientes')
        break
    elif n > 10:
        print('Error son maximo 10 pacientes')
        break
    pacientes = [[0 for x in range(7)] for i in range(n)]
    for i in range(2):
        pacientes[i][6] = [None]*4
        doc = input('Ingrese el documento de identidad del paciente: ')
        nombre = input('Ingrese el nombre del paciente: ')
        sexo = input('Ingrese el sexo del paciente (m) Masculino (f) Femenino: ')
        edad = input('Ingrese la edad del paciente: ')
        peso = float(input('Ingrese el peso del paciente (Kilo gramos): '))
        estatura = float(input('Ingrese la estatura del paciente (Metros): '))
        print('Datos de la cita del paciente')
        fecha = input('Ingrese la fecha: ')
        doctor = input('Ingrese el nombre del doctor que lo atendió: ')
        motivo = input('Ingrese el motivo de la atención: ')
        fecha_prox = input('Ingrese la fecha de la proxima cita: ')
        pacientes[i][0] = doc
        pacientes[i][1] = nombre
        pacientes[i][2] = sexo
        pacientes[i][3] = edad
        pacientes[i][4] = peso
        pacientes[i][5] = estatura
        pacientes[i][6] = [fecha, doctor, motivo, fecha_prox]

    
def mostrar():
    for i in range(n):
        print(f"""
Documento   : {pacientes[i][0]}
Nombre      : {pacientes[i][1]}
Sexo        : {pacientes[i][2]}
Edad        : {pacientes[i][3]}
Peso        : {pacientes[i][4]}
Estatura    : {pacientes[i][5]}
    DATOS DE LA CITA
Fecha                   : {pacientes[i][6][0]}
Doctor que atendio      : {pacientes[i][6][1]}
Motivo de la consulta   : {pacientes[i][6][2]}
Fecha proxima           : {pacientes[i][6][3]}
""")

def calcular():
    icm = []
    condicion=[]
    for i in range(n):
        temp_icm = pacientes[i][4] / pacientes[i][5]
        if temp_icm < 18.5:
            condicion.append('Bajo peso')
        elif temp_icm >= 18.5 or temp_icm <= 24.9:
            condicion.append('Peso adecuado')
        elif temp_icm >= 25 or temp_icm <= 29.9:
            condicion.append('Sobrepeso')
        elif temp_icm >= 25 or temp_icm <= 29.9:
            condicion.append('Obeso')
        elif temp_icm >= 40:
            condicion.append('Extremadamente obeso')
        icm.append(temp_icm)
    for i in range(n):
        print(f'El paciente {pacientes[i][1]} tiene un icm de {icm[i]} y una condicion de {condicion[i]}')
        
mostrar()
calcular()