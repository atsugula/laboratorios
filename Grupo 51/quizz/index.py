# Importamos las librerias necesarias
import function
import familia
import empleados
import esprimos
import sumatoria
# Funcion principal de nuestro programa
print('================= LABORATORIO 3 =================')
while True:
    print("""
        (1) EJERCICIO RECURSIVIDAD
        (2) EJERCICIO CENSO VIRTUAL
        (3) EJERCICIO PAGO EMPLEADOS
        (4) EJERCICIO NUMEROS PRIMOS
        (5) EJERCICIO SUMATORIA
        (6) SALIR
    """)
    decision=int(input('Ingrese la opción que desea: '))
    if (decision==1):
        function.main()
    elif (decision==2):
        familia.main()
    elif (decision==3):
        empleados.main()
    elif (decision==4):
        esprimos.principal()
    elif (decision==5):
        sumatoria.main()
    else:
        break
print('=============== FIN LABORATORIO 3 ===============')
familia.clear()