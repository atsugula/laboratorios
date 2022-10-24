#***********************************************
#       SOLUCION DEL PRIMER PROBLEMA 
#***********************************************
#***********************************************
#       SOLUCION DEL PRIMER PROBLEMA 
#***********************************************
import os
import pathlib
#Definicion de variables globales
datos=[]
#Creamos el inicio de nuestro archivo
def crearArchivo():
    ruta=str(pathlib.Path().absolute())+'/datos_pelicula.txt'
    if os.path.exists(ruta):
        os.remove(ruta)
    datos_pelicula=open('datos_pelicula.txt','w')
    datos_pelicula.write('DATOS DE LA PELICULA \n')
    datos_pelicula.close()
#Funcion que pide los datos necesarios, que muestra el ejercicio
def pedirDatos():
    datos.append(str('TITULO: '+input('Ingrese el título de la película: ')))
    datos.append(str('PAIS DE ORIGEN: '+input('Ingrese el país de origen: ')))
    datos.append(str('GENERO: '+input('Ingrese el género: ')))
    datos.append(str('DURACION: '+input('Ingrese la duración en minutos: ')+' MINUTOS'))
    datos.append(str('ANO DE ESTRENO: '+input('Ingrese el año de estreno: ')))
#Guardamos los datos mediante un for con limite 5
def guardarDatos():
    datos_pelicula=open('datos_pelicula.txt','a')
    datos_pelicula.write('\n')
    for i in datos:
        datos_pelicula.write(i+' \n')
    datos_pelicula.close()
#Mostramos los datos en pantalla
def imprimirDatos():
    clear()
    datos_pelicula=open('datos_pelicula.txt','r')
    contenido=datos_pelicula.read()
    print(contenido)
    datos_pelicula.close()
#Funcion para limpiar pantalla dependiendo del sistema operativo
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
#Se ejecuta el metodo principal
nuevo=str(input('¿Es su primera vez acá? Si(s) No(n) \n'))
if nuevo!='n':
    crearArchivo()
#Pedimos los datos
pedirDatos()
#Guardamos los datos en el archivo
guardarDatos()
#Imprimimos los datos
imprimirDatos()
#***********************************************
#       SOLUCION DEL SEGUNDO PROBLEMA 
#***********************************************
pesoT=float(input('Digite su peso en kilogramos: '))
masa=pesoT*9.8
pesoM=pesoT*3.711
pesoJ=pesoT*24.79
pesoL=pesoT*1.622
print('Su peso en la Luna es: '+str(pesoL)+" kgs")
print('Su peso en Júpiter es: '+str(pesoJ)+" kgs")
print('Su peso en Marte es: '+str(pesoM)+" kgs")
#***********************************************
#       SOLUCION DEL TERCER PROBLEMA 
#***********************************************
import time
pi=3.1416
def graficarInicio():
    time.sleep(1)
    print('#*********************************************************************#')
    time.sleep(2)
    print('  Bienvenido, hoy calcularemos el área y el volumen de un cilindro.')
    time.sleep(1)
    print('#*********************************************************************# \n')
#Inicio del programa
graficarInicio()
h=float(input('Digite la altura del cilindro: '))
r=float(input('Digite el radio de la base del cilindro: '))
v=pi*(r*r)*h
a=(2*pi*r*h)+(2*pi*(r*r))
print('VOLUMEN DEL CILINDRO: '+str(v))
print('AREA DEL CILINDRO: '+str(a))