# Inicializamos todas las variables
x=0
f=0

# Calcular el valor de la funcion
def valorFuncion(x):
    global f
    if (x<=0):
        f=8*(pow(x,2))-6 # pow es para elevar, ejemplo x²
    elif (x>0):
        f=3*(x)+5

# Imprimir todos los datos, según el ejercicio
def imprimir():
    print('f(',str(x),') = ',str(f))

# Pedir los datos
def datosEntrada():
    global x
    x=int(input('Ingrese el valor de x: '))
    
# Metodo principal de nuestro software
datosEntrada()
valorFuncion(x)
imprimir()