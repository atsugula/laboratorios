# Variables globales
datos=""
# Pedimos los datos de los empleados
def datosEmpleados(nEmpleados):
    global datos
    if (nEmpleados>0):
        num_doc=input('Digite el número de documento de identidad: ')
        nombre=input('Digite el nombre completo: ')
        salario=int(input('Digite el salario del empleado: '))
        print('\n')
        # Calculamos la bonificacion
        bonificacion=salario*(10/100)
        # Calculamos el subsidio de transporte
        subsidio=salario*(20/100)
        # Calculamos el descuento en salud
        salud=salario*(4/100)
        # Calculamos el descuento de pension
        pension=salario*(4/100)
        # Calculamos el descuento de retefuente
        retefuente=salario*(5/100)
        # Calculamos el total de pagos
        t_pagos=salario+bonificacion+subsidio
        # Calculamos el total de descuentos
        t_descuentos=salud+pension+retefuente
        # Calculamos el total neto o neto a pagar
        neto=t_pagos-t_descuentos
        datos+=f"""
            ==============    DATOS DEL EMPLEADO    ==============

            NOMBRE                       : {nombre}
            DOCUMENTO                    : {num_doc}
            =================       PAGOS        =================

            SALARIO                      : {salario}
            BONIFICACIÓN DE SERVICIOS    : {bonificacion}
            SUBSIDIO DE TRANSPORTE       : {subsidio}
            =================    DESCUENTOS      =================

            SALUD                        : {salud}
            PENSION                      : {pension}
            RETEFUENTE                   : {retefuente}
            =================      TOTALES       =================

            TOTAL PAGOS                  : {t_pagos}
            TOTAL DESCUENTOS             : {t_descuentos}
            NETO A PAGAR                 : {neto}
        """
        datosEmpleados(nEmpleados-1)
# Método principal del código
nEmpleados=int(input('Ingrese el número de empleados: '))
# Pedimos los datos
datosEmpleados(nEmpleados)
# Mostramos los datos
print(datos)