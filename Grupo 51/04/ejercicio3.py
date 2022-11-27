import random
# Declaramos la matriz
data = [[0 for i in range(6)] for y in range(5)]
depts = ['cauca', 'choco', 'putumayo', 'nariño', 'valle']
months = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio']

# Llenar con datos aleatorios
def fill_data():
    global data
    for i in range(5):
        for y in range(6):
            data[i][y] = round((random.random() * 100), 1)
            
# Mostrar toda la informacion
def show_data():
    print(f"""  
            | [Enero|Febrero|Marzo|Abril|Mayo|Junio]
    Cauca   | [{only_dept(0)}]
    Chocó   | [{only_dept(1)}]
    Nariño  | [{only_dept(2)}]
    Putumayo| [{only_dept(3)}]
    Valle   | [{only_dept(4)}]
    """)
    input('\n------ PRESIONE CUALQUIER TECLA ------')

# Tomar un solo departamento
def only_dept(x):
    return data[x]

# Tomar un solo mes
def only_month(x):
    order = []
    for i in range(5):
        order.append(data[i][x])
    return order

# Promedio de lluvias por mes
def half_month():
    month = input('Ingrese el mes a promediar: ')
    try:
        index_month = months.index(month.lower())
        temp = only_month(index_month)
        print(temp)
        half = sum(temp)/len(temp)
        print(f'El promedio del departamento {month.lower()} es: {round(half, 1)}')
    except:
        print('Departamento no encontrado, revisé.')
    input('\n------ PRESIONE CUALQUIER TECLA ------')

# Promedio de lluvias por departamento
def half_dept():
    dept = input('Ingrese el departamento a promediar: ')
    try:
        index_dept = depts.index(dept.lower())
        temp = only_dept(index_dept)
        half = sum(temp)/len(temp)
        print(temp)
        print(f'El promedio del departamento {dept.lower()} es: {round(half, 1)}')
    except:
        print('Departamento no encontrado, revisé.')
    input('\n------ PRESIONE CUALQUIER TECLA ------')

# Menu del programa
while True:
    option = int(input('''
Elija una opcion:
1. Llenar Matriz de lluvias
2. Imprimir Matriz
3. Promedio de lluvias por departamento
4. Promedio de lluvias por mes
5. Salir \n
Opción: '''))
    if option == 1:
        fill_data()
    if option == 2:
        show_data()
    if option == 3:
        half_dept()
    if option == 4:
        half_month()
    if option == 5:
        break