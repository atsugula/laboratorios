# Importacion librerias necesarias
import os
import pathlib
# Definicion de variables globales
datos=[]
cantFamily=0
# Creamos el inicio de nuestro archivo
def crearArchivo():
    ruta=str(pathlib.Path().absolute())+'/ejercicio1.txt'
    if os.path.exists(ruta):
        os.remove(ruta)
    datos_ejercicio=open('ejercicio1.txt','w')
    datos_ejercicio.write('================ DATOS DEL EJERCICIO 01 ================== \n')
    datos_ejercicio.close()
# Funcion que pide los datos necesarios, que muestra el ejercicio
def pedirJefeFamilia():
    global cantFamily
    datos.append('================ JEFE DE HOGAR ================== \n')
    datos.append(str('NOMBRE           : '+input('Ingrese el nombre: ')))
    datos.append(str('APELLIDO         : '+input('Ingrese el apellido: ')))
    datos.append(str('TIPO DOCUMENTO   :'+input('Ingrese el tipo de documento: ')))
    datos.append(str('DOCUMENTO        : '+input('Ingrese el número de documento: ')))
    datos.append(str('FECHA NACIMIENTO : '+input('Ingrese la fecha de nacimiento: ')))
    datos.append(str('DEPARTAMENTO     : '+input('Ingrese el departamento: ')))
    datos.append(str('CIUDAD           : '+input('Ingrese la ciudad: ')))
    datos.append(str('DIRECCIÓN        : '+input('Ingrese la direccion: ')))
    cantFamily=int(input('Ingrese la cantidad de familiares: '))
    datos.append('CANT. FAMILIARES     : '+str(cantFamily))
    datos.append('================ FAMILIARES ================== \n')
#Funcion que pide los datos necesarios, que muestra el ejercicio
def pedirFamiliares():
    for i in range(1,cantFamily+1):
        print('INGRESE LOS DATOS DEL FAMILIAR',i)
        datos.append(str('NOMBRE           : '+input('Ingrese el nombre del familiar: ')))
        datos.append(str('APELLIDO         : '+input('Ingrese el apellido del familiar: ')))
        datos.append(str('TIPO DOCUMENTO   :'+input('Ingrese el tipo de documento: ')))
        datos.append(str('DOCUMENTO        : '+input('Ingrese el número de documento: ')))
        datos.append(str('FECHA NACIMIENTO : '+input('Ingrese la fecha de nacimiento: ')))
        datos.append(str('PARENTESCO       : '+input('Ingrese el parentesco: ')))
        print('\n')
        datos.append('\n')
# Mostramos los datos en pantalla
def imprimirDatos():
    #clear()
    datos_ejercicio=open('ejercicio1.txt','r')
    contenido=datos_ejercicio.read()
    print(contenido)
    datos_ejercicio.close()
# Guardamos los datos mediante un for el limite 
# depende de la cantidad de datos osea 5
def guardarDatos():
    datos_ejercicio=open('ejercicio1.txt','a')
    datos_ejercicio.write('\n')
    for i in datos:
        datos_ejercicio.write(i+' \n')
    datos_ejercicio.close()
# Funcion para limpiar pantalla dependiendo del sistema operativo
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
# Método principal
def main():
    nuevo=str(input('¿Es su primera vez acá? Si(s) No(n) \n'))
    if nuevo!='n':
        crearArchivo()
    # Pedimos los datos del jefe de familia
    pedirJefeFamilia()
    # Limpiamos pantallas
    clear()
    # Pedimos los datos del familiar
    pedirFamiliares()
    # Limpiamos pantallas
    clear()
    # Guardamos los datos en el archivo
    guardarDatos()
    # Imprimimos los datos
    imprimirDatos()