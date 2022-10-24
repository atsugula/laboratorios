def traerSignos(operacion):
    if operacion:
        return " - "
    else:
        return " + "
def sumatoria():
    numero = int(input('Ingrese el número o limite a recorrer: '))
    y = 3
    x = 1
    num1 = 0
    num2 = 1
    acumulador = 0
    # Nos sirve para saber si sumamos o restamos
    operacion = True
    for i in range(0, numero):
        signo = traerSignos(operacion)
        # Sumamos o hacemos la operacion correspondiente
        if operacion:
            acumulador += x/y
        else:
            acumulador -= x/y
        # Imprimimos la secuencia de nuestra lista
        print(f'P{i+1}({x}/{y})', end=signo)
        # Sumamos los contadores
        x = num1 + num2
        num1 = num2
        num2 = x
        y += 2
        operacion = not operacion
    mensaje = f"El valor acumulado en la posicion {numero} es: {acumulador}"
    print()
    return mensaje
def main():
    print(sumatoria())