# Definicion de variables
rutas = []
pasajeros = []

# Funcion que pide la ruta
def fill_rutas():
    ruta = input('Ingrese el nombre de la ruta: ')
    rutas.append(ruta)

# Funcion que pide los pasajeros
def fill_pasajeros():
    nPasajeros = int(input("Ingrese la cantidad de pasajeros: "))
    pasajeros.append(nPasajeros)

# Funcion que muestra la informacion
def show_info():
    print('------ INFORMACION DE LAS RUTAS ------')
    for i in range(len(pasajeros)):
        print(f"""
        Rutas       :  {rutas[i]}
        Pasajeros   :  {pasajeros[i]}""")

# Funcion ruta con más pasajeros
def more_ruta():
    cont = max(pasajeros)
    print(f'------ LA RUTA QUE MAS PASAJEROS MOVILIZO ------')
    for i in range(len(rutas)):
        if cont == pasajeros[i]:
            print(f'Ruta: {rutas[i]}, movilizó {pasajeros[i]}')

# Funcion sumar pasajeros dia
def p_dia():
    cont = 0
    for i in range(len(pasajeros)):
        cont += pasajeros[i]
    print("La suma de los pasajeros movilizados al dia son: ",cont)
    
while True:
    print("""
    1. Agregar ruta
    2. Mostrar información
    3. Pasajeros movilizados al día
    4. Ruta que más pasajeros movilizó
    5. Salir""")
    option = int(input('Ingrese la opción: '))
    if option == 1:
        fill_rutas()
        fill_pasajeros()
    elif option == 2:
        show_info()
    elif option == 3:
        p_dia()
    elif option == 4:
        more_ruta()
    elif option == 5:
        break