#Inicializamos todas las variables
nombre=''
edad=0
tiempo=0
x=0
# Calcular la prioridad de atención de una persona
def definirPrioridad(edad, tiempo):
    global x
    x=round(edad/tiempo,2) # Redondeamos a dos decimales
    if (x<2):
        prioridad='Bajo'
    elif (x<=2) and (x<5):
        prioridad='Normal'
    elif (x>5):
        prioridad='Alto'
    return prioridad
#Pedir los datos de una persona
def datosEntrada():
    global nombre,edad,tiempo
    nombre=input('Ingrese el nombre: ')
    edad=float(input('Ingrese la edad: '))
    tiempo=float(input('Ingrese el tiempo: '))
#Imprimimos los datos de la persona, anexando la prioridad
def imprimir():
    prioridad=definirPrioridad(edad,tiempo) #Traemos la prioridad de la persona
    print('Nombre: ',nombre)
    print('Edad/Tiempo: ',str(x))
    print('Prioridad: ',str(prioridad))
#Metodo principal de nuestro software
datosEntrada()
imprimir()