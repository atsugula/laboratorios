#*********************************************
#  DETERMINAMOS EL PRECIO DE LAS ENTRADAS
#*********************************************
def deter_precio(sala, zona):
    if sala == "2d" and zona == "general":
        entrada = (9500*nAdultos) + (4750*nNinos)
    elif sala == "2d" and zona == "preferencial":
        entrada = (12000*nAdultos) + (6000*nNinos)
    elif sala == "3d" and zona == "general":
        entrada = (13000*nAdultos) + (6500*nNinos)
    elif sala == "3d" and zona == "preferencial":
        entrada = (15000*nAdultos) + (7500*nNinos)
    else:
        print("Valores incorrectos.")
        entrada = 0
    return entrada
#*********************************************
#       PARTE PRINCIPAL DEL CODIGO
#*********************************************
nAdultos = int(input("Digite el numero de adultos: "))
nNinos = int(input("Digite el numero de niños: "))
sala = input("Ingrese la sala (2D-3D): ")
zona = input("Ingrese la zona (preferencial - general): ")
print("\n\t*******B O L E T O S  D E  C I N E*******")
print("\tEl valor de las entradas al cine es: ", str(deter_precio(sala, zona)))
