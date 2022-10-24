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
#Guardamos los datos mediante un for el limite 
#depende de la cantidad de datos osea 5
def guardarDatos():
    datos_pelicula=open('datos_pelicula.txt','a')
    datos_pelicula.write('\n')
    for i in datos:
        datos_pelicula.write(i+' \n')
    datos_pelicula.close()
#Mostramos los datos en pantalla
def imprimirDatos():
    #clear()
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
