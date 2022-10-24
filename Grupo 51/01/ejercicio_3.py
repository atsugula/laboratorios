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