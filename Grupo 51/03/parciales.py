# Punto 1
""" a=int(input('Ingrese a: '))
b=int(input('Ingrese b: '))
if (a>=10 and b<=12):
    if(b>-2 or b<=15):
        c=a+(3*b)
    else:
        c=(2*a)-b
else:
    c=(5*a)-(2*b)
print(c) """
# Punto 2
""" def sombras(x):
    y=-3
    for i in range(3,11,2):
        y+=x
    return y
def oscuro(a,b):
    y=7
    for i in range(a,b,4):
        y+=1**2
    return y
print(sombras(6))
print(oscuro(2,28)) """
# Punto 3
# Variables globales
salida=1
datosGenerales=""
# Se calcula el descuento
def calDescuento(general, vip):
    boletas=general+vip
    descuento=0
    if boletas>=10:
        descuento=2
        if vip==0 and general>0:
            descuento=12
        elif general==0 and vip>0:
            descuento=20
        else:
            descuento=8
    return descuento
def calPagar(general,vip):
    global datosGenerales
    v_general=85000
    v_vip=160000
    descuento=calDescuento(general, vip)
    if descuento!=0:
        v_total=(general*v_general)+(vip*v_vip)
        v_descuento=(v_total*descuento)/100
        total=v_total-(v_descuento)
    else:
        v_descuento=0
        v_total=(general*v_general)+(vip*v_vip)
        total=v_total-(v_descuento)
    datosGenerales+=f"""
        ===== INFORMACION DE LA VENTA =====
        
        ============= BOLETAS =============
        GENERAL             : {general}
        VIP                 : {vip}
        ============= TOTALES =============
        DESCUENTO           : {descuento} %
        TOTAL SIN DESCUENTO : {v_total}
        TOTAL DESCUENTO     : {v_descuento}
        TOTAL A PAGAR       : {total}
    """
# Pedimos los datos por cada cliente
def pedirDatos():
    general=int(input('Ingrese el numero de boletas generales: '))
    vip=int(input('Ingrese el numero de boletas VIP: '))
    print('\n')
    calPagar(general,vip)
# Metodo principal
while salida==1:
    pedirDatos()
    salida=input('Ya no hay más clientes? Si(1) o No(0)')
print(datosGenerales)
input('')
# Punto 4
""" def funcionRecursiva(n):
    if n==0:
        return 1;
    else:
        return ((n-4)+funcionRecursiva(n-1))
print(funcionRecursiva(9)) """