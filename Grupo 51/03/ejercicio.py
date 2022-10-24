datosEmpleados=""
def pedirDatos():
    global datosEmpleados
    for i in range(1,cantidad_empleados+1):
        numero_de_documento=int(input("digite numero de documento:"))
        nombre_completo=input("digite nombre:")
        salario_del_empleado=int(input("digite salario del empleado:"))
        # Donde se calculan los pagos
        subsidio_transporte = (salario_del_empleado * 0.20)
        bonificacion = (salario_del_empleado * 0.10)
        # Donde se calculan los descuentos
        salud = (salario_del_empleado * 0.04)
        pension = (salario_del_empleado * 0.04)
        retefuente = (salario_del_empleado * 0.05)
        # Donde se calculan los totales
        total_pagos = (subsidio_transporte + bonificacion)
        total_descuento = (salud + pension+ retefuente)
        total_salario = (salario_del_empleado + total_pagos - total_descuento)
        datosEmpleados+=f"""
            ======== DATOS DEL EMPLEADO =========
            Documento      : {numero_de_documento}
            Nombre         : {nombre_completo}
            =============== PAGOS ===============
            Salario        : {salario_del_empleado}
            Bonificacion   : {bonificacion} 
            subsidio       : {subsidio_transporte} 
            ============ DESCUENTOS =============
            Salud          : {salud}
            pension        :{pension}
            retefuente     :{retefuente}
            =========== TOTALES ================
            total_pagos    : {total_pagos}
            Total descuento: {total_descuento}
            Neto a pagar   : {total_salario}
        """
# Metodo principal
cantidad_empleados=int(input("digite cantidad de empleados:"))
pedirDatos()
print(datosEmpleados)