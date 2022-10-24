# Inicializamos todas las variables
nombre=''
frecuencia=0
antiguedad=0
categoria=''
descuento=0
paga=0
des=0
# Calcular la categoria segun la frecuencia
def definirCategoria(frecuencia):
    global categoria, paga
    if (frecuencia==1):
        categoria='Bajo'
        paga=14000
    elif (frecuencia>=2) and (frecuencia<=3):
        categoria='Normal'
        paga=22000
    elif (frecuencia>=4):
        categoria='Alto'
        paga=40000

# Calcular el valor a pagar en un club de bolos
def valorPagar(antiguedad):
    global des, descuento,paga
    if (antiguedad<12):
        des=0
        descuento=paga
    elif (antiguedad>=12) and (antiguedad<=60):
        des=10
        descuento=paga-((paga*10)/100)
    elif (antiguedad>60):
        des=20
        descuento=paga-((paga*20)/100)

# Pedir datos
def datosEntrada():
    global nombre,frecuencia,antiguedad
    nombre=input('Ingrese el nombre: ')
    frecuencia=int(input('Ingrese la frecuencia: '))
    antiguedad=int(input('Ingrese la antiguedad: '))

# Imprimir todos los datos, según el ejercicio
def imprimir():
    print('Nombre: ',nombre)
    print('Categoria: ',categoria)
    print('Descuento a aplicar: ',str(des),' %')
    print('Valor a pagar: ',str(descuento))

# Metodo principal de nuestro software
datosEntrada()
definirCategoria(frecuencia)
valorPagar(antiguedad)
imprimir()